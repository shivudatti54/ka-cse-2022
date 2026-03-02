# SVG Examples by Subject - Sem 3 CSE

This document shows example SVG paths from each subject to help verify the generation.

## BCS301 - Mathematics for Computer Science (56 SVGs)

Example topics:

- `/bcs301-mathematics-for-computer-science/chapters/module-1/topics/probability-distributions/assets/probability-distributions.svg`
- `/bcs301-mathematics-for-computer-science/chapters/module-2/topics/random-variables-discrete-and-continuous/assets/random-variables-discrete-and-continuous.svg`
- `/bcs301-mathematics-for-computer-science/chapters/module-3/topics/markov-chains/assets/markov-chains.svg`

## BCS302 - Digital Design and Computer Organization (77 SVGs)

Example topics:

- `/bcs302-digital-design-and-computer-organization/chapters/module-1/topics/binary-logic/assets/binary-logic.svg`
- `/bcs302-digital-design-and-computer-organization/chapters/module-2/topics/sequential-circuits/assets/sequential-circuits.svg`
- `/bcs302-digital-design-and-computer-organization/chapters/module-3/topics/basic-structure-of-computers/assets/basic-structure-of-computers.svg`

## BCS303 - Operating Systems (86 SVGs)

Example topics:

- `/bcs303-operating-systems/chapters/module-1/topics/operating-system-services/assets/operating-system-services.svg`
- `/bcs303-operating-systems/chapters/module-2/topics/process-synchronization/assets/process-synchronization.svg`
- `/bcs303-operating-systems/chapters/module-3/topics/deadlocks/assets/deadlocks.svg`
- `/bcs303-operating-systems/chapters/module-4/topics/memory-management/assets/memory-management.svg`
- `/bcs303-operating-systems/chapters/module-5/topics/file-system/assets/file-system.svg`

## BCS304 - Data Structures and Applications (54 SVGs)

Example topics:

- `/bcs304-data-structures-and-applications/chapters/module-1/topics/arrays/assets/arrays.svg`
- `/bcs304-data-structures-and-applications/chapters/module-2/topics/linked-lists/assets/linked-lists.svg`
- `/bcs304-data-structures-and-applications/chapters/module-3/topics/queues/assets/queues.svg`
- `/bcs304-data-structures-and-applications/chapters/module-4/topics/trees/assets/trees.svg`
- `/bcs304-data-structures-and-applications/chapters/module-5/topics/graphs/assets/graphs.svg`

## BCS306A - Object Oriented Programming with Java (86 SVGs)

Example topics:

- `/bcs306a-object-oriented-programming-with-java/chapters/module-1/topics/an-overview-of-java/assets/an-overview-of-java.svg`
- `/bcs306a-object-oriented-programming-with-java/chapters/module-2/topics/classes-and-objects/assets/classes-and-objects.svg`
- `/bcs306a-object-oriented-programming-with-java/chapters/module-2/topics/recursion/assets/recursion.svg`
- `/bcs306a-object-oriented-programming-with-java/chapters/module-3/topics/inheritance/assets/inheritance.svg`
- `/bcs306a-object-oriented-programming-with-java/chapters/module-4/topics/exceptions/assets/exceptions.svg`
- `/bcs306a-object-oriented-programming-with-java/chapters/module-5/topics/multithreaded-programming/assets/multithreaded-programming.svg`

## BCS306B - Object Oriented Programming with C++ (63 SVGs)

Example topics:

- `/bcs306b-object-oriented-programming-with-c/chapters/module-1/topics/an-overview-of-c/assets/an-overview-of-c.svg`
- `/bcs306b-object-oriented-programming-with-c/chapters/module-2/topics/classes-and-objects/assets/classes-and-objects.svg`
- `/bcs306b-object-oriented-programming-with-c/chapters/module-3/topics/operator-overloading/assets/operator-overloading.svg`
- `/bcs306b-object-oriented-programming-with-c/chapters/module-4/topics/inheritance/assets/inheritance.svg`
- `/bcs306b-object-oriented-programming-with-c/chapters/module-5/topics/templates/assets/templates.svg`

## Verification Commands

To verify SVG existence and structure:

```bash
# Count all SVGs
find . -name "*.svg" | wc -l

# Check specific subject
find ./bcs303-operating-systems -name "*.svg" | wc -l

# Verify TTS narration structure
grep -c "data-narration=" ./bcs306a-object-oriented-programming-with-java/chapters/module-2/topics/recursion/assets/recursion.svg

# View SVG content
cat ./bcs303-operating-systems/chapters/module-1/topics/operating-system-services/assets/operating-system-services.svg
```

## SVG Features

All generated SVGs include:

1. **Required Structure:**

- xmlns attribute
- data-topic-id matching folder name
- viewBox="0 0 420 400"
- 5 narration sections

2. **Visual Elements:**

- Gradient backgrounds
- Titled header bar
- 5 numbered sections with distinct colors
- Educational icons and shapes

3. **TTS Narration:**

- Each section has data-narration attribute
- Educational explanations (1-2 sentences each)
- Covers key concepts from the topic content

4. **Accessibility:**

- Clear readable fonts (Arial 12-15px)
- High contrast colors
- Numbered sections for navigation
- TTS-ready structure

---

**All 422 SVGs successfully generated and validated!**
