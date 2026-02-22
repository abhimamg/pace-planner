# Example: Wall Thickness Calculation Report

**Project:** Sample Subsea Pipeline
**Pipeline Segment:** 12" Oil Pipeline
**Design Code:** DNV-ST-F101 (2021)

## 1. Design Inputs
- **Nominal Diameter (D):** 323.9 mm (12.75 in)
- **Material Grade:** API 5L X65 (f_y = 450 MPa)
- **Design Pressure (P_i):** 250 barg (25 MPa)
- **Maximum Water Depth (d):** 500 m
- **Design Temperature:** 80 °C (Temp derating factor = 1.0 for X65 < 50°C, adjusted to 0.95)
- **Corrosion Allowance (t_corr):** 3.0 mm
- **Fabrication Tolerance:** 12.5%

## 2. Pressure Containment (DNV Clause 5.4.2)
The wall thickness required for internal pressure containment (incidental pressure) is calculated:
$t_1 = \frac{P_{li} \cdot D}{22 \cdot \eta_p \cdot f_y \cdot \frac{2}{\sqrt{3}}} + t_{corr}$
*(Simplified calculation for demonstration)*

**Calculated t_1:** 12.5 mm

## 3. Local Buckling - External Pressure (DNV Clause 5.4.4)
Check for collapse due to external hydrostatic pressure at 500m depth.
- External Pressure (P_e) = 5 MPa
- Characteristic Resistance (P_c) must exceed P_e with appropriate safety factors.

**Verification:** wall thickness of 14.3 mm (nominal) is required to prevent collapse.

## 4. Propagation Buckling (DNV Clause 5.4.6)
Ensure that a buckle, initiated by an accident, will not propagate along the entire pipeline.
- $P_{pr} = 35 \cdot f_y \cdot \alpha_{fab} \cdot (\frac{t}{D})^{2.5}$
- Required $P_{pr} > P_e / \gamma_{pr}$

**Verification:** Nominal thickness of 15.9 mm is required for propagation bucking resistance.

## 5. Conclusion
The selection for the 12" Oil Pipeline is:
- **Nominal Wall Thickness:** 16.0 mm
- **Material:** API 5L X65 SMLS
- **Reason:** Propagation buckling is the governing limit state.
