# Fluoride Problem in Drinking Water

## Introduction

Fluoride is a chemical element that occurs naturally in the environment and is present in varying concentrations in groundwater and surface water sources. While fluoride in optimal concentrations (0.5-1.5 mg/L) is known to prevent dental caries and promote bone health, excessive fluoride intake through drinking water leads to a serious health condition known as fluorosis. This environmental health problem affects millions of people worldwide, particularly in regions with high geological fluoride content in rocks and soils.

In India, the fluoride problem in drinking water has become a major public health concern, with several states including Rajasthan, Gujarat, Andhra Pradesh, Telangana, Karnataka, and Tamil Nadu reporting high fluoride concentrations in groundwater beyond the permissible limits set by the Bureau of Indian Standards (BIS). The World Health Organization (WHO) recommends a maximum concentration of 1.5 mg/L of fluoride in drinking water, while India's national standard (IS 10500:2012) specifies 1.5 mg/L as the acceptable limit. Understanding the sources, effects, prevention, and remediation methods for fluoride contamination is crucial for environmental engineers, computer science professionals working on smart water management systems, and all citizens concerned with environmental sustainability.

## Key Concepts

### Sources of Fluoride in Water

Fluoride enters groundwater through natural and anthropogenic processes. Natural sources include the weathering and dissolution of fluoride-bearing minerals such as fluorite (CaF₂), cryolite (Na₃AlF₆), fluoroapatite (Ca₅(PO₄)₃F), and topaz. Geological formations rich in these minerals release fluoride into groundwater through chemical reactions and leaching processes. Areas with granitic and gneissic rock formations typically have higher fluoride concentrations in their groundwater.

Anthropogenic sources of fluoride contamination include industrial discharges from aluminum smelting plants, fertilizer factories, glass and ceramic industries, and coal-fired power stations. Agricultural activities contribute through the use of fluoride-containing fertilizers and pesticides. Additionally, wastewater from certain manufacturing processes can contaminate surface and groundwater sources.

### Health Effects of Fluoride

**Dental Fluorosis:** This is the earliest visible sign of excessive fluoride exposure, characterized by white spots, streaks, or brown stains on tooth enamel. In mild cases, the appearance is chalky white patches, while severe cases exhibit pitting, roughness, and brown discoloration of teeth. Dental fluorosis occurs when children consume excess fluoride during the period of tooth development (birth to 8 years old).

**Skeletal Fluorosis:** Prolonged intake of high fluoride water (above 4-5 mg/L) leads to skeletal fluorosis, a serious condition affecting bones and joints. Symptoms include pain and stiffness in the joints, backache, difficulty in walking, and in severe cases, complete immobilization. The disease progresses through three stages: osteosclerosis (hardening of bones), osteophytosis (bone outgrowths), and finally, crippling skeletal fluorosis with joint fusion.

**Other Health Impacts:** Research indicates that excessive fluoride exposure may affect thyroid function, reduce IQ in children, cause gastrointestinal problems, and potentially lead to reproductive health issues. Fluoride toxicity can also interfere with calcium metabolism and enzyme functions in the body.

### Fluorosis in India

India is one of the worst-affected countries globally, with over 200 million people at risk from fluoride-contaminated water. The problem is particularly severe in the states of Rajasthan, where approximately 90% of districts have fluoride levels above the permissible limit. Gujarat, Karnataka, Andhra Pradesh, Telangana, and Madhya Pradesh also report extensive fluoride contamination. In Karnataka, districts like Bagalkot, Bijapur, Gulbarga, Raichur, and Koppal are known for high fluoride levels in groundwater.

### Permissible Limits and Standards

The Bureau of Indian Standards (BIS) has established the following guidelines for fluoride in drinking water:

- Desirable limit: 1.0 mg/L
- Acceptable limit: 1.5 mg/L
- Permissible limit in the absence of alternate source: 2.0 mg/L

The World Health Organization (WHO) guideline value is 1.5 mg/L, while the United States Environmental Protection Agency (EPA) has set a maximum contaminant level of 4.0 mg/L.

### Defluoridation Methods

Various techniques have been developed to remove excess fluoride from drinking water:

**Activated Alumina:** This is the most widely used defluoridation medium. Activated alumina (AA) adsorbs fluoride ions from water through ion exchange process. The capacity of activated alumina to remove fluoride is influenced by pH, initial fluoride concentration, contact time, and temperature. The media requires periodic regeneration with sodium hydroxide or sulfuric acid.

**Reverse Osmosis (RO):** This membrane technology can effectively remove fluoride along with other contaminants. RO systems can achieve 85-95% fluoride removal efficiency. However, they are expensive, require significant water pressure, and produce concentrated brine that requires disposal.

**Nalgonda Technique:** Developed by the National Environmental Engineering Research Institute (NEERI), this method uses aluminum sulfate (alum) and lime for fluoride removal. The process involves adding alum and lime to water, allowing flocculation and settling, then filtering the clear water. This is a low-cost method suitable for community-level treatment.

**Bone Char:** This material, produced by pyrolyzing animal bones, has shown effectiveness in fluoride adsorption. Bone char contains hydroxyapatite and calcium phosphate, which exchange fluoride ions.

**Electrocoagulation:** This emerging technique uses sacrificial electrodes (typically aluminum or iron) to coagulate and precipitate fluoride from water. It offers advantages like no chemical addition and sludge production, but requires electricity.

### Detection and Monitoring

