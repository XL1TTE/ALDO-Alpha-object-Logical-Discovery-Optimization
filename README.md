# 🎯 ALDO: Alpha-object Logical Discovery & Optimization

Welcome to **ALDO**! This tool is designed for academic and research purposes, specifically focusing on the **Alpha-Object approach** for finding maximal logical regularities.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Overview

This application helps researchers and students formulate mathematical optimization models to find patterns in classification datasets. It implements the **Alpha-Object methodology**, where patterns are anchored to specific observations to maximize coverage while strictly avoiding negative class objects.

### ✨ Key Features

*   **Dual Mode Interface:** 
    *   🎮 **Interactive CLI:** A beautiful, guided experience with progress bars and menus.
    *   🛠️ **CLI Tool:** A powerful command-line utility for automation and scripting.
*   **Native OS Integration:** Standard Windows File Open/Save dialogs for a seamless experience.
*   **Beautiful Formatting:**
    *   📄 **Plain Text:** Clean, readable format for quick inspection.
    *   📊 **Markdown + LaTeX:** High-quality mathematical notation ready for reports and academic papers.
*   **Modern Architecture:** Built with type safety, strategy patterns, and clean separation of concerns.

---

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/XL1TTE/ALDO-Alpha-object-Logical-Discovery-Optimization.git
    cd ALDO-Alpha-object-Logical-Discovery-Optimization
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    # source .venv/bin/activate  # Unix/macOS
    ```

3.  **Install dependencies:**
    ```bash
    pip install -e .
    ```

---

## 🛠️ Usage

### 🎮 Interactive Mode (Recommended)
Perfect for beginners and manual exploration.
```bash
python cli_main.py
# or
pattern-interactive
```

### 🛠️ Tool Mode (Automated)
Ideal for batch processing and integration into other workflows.
```bash
python tool_main.py generate --csv "data.csv" --output "models.md" --format md
# or
pattern-tool generate -i "data.csv" -o "models.txt"
```

---

## 📁 Project Structure

```text
Lab_3/
├── cli_main.py          # 🚀 Interactive Entry Point
├── tool_main.py         # 🛠️ CLI Tool Entry Point
├── pyproject.toml       # 📦 Dependency Management
├── src/
│   ├── cli/             # 🖥️ UI Orchestration
│   ├── formatters/      # 🎨 Formatting Strategy (TXT, MD)
│   ├── generator.py     # 🧠 Core Mathematical Logic
│   ├── data_manager.py  # 📊 Data Loading & Generation
│   └── native_dialogs.py # 🪟 Windows API Integration
└── ...
```

---

## 📝 Mathematical Context

The generator builds models following the logic:
*   **Objective:** $\max Z = \sum \mathbb{I}(x \in [a, b])$
*   **Constraint 1:** The $\alpha$-object MUST be within $[a, b]$.
*   **Constraint 2:** NO objects from the opposite class can be within $[a, b]$.

---
