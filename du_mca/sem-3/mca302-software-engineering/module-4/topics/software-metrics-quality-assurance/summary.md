# Software Metrics and Quality Assurance - Summary

## Key Definitions and Concepts

- **Software Metrics**: Quantitative measures used to assess software products, processes, and projects. Categorized as product, process, and project metrics.

- **Function Points (FP)**: Size metric measuring functionality from user perspective, independent of programming language. Calculated as: FP = Total Weight × Value Adjustment Factor.

- **Cyclomatic Complexity**: Measure of control flow complexity representing linearly independent paths. Formula: M = E - N + 2P or M = Number of Decision Points + 1.

- **Defect Density**: Quality metric calculated as Number of Defects divided by Size (per KLOC or function point).

- **Quality Assurance (QA)**: Process-oriented, preventive approach focusing on improving development processes to prevent defects.

- **Quality Control (QC)**: Product-oriented, detective approach focusing on detecting and correcting defects through testing and inspection.

## Important Formulas and Theorems

- **Cyclomatic Complexity**: M = E - N + 2P or M = Decision Points + 1
- **Function Points**: FP = Σ(Component Weights) × VAF
- **Defect Density**: Defects / Size (per KLOC or FP)
- **Defect Removal Efficiency (DRE)**: (Defects Removed / Total Defects) × 100%
- **Halstead Volume**: V = N × log2(n), where N = total operators/operands, n = unique operators/operands

## Key Points

- Software metrics provide objective, quantitative data for project management and quality decisions.
- Function points measure user-perceived functionality and are language-independent, making them superior to LOC for cross-project comparisons.
- Cyclomatic complexity > 10 indicates code requiring careful testing; > 20 indicates high-risk code.
- ISO 25010 defines eight quality characteristics: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability.
- Quality Assurance prevents defects through process improvement; Quality Control detects defects through testing.
- Industry benchmark for excellent quality: < 1 defect per thousand LOC.
- Metrics should be used in combination—not relying on a single metric provides better insight.
- Process metrics enable continuous improvement of development practices.

## Common Mistakes to Avoid

- Confusing Quality Assurance with Quality Control—QA is preventive and process-focused, QC is detective and product-focused.
- Using LOC alone for size measurement—它 varies with language and coding style, making cross-project comparisons unreliable.
- Interpreting high complexity as always bad—some complexity is necessary; focus on managing unnecessary complexity.
- Ignoring the context of metrics—defect density benchmarks vary by application domain and development methodology.

## Revision Tips

1. Practice calculating cyclomatic complexity from flow graphs and pseudo-code—this is frequently tested in exams.

2. Memorize ISO 25010's eight quality characteristics and their sub-characteristics for quality model questions.

3. Understand the relationships: higher complexity often leads to lower maintainability and higher defect density.

4. Review function point calculation examples to understand component weighting and VAF adjustment.

5. Know industry benchmarks for defect density: < 1 (excellent), 1-2 (good), 2-5 (average), > 5 (poor).

6. Create comparison tables for different metrics types (product vs. process vs. project) and quality models (McCall vs. ISO 25010).