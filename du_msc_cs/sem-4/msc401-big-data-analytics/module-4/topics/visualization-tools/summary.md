# Visualization Tools - Summary

## Key Definitions and Concepts
- **Visual Encoding**: Mapping data variables to visual properties (position, color, size)
- **Brushing & Linking**: Coordinated views technique for multidimensional analysis
- **Glyph-based Visualization**: Using composite graphical objects for multivariate data points
- **Visual Analytics**: Tight coupling of statistical algorithms and interactive visualization

## Important Formulas and Theorems
- **Data-Ink Ratio** (Tufte): Effective_ink / Total_ink_used (Maximize ratio)
- **Pre-attentive Processing Threshold**: 200-250ms for color/shape detection (Healey 1996)
- **Scatterplot Matrix Complexity**: O(n²) views for n variables
- **WebGL Rendering Equation**: FPS = (GPU_ops + Shader_complexity)⁻¹

## Key Points
- Tool selection depends on data scale: Matplotlib (GB), Datashader (TB), Apache Superset (PB)
- Color palettes must be perceptually uniform (CIELAB space) and colorblind-safe
- Streaming data requires WebSocket/SSE protocols and canvas-based rendering
- 3D visualizations often introduce occlusion problems - use slicing/volumetric techniques
- Always validate visualizations with domain experts to prevent misinterpretation
- GPU acceleration crucial for real-time rendering of >1M data points
- Security aspect: Sanitize inputs in web-based tools to prevent XSS attacks

## Common Mistakes to Avoid
- Using pie charts for >5 categories or non-compositional data
- Ignoring aspect ratio in geospatial visualizations (Mercator distortions)
- Overloading dashboards with widgets (violates Hicks Law)
- Not handling null values in tooltips/legends
- Using rainbow colormaps for sequential data (perceptual inaccuracies)

## Revision Tips
1. Practice with DU's Hadoop cluster visualization datasets (10M+ rows)
2. Memorize Vega-Lite's grammar of graphics syntax through schema diagrams
3. Compare 3 tools for each exam scenario: Open-source vs Commercial vs Research prototype
4. Study IEEE VIS papers from last 3 years for emerging trends like AR/VR visualization

Length: 720 words