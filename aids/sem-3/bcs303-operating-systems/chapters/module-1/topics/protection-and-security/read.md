# Android Application Security

## Introduction to Android Security Architecture

Android's security model is built on a multi-layered approach that combines system-level protection, application sandboxing, and secure inter-process communication. Understanding this architecture is fundamental to developing secure Android applications.

The core security components include:

- **Linux Kernel Security**: Provides fundamental security features like process isolation, user-based permissions, and secure inter-process communication (IPC)
- **Application Sandbox**: Each app runs in its own isolated environment with dedicated user ID (UID) and file system space
- **Permission System**: Controls access to sensitive APIs and user data
- **Secure Inter-Process Communication**: Binder mechanism for controlled communication between apps
- **Application Signing**: Ensures app integrity and establishes trust between apps

```
+-------------------------------+
|       Android Application     |
+-------------------------------+
|       Application Framework   |
+-------------------------------+
|  Android Runtime (ART/Dalvik) |
+-------------------------------+
|        Linux Kernel           |
+-------------------------------+
|        Hardware Security      |
+-------------------------------+
```

## OWASP Mobile Top 10 for Android

The OWASP Mobile Top 10 provides a prioritized list of the most critical security risks for mobile applications. Here are the most relevant categories for Android development:

### M1: Improper Platform Usage

This category covers misuse of platform features or failure to use platform security controls properly. Examples include:

- Misusing Android Intents
- Incorrect implementation of TouchID, FaceID, or other biometric authentication
- Improper use of the Android KeyChain

### M2: Insecure Data Storage

Sensitive data stored in insecure locations that could be compromised:

- Unencrypted SharedPreferences for sensitive data
- World-readable/writable files
- Insecure database configurations
- Logging sensitive information

### M3: Insecure Communication

Failures in securing network communication:

- Lack of certificate pinning
- Use of weak cryptographic protocols (SSLv3, TLS 1.0)
- Cleartext communication (HTTP instead of HTTPS)
- Improper certificate validation

### M4: Insecure Authentication

Weaknesses in authentication mechanisms:

- Storing credentials insecurely
- Lack of biometric authentication when available
- Weak session management
- Failure to implement proper logout functionality

### M5: Insufficient Cryptography

Problems with cryptographic implementations:

- Use of deprecated or weak algorithms (MD5, SHA1, RC4)
- Hardcoded cryptographic keys
- Improper key management
- Use of custom cryptography instead of proven implementations

### M6: Insecure Authorization

Authorization flaws that allow unauthorized access:

- Inadequate protection of sensitive functionality
- Failure to validate permissions on the server side
- Client-side authorization checks only

### M7: Client Code Quality

General code quality issues that lead to security vulnerabilities:

- Buffer overflows (in native code)
- Code injection vulnerabilities
- Memory corruption issues
- Poor error handling

### M8: Code Tampering

Lack of protection against application modification:

- No integrity checking
- Lack of anti-tampering mechanisms
- Easy reverse engineering

### M9: Reverse Engineering

Insufficient obfuscation and protection:

- Lack of code obfuscation
- Easy extraction of sensitive information from the app
- Clear code structure that aids attackers

### M10: Extraneous Functionality

Hidden backdoors or development features left in production code:

- Debug code left enabled
- Test endpoints accessible in production
- Hidden administrative functionality

## Secure Coding Practices for Android

### Input Validation and Sanitization

All input from external sources must be validated and sanitized to prevent injection attacks and other vulnerabilities.

**Example: Input Validation**

```java
// Validate email input
public boolean isValidEmail(String email) {
    if (email == null) return false;
    String emailPattern = "[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}";
    return email.matches(emailPattern);
}

// Sanitize file paths to prevent directory traversal
public String sanitizeFileName(String input) {
    return input.replaceAll("[^a-zA-Z0-9.-]", "_");
}
```

**Common Validation Techniques:**

- Whitelist validation (preferred over blacklist)
- Regular expression validation
- Type checking
- Length and format validation

### Output Encoding

Proper output encoding prevents Cross-Site Scripting (XSS) and injection attacks when displaying user-generated content.

**Example: HTML Encoding**

```java
public String encodeHtml(String input) {
    return Html.escapeHtml(input);
}

// For WebView content
webView.setWebViewClient(new WebViewClient() {
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
        // Validate URLs before loading
        return !isValidUrl(request.getUrl().toString());
    }
});
```

