# Global States

### Definitions

- **Global State**: A global state is the current state of a distributed system, representing the overall system's configuration, including the states of all processes, clocks, and events.
- **Global State Vector (GSV)**: A vector that represents the global state of a distributed system, typically comprising the states of all processes, clocks, and events.

### Key Concepts

- **Clocks**: Clocks are the heartbeat of a distributed system, measuring the time elapsed since the last event. Each process has its own clock, which is synchronized with other clocks using a synchronization protocol.
- **Events**: Events are the actions taken by processes in a distributed system. Events can trigger changes in the global state of the system.
- **Process States**: Processes can be in one of three states: running, waiting, or terminated. The state of a process affects the global state of the system.

### Formulas and Theorems

- **Global State Formula**: `GS = (PS \* |P|) + (Clocks \* |C|) + (Events \* |E|)`
  - `GS`: Global State
  - `PS`: Process States
  - `|P|`: Number of processes
  - `Clocks`: Clocks
  - `|C|`: Number of clocks
  - `Events`: Events
  - `|E|`: Number of events
- **Synchronization Theorem**: If two clocks are synchronized, the global state of a distributed system is uniquely determined by the clocks and events.

### Important Theorems

- **Hart's Theorem**: A distributed system is globally consistent if and only if all processes agree on the global state.
- **Lamport's Theorem**: A distributed system is globally consistent if and only if all processes agree on the global state and the clocks are synchronized.

### Important Definitions

- **Global Consistency**: The condition where all processes agree on the global state of a distributed system.
- **Synchronization**: The process of synchronizing clocks and events in a distributed system to ensure global consistency.
