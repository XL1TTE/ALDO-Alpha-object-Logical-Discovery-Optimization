import csv
import random
from typing import List

def generate_synthetic_data(n_pos: int = 5, n_neg: int = 5, n_features: int = 2) -> List[List[float]]:
    data: List[List[float]] = []
    
    # Generate positive points centered around 1.0 - 2.0
    for _ in range(n_pos):
        row = [round(random.uniform(0.5, 2.0), 2) for _ in range(n_features)]
        row.append(1.0) # Class
        data.append(row)
        
    # Generate negative points centered around 3.0 - 5.0
    for _ in range(n_neg):
        row = [round(random.uniform(3.0, 5.0), 2) for _ in range(n_features)]
        row.append(0.0) # Class
        data.append(row)
        
    return data

def load_data_from_csv(file_path: str) -> List[List[float]]:
    data: List[List[float]] = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Skip header if present (check if first row is numeric)
            first_row = next(reader)
            try:
                float(first_row[0])
                data.append([float(x) for x in first_row])
            except ValueError:
                pass # It was a header
                
            for row in reader:
                if row and len(row) > 0:
                    data.append([float(x) for x in row])
        return data
    except Exception as e:
        raise ValueError(f"Failed to load CSV: {e}")
