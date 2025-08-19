import streamlit as st
from qiskit import QuantumCircuit
from quantum_core.gates import apply_gate
from quantum_core.algorithms import deutsch_jozsa, grover
from quantum_core.utils import render_circuit

st.set_page_config(page_title="Quantum Visualizer", layout="wide")
st.title("🧠 Quantum Algorithm Visualizer")

st.sidebar.image("assets/logo.png", width=150)
st.sidebar.header("Build Your Circuit")

num_qubits = st.sidebar.slider("Number of Qubits", 1, 5, 2)
qc = QuantumCircuit(num_qubits)

gate = st.sidebar.selectbox("Select Gate", ["H", "X", "Y", "Z", "CX", "Measure"])
target_qubit = st.sidebar.number_input("Target Qubit", 0, num_qubits - 1, 0)

if st.sidebar.button("Apply Gate"):
    qc = apply_gate(qc, gate, target_qubit)

st.subheader("🔍 Circuit Diagram")
st.pyplot(render_circuit(qc))

st.subheader("⚛️ Quantum Algorithms")
algo = st.selectbox("Choose Algorithm", ["None", "Deutsch-Jozsa", "Grover’s Search"])

if algo == "Deutsch-Jozsa":
    qc = deutsch_jozsa()
    st.pyplot(render_circuit(qc))
elif algo == "Grover’s Search":
    qc = grover()
    st.pyplot(render_circuit(qc))
