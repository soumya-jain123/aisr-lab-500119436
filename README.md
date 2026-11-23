# Algorithms for Intelligent Systems and Robotics (CSAI4014) — Laboratory Repository

**Student Name:** Soumya Jain  
**SAP ID:** 500119436  
**Roll Number:** R2142230988  
**Batch:** B (B.Tech CSE AI & ML B2)  
**Partner(s):** Individual  
**Course Teacher:** Dr. Resham Raj Shivwanshi  

---

## Experiments Overview

| Experiment No. | Experiment Title / Name | Purpose / What It Is For |
| :--- | :--- | :--- |
| **Experiment 1** | **Time and Frequency Domain, and the Pendulum** | Constructs a multi-tone signal to study DFT/FFT amplitude spectra, demonstrates Shannon-Nyquist aliasing (5 Hz sampled at 8 Hz), examines spectral leakage, and integrates the nonlinear damped pendulum ODE to plot phase portraits and period vs. amplitude. |
| **Experiment 2** | **The Eight Queens Problem** | Formulates N-Queens as a Constraint Satisfaction Problem (CSP) and compares permutation generate-and-test against recursive backtracking with pruning for n = 4 to 10. |
| **Experiment 3** | **Breadth-First and Depth-First Search** | Represents a 2D maze as an implicit graph and compares BFS and DFS (implemented via a single deque-based function) on cells expanded, path length, and frontier memory. |
| **Experiment 4** | **Hill Climbing** | Evaluates steepest-ascent hill climbing on 8-Queens, observes local-optima entrapment, and verifies random-restart recovery against the theoretical model $P(k) = 1 - (1 - p)^k$. |
| **Experiment 5** | **Reinforcement Learning (Tabular Q-Learning)** | Models a 5 × 7 grid world as an MDP and applies off-policy tabular Q-learning with $\varepsilon$-greedy exploration across $\varepsilon \in \{0.01, 0.10, 0.20, 0.50\}$. |
| **Experiment 6** | **A Simple Neural Network** | Implements a 2-4-1 MLP from scratch in NumPy using backpropagation to solve XOR and compares convergence across learning rates. |
| **Experiment 7** | **Mobile Robot Simulation in Webots: Reactive Swarm and Lidar Navigation** | Simulates an e-puck swarm using Braitenberg obstacle avoidance and a Pioneer 3-DX using lidar Follow-The-Gap (FTG) navigation in Webots R2025a. |
| **Experiment 8** | **Cross-Embodiment Transfer of a Manipulation Skill (PyBullet)** | Evaluates kinematic, observation, action, and capability gaps across KUKA iiwa, Franka Panda, xArm6, and KUKA mini using task-space IK and behaviour cloning. |

---

## Repository Structure

```text
aisr-lab-500119436/
├── README.md
├── exp01-signals/     # Notebook and figures for Exp 1
├── exp02-queens/      # Notebook and figures for Exp 2
├── exp03-search/      # Notebook and figures for Exp 3
├── exp04-hillclimb/   # Notebook and figures for Exp 4
├── exp05-rl/          # Notebook and figures for Exp 5
├── exp06-neural/      # Notebook and figures for Exp 6
├── exp07-webots/      # Webots simulation controllers, runs, and logs
├── exp08-xembody/     # Cross-embodiment PyBullet manipulation experiments
└── figures/           # Generated report figures
```

---

## Sources and AI Tools Used

- **Course Lab Manual & Repository Guides:** CSAI4014 Lab Manual (Ch. 2–7), `webots-robotics-sim` (`README.md`, `GUIDE.md`), `AISR-Cross-Embodiment-PyBullet` (`MANUAL.md`).
- **Textbooks & Papers:** Oppenheim & Schafer (DFT/aliasing), Åström & Murray (pendulum dynamics), Russell & Norvig (CSP, BFS/DFS, hill climbing), Sutton & Barto (Q-learning), Michel (Webots), Open X-Embodiment Collaboration, Coumans & Bai (PyBullet).
- **AI Assistant:** Antigravity AI Assistant (used for running local experiments, generating plots, and structuring the laboratory report).
