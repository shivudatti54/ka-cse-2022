### Definitions and Theorems

- **Boundary Point**: A foreground pixel in a binary image that has at least one background pixel in its 8-connected neighborhood.
- **Digital Boundary**: The set of all boundary points forming the perimeter of an object region.
- **Chain Code**: A sequence of directional codes encoding the traversal path along a closed boundary.

### Boundary Following

- **Moore Neighbor Tracing Algorithm**: The standard method for boundary extraction; traverses boundary by examining 8-connected neighbors in counterclockwise order.
- **Starting Point Selection**: Critical for consistent results; commonly uses top-leftmost foreground pixel.
- **Time Complexity**: O(N) where N is the number of boundary pixels.

### Chain Codes

- **Directional Codes**: 4-directional (0-3) or 8-directional (0-7) encoding scheme.
- **Normalization**: First difference calculation and circular rotation ensure rotation and translation invariance.
- **Properties**: Compact representation, easy computation of geometric features, sensitivity to noise.