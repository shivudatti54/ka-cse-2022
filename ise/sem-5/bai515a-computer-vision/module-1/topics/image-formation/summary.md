# Image Formation

## Overview

Image formation is the fundamental process by which 3D scenes are projected onto 2D image planes through optical systems. This process involves geometric transformations, lens optics, and the physics of light capture that form the foundation for all computer vision tasks.

## Key Points

- **Perspective Projection**: Maps 3D world coordinates to 2D image coordinates through pinhole camera model
- **Camera Intrinsics**: Focal length, principal point, and pixel aspect ratio define internal camera geometry
- **Camera Extrinsics**: Rotation and translation define camera position and orientation in world coordinates
- **Pinhole Model**: Simplest camera model where light rays pass through single point to form inverted image
- **Lens Systems**: Real cameras use lens assemblies for focusing with parameters like focal length, aperture, f-number
- **Depth of Field**: Range of distances appearing in focus, controlled by aperture size and focal length
- **Field of View**: Angular extent of observable world, determined by focal length and sensor size

## Important Concepts

- Projection equation relates 3D point to 2D image: similar triangles principle with focal length
- Camera calibration determines intrinsic and extrinsic parameters from known correspondences
- Lens distortions (radial and tangential) must be modeled and corrected for accurate measurements
- Image formation is a many-to-one mapping causing ambiguity in depth recovery

## Notes

- Understand the relationship between focal length, sensor size, and field of view
- Know how to derive the perspective projection equations from geometric principles
- Remember that pinhole model is idealized - real cameras have lens distortions
- Be able to explain why recovering 3D from 2D is an ill-posed problem
- Understand the trade-offs between aperture size, depth of field, and light gathering
