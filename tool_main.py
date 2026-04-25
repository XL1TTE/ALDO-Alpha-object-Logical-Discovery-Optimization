import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.cli.tool import app

if __name__ == "__main__":
    app()
