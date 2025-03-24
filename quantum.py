from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import random

def quantum_coin_flip(shots=1024):
    """
    Simulates a quantum coin flip using Qiskit.

    Args:
        shots (int): The number of times to run the simulation.  More shots
                     give more accurate statistics.  Defaults to 1024.

    Returns:
        dict: A dictionary containing the counts of '0' and '1' outcomes.
              For example: {'0': 512, '1': 512}
    """
    # Create a quantum circuit with 1 qubit
    qc = QuantumCircuit(1)

    # Apply a Hadamard gate (H gate) to the qubit.
    # The H gate puts the qubit into a superposition of |0> and |1>,
    # which is analogous to a coin spinning in the air.
    qc.h(0)

    # Add measurement
    qc.measure_all()

    # Create a simulator
    simulator = AerSimulator()
    
    # Run the circuit directly with the simulator
    result = simulator.run(qc, shots=shots).result()
    
    # Get the counts
    counts = result.get_counts()
    
    # Print and plot the results.
    print("Quantum Coin Flip Results:")
    plot_histogram(counts).show()  # Shows the plot

    return counts  # Return the counts


def classical_coin_flip(shots=1024):
    """
    Simulates a classical coin flip using Python's random module.

    Args:
        shots (int): The number of times to flip the coin.
                     Defaults to 1024.

    Returns:
        dict: A dictionary containing the counts of '0' (tails) and
              '1' (heads) outcomes.
    """
    classical_results = []
    for _ in range(shots):
        # random.randint(0, 1) returns either 0 or 1 with equal probability.
        classical_results.append(random.randint(0, 1))

    classical_counts = {}
    for result in classical_results:
        # Count the number of times each outcome (0 or 1) occurs.
        if str(result) in classical_counts:
            classical_counts[str(result)] += 1
        else:
            classical_counts[str(result)] = 1

    # Print and plot the results.
    print("\nClassical Coin Flip Results:")
    plot_histogram(classical_counts).show()  # Shows the plot

    return classical_counts  # Return the counts


def compare_results(quantum_counts, classical_counts):
    """
    Compares the results of the quantum and classical coin flips.

    Args:
        quantum_counts (dict): The results from quantum_coin_flip().
        classical_counts (dict): The results from classical_coin_flip().
    """
    print("\nComparison:")
    print("Quantum Results:", quantum_counts)
    print("Classical Results:", classical_counts)

    # Calculate and print probabilities for easier comparison.
    total_shots = sum(quantum_counts.values())
    quantum_probabilities = {
        bit: count / total_shots for bit, count in quantum_counts.items()
    }
    print("\nQuantum Probabilities:", quantum_probabilities)

    total_shots = sum(classical_counts.values())
    classical_probabilities = {
        bit: count / total_shots for bit, count in classical_counts.items()
    }
    print("Classical Probabilities:", classical_probabilities)

    # Additional plot showing both results on one graph using matplotlib.
    plt.figure()  # Create a new figure for the combined plot.

    # Subplot for Quantum results
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, select the first subplot
    plt.title("Quantum")
    plt.bar(quantum_counts.keys(), quantum_counts.values())

    # Subplot for Classical results
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, select the second subplot
    plt.title("Classical")
    plt.bar(classical_counts.keys(), classical_counts.values())

    plt.tight_layout()  # Adjust layout to prevent overlapping titles/labels
    plt.show()  # Display the combined plot


if __name__ == "__main__":
    # Main execution block.  This code runs when you execute the script.
    # Before running this, make sure you have qiskit-aer installed:
    # pip install qiskit qiskit-aer matplotlib
    shots = 2048  # Increase the number of shots for better statistics
    quantum_result = quantum_coin_flip(shots=shots)  # Run quantum simulation
    classical_result = classical_coin_flip(shots=shots)  # Run classical simulation
    compare_results(quantum_result, classical_result)  # Compare the results
