# Pypsa-China-ElecCoalFleet-Draworld

Capacity-expansion model with explicit coal-units

---

## Overview

Pypsa-China-ElecCoalFleet-Draworld is a high-resolution capacity-expansion and asset rationalization framework built on PyPSA. It models the long-term evolutionary path of China's power system from 2025 to 2050. 

Instead of treating the coal fleet as a uniform aggregate, the model explicitly tracks over 3,000 individual, heterogeneous coal units. It simulates how this fleet responds to strict climate constraints, market forces, and policy-driven "periodic shock therapy" across a recursive timeline.

---

## Model Design

- **Granular Asset Tracking:** Explicit modeling of over 3000 individual coal units with distinct efficiencies, start-up costs, and vintages.
- **Endogenous Asset Lifetime:** Determines early retirement and phase-out dynamics as optimized economic choices rather than fixed parameters.
- **Exogenous VRE Trajectories:** Imposes predefined wind and solar deployment paths (e.g., +200 GW/year) to reflect political commitments.
- **Nodal Market Clearing:** Captures high-resolution spatial price signals (LMPs) and transmission bottlenecks across provincial grids.
- **Recursive Timeline (2035–2050):** Simulates 5-year iterative steps under tight binding constraints:
  - Zero electricity demand growth (saturation post-2035)
  - Strict curtailment discipline ($<10\%$)
  - Zero-emission power sector target by 2050 (with no CCS)
  - Automatic "deletion" of coal units that lose their generation roles under economic dispatch.

Outputs include:
- Fleet lifetime distribution profiles (quantifying "immature" retirements)
- Stranded asset volumes (GW) and localized capacity impacts
- Financial requirement metrics for capacity payment mechanisms (benchmarked at 330 RMB/kW/year)
- Full solved PyPSA network files (`.nc`)

---

## Web & Visualization Interface

- **Nodal Price & Flow Maps:** Interactive spatial visualization of transmission bottlenecks and regional price divergence.
- **Fleet Lifetime Dashboards:** Distribution curves comparing unit-level operational lifespans against standard design lives.
- **Capacity Payment Analysis:** Visual tools to assess the monetary scale needed to maintain retired units as strategic reserves.

---

## Applications

The platform is designed to support:

- **Coal Phase-out Pathways:** Diagnosing which units are forced into "zombie" states or operational compression under rapid transitions.
- **Stranded Asset Risk Valuation:** Quantifying the asset longevity gap and economic shocks of premature retirements.
- **Capacity Market Design:** Evaluating the financial burden and necessary magnitudes of capacity payments to keep units online for reliability.
- **Policy Credibility Stress Tests:** Verifying whether long-term net-zero targets remain physically and economically viable under rigid institutional constraints.
- **Market Design Comparison:** Contrasting China's administrative allocation approach against textbook economic dispatch principles.

---

## License
AGPL-3.0, aligned with the open modeling ecosystem of PyPSA.

---

## Statement

Pypsa-China-ElecCoalFleet-Draworld is a research, scenario-exploration, and policy-workshop tool. It is designed for long-term power system structural analysis and does not represent official regulatory timelines or commercial trading strategies.