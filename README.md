# Cache Memory Simulation using Git Collaboration

## Institution
**AMAL JYOTHI COLLEGE OF ENGINEERING**  
Kanjirappally  

## Programme
**MCA 2025–27 (Semester 1)**  

## Course Codes
- **24MCAT103 – Digital Fundamentals and Computer Architecture**
- **24MCAT107 – Advanced Software Engineering**

## Assignment Title
**Simulating Cache Memory Mapping and Replacement Algorithms using Git Collaboration**

---

## Project Overview
This project implements a **Set-Associative Cache Memory Simulator** to demonstrate cache mapping and replacement concepts from Computer Architecture.  
The simulator is developed using **Java (Swing GUI)** and version-controlled using **GitHub**, applying collaborative software engineering practices.

The application visually represents cache behavior, including **cache hits, cache misses, empty slot insertion, and round-robin replacement**, while logging each computation step.

---

## Part A – Set Associative Cache Mapping Simulation

### Cache Configuration
- **Number of Sets:** 4  
- **Associativity (Ways):** 2-Way  
- **Replacement Policy:** Round Robin (FIFO style)

### Mapping Technique
Each memory address is divided into:
- **Set Index** = `Address % Number_of_Sets`
- **Tag** = `Address / Number_of_Sets`

### Algorithm
1. Read memory address and data
2. Compute set index using modulo operation
3. Compute tag using division
4. Check all ways in the selected set
5. If tag matches → **HIT** and update data
6. If no match and empty way exists → **MISS** and insert
7. If set is full → **MISS** and replace using Round Robin
8. Display cache contents and log steps in GUI

### Sample Input
Address: 6 Data: X
Address: 3 Data: A
Address: 7 Data: B
Address: 6 Data: Z

---

### Sample Output
Set 2 → MISS → Inserted
Set 3 → MISS → Inserted
Set 3 → MISS → Inserted
Set 2 → HIT → Updated
---
## Part B – Git Collaboration (24MCAT107)

### Repository Details
- **Repository Name:** `CacheSim_Project_Team_X`
- **Platform:** GitHub
- **Repository Link:**  
  https://github.com/viper004/df_assignment

### Branching Strategy
Each team member worked in a **separate branch**:
- Feature-based development
- Frequent commits with meaningful messages
- Proper merging into main branch

### Git Evidence Included
- Git commit logs
- Git branch list
- Git merge history
- Contribution graph

### Branch Link
https://github.com/viper004/df_assignment/tree/set-associative

---

## Tools & Technologies Used
- **Programming Language:** Java
- **GUI Framework:** Java Swing
- **Version Control:** Git
- **Repository Hosting:** GitHub
- **IDE:** Any Java-supported IDE (IntelliJ / Eclipse / VS Code)

---

## Learning Outcomes
- Practical understanding of **set-associative cache mapping**
- Implementation of **cache replacement algorithms**
- Visualization of cache operations using GUI
- Hands-on experience with **Git branching, merging, and collaboration**
- Improved debugging, teamwork, and software version control skills

---

## Reflection
Implementing the set-associative cache simulator helped convert theoretical cache memory concepts into real-world software logic.  
Using Git for collaboration improved team coordination, version tracking, and conflict resolution skills.  
Challenges included implementing correct replacement logic and synchronizing GUI updates with cache operations.  
Overall, the project strengthened both **technical knowledge** and **collaborative development skills**.

---

## Author
**MCA 2025–27 (S1)**  
AMAL JYOTHI COLLEGE OF ENGINEERING
