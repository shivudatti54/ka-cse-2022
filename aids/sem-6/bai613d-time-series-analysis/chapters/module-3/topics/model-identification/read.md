# File Identification and Hashing in Static Malware Analysis

## Introduction to File Identification

File identification is the foundational first step in the static analysis of any suspected malware sample. Before an analyst can begin to understand what a file *does*, they must first understand what a file *is*. This process involves gathering basic metadata about the file to form an initial assessment and create a unique identifier for the sample.

The primary goals of file identification are:
- Determine the file type and format
- Gather basic file metadata (size, timestamps)
- Create a unique cryptographic fingerprint (hash) of the file
- Identify potential obfuscation or packing techniques

## File Types and Formats

Malware can come in various formats, and correctly identifying the file type is crucial for determining the appropriate analysis techniques.

### Common Malware File Types

| File Type | Extension | Description | Analysis Approach |
|-----------|-----------|-------------|-------------------|
| Portable Executable | .exe, .dll, .sys | Windows executable files | PE analysis, disassembly |
| Executable and Linkable Format | (none), .elf | Linux/Unix executables | ELF analysis, disassembly |
| Mach-O | (none), .dylib | macOS executables | Mach-O analysis |
| Script Files | .js, .vbs, .ps1 | Script-based malware | Script analysis, deobfuscation |
| Document Files | .pdf, .doc, .xls | Malicious documents | Document analysis, macro extraction |
| Archive Files | .zip, .rar, .7z | Compressed containers | Extraction, password cracking |

### Determining File Type

The file extension can be misleading, as malware authors often rename files to disguise their true nature. Analysts use multiple methods to determine file type:

1. **File Signature Analysis**: Files contain "magic bytes" - specific sequences of bytes at the beginning that identify their format.

```
Example PE file signature (DOS header):
00000000: 4d5a 9000 0300 0000 0400 0000 ffff 0000  MZ..............
00000010: b800 0000 0000 0000 4000 0000 0000 0000  ........@.......
```

Common magic bytes:
- PE files: `MZ` (4D 5A)
- PDF files: `%PDF` (25 50 44 46)
- ZIP files: `PK` (50 4B)

2. **Unix `file` Command**: Uses a database of magic numbers to identify file types.
3. **Hex Editors**: Manual inspection of file headers.

## Cryptographic Hashing

Hashing is the process of generating a fixed-size, unique digital fingerprint of a file using cryptographic algorithms. This fingerprint serves as a unique identifier for the file.

### Hash Algorithms Used in Malware Analysis

| Algorithm | Output Size | Characteristics | Common Use |
|-----------|------------|-----------------|------------|
| MD5 | 128 bits | Fast, collision vulnerabilities | Quick identification, basic checks |
| SHA-1 | 160 bits | Better security than MD5, but deprecated | Historical samples, some databases |
| SHA-256 | 256 bits | Current standard, secure | Primary identification, sharing IOCs |
| SHA-3 | Variable | Newest standard, different design | Future-proof identification |
| SSDEEP | Variable | Fuzzy hashing, similar file detection | Clustering similar malware |

### Calculating Hashes

Command-line examples for hash calculation:

**Windows (PowerShell):**
```powershell
Get-FileHash -Algorithm SHA256 malware.exe
```

**Linux/macOS:**
```bash
sha256sum malware.exe
md5sum malware.exe
```

**Python example:**
```python
import hashlib

def calculate_hash(filename, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

print(f"SHA256: {calculate_hash('malware.exe')}")
```

## Uses of Hashes in Malware Analysis

### 1. Sample Identification and Tracking
Hashes provide a unique identifier for malware samples, allowing analysts to:
- Track samples across multiple analyses
- Share indicators with other analysts
- Search for existing analysis in databases

### 2. VirusTotal and Threat Intelligence Integration
Hashes can be submitted to online services like VirusTotal to:
- Check if a file is known malware
- Gather existing analysis reports
- Identify related samples

### 3. Integrity Verification
Hashes verify that files haven't been modified during:
- Transfer between analysts
- Storage and archival
- Analysis procedures

### 4. Clustering and Family Identification
Fuzzy hashing (like SSDEEP) helps identify similar files that might belong to the same malware family, even if they've been slightly modified.

## File Metadata Analysis

Beyond the file content itself, valuable information can be gleaned from file metadata:

### Timestamps
- **Creation, modification, and access times**: Can indicate when malware was compiled or modified
- **Often manipulated** by malware authors to confuse investigators

### PE File Metadata (If Applicable)
For Windows executables, valuable information includes:
- Compilation timestamp
- Imported libraries and functions
- Version information
- Digital signatures (often stolen or forged)

## Tools for File Identification and Hashing

### Command-Line Tools
- **file**: Identifies file type
- **md5sum/sha256sum**: Calculate hashes
- **strings**: Extracts readable text from binary files
- **exiftool**: Extracts metadata from various file types

### Graphical Tools
- **PE-bear**: PE file analyzer
- **HxD**: Hex editor with hash calculation
- **010 Editor**: Advanced template-based hex editor

### Python Libraries
- **pefile**: PE file parsing
- **hashlib**: Hash calculation
- **python-magic**: File type identification

## Practical Workflow Example

```
+---------------------+     +---------------------+     +---------------------+
|    Initial File     |     |   File Identification|     |   Hash Calculation  |
|   malware.bin       |---->|   Type: PE32         |---->|   MD5: a1b2c3...    |
|                     |     |   Size: 245KB        |     |   SHA256: x9y8z7... |
+---------------------+     +---------------------+     +---------------------+
          |                           |                           |
          |                           |                           |
          v                           v                           v
+---------------------+     +---------------------+     +---------------------+
|  Metadata Extraction|     |  VirusTotal Check   |     |   Database Query    |
|   Compile time:     |     |   45/70 detections  |     |   Known sample:     |
|   2023-05-15 14:32  |     |   Family: Emotet    |     |   Emotet variant     |
+---------------------+     +---------------------+     +---------------------+
```

## Advanced Topics: Fuzzy Hashing and Similarity Analysis

Traditional cryptographic hashes are designed to change completely with even minor modifications. Fuzzy hashing addresses this limitation:

### SSDEEP Fuzzy Hashing
SSDEEP creates similar hashes for similar files, allowing analysts to:
- Identify variants of the same malware family
- Detect slightly modified samples
- Cluster related malware

### Example SSDEEP Comparison
```
File1: 3072:u+ysXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2iS2iS2i4S2iS2i:u+sXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2i
File2: 3072:u+ysXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2iS2iS2i4S2iS2i:u+sXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2i
Similarity: 100% (identical files)

File1: 3072:u+ysXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2iS2iS2i4S2iS2i:u+sXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2i
File3: 3072:u+ysXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2iS2iS2i4S2iS2j:u+sXx4iS2i4S2iS2iS2i4S2iS2iS2iS2i4S2iS2j
Similarity: 98% (slightly modified)
```

## Exam Tips

1. **Always verify file type** using multiple methods - never trust the extension alone
2. **SHA-256 is the current standard** for malware identification and sharing IOCs
3. **Remember that hash collisions** are theoretically possible with MD5 and SHA-1
4. **Use fuzzy hashing** when dealing with packed or obfuscated malware that might have multiple variants
5. **Timestamp analysis** can provide valuable clues but can be easily forged
6. **Document all hashes** in your analysis report for future reference and sharing