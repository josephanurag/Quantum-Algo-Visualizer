# Quantum-Algo-Visualizer
Quantum Algorithm Visualizer is an interactive Python application that lets users explore and simulate quantum circuits and algorithms in real time. Built with Qiskit and Streamlit, it’s designed to make quantum computing concepts accessible through intuitive visualizations and hands-on experimentation.

- Built with **Qiskit** and **Streamlit** for interactive quantum circuit simulation  
- Supports key algorithms like **Deutsch-Jozsa**, **Grover’s Search**, and custom gate logic  
- Visualizes quantum circuits using **Matplotlib** for clarity and educational value  
- Modular codebase with separate components for gates, algorithms, and rendering  
- Clean UI with sidebar controls for gate selection and qubit manipulation
- install packages
  1. pip install qiskit
  2. pip install streamlit
  3. pip install matplotlib
  4. pip install toml
- Easy setup via `requirements.txt` using `pip install -r requirements.txt`  
- Docker-ready with `Dockerfile` for containerized deployment  
- Run locally with `streamlit run app.py` or deploy via Docker (`8501` port)  
- Cloud-friendly: supports deployment on Streamlit Cloud, Render, or Railway  
- Ideal for portfolios showcasing quantum + UI + modular architecture skill
  
## Setup
```bash
git clone https://github.com/yourusername/quantum-algorithm-visualizer.git
cd quantum-algorithm-visualizer
pip install -r requirements.txt
streamlit run app.py

LIVE LINK:
https://quantum-al.streamlit.app/

### Deployment (Streamlit Cloud)
1. Push to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo and select `app.py` as the entry point
4. Done! Share your live link
---
