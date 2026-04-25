from __future__ import annotations
from typing import List

class PatternModel:
    """Pure data class for holding optimization model parameters."""
    
    alpha_idx: int
    alpha_obj: List[float]
    is_positive: bool
    target_set: List[int]
    opposite_set: List[int]
    data: List[List[float]]

    def __init__(
        self, 
        alpha_idx: int, 
        alpha_obj: List[float], 
        is_positive: bool, 
        target_set: List[int], 
        opposite_set: List[int], 
        data: List[List[float]]
    ) -> None:
        self.alpha_idx = alpha_idx
        self.alpha_obj = alpha_obj
        self.is_positive = is_positive
        self.target_set = target_set
        self.opposite_set = opposite_set
        self.data = data

def generate_models(data: List[List[float]]) -> List[PatternModel]:
    pos_indices: List[int] = [i for i, row in enumerate(data) if row[2] == 1]
    neg_indices: List[int] = [i for i, row in enumerate(data) if row[2] == 0]
    
    models: List[PatternModel] = []
    for i in range(len(data)):
        alpha_obj = data[i]
        is_pos = alpha_obj[2] == 1
        target = pos_indices if is_pos else neg_indices
        opposite = neg_indices if is_pos else pos_indices
        models.append(PatternModel(i, alpha_obj, is_pos, target, opposite, data))
    return models
