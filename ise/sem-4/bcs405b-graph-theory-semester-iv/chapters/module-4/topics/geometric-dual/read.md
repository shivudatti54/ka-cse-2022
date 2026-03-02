mermaid
flowchart TD
subgraph Original Plane Graph G
direction LR
A --- B
B --- D
A --- C
C --- D
B --- C
end

    subgraph Its Geometric Dual G*
        direction LR
        f1*["f1*<br>(inside f1)"] --- f2*["f2*<br>(inside f2)"]
        f2* --- f3*["f3*<br>(inside outer face f3)"]
        f1* --- f3*
        f3* -.-> f3*[["Self-loop<br>(corresponding to bridge)"]]
    end
