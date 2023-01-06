# === Floats ===


# What will the following lines print out and why?
if __name__ == "__main__":
    print(0.1 + 0.2 == 0.3)

    print(1.0 + 2.0 == 3.0)

    print(0.2 + 0.3 + 0.4 == 0.2 + 0.4 + 0.3)

    print(1.0 + 1e100 > 1e100)


# Write functions and tests for approximate comparisons


def approx_eq(a: float, b: float) -> bool:
    pass


def approx_neq(a: float, b: float) -> bool:
    pass


def approx_gt():
    pass


def approx_ge():
    pass


def approx_lt():
    pass


def approx_le():
    pass
