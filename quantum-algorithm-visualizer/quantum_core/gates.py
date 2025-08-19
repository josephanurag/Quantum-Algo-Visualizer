from qiskit import QuantumCircuit

def apply_gate(circuit, gate_name, qubit):
    if gate_name == "H":
        circuit.h(qubit)
    elif gate_name == "X":
        circuit.x(qubit)
    elif gate_name == "Y":
        circuit.y(qubit)
    elif gate_name == "Z":
        circuit.z(qubit)
    elif gate_name == "CX":
        circuit.cx(0, 1)
    elif gate_name == "Measure":
        circuit.measure_all()
    return circuit