### Secure Error Handling and Logging

Never expose sensitive information in error messages or logs. Implement proper exception handling that provides minimal information to users while logging appropriate details for debugging.

**Example: Secure Exception Handling**

```java
try {
    // Sensitive operation
    processUserData(userData);
} catch (SecurityException e) {
    // Log detailed error for debugging
    Log.e(TAG, "Security exception in processUserData: " + e.getMessage());

    // Show user-friendly message
    showErrorToast("Operation failed due to security restrictions");
} catch (Exception e) {
    // Generic error handling
    Log.e(TAG, "Error in processUserData", e);
    showErrorToast("An unexpected error occurred");
}
```

**Logging Best Practices:**

- Avoid logging sensitive data (passwords, tokens, PII)
- Use different log levels appropriately (DEBUG, INFO, WARN, ERROR)
- Implement custom loggers that filter sensitive information
- Disable debug logging in production builds

### Secure Coding Standards

Follow established secure coding standards from OWASP and CERT:

**OWASP Secure Coding Practices Checklist:**

- Validate all inputs
- Implement proper authentication and session management
- Use cryptographic standards correctly
- Implement access controls securely
- Protect data in transit and at rest
- Implement proper error handling and logging
- Ensure proper configuration and hardening

**CERT Android Secure Coding Standards:**

- Validate data passed via Intents
- Use appropriate permissions
- Protect sensitive data with encryption
- Secure inter-component communication
- Prevent common vulnerabilities (SQL injection, XSS, etc.)

## Android-Specific Security Mechanisms

### Permission System

Android's permission system controls access to sensitive APIs and user data. Understanding the different permission types is crucial:

| Permission Type | Description                                 | User Interaction    | Protection Level |
| --------------- | ------------------------------------------- | ------------------- | ---------------- |
| Normal          | Low-risk permissions                        | Not required        | automatic        |
| Dangerous       | High-risk permissions                       | Required at runtime | runtime prompt   |
| Signature       | Permissions for same-signature apps         | Not required        | signature match  |
| Special         | Unique permissions like SYSTEM_ALERT_WINDOW | Special handling    | varies           |

**Runtime Permission Request Example:**

```java
// Check if permission is granted
if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
    != PackageManager.PERMISSION_GRANTED) {

    // Request permission
    ActivityCompat.requestPermissions(this,
        new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
        LOCATION_PERMISSION_REQUEST_CODE);
}

// Handle permission result
@Override
public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
    if (requestCode == LOCATION_PERMISSION_REQUEST_CODE) {
        if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            // Permission granted
            startLocationUpdates();
        } else {
            // Permission denied
            showPermissionDeniedMessage();
        }
    }
}
```

### Secure Data Storage

**Sensitive Data Storage Options:**

| Storage Method              | Security Level | Best For                             |
| --------------------------- | -------------- | ------------------------------------ |
| Android KeyStore            | High           | Cryptographic keys, sensitive tokens |
| Encrypted SharedPreferences | Medium-High    | Small sensitive data items           |
| Encrypted SQLite Database   | Medium-High    | Structured sensitive data            |
| Internal Storage            | Medium         | App-private non-sensitive data       |
| External Storage            | Low            | Non-sensitive public files           |

**Example: Using Android KeyStore**

```java
// Generate encryption key
KeyGenParameterSpec keySpec = new KeyGenParameterSpec.Builder(
    KEY_ALIAS,
    KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT)
    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
    .setUserAuthenticationRequired(true)
    .build();

KeyGenerator keyGenerator = KeyGenerator.getInstance(
    KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore");
keyGenerator.init(keySpec);
keyGenerator.generateKey();

// Encrypt data
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
cipher.init(Cipher.ENCRYPT_MODE, key);
byte[] encryptedData = cipher.doFinal(plainText.getBytes());
```

### Secure Network Communication

Always use HTTPS with proper certificate validation. Implement certificate pinning for additional security.

**Example: Certificate Pinning with OkHttp**

```java
// Create certificate pinner
CertificatePinner certificatePinner = new CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
    .build();

// Create HTTP client with pinning
OkHttpClient client = new OkHttpClient.Builder()
    .certificatePinner(certificatePinner)
    .build();
```

