import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from text_based_engine.runner import run

if __name__ == "__main__":
    run("example/example.txt")
