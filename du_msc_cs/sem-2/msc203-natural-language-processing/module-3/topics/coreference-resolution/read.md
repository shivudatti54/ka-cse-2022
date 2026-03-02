# Coreference Resolution

## Introduction
Coreference resolution is the NLP task of identifying all linguistic expressions that refer to the same real-world entity in a text. This fundamental discourse analysis problem enables machines to understand context and maintain entity consistency across sentences. For example, resolving "she" to "Dr. Sharma" in "Dr. Sharma published the paper. She received awards." 

This task is crucial for:
1. Machine translation (maintaining pronoun consistency across languages)
2. Text summarization (tracking entities across documents)
3. Dialogue systems (maintaining coherent conversations)
4. Information extraction (linking entity mentions)

Current research challenges include handling implicit references, cross-document coreference, and multilingual resolution. Recent advances use transformer architectures (BERT, SpanBERT) and graph neural networks for better mention detection and clustering.

## Key Concepts
1. **Mention Detection**: Identifying potential references (pronouns, noun phrases, named entities)
2. **Anaphora vs Cataphora**: Forward vs backward references ("The doctor finished *her* rounds" vs "When *she* arrived, Dr. Kapoor...")
3. **Cluster Formation**: Grouping mentions using:
   - Rule-based systems (Hobbs algorithm)
   - Machine learning (mention-pair models)
   - Neural approaches (end-to-end clustering)
4. **Evaluation Metrics**:
   - MUC (link-based)
   - B³ (mention-based)
   - CEAF (entity-based)
5. **Zero-shot Coreference**: Resolving references in unseen domains using models like CorefQA
6. **Cross-document Coreference**: Linking entities across multiple texts (critical for news aggregation)

## Examples
**Example 1: Pronominal Resolution**
Text: "The algorithm achieved 98% accuracy. It was published in ACL 2023."
Steps:
1. Detect mentions: ["The algorithm", "It"]
2. Check gender/number compatibility (neuter)
3. Resolve "It" -> "The algorithm" (same syntactic role)

**Example 2: Bridging Reference**
Text: "The conference room was booked. Its projector malfunctioned."
Resolution:
"Its" refers to "The conference room" via part-whole relationship (bridging coreference)

**Example 3: Winograd Schema**
Text: "The trophy didn't fit in the suitcase because *it* was too large."
Resolution:
Requires world knowledge to determine "it" refers to "trophy" (not suitcase)

## Exam Tips
1. Memorize definitions of anaphora/cataphora with examples
2. Understand differences between MUC, B³, and CEAF metrics
3. Practice drawing coreference chains for complex sentences
4. Study limitations of rule-based vs neural approaches
5. Know recent papers (e.g., SpanBERT for mention detection)
6. Prepare to analyze failure cases (e.g., ambiguous pronouns)
7. Understand how coreference aids downstream tasks like QA systems