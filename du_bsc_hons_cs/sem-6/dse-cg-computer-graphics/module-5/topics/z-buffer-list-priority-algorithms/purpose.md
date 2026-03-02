## Purpose and Learning Objectives

**Purpose**  
Real‑time 3D rendering is central to video games, virtual reality, scientific visualisation, and CAD systems. The Z‑Buffer and List‑Priority algorithms are fundamental hidden‑surface removal techniques that ensure correct depth ordering of geometry, enabling visually accurate and performant rendering pipelines. Understanding these algorithms equips students with the knowledge to implement, optimise, and critically evaluate modern graphics systems.

**Learning Objectives**
- Explain the principles of hidden‑surface removal and its importance in the rendering pipeline.
- Describe the Z‑Buffer algorithm, including depth buffer allocation, per‑pixel depth testing, and computational complexity.
- Compare the Z‑Buffer method with list‑priority (painter’s) algorithms in terms of correctness, memory overhead, and runtime performance.
- Implement a basic Z‑Buffer renderer that performs depth testing and colour writes for simple 3D scenes.
- Apply list‑priority sorting strategies to order planar polygons and resolve depth ambiguities.
- Analyse the effects of polygon ordering and limited depth precision on visual artefacts such as z‑fighting.
- Evaluate trade‑offs between software‑based and hardware‑accelerated Z‑Buffer implementations for real‑time applications.
- Design a hybrid rendering approach that combines Z‑Buffer and priority‑list techniques to balance accuracy and efficiency.