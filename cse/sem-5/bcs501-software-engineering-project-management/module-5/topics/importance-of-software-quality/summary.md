# Importance of Software Quality - Summary

## Key Definitions and Concepts

- **Software Quality**: The degree to which a software product meets specified requirements and customer expectations across eight dimensions: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability (ISO 25010).
- **Software Quality Assurance (SQA)**: A process-oriented, preventive approach encompassing all activities aimed at ensuring software meets quality standards throughout the development lifecycle.
- **Software Testing**: A product-oriented, detective activity that evaluates software to identify defects; a component of SQA but not synonymous with it.
- **Defect Density**: The number of defects per thousand lines of code (KLOC), calculated as Number of Defects / Size in KLOC. Industry benchmark for good quality is 1-3 defects/KLOC.

## Important Formulas and Theorems

- **Cost of Quality**: Total cost = Prevention Costs + Appraisal Costs + Failure Costs (Internal + External)
- **Defect Density**: DD = Number of Defects / Size in KLOC
- **Defect Detection Ratio**: DDR = (Defects Found in Testing / Total Defects) × 100%
- **Shift Left Principle**: Moving quality activities earlier in the development lifecycle reduces defect fix costs exponentially as the project progresses.

## Key Points

- External failure costs can be 30-100 times higher than fixing defects in requirements or design phases
- Prevention-oriented quality approaches are more economically viable than purely detective approaches
- The McCall Quality Model identifies eleven quality factors including correctness, reliability, and usability
- CMMI defines five maturity levels from Initial (ad-hoc) to Optimizing (continuously improving)
- Modern practices emphasize continuous integration, automated testing, and Test-Driven Development (TDD)
- Quality metrics should be tracked over time to identify trends rather than relying on single measurements
- Software quality directly impacts business outcomes including costs, customer satisfaction, and competitive advantage

## Common Mistakes to Avoid

- Confusing Software Quality Assurance with Software Testing—they are related but distinct concepts
- Assuming that more testing automatically means better quality; effectiveness matters more than volume
- Relying solely on defect density without considering defect severity or customer impact
- Treating quality as a final phase rather than an integrated activity throughout development
- Ignoring the cost-benefit analysis of quality investments; diminishing returns apply beyond optimal investment levels

## Revision Tips

1. Create a comparison table between ISO 25010 characteristics and McCall quality factors
2. Practice calculating defect density and interpreting results against industry benchmarks
3. Remember that "shift left" refers to moving quality activities earlier in the lifecycle
4. Focus on understanding why prevention is more cost-effective than detection—know the cost ratios
5. Review real-world software failures (like the Mars Orbiter) to appreciate the consequences of poor quality
