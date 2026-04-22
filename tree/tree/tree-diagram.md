# 🌳 Reflection Tree Diagram

Below is the visual representation of the deterministic reflection flow.

```mermaid
flowchart TD

%% ===== AXIS 1 =====
subgraph AXIS1["Axis 1: Locus of Control (Victim ↔ Victor)"]
START([Start]) --> A1[How did today leave you feeling?]

A1 -->|Drained / Frustrated| A1_LOW[What did you do when things went wrong?]
A1 -->|Okay / Satisfied| A1_HIGH[Why did things go well?]

A1_LOW --> D1{Decision}
D1 -->|Focused on control| R1[Reflection: Internal (Agency ↑)]
D1 -->|Others| R2[Reflection: External (Control ↓)]

A1_HIGH --> D2{Decision}
D2 -->|Prepared / Adapted| R3[Reflection: Internal (Agency ↑)]
D2 -->|Team / Luck| R4[Reflection: External (Control ↓)]
end

%% ===== BRIDGE =====
R1 --> B1
R2 --> B1
R3 --> B1
R4 --> B1

B1[Bridge → Shift from Control to Contribution]

%% ===== AXIS 2 =====
subgraph AXIS2["Axis 2: Contribution vs Entitlement"]
B1 --> A2[Interaction today?]

A2 -->|Helped / Went beyond| A2C[Why did you contribute?]
A2 -->|Did work / Unrecognized| A2E[What stood out?]

A2C --> R5[Reflection: Contribution (Giving mindset)]
A2E --> R6[Reflection: Entitlement (Expectation mindset)]
end

%% ===== BRIDGE =====
R5 --> B2
R6 --> B2

B2[Bridge → Expand Perspective]

%% ===== AXIS 3 =====
subgraph AXIS3["Axis 3: Radius of Concern (Self → Others)"]
B2 --> A3[Who comes to mind?]

A3 -->|Just me| A3S[Was anyone else affected?]
A3 -->|Others| A3O[What impact did you notice?]

A3S --> R7[Reflection: Self-focused (Narrow view)]
A3O --> R8[Reflection: Others-focused (Wide impact)]
end

%% ===== SUMMARY =====
R7 --> SUM
R8 --> SUM

SUM[Summary: Your day across Control + Contribution + Perspective]

SUM --> FINAL[Insight = Control + Contribution + Perspective]

FINAL --> END([End])