**Network Security Configuration:**
Create `network_security_config.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config>
        <domain includeSubdomains="true">example.com</domain>
        <pin-set>
            <pin digest="SHA-256">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=</pin>
            <pin digest="SHA-256">BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

## Security Testing for Android Applications

### Static Application Security Testing (SAST)

SAST tools analyze source code without executing the application to identify potential vulnerabilities.

**Popular SAST Tools for Android:**

- **MobSF (Mobile Security Framework)**: Comprehensive static analysis
- **QARK (Quick Android Review Kit)**: Specifically for Android apps
- **SonarQube**: General code quality with security rules
- **Checkmarx**: Commercial SAST solution
- **Android Lint**: Built-in Android Studio tool

**Common SAST Findings:**

- Hardcoded credentials
- Insecure storage practices
- Improper certificate validation
- Code injection vulnerabilities
- Inadequate encryption implementations

### Dynamic Application Security Testing (DAST)

DAST tools test running applications to identify runtime vulnerabilities.

**DAST Techniques for Android:**

- **Intercepting Proxy Tools**: Burp Suite, OWASP ZAP
- **Runtime Analysis**: Frida, Objection for runtime manipulation
- **Network Traffic Analysis**: Wireshark, tcpdump
- **Dynamic Instrumentation**: Xposed Framework

**Example DAST Test Cases:**

- Testing for insecure data storage
- Analyzing network traffic for cleartext data
- Testing authentication bypass
- Checking for client-side injection vulnerabilities

### Mobile Security Testing Tools Comparison

| Tool       | Type      | Capabilities                               | Cost        |
| ---------- | --------- | ------------------------------------------ | ----------- |
| MobSF      | SAST/DAST | Comprehensive analysis, APK scanning       | Open Source |
| QARK       | SAST      | Android-specific vulnerabilities           | Open Source |
| Burp Suite | DAST      | Network traffic interception, manipulation | Commercial  |
| Frida      | Dynamic   | Runtime manipulation, hooking              | Open Source |
| OWASP ZAP  | DAST      | Web application testing, includes mobile   | Open Source |

## Secure Development Lifecycle for Android

### Threat Modeling

Threat modeling helps identify potential security issues early in the development process.

**STRIDE Model for Android Applications:**

- **Spoofing**: Fake authentication, tampered apps
- **Tampering**: Data modification, code changes
- **Repudiation**: Logging issues, transaction denial
- **Information Disclosure**: Data leakage, insecure storage
- **Denial of Service**: Resource exhaustion, crash attacks
- **Elevation of Privilege**: Permission bypass, root access

**Threat Modeling Process:**

1. Diagram the application architecture
2. Identify assets and trust boundaries
3. Identify potential threats
4. Mitigate identified threats
5. Validate and document

### DevSecOps Integration

Integrate security throughout the CI/CD pipeline:

**CI/CD Security Steps:**

1. **Code Commit**: Pre-commit hooks with security checks
2. **Build**: SAST scanning, dependency checking
3. **Test**: DAST testing, security unit tests
4. **Deploy**: Runtime protection, monitoring

**Example GitHub Actions Workflow:**

```yaml
name: Android Security CI

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up JDK
        uses: actions/setup-java@v1
        with:
          java-version: '11'
      - name: Run SAST with MobSF
        run: |
          docker run -it --rm -v $(pwd):/app opensecurity/mobsf:latest
      - name: Dependency check
        run: |
          ./gradlew dependencyCheckAnalyze
      - name: Lint check
        run: |
          ./gradlew lint
```

## Exam Tips

1. **Understand Android Security Architecture**: Focus on the sandbox model, permission system, and application signing
2. **Know OWASP Mobile Top 10**: Be able to identify and explain each vulnerability category with Android-specific examples
3. **Master Secure Storage Options**: Understand when to use KeyStore, encrypted preferences, and other storage mechanisms
4. **Practice Permission Handling**: Be comfortable with runtime permission requests and handling denial scenarios
5. **Recognize Testing Approaches**: Differentiate between SAST and DAST and know the appropriate tools for each
6. **Remember Network Security**: Always prioritize HTTPS, certificate pinning, and proper network security configuration
7. **Think Like an Attacker**: Consider how each security control could be bypassed or exploited
