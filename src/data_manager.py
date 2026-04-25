import csv
import random
from typing import List

def generate_synthetic_data(n_pos: int = 5, n_neg: int = 5) -> List[List[float]]:
    data: List[List[float]] = []
    # Generate positive points centered around (1, 2)
    for _ in range(n_pos):
        data.append([round(random.uniform(0.5, 2.0), 2), round(random.uniform(1.0, 3.0), 2), 1.0])
    # Generate negative points centered around (4, 4)
    for _ in range(n_neg):
        data.append([round(random.uniform(3.0, 5.0), 2), round(random.uniform(3.0, 5.0), 2), 0.0])
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
                if row:
                    data.append([float(x) for x in row])
        return data
    except Exception as e:
        raise ValueError(f"Failed to load CSV: {e}")
