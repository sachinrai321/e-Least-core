from least_core import calculate_least_core

class Server:
    def __init__(self, clients):
        self.clients = clients
    
    def select_clients(self, values):
        players = [client.id for client in self.clients]
        
        # Calculate least core
        least_core_value, least_core_distribution = calculate_least_core(players, values)
        
        # Use least core distribution for client selection
        threshold = 0.1
        selected_clients = [self.clients[i] for i in range(len(players)) if least_core_distribution[i] > threshold]
        
        return selected_clients

# Example usage:
# server = Server(clients)
# selected_clients = server.select_clients(values)
