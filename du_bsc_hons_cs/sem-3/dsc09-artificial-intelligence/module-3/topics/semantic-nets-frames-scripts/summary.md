# Semantic Networks, Frames, and Scripts  

**Introduction**  
These are three classic knowledge‑representation techniques studied under the *Knowledge Representation & Reasoning* module of the Delhi University BSc (Hons) Computer Science (NEP 2024 UGCF) AI syllabus. They enable AI systems to model objects, concepts, and events in a way that supports inference, inheritance, and story understanding.

---

### Semantic Networks  
- **Definition**: A graph‑based model where **nodes** represent concepts and **edges** (arcs) denote binary relations (e.g., *Is‑A*, *Has‑Part*, *Lives‑In*).  
- **Structure**: Nodes are labeled; directed arcs carry relationship names.  
- **Inference**: Traversal of links yields **inheritance** (properties propagate from super‑type to sub‑type) and **association** (retrieving related concepts).  
- **Advantages**: Intuitive, easy to visualise, supports quick reasoning.  
- **Limitations**: Lack of formal semantics, can become cluttered, no built‑in handling of default or probabilistic knowledge.  
- **Example**:  
  ```
  Animal ──Is‑A──> Mammal ──Is‑A──> Dog
  Dog ──Has‑Part──> Tail
  ```

---

### Frames  
- **Definition**: Structured objects (objects of knowledge) that bundle **slots** (attributes) and **fillers** (values) together.  
- **Key Features**  
  - **Slots** can hold values, **procedural attachments** (demons), or **default** information.  
  - **Inheritance**: Frames form a hierarchy; a sub‑frame inherits slot values from its parent unless explicitly overridden.  
  - **Constraints**: Slot facets (e.g., *type*, *cardinality*) validate fillers.  
- **Advantages**: Richer than semantic nets, supports **object‑oriented** concepts, allows default reasoning.  
- **Limitations**: Complexity grows with deep hierarchies; inference can be slower.  
- **Example**  
  ``` 
  Frame: Vehicle
    Slots:
      - Wheels: 4
      - Propulsion: Engine
      - Subclass: Car, Bicycle
  ```

---

### Scripts  
- **Definition**: A representation of a **stereotyped sequence of events** (a scenario) that describes typical situations, roles, and actions.  
- **Components**  
  - **Tracks**: Different variations of the script (e.g., *Restaurant* script may have “Fast‑Food” and “Fine‑Dining” tracks).  
  - **Scenes**: Sequential sub‑events (e.g., *Entering*, *Ordering*, *Eating*, *Leaving*).  
  - **Roles**: Actors involved (e.g., *Customer*, *Server*).  
  - **Props**: Objects used (e.g., *Menu*, *Bill*).  
- **Purpose**: Enable story comprehension, question answering, and plan recognition by matching observed events to expected scripts.  
- **Limitations**: Inflexible for novel situations; requires extensive domain modeling.  
- **Example**  
  ```
  Script: Restaurant
    Track: Fine‑Dining
    Scenes: 1. Enter, 2. Be Seated, 3. Order, 4. Eat, 5. Pay, 6. Leave
  ```

---

**Conclusion**  
Semantic networks, frames, and scripts together provide a spectrum of representational expressiveness—from simple graph structures to richer object‑oriented schemas and event sequences. Mastery of these techniques is essential for the Delhi University AI exam, as they form the foundation for modern knowledge‑representation systems and cognitive modeling.