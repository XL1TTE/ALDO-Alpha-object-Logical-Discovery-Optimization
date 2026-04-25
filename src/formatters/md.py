from __future__ import annotations
from typing import TYPE_CHECKING
from .base import BaseFormatter

if TYPE_CHECKING:
    from ..generator import PatternModel

class MarkdownFormatter(BaseFormatter):
    def format(self, model: PatternModel) -> str:
        class_label = "Positive" if model.is_positive else "Negative"
        md = f"## Alpha-Object {model.alpha_idx} ({class_label})\n\n"
        md += f"**Alpha coordinates:** `({model.alpha_obj[0]}, {model.alpha_obj[1]})`\n\n"
        
        # Objective in LaTeX
        md += "### Objective\n"
        md += "$$\\max Z = \\sum_{i \\in S^+} \\mathbb{I}(a_1 \\le x_{i1} \\le b_1 \\land a_2 \\le x_{i2} \\le b_2)$$\n\n"
        md += "Specifically:\n"
        terms = [
            f"\\mathbb{{I}}({model.data[i][0]} \\in [a_1, b_1] \\land {model.data[i][1]} \\in [a_2, b_2])" 
            for i in model.target_set
        ]
        md += "$$Z = " + " + ".join(terms) + "$$\n\n"
        
        # Constraints in LaTeX
        md += "### Constraints\n"
        md += "1. **Anchor constraint (Alpha):**\n"
        md += f"   $$a_1 \\le {model.alpha_obj[0]} \\le b_1, \\quad a_2 \\le {model.alpha_obj[1]} \\le b_2$$\n\n"
        md += "2. **Negative constraints (Opposite Class):**\n"
        md += "$$\\forall i \\in S^-, \\quad \\mathbb{I}(x_{i1} \\in [a_1, b_1] \\land x_{i2} \\in [a_2, b_2]) = 0$$\n\n"
        md += "Explicitly:\n"
        for i in model.opposite_set:
            md += f"- $$\\mathbb{{I}}({model.data[i][0]} \\in [a_1, b_1] \\land {model.data[i][1]} \\in [a_2, b_2]) = 0$$\n"
        
        return md

    def get_extension(self) -> str:
        return "md"

    def get_header(self) -> str:
        return "# Pattern Discovery Optimization Models\n\n"

    def get_separator(self) -> str:
        return "\n---\n\n"
