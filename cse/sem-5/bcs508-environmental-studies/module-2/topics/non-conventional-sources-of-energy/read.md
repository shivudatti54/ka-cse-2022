# Non-Conventional Sources of Energy

## Introduction

The global energy landscape is undergoing a significant transformation driven by the depletion of fossil fuels, environmental concerns, and the urgent need for sustainable development. Non-conventional sources of energy, also known as renewable energy sources, have emerged as viable alternatives to traditional fossil-based energy systems. These energy sources are inexhaustible, environmentally friendly, and play a crucial role in reducing carbon emissions and mitigating climate change.

For CSE students, understanding non-conventional energy sources is essential not only from an environmental perspective but also because the IT industry is increasingly focusing on green computing and sustainable technologies. The integration of renewable energy with computing infrastructure, data centers, and smart grid technologies represents the future of both energy and IT sectors. This module covers various non-conventional energy sources, their working principles, advantages, limitations, and their applications in modern engineering systems.

## Key Concepts

### 1. Solar Energy

Solar energy is radiant light and heat from the Sun that is harnessed using a range of technologies such as solar photovoltaic (PV) systems, solar thermal power, and solar architecture.

**Solar Photovoltaic (PV) Systems:**

- Convert sunlight directly into electricity using semiconductor materials (silicon-based cells)
- PV cells are combined into modules and arrays to generate usable power
- Two main types: monocrystalline and polycrystalline silicon cells
- Efficiency ranges from 15-25% for commercial panels

**Solar Thermal Power:**

- Uses mirrors or lenses to concentrate sunlight to produce heat
- Heat is then used to generate steam for driving turbines
- Three types: parabolic trough, solar tower, and dish Stirling systems

**Applications:**

- Solar water heaters
- Solar-powered calculators and gadgets
- Grid-connected and off-grid PV systems
- Solar-powered EV charging stations

### 2. Wind Energy

Wind energy is captured using wind turbines that convert the kinetic energy of wind into mechanical power, which is then converted to electricity.

**Wind Turbine Types:**

- **Horizontal Axis Wind Turbines (HAWT):** Most common type with three-bladed rotor
- **Vertical Axis Wind Turbines (VAWT):** Darrieus and Savonius types, omnidirectional

**Key Components:**

- Rotor blades
- Nacelle (containing generator and gearbox)
- Tower
- Foundation
- Control systems

**Wind Power Equation:**
Power = ½ × ρ × A × V³ × Cp

Where:

- ρ = air density (kg/m³)
- A = swept area (m²)
- V = wind velocity (m/s)
- Cp = power coefficient (theoretical maximum 0.59)

### 3. Biomass Energy

Biomass energy is derived from organic materials, a renewable and sustainable source of energy that can be used directly or converted into biofuels.

**Types of Biomass:**

- Agricultural residues (crop stalks, husks)
- Forestry waste
- Animal manure
- Municipal solid waste
- Energy crops (switchgrass, miscanthus)

**Conversion Technologies:**

- **Combustion:** Direct burning of biomass for heat and power
- **Gasification:** Conversion of biomass into producer gas
- **Pyrolysis:** Heating in absence of oxygen to produce bio-oil
- **Anaerobic Digestion:** Biological process producing biogas (methane and CO2)
- **Fermentation:** Production of ethanol from sugars and starches

### 4. Geothermal Energy

Geothermal energy is heat derived within the earth's crust, used for heating or electricity generation.

**Geothermal Resources:**

- Hydrothermal resources (hot water and steam)
- Enhanced geothermal systems (engineered reservoirs)
- Geopressured resources

**Applications:**

- Direct heating (greenhouse, district heating)
- Electricity generation (flash steam, binary cycle)
- Heat pumps for building heating/cooling

### 5. Ocean Energy

Ocean energy encompasses various forms of energy derived from the ocean.

**Types:**

- **Tidal Energy:** Energy from ocean tides using tidal barrages or turbines
- **Wave Energy:** Energy from surface waves using oscillating water columns, terminators, or attenuators
- **Ocean Thermal Energy Conversion (OTEC):** Temperature difference between warm surface and cold deep water
- **Marine Currents:** Energy from ocean currents using underwater turbines

### 6. Hydrogen Energy

Hydrogen is considered an ideal energy carrier with high energy content by weight.

**Production Methods:**

