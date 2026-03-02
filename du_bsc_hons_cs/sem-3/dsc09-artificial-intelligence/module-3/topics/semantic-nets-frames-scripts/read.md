# Semantic Networks, Frames, and Scripts

## A Comprehensive Study Material for BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

Knowledge representation is a fundamental pillar of Artificial Intelligence that deals with how knowledge can be encoded in a form that a computer system can utilize to solve complex problems. Among the various knowledge representation paradigms, **Semantic Networks**, **Frames**, and **Scripts** represent classic approaches that attempt to model human knowledge structure in a computationally tractable manner.

These representation schemes emerged from the recognition that human memory and understanding are highly structured—concepts are not stored in isolation but are interconnected through relationships. For the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, this topic forms a crucial component of the Artificial Intelligence paper, typically carrying significant weightage in examinations.

### Real-World Relevance

The practical applications of these knowledge representation techniques are extensive:

- **Natural Language Processing**: Semantic networks enable machines to understand word meanings and relationships
- **Expert Systems**: Frames provide structured templates for representing domain knowledge
- **Story Understanding**: Scripts help AI systems comprehend narratives and predict events
- **Recommendation Systems**: Semantic relationships power content-based filtering
- **Ontology Development**: Modern knowledge graphs (like Google's Knowledge Graph) evolved from semantic network concepts
- **Medical Diagnosis**: Frame-based expert systems represent symptoms and diseases

---

## 2. Semantic Networks

### 2.1 Definition and Overview

A **Semantic Network** (or Semantic Net) is a directed graph structure consisting of nodes (representing concepts, objects, or entities) and edges (representing relationships between these concepts). The term "semantic" refers to meaning—the network captures the meaning of concepts through their relationships.

Semantic networks were first introduced by Ross Quillian in 1966 as a model for human semantic memory. They provide a natural way to represent hierarchical, associative, and relational knowledge.

### 2.2 Components

| Component | Description |
|-----------|-------------|
| **Nodes** | Represent concepts, objects, events, or states |
| **Edges/Arcs** | Represent relationships or associations between nodes |
| **Labels** | Name the type of relationship (IS-A, HAS-A, etc.) |
| **Pointers** | Connect related nodes bidirectionally |

### 2.3 Types of Relationships

Semantic networks utilize various relationship types:

1. **ISA (Is-A) / AKO (A-Kind-Of)**: Expresses inheritance hierarchy
   - `Robin ISA Bird` means "A robin is a kind of bird"

2. **HAS-A / PART-OF**: Represents composition/aggregation
   - `Car HAS-A Engine`
   - `Hand PART-OF Body`

3. **Instance**: Connects specific instances to their classes
   - `Tweety Instance Bird`

4. **Attributes**: Describe properties of nodes
   - `Color(Apple) = Red`

5. **Member-of**: Relates elements to sets
   - `Delhi Member-of Indian_Cities`

### 2.4 Example: Animal Classification

```
                    [ENTITY]
                       |
                   [ANIMAL]
                   /   |   \
           [MAMAL]   [BIRD]  [FISH]
              |        |        |
         [CARNIVORE] [CAN_FLY] [CAN_SWIM]
              |        |
        [LION]      [EAGLE]
        /    \      /     \
    [ROARS] [HAS_MANE] [FLIES] [HAS_TALONS]
```

### 2.5 Implementation in Python

```python
class SemanticNetwork:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node_name, attributes=None):
        """Add a concept/node to the network"""
        self.nodes[node_name] = attributes if attributes else {}
    
    def add_edge(self, from_node, to_node, relation):
        """Add a relationship between nodes"""
        if from_node in self.nodes and to_node in self.nodes:
            self.edges.append({
                'from': from_node,
                'to': to_node,
                'relation': relation
            })
    
    def get_relations(self, node):
        """Retrieve all relationships for a node"""
        relations = []
        for edge in self.edges:
            if edge['from'] == node or edge['to'] == node:
                relations.append(edge)
        return relations
    
    def find_path(self, start, end, path=[]):
        """Find path between two nodes using BFS"""
        path = path + [start]
        if start == end:
            return path
        if start not in self.nodes:
            return None
        
        for edge in self.edges:
            if edge['from'] == start and edge['to'] not in path:
                new_path = self.find_path(edge['to'], end, path)
                if new_path:
                    return new_path
        return None

# Example usage
sn = SemanticNetwork()

# Add nodes (concepts)
nodes = ['Animal', 'Bird', 'Fish', 'Mammal', 'Eagle', 'Shark', 'Lion']
for node in nodes:
    sn.add_node(node)

# Add edges (relationships)
sn.add_edge('Animal', 'Bird', 'ISA')
sn.add_edge('Animal', 'Fish', 'ISA')
sn.add_edge('Animal', 'Mammal', 'ISA')
sn.add_edge('Bird', 'Eagle', 'ISA')
sn.add_edge('Fish', 'Shark', 'ISA')
sn.add_edge('Mammal', 'Lion', 'ISA')
sn.add_edge('Bird', 'CAN_FLY', 'HAS_PROPERTY')
sn.add_edge('Fish', 'CAN_SWIM', 'HAS_PROPERTY')

# Query the network
print("Relations for Eagle:", sn.get_relations('Eagle'))
print("Path from Animal to Lion:", sn.find_path('Animal', 'Lion'))
```

### 2.6 Advantages and Limitations

| Advantages | Limitations |
|------------|-------------|
| Natural, intuitive representation | Can become exponentially large |
| Supports inference through inheritance | No standardized formalism |
| Hierarchical knowledge representation | Ambiguous interpretation of edges |
| Efficient for associative retrieval | Network traversal can be computationally expensive |
| Easy to visualize and understand | Difficulty handling exceptions to rules |

---

## 3. Frames

### 3.1 Definition and Overview

**Frames** were introduced by Marvin Minsky in 1974 as a data structure for representing stereotyped situations, objects, or concepts. A frame is a knowledge representation scheme that organizes knowledge into hierarchical structures with slots, where each slot can hold specific values, constraints, or pointers to other frames.

Frames combine declarative and procedural knowledge, making them particularly powerful for representing complex, structured information. They can be viewed as an extension of semantic networks with added capabilities for default reasoning, constraints, and procedural attachment.

### 3.2 Structure of a Frame

A frame consists of:

1. **Frame Name**: Identifies the frame concept
2. **Slots**: Attributes or properties of the concept
3. **Facets**: Specifications that describe how slot values should be handled
4. **Slot Values**: Actual data or pointers to other frames
5. **Inheritance**: Property where frames can inherit from parent frames

### 3.3 Types of Slots

```
┌─────────────────────────────────────────┐
│            FRAME: PERSON                │
├─────────────────────────────────────────┤
│  Slots:                                 │
│  ├─ Name: [Value: REQUIRED]            │
│  ├─ Age: [Value: INTEGER, Range: 0-150]│
│  ├─ Occupation: [Default: UNEMPLOYED]  │
│  ├─ Spouse: [Value: PERSON]            │
│  ├─ Children: [Value: LIST OF PERSON]  │
│  └─ Address: [Frame: ADDRESS]          │
│                                         │
│  Facets:                                │
│  ├─ IF-NEEDED: compute_age()           │
│  ├─ IF-ADDED: validate_person()        │
│  └─ IF-REMOVED: update_dependents()    │
└─────────────────────────────────────────┘
```

### 3.4 Facets and Their Purposes

| Facet | Purpose | Example |
|-------|---------|---------|
| **Value** | Specifies allowed values | Color: {Red, Green, Blue} |
| **Default** | Value used when no specific value is provided | Age: Default is 0 |
| **Range** | Numerical constraints | Age: Range 0-150 |
| **Required** | Must have a value | Name: Required |
| **IF-NEEDED** | Procedure called when value is accessed | IF-NEEDED: compute_age() |
| **IF-ADDED** | Procedure called when value is set | IF-ADDED: validate_entry() |
| **IF-REMOVED** | Procedure called when value is deleted | IF-REMOVED: cleanup_relations() |

### 3.5 Inheritance in Frames

Frames support multiple inheritance through the ISA relationship:

```
                    [ANIMAL]
                    /   |   \
             [MAMMAL] [BIRD] [FISH]
                |        |        |
           [CARNIVORE] [FLYING] [SWIMMING]
                |        |
           [LION]    [EAGLE]
           
Frame: LION
  ISA: CARNIVORE, MAMMAL
  Default-Properties:
    - Color: Golden
    - Habitat: Grassland
    - Is-Dangerous: Yes
    
Frame: EAGLE
  ISA: FLYING, BIRD
  Default-Properties:
    - Color: Brown
    - Can-Fly: Yes
    - Habitat: Mountains
```

When querying properties, the system searches up the inheritance hierarchy to find values.

### 3.6 Frame Implementation in Python

```python
class Frame:
    def __init__(self, name, parent_frames=None):
        self.name = name
        self.slots = {}
        self.parent_frames = parent_frames if parent_frames else []
        
    def add_slot(self, slot_name, value=None, default=None, 
                 facet_type=None, range_restriction=None):
        """Add a slot to the frame"""
        self.slots[slot_name] = {
            'value': value,
            'default': default,
            'facet_type': facet_type,
            'range': range_restriction
        }
    
    def get_slot_value(self, slot_name):
        """Get slot value with inheritance"""
        # Check own slots first
        if slot_name in self.slots:
            slot = self.slots[slot_name]
            if slot['value'] is not None:
                return slot['value']
            elif slot['default'] is not None:
                return slot['default']
        
        # Search parent frames for inheritance
        for parent in self.parent_frames:
            parent_value = parent.get_slot_value(slot_name)
            if parent_value is not None:
                return parent_value
        
        return None
    
    def set_slot_value(self, slot_name, value):
        """Set a slot value with validation"""
        if slot_name in self.slots:
            slot = self.slots[slot_name]
            if slot['range'] and value not in slot['range']:
                print(f"Value {value} not in allowed range {slot['range']}")
                return False
        self.slots[slot_name] = {'value': value}
        return True
    
    def display(self):
        """Display frame contents"""
        print(f"\nFrame: {self.name}")
        print("ISA:", [p.name for p in self.parent_frames])
        print("Slots:")
        for slot_name, slot_data in self.slots.items():
            print(f"  {slot_name}: {slot_data}")

# Create frame hierarchy for a university system

# Base frame
person_frame = Frame("PERSON")
person_frame.add_slot("can_breathe", default=True)
person_frame.add_slot("has_heart", default=True)
person_frame.add_slot("age", range_restriction=(0, 150))

# Student frame inherits from PERSON
student_frame = Frame("STUDENT", parent_frames=[person_frame])
student_frame.add_slot("enrolled", default=True)
student_frame.add_slot("major", default="Undeclared")
student_frame.add_slot("gpa", range_restriction=(0.0, 4.0), default=0.0)

# Undergrad frame inherits from STUDENT
undergrad_frame = Frame("UNDERGRAD", parent_frames=[student_frame])
undergrad_frame.add_slot("year", range_restriction=(1, 5), default=1)
undergrad_frame.add_slot("minor", value=None)

# Set specific values
undergrad_frame.set_slot_value("gpa", 3.75)
undergrad_frame.set_slot_value("major", "Computer Science")

# Demonstrate inheritance
undergrad_frame.display()
print("\nInherited properties:")
print(f"  can_breathe: {undergrad_frame.get_slot_value('can_breathe')}")
print(f"  has_heart: {undergrad_frame.get_slot_value('has_heart')}")
print(f"  age range: {undergrad_frame.slots['age']['range']}")
```

### 3.7 Frame Example: University Course System

```
┌─────────────────────────────────────────────────────────────────┐
│                     FRAME: COURSE                               │
├─────────────────────────────────────────────────────────────────┤
│  Course_Code: [Value: Required, Pattern: XXXX-###]            │
│  Course_Name: [Value: Required]                                │
│  Credits: [Value: {1,2,3,4}, Default: 3]                       │
│  Instructor: [Value: FACULTY]                                  │
│  Prerequisites: [Value: LIST OF COURSE]                        │
│  Schedule: [Value: SLOT-CLASS SCHEDULE]                       │
│  Enrollment: [IF-NEEDED: count_enrolled()]                     │
│  Max_Strength: [Value: 60, Default: 60]                        │
│                                                                 │
│  IF-ADDED: [validate_course()]                                 │
│  IF-REMOVED: [notify_administrator()]                          │
└─────────────────────────────────────────────────────────────────┘
```

### 3.8 Advantages of Frames

- **Structured Organization**: Frames provide a hierarchical, organized approach to knowledge representation
- **Default Reasoning**: Support for default values enables handling incomplete information
- **Inheritance**: Properties can be inherited, reducing redundancy
- **Procedural Attachment**: Facets allow embedding procedural knowledge
- **Modularity**: Frames can be organized as independent modules
- **Multiple Inheritance**: Support for complex conceptual relationships

---

## 4. Scripts

### 4.1 Definition and Overview

**Scripts** were introduced by Roger Schank and Robert Abelson in 1977 as a knowledge representation structure for representing stereotypical sequences of events or situations. While frames represent static knowledge about objects and concepts, scripts represent dynamic, temporal knowledge about events and actions.

A script is essentially a structured representation of a standard sequence of events that occurs in a particular context. It helps AI systems predict what will happen next in a given situation and understand narratives by filling in implicit information.

### 4.2 Components of a Script

A script consists of several key components:

| Component | Description |
|-----------|-------------|
| **Track** | The specific type or variation of the script |
| **Entry Conditions** | Conditions that must be true for the script to apply |
| **Props** | Objects/entities involved in the events |
| **Roles** | Functions played by participants |
| **Scenes** | Sequential episodes that make up the event sequence |
| **Results** | State changes that occur after the script executes |
| **Inference** | Implicit conclusions that can be drawn |

### 4.3 Structure of a Script

```
┌─────────────────────────────────────────────────────────────────┐
│                     SCRIPT: RESTAURANT                          │
├─────────────────────────────────────────────────────────────────┤
│  Track: Casual Dining                                           │
│                                                                 │
│  Entry Conditions:                                              │
│    - Customer is hungry                                         │
│    - Customer has money                                         │
│    - Restaurant is open                                         │
│                                                                 │
│  Props:                                                         │
│    - Table, Menu, Food, Bill, Money, Waiter                    │
│                                                                 │
│  Roles:                                                         │
│    - Customer, Waiter, Chef, Cashier                           │
│                                                                 │
│  Scenes:                                                        │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ Scene 1: ENTERING                                      │ │
│    │   - Customer enters restaurant                         │ │
│    │   - Host greets customer                               │ │
│    │   - Customer is seated                                 │ │
│    └─────────────────────────────────────────────────────────┘ │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ Scene 2: ORDERING                                       │ │
│    │   - Waiter brings menu                                 │ │
│    │   - Customer reads menu                                 │ │
│    │   - Customer places order                              │ │
│    │   - Waiter takes order to kitchen                      │ │
│    └─────────────────────────────────────────────────────────┘ │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ Scene 3: EATING                                         │ │
│    │   - Food is prepared                                   │ │
│    │   - Waiter serves food                                 │ │
│    │   - Customer eats                                      │ │
│    └─────────────────────────────────────────────────────────┘ │
│    ┌─────────────────────────────────────────────────────────┐ │
│    │ Scene 4: LEAVING                                        │ │
│    │   - Waiter brings bill                                 │ │
│    │   - Customer pays                                      │ │
│    │   - Customer leaves                                    │ │
│    └─────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Results:                                                       │
│    - Customer is satisfied                                     │
│    - Customer's hunger is reduced                              │
│    - Restaurant gains revenue                                  │
│                                                                 │
│  Inferences:                                                   │
│    - Customer used money                                       │
│    - Customer consumed food                                    │
│    - Restaurant staff were involved                           │
└─────────────────────────────────────────────────────────────────┘
```

### 4.4 Script Implementation in Python

```python
class ScriptEvent:
    def __init__(self, action, actor, object=None, instrument=None):
        self.action = action
        self.actor = actor
        self.object = object
        self.instrument = instrument
    
    def __str__(self):
        return f"{self.actor} {self.action}" + \
               (f" {self.object}" if self.object else "") + \
               (f" with {self.instrument}" if self.instrument else "")

class Script:
    def __init__(self, name, track=None):
        self.name = name
        self.track = track
        self.entry_conditions = []
        self.props = []
        self.roles = []
        self.scenes = []
        self.results = []
        self.inferences = []
    
    def add_entry_condition(self, condition):
        self.entry_conditions.append(condition)
    
    def add_prop(self, prop):
        self.props.append(prop)
    
    def add_role(self, role):
        self.roles.append(role)
    
    def add_scene(self, scene_name, events):
        self.scenes.append({'name': scene_name, 'events': events})
    
    def add_result(self, result):
        self.results.append(result)
    
    def add_inference(self, inference):
        self.inferences.append(inference)
    
    def check_conditions(self, state):
        """Check if entry conditions are satisfied"""
        satisfied = []
        for condition in self.entry_conditions:
            if condition in state:
                satisfied.append(condition)
        return satisfied, len(satisfied) == len(self.entry_conditions)
    
    def execute(self, context):
        """Execute the script and generate predictions"""
        print(f"\n=== Executing Script: {self.name} ===")
        print(f"Track: {self.track}")
        print(f"\nEntry Conditions: {self.entry_conditions}")
        print(f"Props: {self.props}")
        print(f"Roles: {self.roles}")
        
        print("\n--- Scene Sequence ---")
        for scene in self.scenes:
            print(f"\n[{scene['name']}]")
            for event in scene['events']:
                print(f"  → {event}")
        
        print(f"\n--- Results ---")
        for result in self.results:
            print(f"  ✓ {result}")
        
        print(f"\n--- Inferences ---")
        for inference in self.inferences:
            print(f"  ∘ {inference}")

# Create Restaurant Script
restaurant_script = Script("RESTAURANT", "Casual Dining")
restaurant_script.add_entry_condition("Customer is hungry")
restaurant_script.add_entry_condition("Customer has money")
restaurant_script.add_entry_condition("Restaurant is open")

restaurant_script.add_prop("Table")
restaurant_script.add_prop("Menu")
restaurant_script.add_prop("Food")
restaurant_script.add_prop("Bill")
restaurant_script.add_prop("Money")

restaurant_script.add_role("Customer")
restaurant_script.add_role("Waiter")
restaurant_script.add_role("Chef")
restaurant_script.add_role("Host")

# Scene 1: Entering
restaurant_script.add_scene("ENTERING", [
    ScriptEvent("enters", "Customer", "restaurant"),
    ScriptEvent("greets", "Host", "Customer"),
    ScriptEvent("seats", "Host", "Customer", "table")
])

# Scene 2: Ordering
restaurant_script.add_scene("ORDERING", [
    ScriptEvent("brings", "Waiter", "menu"),
    ScriptEvent("reads", "Customer", "menu"),
    ScriptEvent("places", "Customer", "order"),
    ScriptEvent("takes", "Waiter", "order", "kitchen")
])

# Scene 3: Eating
restaurant_script.add_scene("EATING", [
    ScriptEvent("prepares", "Chef", "food"),
    ScriptEvent("serves", "Waiter", "food"),
    ScriptEvent("eats", "Customer", "food")
])

# Scene 4: Leaving
restaurant_script.add_scene("LEAVING", [
    ScriptEvent("brings", "Waiter", "bill"),
    ScriptEvent("pays", "Customer", "bill", "money"),
    ScriptEvent("leaves", "Customer", "restaurant")
])

# Results and Inferences
restaurant_script.add_result("Customer hunger reduced")
restaurant_script.add_result("Restaurant gained revenue")
restaurant_script.add_result("Customer is satisfied")

restaurant_script.add_inference("Customer used money")
restaurant_script.add_inference("Chef prepared food")
restaurant_script.add_inference("Waiter facilitated service")

# Execute script
current_state = ["Customer is hungry", "Customer has money", "Restaurant is open"]
restaurant_script.execute(current_state)
```

### 4.5 Another Example: Movie Theatre Script

```
┌─────────────────────────────────────────────────────────────────┐
│                      SCRIPT: MOVIE                              │
├─────────────────────────────────────────────────────────────────┤
│  Track: Standard Movie Viewing                                  │
│                                                                 │
│  Entry Conditions:                                              │
│    - Person wants to watch movie                                │
│    - Person has ticket                                          │
│                                                                 │
│  Props:                                                         │
│    - Ticket, Popcorn, Soda, Seat, Screen, Movie                │
│                                                                 │
│  Roles:                                                         │
│    - Viewer, Ticket Seller, Concession Worker                  │
│                                                                 │
│  Scenes:                                                        │
│    1. BUYING TICKET: Purchase ticket, Enter theatre           │
│    2. GETTING SNACKS: Buy popcorn/soda, Enter theatre          │
│    3. FINDING SEAT: Locate seat, Sit down                      │
│    4. WATCHING: View trailers, Watch movie                     │
│    5. LEAVING: Exit theatre, Dispose waste                     │
│                                                                 │
│  Results:                                                       │
│    - Person watched movie                                       │
│    - Money transferred                                          │
│    - Person experienced entertainment                          │
│                                                                 │
│  Inferences:                                                    │
│    - Person sat in dark                                         │
│    - Person consumed snacks                                    │
│    - Person saw visual content                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.6 Applications of Scripts

- **Story Understanding**: AI systems use scripts to understand narratives and predict plot developments
- **Question Answering**: Scripts help answer implicit questions about situations
- **Dialogue Systems**: Virtual assistants use scripts to understand user intents
- **Plan Recognition**: Understanding user actions in context
- **Text Comprehension**: Filling in missing information in texts
- **Expert Systems**: Representing procedural knowledge in domains

### 4.7 Advantages and Limitations

| Advantages | Limitations |
|------------|-------------|
| Captures temporal/sequential knowledge | Limited flexibility for novel situations |
| Enables prediction of unstated events | Can be too rigid for complex scenarios |
| Supports inference and comprehension | Requires significant manual authoring |
| Models human memory structures | Difficulty handling exceptions |
| Useful for story understanding | May not scale to diverse real-world events |

---

## 5. Comparison: Semantic Networks, Frames, and Scripts

| Aspect | Semantic Networks | Frames | Scripts |
|--------|-------------------|--------|---------|
| **Primary Purpose** | Represent relationships between concepts | Represent static knowledge about objects | Represent temporal sequences of events |
| **Structure** | Graph (nodes + labeled edges) | Hierarchical with slots and facets | Sequential scenes with events |
| **Knowledge Type** | Declarative | Declarative + Procedural | Procedural |
| **Inference** | Traversal, inheritance | Default reasoning, inheritance | Prediction, completion |
| **Strength** | Relationship modeling | Structured organization | Event sequence modeling |
| **Best For** | Conceptual hierarchies | Object-oriented domains | Narrative understanding |

---

## 6. Key Takeaways

1. **Semantic Networks** are directed graphs that represent knowledge through nodes (concepts) and edges (relationships), supporting inheritance and associative reasoning.

2. **Frames** extend semantic networks by organizing knowledge into hierarchical structures with slots containing values, defaults, and procedural attachments (facets).

3. **Scripts** represent stereotypical sequences of events, enabling AI systems to predict outcomes and understand narratives by filling in implicit information.

4. These representation schemes were foundational to early AI research and influenced modern technologies like knowledge graphs and ontologies.

5. Each representation has specific strengths: semantic networks for relationships, frames for structured objects, and scripts for event sequences.

6. Python implementations demonstrate how these theoretical concepts can be practically realized in software systems.

7. Understanding these paradigms is essential for comprehending the evolution of knowledge representation in AI and their continued relevance in modern applications.

---

## 7. Assessment Items

### 7.1 Multiple Choice Questions (Level - Application & Analysis)

1. **In a semantic network, if "Sparrow ISA Bird" and "Bird ISA Animal", which of the following is TRUE about inheritance?**
   - (a) Sparrow inherits all properties of Animal directly
   - (b) Inheritance in semantic networks is automatic through ISA links
   - (c) Sparrow cannot inherit properties from Animal
   - (d) Properties must be manually copied to each node

2. **A frame has a slot "Age" with a facet "IF-NEEDED: compute_age()". When will this procedure be invoked?**
   - (a) When the age value is deleted
   - (b) When the age value is modified
   - (c) When the age value is accessed but not present
   - (d) When a new frame is created

3. **Which component of a script represents the objects involved in the event sequence?**
   - (a) Props
   - (b) Roles
   - (c) Scenes
   - (d) Entry Conditions

4. **In the restaurant script, if the entry condition "Customer has money" is not satisfied, what happens?**
   - (a) The script executes partially
   - (b) The script cannot be applied
   - (c) The script modifies the condition
   - (d) The script skips to the next scene

5. **Which knowledge representation scheme is BEST suited for representing the concept of "a university course" with its attributes, prerequisites, and default values?**
   - (a) Semantic Network
   - (b) Script
   - (c) Frame
   - (d) Propositional Logic

6. **What distinguishes frames from semantic networks?**
   - (a) Frames use graphs while semantic networks use tables
   - (b) Frames support procedural attachments (facets) while semantic networks do not
   - (c) Frames cannot represent inheritance
   - (d) Frames are newer than semantic networks

7. **In a frame hierarchy with multiple inheritance, if both parent frames have different default values for the same slot, which value will be inherited?**
   - (a) First parent in the list
   - (b) Last parent in the list
   - (c) System selects randomly
   - (d) Ambiguity must be resolved explicitly

8. **A script for "air travel" would most likely include which scene sequence?**
   - (a) Order food → Board plane → Cook meal
   - (b) Check-in → Boarding → Flight → Deplaning → Baggage claim
   - (c) Buy ticket → Watch movie → Sleep
   - (d) Reserve seat → Cancel reservation → Refund

9. **Which facet allows automatic execution of validation code when a slot value is modified?**
   - (a) IF-NEEDED
   - (b) IF-ADDED
   - (c) IF-REMOVED
   - (d) DEFAULT

10. **Modern knowledge graphs (like Google's) are most closely related to which classical representation?**
    - (a) Frames
    - (b) Scripts
    - (c) Semantic Networks
    - (d) Production Rules

### 7.2 True or False

1. Semantic networks can only represent "ISA" relationships. **(False)**
2. Frames support both single and multiple inheritance. **(True)**
3. Scripts are best suited for representing static knowledge about objects. **(False)**
4. The "Result" component of a script describes the state changes after execution. **(True)**
5. Facets in frames can contain procedural code. **(True)**
6. Semantic networks are always represented as directed acyclic graphs. **(False)**
7. Scripts require all entry conditions to be satisfied before execution. **(True)**
8. Default values in frames are used when no explicit value is provided. **(True)**
9. Scripts and frames cannot be used together in a knowledge base. **(False)**
10. The inference component of a script allows deriving implicit information. **(True)**

### 7.3 Short Answer Questions (5 marks each)

1. **Explain the concept of inheritance in semantic networks. How does it differ from inheritance in frame systems?**

2. **List and explain any four types of facets available in frame representations, with their purposes.**

3. **Differentiate between "Props" and "Roles" in a script with an appropriate example.**

4. **What are entry conditions in scripts? Why are they important? Explain with an example.**

5. **How does procedural attachment (facets) enhance the expressive power of frames over semantic networks?**

6. **Draw and explain a semantic network representing the relationships between: Computer Science, Programming, Python, Java, Language.**

7. **Explain the role of inference in script-based understanding with a suitable example.**

### 7.4 Long Answer Questions (10 marks each)

1. **Define frames in knowledge representation. Explain the structure of a frame with a detailed example of a "University" frame system showing at least 5 slots with appropriate facets.**

2. **What is a script? Explain all its components in detail. Design a complete script for the scenario "Shopping at a Supermarket" including at least 4 scenes, props, roles, and inference.**

3. **Compare and contrast Semantic Networks, Frames, and Scripts as knowledge representation paradigms. Provide suitable examples to illustrate when each would be most appropriate.**

4. **Explain the concept of multiple inheritance in frames. How is conflict resolution handled? Illustrate with a diagram showing at least three levels of inheritance and explain the property lookup process.**

5. **How do modern knowledge graphs relate to classical semantic networks? Discuss with examples of current applications and limitations of classical representations that led to the evolution of knowledge graphs.**

---

## 8. References for Further Study

- Russell, S. & Norvig, P. - *Artificial Intelligence: A Modern Approach* (Chapter 12)
- Giarratano, J.C. & Riley, G.D. - *Expert Systems: Principles and Programming*
- Delhi University BSc (Hons) Computer Science - AI Syllabus (NEP 2024 UGCF)
- Winston, P.H. - *Artificial Intelligence*
- Schank, R.C. & Abelson, R.P. - *Scripts, Plans, Goals, and Understanding*

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*