Fluoride concentration in water is measured using various analytical techniques:

- Ion-Selective Electrode (ISE) method
- Spectrophotometric methods (SPADNS, Alizarin)
- Ion Chromatography
- HPLC (High-Performance Liquid Chromatography)

For field testing, portable fluoride test kits based on colorimetry are available, providing quick approximate measurements.

## Examples

### Example 1: Calculating Fluoride Removal Efficiency

**Problem:** A water treatment plant processes 50,000 liters of water per day with an initial fluoride concentration of 3.5 mg/L. After treatment using activated alumina, the final fluoride concentration is 0.8 mg/L. Calculate the percentage removal efficiency and the amount of fluoride removed per day.

**Solution:**

Given:

- Initial fluoride concentration (C₁) = 3.5 mg/L
- Final fluoride concentration (C₂) = 0.8 mg/L
- Volume of water treated (V) = 50,000 L/day

Step 1: Calculate fluoride removed per liter
Fluoride removed per liter = C₁ - C₂ = 3.5 - 0.8 = 2.7 mg/L

Step 2: Calculate percentage removal efficiency
Removal efficiency = [(C₁ - C₂) / C₁] × 100
= [(3.5 - 0.8) / 3.5] × 100
= (2.7 / 3.5) × 100
= 77.14%

Step 3: Calculate total fluoride removed per day
Total fluoride removed = (C₁ - C₂) × V
= 2.7 mg/L × 50,000 L
= 135,000 mg
= 135 grams per day

**Answer:** The removal efficiency is 77.14%, and approximately 135 grams of fluoride are removed daily.

### Example 2: Determining Safe Water Mixing

**Problem:** A village has two water sources: Source A with fluoride concentration of 4.2 mg/L (unsafe) and Source B with fluoride concentration of 0.3 mg/L (below optimal). The village wants to achieve the WHO-recommended fluoride level of 1.0 mg/L by mixing water from both sources. Calculate the ratio in which these two sources should be mixed.

**Solution:**

Let x be the fraction of water from Source A and (1-x) be the fraction from Source B.

Using mixing equation:
C_mixed = C₁ × x + C₂ × (1-x)

Where:

- C_mixed = 1.0 mg/L (desired)
- C₁ = 4.2 mg/L (Source A)
- C₂ = 0.3 mg/L (Source B)

Substituting values:
1.0 = 4.2x + 0.3(1-x)
1.0 = 4.2x + 0.3 - 0.3x
1.0 - 0.3 = 4.2x - 0.3x
0.7 = 3.9x
x = 0.7 / 3.9
x = 0.1795 ≈ 0.18

Therefore:

- Source A (4.2 mg/L): 18%
- Source B (0.3 mg/L): 82%

**Answer:** Mix approximately 18% water from Source A with 82% water from Source B to achieve the desired 1.0 mg/L fluoride concentration.

### Example 3: Bone Char Dosage Calculation

**Problem:** A community water supply has fluoride concentration of 3.0 mg/L and needs to be reduced to 1.5 mg/L. If the fluoride adsorption capacity of bone char is 2.5 mg F⁻ per gram of bone char, calculate the amount of bone char required to treat 10,000 liters of water.

**Solution:**

Given:

- Initial fluoride concentration = 3.0 mg/L
- Final fluoride concentration = 1.5 mg/L
- Volume of water = 10,000 L
- Adsorption capacity = 2.5 mg F⁻/g

Step 1: Calculate fluoride to be removed per liter
Fluoride to remove = 3.0 - 1.5 = 1.5 mg/L

Step 2: Calculate total fluoride to remove
Total fluoride = 1.5 mg/L × 10,000 L = 15,000 mg = 15 g

Step 3: Calculate bone char required
Bone char required = Total fluoride / Adsorption capacity
= 15 g / 2.5 g F⁻/g bone char
= 6 kg of bone char

**Answer:** Approximately 6 kg of bone char is required to treat 10,000 liters of water from 3.0 mg/L to 1.5 mg/L fluoride concentration.

## Exam Tips

1. **Know the permissible limits:** Remember that BIS recommends 1.0 mg/L as desirable and 1.5 mg/L as acceptable limit for fluoride in drinking water. The WHO guideline is 1.5 mg/L.

2. **Understand the difference between dental and skeletal fluorosis:** Dental fluorosis affects teeth during development (white spots, staining), while skeletal fluorosis affects bones and joints (pain, stiffness, crippling) in adults with prolonged exposure.

3. **Key defluoridation methods:** Remember the Nalgonda technique (using alum and lime), activated alumina adsorption, reverse osmosis, and bone char methods as common defluoridation techniques.

4. **Fluoride-bearing minerals:** Know that fluorite (CaF₂), cryolite (Na₃AlF₆), and fluoroapatite are the main natural sources of fluoride in rocks.

5. **Affected states in India:** Rajasthan, Gujarat, Karnataka, Andhra Pradesh, and Telangana are the major states affected by fluoride contamination in groundwater.

6. **Fluoride removal efficiency calculation:** Practice problems involving percentage removal efficiency and mixing calculations, as these are commonly asked in exams.

7. **pH effect on fluoride removal:** Remember that fluoride adsorption is most effective in the pH range of 5.5-7.0 for activated alumina. At higher pH, fluoride removal efficiency decreases due to competition with OH⁻ ions.

8. **Write neat diagrams:** If asked to explain defluoridation methods, include labeled diagrams of the Nalgonda technique or activated alumina column as these carry marks.
