from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

def generate_key():

    qc = QuantumCircuit(8,8)

    qc.h(range(8))
    qc.measure(range(8), range(8))

    simulator = AerSimulator()

    compiled = transpile(qc, simulator)

    result = simulator.run(compiled, shots=1).result()

    counts = result.get_counts()

    key = list(counts.keys())[0]

    return key