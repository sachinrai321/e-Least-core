import numpy as np
import torch
from torch.utils.data import Dataset
from data_preprocess import NIIDClientSplit 

# Define a custom dataset class
class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx][0], self.data[idx][1], idx  # returning data, target, and index

# Create a dataset with data and labels (example using tuples)
train_dataset = [(np.random.rand(10), i % 10) for i in range(1000)]

# Convert the list of tuples into a PyTorch dataset
train_data = CustomDataset(train_dataset)

# Number of clients
num_clients = 100

# Dirichlet parameter (alpha)
alpha = 0.5

def NIIDClientSplit(train_data, num_clients, alpha):
    # Get unique target labels and their counts
    unique_targets, target_counts_global = np.unique(
        [sample[1] for sample in train_data],
        return_counts=True
    )

    # Number of samples in the dataset
    num_samples = len(train_data)

    # Sample number of samples for each client according to a Dirichlet distribution
    num_samples_per_client = np.random.dirichlet([alpha] * num_clients) * num_samples

    # Round the number of samples per client to integers
    num_samples_per_client = np.round(num_samples_per_client).astype(int)

    # Ensure that the total number of samples matches the original number of samples
    while np.sum(num_samples_per_client) != num_samples:
        if np.sum(num_samples_per_client) > num_samples:
            idx = np.random.randint(0, num_clients)
            if num_samples_per_client[idx] > 0:
                num_samples_per_client[idx] -= 1
        else:
            idx = np.random.randint(0, num_clients)
            num_samples_per_client[idx] += 1

    # Assign samples to clients randomly
    client_indices = []
    start_idx = 0
    for num in num_samples_per_client:
        end_idx = start_idx + num
        client_indices.append(list(range(start_idx, end_idx)))
        start_idx = end_idx

    return client_indices

# Splitting the dataset using NIIDClientSplit
client_indices = NIIDClientSplit(train_data, num_clients, alpha)

# client_indices is a list containing indices of data samples for each client
# Each element of client_indices represents a client's subset of the dataset
print(client_indices)
