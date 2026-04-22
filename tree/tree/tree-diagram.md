# 🌳 Reflection Tree Diagram

Below is the visual representation of the deterministic reflection flow.

```mermaid
flowchart TD

subgraph AXIS1["Axis 1: Locus of Control"]
START([Start]) --> A1["How did today leave you feeling?"]

A1 -->|Drained / Frustrated| A1_LOW["What did you do when things went wrong?"]
A1 -->|Okay / Satisfied| A1_HIGH["Why did things go well?"]

A1_LOW --> D1{Decision}
D1 -->|Focused on control| R1["Reflection: Internal - High Agency"]
D1 -->|Others| R2["Reflection: External - Low Control"]

A1_HIGH --> D2{Decision}
D2 -->|Prepared / Adapted| R3["Reflection: Internal - High Agency"]
D2 -->|Team / Luck| R4["Reflection: External - Low Control"]
end

R1 --> B1
R2 --> B1
R3 --> B1
R4 --> B1

B1["Bridge: Control to Contribution"]

subgraph AXIS2["Axis 2: Contribution vs Entitlement"]
B1 --> A2["Interaction today?"]

A2 -->|Helped / Went beyond| A2C["Why did you contribute?"]
A2 -->|Did work / Unrecognized| A2E["What stood out?"]

A2C --> R5["Reflection: Contribution - Giving mindset"]
A2E --> R6["Reflection: Entitlement - Expectation mindset"]
end

R5 --> B2
R6 --> B2

B2["Bridge: Expand Perspective"]

subgraph AXIS3["Axis 3: Radius of Concern"]
B2 --> A3["Who comes to mind?"]

A3 -->|Just me| A3S["Was anyone else affected?"]
A3 -->|Others| A3O["What impact did you notice?"]

A3S --> R7["Reflection: Self-focused - Narrow view"]
A3O --> R8["Reflection: Others-focused - Wide impact"]
end

R7 --> SUM
R8 --> SUM

SUM["Summary: Control + Contribution + Perspective"]

SUM --> END([End])
