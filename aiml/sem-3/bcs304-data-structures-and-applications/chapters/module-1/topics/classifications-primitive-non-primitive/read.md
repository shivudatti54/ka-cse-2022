mermaid
graph TD
    A[Data Structures] --> B(Primitive)
    A --> C(Non-Primitive)
    
    B --> B1(Integer)
    B --> B2(Float)
    B --> B3(Character)
    B --> B4(Pointer)
    B --> B5(Boolean)
    
    C --> C1(Linear)
    C --> C2(Non-Linear)
    
    C1 --> C1a(Array)
    C1 --> C1b(Linked List)
    C1 --> C1c(Stack)
    C1 --> C1d(Queue)
    
    C2 --> C2a(Tree)
    C2 --> C2b(Graph)
    
    C --> C3(Static)
    C --> C4(Dynamic)