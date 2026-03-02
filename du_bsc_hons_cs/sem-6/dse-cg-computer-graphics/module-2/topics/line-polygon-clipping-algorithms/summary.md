# Line & Polygon Clipping Algorithms – Quick Revision (Delhi University – BSc (Hons) CS, NEP 2024 UGCF)

**Introduction**  
Clipping is a fundamental rendering operation that discards portions of geometric primitives that lie outside the view‑port (or a user‑defined region). For line segments the problem reduces to cutting a line to fit inside a convex window; for polygons the task becomes removing parts that fall outside a clipping region while preserving the integrity of the resulting polygon. The Delhi University syllabus lists the Cohen‑Sutherland, Liang‑Barsky, Cyrus‑Beck, and Sutherland‑Hodgman algorithms as core topics.

---

### Core Concepts (Bullet‑point Summary)

- **Clipping Window**: Usually a convex rectangle (axis‑aligned) in 2D; can be any convex polygon in more general algorithms.
- **Region Codes (Cohen‑Sutherland)**: 4‑bit code describing the position of a point relative to the four half‑planes (top, bottom, left, right). Enables rapid trivial acceptance/rejection.
- **Parametric Representation**:
  - **Line**: \(P(t) = P_1 + t(P_2-P_1), \; t∈[0,1]\)
  - **Cyrus‑Beck / Liang‑Barsky**: Solve linear inequalities to find the interval of \(t\) that remains inside the clipping region.
- ** Sutherland‑Hodgman Polygon Clipping**:
  - Sequentially clip the polygon against each edge of the convex clipping region.
  - For each edge, iterate over polygon vertices; generate new vertices where edges intersect the clipping boundary.
  - Works for convex clipping regions; can be extended with re‑entrant handling for concave windows.
- **Cohen‑Sutherland (Line Clipping)**
  1. Compute region codes for both endpoints.
  2. If both codes = 0 → **accept** (trivial).
  3. If logical AND of codes ≠ 0 → **reject** (trivial).
  4. Otherwise, compute intersection with one of the four boundary lines, replace the endpoint having the non‑zero code, and repeat.
- **Liang‑Barsky (Parametric Line Clipping)**
  - Treats the clipping window as four inequalities \(p_i t ≤ q_i\).
  - Computes entering (\(t_1\)) and leaving (\(t_2\)) parameters; the clipped segment corresponds to \(t∈[t_1,t_2]\).
  - Efficient for axis‑aligned rectangles; fewer multiplications than Cohen‑Sutherland.
- **Cyrus‑Beck (General Convex Polygon)**
  - Uses normal vectors of each clipping edge to determine \(t\) values for potential entry/exit.
  - Generalises Liang‑Barsky to any convex clipping polygon.
- **Sutherland‑Hodgman (Polygon)**
  - Input: list of polygon vertices.
  - For each clipping edge, produce a new vertex list:
    - **If current vertex inside** and **previous vertex inside** → keep current vertex.
    - **If current inside, previous outside** → add intersection.
    - **If current outside, previous inside** → add intersection, then discard current.
    - **If both outside** → discard both.
  - Resulting vertex list is clipped against the next edge; repeat for all edges.
- **Complexity & Performance**
  - Cohen‑Sutherland: \(O(1)\) per line (constant intersections in worst case).
  - Liang‑Barsky / Cyrus‑Beck: \(O(N)\) where \(N\) = number of clipping edges.
  - Sutherland‑Hodgman: \(O(V·E)\) where \(V\) = vertices, \(E\) = edges of clipping polygon.

---

### Exam‑Focus Tips
- Remember **region‑code** logic for Cohen‑Sutherland and the **parametric inequality** setup for Liang‑Barsky.
- For polygon clipping, be ready to **trace one iteration** of Sutherland‑Hodgman manually: identify inside/outside status, compute intersections, and form the new vertex list.
- Know the **difference between convex and non‑convex** clipping windows; the above algorithms assume convex windows unless additional decomposition is performed.

---

**Conclusion**  
Line clipping (Cohen‑Sutherland, Liang‑Barsky, Cyrus‑Beck) and polygon clipping (Sutherland‑Hodgman) constitute the core algorithmic toolbox for view‑plane operations in computer graphics. Master their region‑code logic, parametric formulation, and step‑by‑step processing to efficiently solve clipping problems in both exam questions and real‑world rendering pipelines.