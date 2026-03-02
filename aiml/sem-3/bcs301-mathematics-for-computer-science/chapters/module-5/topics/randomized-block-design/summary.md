# Randomized Block Design

## Revision Notes

### Definitions and Notations

- **Randomized Block Design (RBD):** A type of experimental design used to control for confounding variables.
- **Block:** A subset of experimental units that are similar in some way.
- **Treatment:** The factor being tested.
- **Replicate:** A set of measurements for a single treatment.
- **Block size:** The number of treatments in a block.
- **Block size (n):** The number of replications.
- **Replicate size (k):** The number of observations per replicate.

### Theorem

- **Blough's Theorem:** For a randomized block design with k replications, n treatments, and b blocks, the expected mean square for treatment (MS-T) is given by:
  \[ MS-T = \frac{1}{nk} \sum*{i=1}^{n} \sum*{j=1}^{b} (T\_{ij} - \overline{T})^2 \]
  where T_ij is the ith treatment in the jth block.

### Formulas

- **Total Sum of Squares (SST):** The sum of the squared differences between all observations and the overall mean:
  \[ SST = \sum*{i=1}^{n} \sum*{j=1}^{b} (X\_{ij} - \overline{X})^2 \]
  where X_ij is the ith observation in the jth block.
- **Sum of Squares for Treatment (SST-T):** The sum of the squared differences between the treatments and the overall mean:
  \[ SST-T = \sum*{i=1}^{n} \sum*{j=1}^{b} (T\_{ij} - \overline{T})^2 \]
- **Mean Square for Treatment (MS-T):** The average of the squared differences between the treatments and the overall mean:
  \[ MS-T = \frac{SST-T}{n-k} \]
- **Mean Square Error (MSE):** The average of the squared differences between the observations and the treatment means:
  \[ MSE = \frac{SST-E} {nk-b} \]
  where E is the error sum of squares.

### Other Key Points

- **Confounding Variable:** A variable that affects the relationship between the treatment and the response variable.
- **Blocking:** The process of dividing the experimental units into blocks to control for confounding variables.
- **Randomization:** The process of randomly assigning treatments to blocks to ensure that the blocks are balanced.
