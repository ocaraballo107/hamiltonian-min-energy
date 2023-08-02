# This program finds the minimum value of a Hamiltonian using Quadratic Unconstrained Binary Optimization.
from qiskit import BasicAer, transpile, assemble
from qiskit.aqua.algorithms import QAOA
from qiskit.aqua.components.optimizers import SPSA
from qiskit.optimization.applications.ising import docplex
from qiskit.optimization.applications.ising.common import sample_most_likely

# Define the objective function f(x) = x^2 - 4x + 4
def objective(x):
    return x ** 2 - 4 * x + 4

def main():
    # Create a docplex model to represent the QUBO problem
    model = docplex.DocplexModel()
    x = model.binary_var(name='x')
    model.minimize(objective(x))

    # Convert the docplex model to an Ising Hamiltonian
    qubit_op, offset = docplex.get_operator(model)

    # Set up the Quantum Approximate Optimization Algorithm (QAOA)
    optimizer = SPSA(max_trials=100)
    quantum_instance = BasicAer.get_backend('qasm_simulator')
    qaoa = QAOA(qubit_op, optimizer, p=1)

    # Run QAOA and get the result
    result = qaoa.run(quantum_instance)

    # Extract the solution
    x_solution = sample_most_likely(result.eigenstate)

    # Calculate the minimum value of the objective function
    min_value = objective(x_solution)

    print("Minimum value found:", min_value)
    print("x =", x_solution)

if __name__ == "__main__":
    main()
