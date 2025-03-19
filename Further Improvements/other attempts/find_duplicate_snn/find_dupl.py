import torch
import torch.nn as nn
import os

def load_state_dict(pth_file):
    """Loads a state dict from a .pth file."""
    print(pth_file)
    ann = nn.Sequential(
        nn.Linear(3, 256),  # Input layer: 3 features (mu, sigma, x)
        nn.ReLU(),
        nn.Linear(256, 256),  # first hidden layer
        nn.ReLU(),
        nn.Linear(256, 256),  # second hidden layer
        nn.ReLU(),
        nn.Linear(256, 1)    # Output layer: single value for f(x; mu, sigma)
    )
    try:
        #ann.load_state_dict()
        return torch.load(pth_file, map_location=torch.device('cpu'))
    except Exception as e:
        print(f"Error loading {pth_file}: {e}")
        return None

def find_matching_state_dict(base_path, given_pth_file):
    """Finds the .pth file in subdirectories that matches the given one."""
    given_state_dict = load_state_dict(given_pth_file)
    if given_state_dict is None:
        print("Failed to load given .pth file.")
        return None

    matching_file = None

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".pth"):
                file_path = os.path.join(root, file)
                
                if file_path == given_pth_file:
                    continue  # Skip the given file itself
                
                state_dict = load_state_dict(file_path)
                
                if state_dict and all(torch.equal(state_dict[k], given_state_dict[k]) for k in given_state_dict):
                    matching_file = file_path
                    print(f"Match found: {file_path}")
    
    if matching_file:
        return matching_file
    print("No matching state dict found.")
    return None

# Example usage
base_directory = "./other_files"  # Search in current directory and subdirectories
given_pth_file = "./low_range_log1p.pth"  # Replace with your actual file

match = find_matching_state_dict(base_directory, given_pth_file)
if match:
    print(f"The given .pth file matches with: {match}")
else:
    print("No match found.")
