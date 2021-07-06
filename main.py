def f(i: int = 0):
    i = "test"  # This is a mypy violation.
    print(i)

if __name__ == "__main__":
    f()
