mermaid
stateDiagram-v2
direction LR
[*] --> Active
Active --> PartiallyCommitted : End of final statement
Active --> Failed : Can't proceed

    PartiallyCommitted --> Committed : Commit
    PartiallyCommitted --> Failed : Failure at commit

    Failed --> Aborted : Rollback
    Aborted --> Terminated : [*]

    Committed --> Terminated : [*]
