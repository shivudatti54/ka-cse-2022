mermaid
flowchart TD
A[Shell Issues Prompt<br>and Waits] --> B[User Enters Command]
B --> C[Read Command<br>from stdin]
C --> D[Parse Command<br>Tokenize, identify meta-characters]
D --> E[Execute Command<br>Fork, Exec, Wait]
E --> F[Command Execution Complete]
F --> A
