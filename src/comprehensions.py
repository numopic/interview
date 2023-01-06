# === Comprehensions ===

POINTS = [
    {"x": 0.1, "y": 0.0},
    {"x": 0.2, "y": -0.1},
    {"x": 0.16, "y": 2.1},
    {"x": -1.3, "y": 0.13},
    {"x": 1.05, "y": 0.17},
    {"x": 0.95, "y": -0.27},
    {"x": -0.72, "y": -0.75},
    {"x": 0.76, "y": 0.17},
    {"x": 0.35, "y": 0.24},
    {"x": 0.14, "y": 0.28},
]

# Filter points with x greater or equal to 0
points_with_x_ge_0 = []

# Filter points strictly above the line with equation
# `y = 0.5 * x - 0.2`
points_above_line = []
