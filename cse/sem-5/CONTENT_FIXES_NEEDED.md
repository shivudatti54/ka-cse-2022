# Content Fixes Required - Priority List

Generated: 2026-02-09

## CRITICAL: Wrong Subject Content (39 topics)

These topics contain content from completely wrong subjects and need immediate replacement.

### BCS501 - Software Engineering & PM (5 topics)

1. `/chapters/module-3/topics/core-principles`

- **Current:** Security/Network content
- **Expected:** Software engineering core principles

2. `/chapters/module-3/topics/what-is-agility`

- **Current:** Artificial Intelligence content
- **Expected:** Agile methodology in software development

3. `/chapters/module-4/topics/introduction`

- **Current:** Distributed Systems content
- **Expected:** Software project management introduction

4. `/chapters/module-4/topics/management-and-management-control`

- **Current:** Log Management (Networks)
- **Expected:** Project management and control

5. `/chapters/module-5/topics/introduction`

- **Current:** Distributed Systems content
- **Expected:** Software engineering topic for Module 5

### BCS502 - Computer Networks (3 topics)

1. `/chapters/module-2/topics/lc-services`

- **Current:** Operating System Services
- **Expected:** Network layer/LC services

2. `/chapters/module-4/topics/features`

- **Current:** HOG Features (Computer Vision/Graphics)
- **Expected:** Network protocol features

3. `/chapters/module-4/topics/services`

- **Current:** Operating System Services
- **Expected:** Network services

### BCS503 - Theory of Computation (2 topics)

1. `/chapters/module-2/topics/applications-of-regular-expressions`

- **Current:** Too network-focused, not TOC-focused
- **Expected:** Applications in formal language theory, compiler design

2. `/chapters/module-5/topics/rajeev-motwani`

- **Current:** Network-focused biography
- **Expected:** Contributions to Theory of Computation

### BCS508 - Environmental Studies (4 topics)

1. `/chapters/module-1/topics/structure-of-ecosystem`

- **Current:** AI Agent Structures
- **Expected:** Ecosystem structure (producers, consumers, decomposers, trophic levels)

2. `/chapters/module-1/topics/types`

- **Current:** Types of Machine Learning
- **Expected:** Types of ecosystems or environmental topics

3. `/chapters/module-4/topics/functional-elements-of-swm`

- **Current:** Partially network-focused
- **Expected:** Solid Waste Management functional elements

4. `/chapters/module-5/topics/elite-publishing-house`

- **Current:** Network-focused
- **Expected:** E-waste management content

### BCS515A - Computer Graphics (3 topics)

1. `/chapters/module-1/topics/applications-of-computer-graphics`

- **Current:** Too network-focused
- **Expected:** Graphics applications (CAD, gaming, visualization, etc.)

2. `/chapters/module-2/topics/display-lists-and-modeling`

- **Current:** Network-focused
- **Expected:** OpenGL display lists and 3D modeling

3. `/chapters/module-2/topics/modeling`

- **Current:** Threat Modeling (Security)
- **Expected:** 3D modeling, geometric modeling

### BCS515B - Artificial Intelligence (2 topics)

1. `/chapters/module-1/topics/intelligent-agents`

- **Current:** Too network-focused description
- **Expected:** Pure AI agent concepts

2. `/chapters/module-1/topics/introduction`

- **Current:** Distributed Systems content
- **Expected:** Introduction to Artificial Intelligence

### BCS515C - Unix System Programming (7 topics)

1. `/chapters/module-1/topics/introduction`

- **Current:** Distributed Systems
- **Expected:** Unix/Linux introduction

2. `/chapters/module-2/topics/shell-programming`

- **Current:** Parallel Programming
- **Expected:** Shell scripting (bash, sh)

3. `/chapters/module-3/topics/introduction`

- **Current:** Distributed Systems
- **Expected:** File systems or process management intro

4. `/chapters/module-4/topics/introduction`

- **Current:** Distributed Systems
- **Expected:** IPC or signals introduction

5. `/chapters/module-4/topics/pclose-functions`

- **Current:** Loss Functions (ML/AI)
- **Expected:** popen/pclose system calls

6. `/chapters/module-4/topics/wait4-functions`

- **Current:** MPI/Distributed Memory Programming
- **Expected:** wait, waitpid, wait3, wait4 system calls

7. `/chapters/module-5/topics/introduction`

- **Current:** Likely wrong content
- **Expected:** Advanced Unix topics introduction

### BCS515D - Distributed Systems (13 topics)

Multiple topics flagged for wrong subject content - needs comprehensive review.

---

## MEDIUM: Content Mismatches (18 topics)

Content doesn't match topic name but may be salvageable.

### BCS501 - Software Engineering (1)

- `/chapters/module-2/topics/validating-requirements-requirements-modeling-scen`
- Contains UML diagrams but topic name suggests scenarios

### BCS502 - Computer Networks (1)

- `/chapters/module-4/topics/user-datagram-protocol`
- Just packet header, needs explanation

### BCS503 - Theory of Computation (1)

- `/chapters/module-5/topics/second-edition`
- Poor topic name, rename to actual topic

### BCS515A - Computer Graphics (5)

- `/chapters/module-2/topics/input-and-interaction` - Review content alignment
- `/chapters/module-2/topics/text-book-1-chapter-3-31-to-37` - Rename topic
- `/chapters/module-4/topics/52-and-chapter-6-61` - Rename topic
- `/chapters/module-4/topics/63-and-65` - Rename topic
- `/chapters/module-5/topics/text-book-1-chapter-7-71-to-74-text-book-2-chapter` - Rename topic

### BCS515C - Unix System Programming (5)

- `/chapters/module-3/topics/fchdir-and-getcwd-functions-device-special-files`
- `/chapters/module-3/topics/files-and-dictionaries` (should be "directories")
- `/chapters/module-4/topics/exec-functions-overview-of-ipc-methods`
- `/chapters/module-4/topics/race-conditions`
- `/chapters/module-5/topics/system-function`

### BCS515D - Distributed Systems (5)

- `/chapters/module-1/topics/51-55` - Rename topic
- `/chapters/module-2/topics/131-133` - Rename topic
- `/chapters/module-3/topics/global-states-1-12082024-annexure-ii-2-textbook-ch` - Rename topic
- `/chapters/module-4/topics/textbook-chapter-151-155` - Rename topic
- `/chapters/module-5/topics/textbook-chapter-171-176` - Rename topic

---

## Fix Priority Order

1. **Phase 1 (Critical):** Fix all 39 wrong subject content topics

- Start with subjects having most issues: Distributed Systems (13), Unix (7), SE (5)

2. **Phase 2 (Naming):** Rename topics with poor naming conventions

- Replace textbook section numbers with descriptive names
- Fix typos (dictionaries → directories)

3. **Phase 3 (Review):** Manual review of content mismatches

- Verify content is accurate even if naming is off
- Update content or names as needed

4. **Phase 4 (Format):** Update MCQ validation script

- Not a content issue, just validation script needs update

---

## Estimated Effort

- **Critical Fixes:** 39 topics × 30 min = ~20 hours
- **Naming Fixes:** 15 topics × 5 min = ~1.5 hours
- **Content Review:** 18 topics × 15 min = ~4.5 hours
- **Script Update:** ~1 hour

**Total:** ~27 hours of work

---

## Validation Process

After fixes:

1. Re-run contextual validation
2. Verify no wrong subject content remains
3. Check all topics have proper descriptive names
4. Manual spot-check of corrected topics
