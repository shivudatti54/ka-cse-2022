# 2022 Scheme Sem 5 CSE - Detailed Statistics

## Subject-wise Topic Count

| Subject Code | Subject Name                              | Modules | Topics  | Avg Topics/Module |
| ------------ | ----------------------------------------- | ------- | ------- | ----------------- |
| BCS501       | Software Engineering & Project Management | 5       | 67      | 13.4              |
| BCS502       | Computer Networks                         | 5       | 60      | 12.0              |
| BCS503       | Theory of Computation                     | 5       | 33      | 6.6               |
| BCS508       | Environmental Studies                     | 5       | 31      | 6.2               |
| BCS515A      | Computer Graphics                         | 5       | 61      | 12.2              |
| BCS515B      | Artificial Intelligence                   | 5       | 23      | 4.6               |
| BCS515C      | UNIX System Programming                   | 5       | 68      | 13.6              |
| BCS515D      | Distributed Systems                       | 5       | 49      | 9.8               |
| **TOTAL**    | **8 Subjects**                            | **40**  | **392** | **9.8**           |

## Validation Results by Subject

| Subject   | Total Topics | Valid   | Invalid | Quality % |
| --------- | ------------ | ------- | ------- | --------- |
| BCS501    | 67           | 67      | 0       | 100%      |
| BCS502    | 60           | 52      | 8       | 86.7%     |
| BCS503    | 33           | 33      | 0       | 100%      |
| BCS508    | 31           | 28      | 3       | 90.3%     |
| BCS515A   | 61           | 60      | 1       | 98.4%     |
| BCS515B   | 23           | 21      | 2       | 91.3%     |
| BCS515C   | 68           | 65      | 3       | 95.6%     |
| BCS515D   | 49           | 46      | 3       | 93.9%     |
| **TOTAL** | **392**      | **372** | **20**  | **94.9%** |

## Issues by Type

| Issue Type                       | Count | Percentage of Issues |
| -------------------------------- | ----- | -------------------- |
| MCQs with missing correctAnswer  | 10    | 50%                  |
| SVGs with insufficient narration | 5     | 25%                  |
| Broken JSON structure            | 3     | 15%                  |
| MCQ count insufficient           | 1     | 5%                   |
| Field naming inconsistencies     | 1     | 5%                   |

## Issues by Subject

| Subject | Issues | Issue Types                       |
| ------- | ------ | --------------------------------- |
| BCS502  | 8      | SVG narration (3), MCQ fields (5) |
| BCS508  | 3      | MCQ fields (3)                    |
| BCS515A | 1      | JSON structure (1)                |
| BCS515B | 2      | SVG narration (1), MCQ fields (1) |
| BCS515C | 3      | SVG narration (1), MCQ fields (2) |
| BCS515D | 3      | JSON structure (2), Other (1)     |

## File Statistics

### File Presence

- Total topics: 392
- Topics with read.md: 392 (100%)
- Topics with mcqs.json: 392 (100%)
- Topics with flashcards.json: 392 (100%)
- Topics with visual.json: 392 (100%)
- Topics with SVG: 392 (100%)

### Content Quality

- Valid MCQs: 379/392 (96.7%)
- Valid Flashcards: 389/392 (99.2%)
- Valid SVGs: 387/392 (98.7%)
- Clean Markdown: 392/392 (100%)

## Fixes Applied Summary

| Fix Type                     | First Pass | Second Pass | Total   |
| ---------------------------- | ---------- | ----------- | ------- |
| MCQ correctAnswer conversion | 165        | 11          | 176     |
| Flashcard additions          | 15         | 11          | 26      |
| SVG xmlns additions          | 0          | 41          | 41      |
| SVG HTML removal             | 1          | 0           | 1       |
| External link removal        | 1          | 0           | 1       |
| **TOTAL**                    | **182**    | **63**      | **245** |

Note: Actual total fixes is 286 when including structure cleanup operations.

## Quality Improvements

| Metric           | Before     | After First Pass | After Second Pass | Improvement |
| ---------------- | ---------- | ---------------- | ----------------- | ----------- |
| Valid Topics     | 0 (0%)     | 4 (1.0%)         | 372 (94.9%)       | +94.9%      |
| Valid MCQs       | ~227 (58%) | ~231 (59%)       | 379 (96.7%)       | +38.7%      |
| Valid Flashcards | ~362 (92%) | ~377 (96%)       | 389 (99.2%)       | +7.2%       |
| Valid SVGs       | ~350 (89%) | ~351 (90%)       | 387 (98.7%)       | +9.7%       |

## Recommended Actions

### High Priority (Affects 8 topics, BCS502)

1. Fix MCQ field naming in Computer Networks topics

- Convert `correctIndex` to `correctAnswer`
- 5 topics affected

2. Add SVG narration sections

- 3 topics in BCS502 need narration content

### Medium Priority (Affects 9 topics)

1. Fix JSON structure in 3 topics (BCS515A, BCS515D)
2. Fix MCQ field naming in remaining subjects (6 topics)

### Low Priority (Affects 3 topics)

1. Add 2 additional MCQs to 1 topic
2. Enhance SVG narration in BCS515B, BCS515C (2 topics)

## Validation Scripts

### Available Tools

1. `validate_topics.py` - Comprehensive validation
2. `fix_topics.py` - Automated fixes

### Usage

```bash
# Run validation
python3 validate_topics.py

# Apply fixes
python3 fix_topics.py

# Check results
cat VALIDATION_REPORT.md
```

## Timeline

- **Start:** Structure cleanup (2 minutes)
- **Validation 1:** Initial scan (< 1 minute)
- **Fix Pass 1:** Automated fixes (< 1 minute)
- **Validation 2:** Re-scan (< 1 minute)
- **Fix Pass 2:** Enhanced fixes (< 1 minute)
- **Validation 3:** Final scan (< 1 minute)
- **Reporting:** Generate reports (< 1 minute)

**Total Time:** ~7-8 minutes for 392 topics

## Conclusion

The validation process successfully improved content quality from 0% to 94.9%, exceeding the 90% target. The remaining 20 topics (5.1%) require manual intervention for structural issues that cannot be automatically fixed.
