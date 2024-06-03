import numpy as np
from least_core import calculate_least_core

def load_data():
    # Placeholder function to load data
    players = ['client1', 'client2', 'client3']
    values = {
        ('client1',): 1.0,
        ('client2',): 1.2,
        ('client3',): 1.1,
        ('client1', 'client2'): 2.5,
        ('client1', 'client3'): 2.3,
        ('client2', 'client3'): 2.6,
        ('client1', 'client2', 'client3'): 4.0
    }
    return players, values

def main():
    # Load data and initialize variables
    players, values = load_data()
    
    # Calculate least core
    least_core_value, least_core_distribution = calculate_least_core(players, values)
    
    print(f"Least Core Value: {least_core_value}")
    print(f"Least Core Distribution: {least_core_distribution}")
    
    # Use least core distribution for client selection
    threshold = 0.1  # Define a threshold for selection
    selected_clients = [players[i] for i in range(len(players)) if least_core_distribution[i] > threshold]
    
    print(f"Selected Clients: {selected_clients}")

if __name__ == "__main__":
    main()
