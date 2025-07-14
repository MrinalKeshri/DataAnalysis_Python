#1st Challenge
# Link ("https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator")

import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(input_list).reshape(3, 3)

    calculations = {
        "mean": [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a).item()],
        "variance": [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a).item()],
        "standard deviation": [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a).item()],
        "max": [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a).item()],
        "min": [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a).item()],
        "sum": [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a).item()]
    }

    return calculations
