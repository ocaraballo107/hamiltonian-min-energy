## Hamiltonian Minimun Value of Energy implemented on IBM-Q, Python.

This program uses quantum annealing using IBM-Q and Qiskit to solve a simple Quadratic Unconstrained Binary Optimization (QUBO) problem.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This code uses Qiskit Aqua's Quantum Approximate Optimization Algorithm (QAOA) to solve the QUBO problem. The QUBO is created by first defining the objective function f(x), then converting it into an Ising Hamiltonian using docplex.get_operator. The QAOA algorithm is then used to find the solution that minimizes the Hamiltonian.

## Installation

To install the GitHub repository for Hamiltonian Min application, follow these steps. 
First, To run this code, you need to have an IBM Quantum Experience account and install the Qiskit library using pip (pip install qiskit).
Once cloned, navigate to the project's root directory in the terminal and run the command "hamiltonian-min.py" to start the program. 

# Example usage:

Define the objective function f(x) = x^2 - 4x + 4

## Clone Repository

git clone https://github.com/ocaraballo107/codes/hamilton-min.git

## Navigate to the project directory

In your environment cd your-project.

## Usage

On your terminal, once hamilton-min.py is running:

Define the objective function. Ex: f(x) = x^2 - 4x + 4

## Features

This code uses Qiskit Aqua's Quantum Approximate Optimization Algorithm (QAOA) to solve the QUBO problem. 
The QUBO is created by first defining the objective function f(x), then converting it into an Ising Hamiltonian using docplex.get_operator. 
The QAOA algorithm is then used to find the solution that minimizes the Ising Hamiltonian.

The result will be the optimal value of x that minimizes the function f(x).

Please note that this example uses the simulator backend for simplicity. To run on an actual IBM Quantum device, you need to have access to a real quantum system and modify the quantum_instance accordingly. Keep in mind that noise in real quantum devices may affect the performance of the algorithm.

## Contact

I can be reach for questions regarding this project at: ocaraballo107@gmail.com

# License

This project is under MIT Full Stack license program.
