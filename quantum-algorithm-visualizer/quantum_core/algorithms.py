from qiskit import QuantumCircuit

def deutsch_jozsa():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0], [0])
    return qc

def grover():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    return qc