- Electrolysis of water (using renewable electricity)
- Steam methane reforming (from natural gas)
- Biomass gasification
- Photoelectrochemical water splitting

**Applications:**

- Fuel cells for vehicles
- Backup power systems
- Energy storage
- Industrial processes

### 7. Fuel Cells

Fuel cells convert chemical energy directly into electrical energy through electrochemical reactions.

**Types of Fuel Cells:**

- Proton Exchange Membrane (PEMFC)
- Solid Oxide Fuel Cell (SOFC)
- Molten Carbonate Fuel Cell (MCFC)
- Direct Methanol Fuel Cell (DMFC)

**Advantages:**

- High efficiency (40-60%)
- Low emissions (only water)
- Quiet operation
- Modular and scalable

## Examples

### Example 1: Solar PV System Design

**Problem:** Calculate the number of 300W solar panels required to power a house consuming 12 kWh per day in a location with 5 peak sun hours.

**Solution:**

Step 1: Calculate daily energy requirement in watts

- Daily consumption = 12 kWh = 12,000 Wh

Step 2: Account for system losses (typically 20% loss)

- Required generation = 12,000 / 0.8 = 15,000 Wh

Step 3: Calculate panel output per day

- Each panel produces = 300W × 5 hours = 1,500 Wh/day

Step 4: Calculate number of panels

- Number of panels = 15,000 / 1,500 = 10 panels

**Answer:** 10 solar panels of 300W each are required.

### Example 2: Wind Power Calculation

**Problem:** A wind turbine with rotor diameter of 20m is installed in an area with average wind velocity of 6 m/s. Air density is 1.225 kg/m³ and power coefficient is 0.35. Calculate the available power and output power.

**Solution:**

Step 1: Calculate swept area

- Radius = 20/2 = 10m
- Area = π × r² = π × 10² = 314.16 m²

Step 2: Calculate available wind power

- P_available = ½ × ρ × A × V³
- P_available = 0.5 × 1.225 × 314.16 × 6³
- P_available = 0.5 × 1.225 × 314.16 × 216
- P_available = 40,195 W ≈ 40.2 kW

Step 3: Calculate output power

- P_output = Cp × P_available
- P_output = 0.35 × 40,195
- P_output = 14,068 W ≈ 14.1 kW

**Answer:** Available power is 40.2 kW, output power is 14.1 kW

### Example 3: Biogas Production

**Problem:** A dairy farm produces 100 kg of cow dung per day. Calculate the approximate biogas yield if each kg of cow dung produces 0.04 m³ of biogas. Also calculate the methane content if methane constitutes 60% of biogas.

**Solution:**

Step 1: Calculate total biogas production

- Biogas = 100 kg × 0.04 m³/kg = 4 m³/day

Step 2: Calculate methane content

- Methane = 4 m³ × 0.60 = 2.4 m³/day

Step 3: Calculate energy equivalent (approx. 6 kWh/m³ of methane)

- Energy = 2.4 × 6 = 14.4 kWh/day

**Answer:** Biogas production is 4 m³/day with 2.4 m³ of methane, equivalent to approximately 14.4 kWh of energy.

## Exam Tips

1. **Know the classification:** Remember the main categories - Solar, Wind, Biomass, Geothermal, Ocean, and Hydrogen energy. exams often ask for classification.

2. **Remember key formulas:** The wind power equation P = ½ρAV³Cp is frequently asked in numerical problems.

3. **Difference between conventional and non-conventional:** Understand that non-conventional sources are renewable, abundant, and environmentally friendly compared to conventional fossil fuels.

4. **Solar cell types:** Be familiar with the difference between monocrystalline, polycrystalline, and thin-film solar cells - their efficiencies and applications.

5. **Biomass conversion methods:** Know the various biomass conversion techniques: combustion, gasification, pyrolysis, anaerobic digestion, and fermentation.

6. **Fuel cell types:** Remember at least 2-3 types of fuel cells (PEMFC, SOFC) and their applications.

7. **Advantages over fossil fuels:** Emphasize in answers: inexhaustible, pollution-free, minimal operating costs after initial investment, reduced greenhouse gas emissions.

8. **Limitations:** Be prepared to discuss challenges like high initial cost, intermittency, storage issues, and geographic limitations.

9. **Green computing connection:** For CSE students, understand how renewable energy is used in data centers and for green computing initiatives.

10. **Numerical problems:** Practice wind power and solar PV calculations - these are commonly asked in exams.
