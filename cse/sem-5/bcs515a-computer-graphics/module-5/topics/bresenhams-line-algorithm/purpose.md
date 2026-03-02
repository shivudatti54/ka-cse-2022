# Learning Objectives

After studying this topic, you should be able to:

1. Explain the fundamental concept of raster line drawing and the need for line algorithms in computer graphics.

2. Describe Bresenham's Line Algorithm and explain why it is more efficient than other line drawing algorithms like DDA.

3. Calculate the initial decision parameter P₀ using the formula P₀ = 2Δy - Δx.

4. Apply the algorithm step-by-step to trace and determine which pixels should be illuminated for a given line segment.

5. Update the decision parameter at each iteration using the correct formulas based on whether Pk is negative or non-negative.

6. Extend Bresenham's algorithm to handle lines in all octants by considering symmetry and appropriate coordinate transformations.

7. Compare the advantages of Bresenham's algorithm over DDA, particularly in terms of computational efficiency and accuracy.

8. Implement Bresenham's algorithm for drawing lines with positive, negative, shallow, and steep slopes in practical graphics applications.
