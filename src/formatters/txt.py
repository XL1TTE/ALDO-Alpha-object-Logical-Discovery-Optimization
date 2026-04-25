from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseFormatter

if TYPE_CHECKING:
    from ..generator import PatternModel

class TxtFormatter(BaseFormatter):
    def format(self, model: PatternModel) -> str:
        class_label = "Positive" if model.is_positive else "Negative"
        text = f"--- Optimization Model for Alpha-Object {model.alpha_idx} ({class_label}) ---\n"
        text += f"Alpha coordinates: {model.alpha_obj[:-1]}\n\n"
        
        # Objective
        terms = [
            f"I(a_1 <= {model.data[i][0]} <= b_1 AND a_2 <= {model.data[i][1]} <= b_2)" 
            for i in model.target_set
        ]
        text += "Objective: Maximize Z = " + " + ".join(terms) + "\n\n"
        
        # Constraints
        text += "Constraints:\n"
        text += f"  1. a_1 <= {model.alpha_obj[0]} <= b_1, a_2 <= {model.alpha_obj[1]} <= b_2\n"
        for i in model.opposite_set:
            text += f"  2. I(a_1 <= {model.data[i][0]} <= b_1 AND a_2 <= {model.data[i][1]} <= b_2) = 0\n"
        
        return text

    def get_extension(self) -> str:
        return "txt"

    def get_separator(self) -> str:
        return "\n" + "="*50 + "\n\n"
