class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


def main() -> None:
    p = Point(3, 4)
    print(p)  # Output: (3, 4)


if __name__ == "__main__":
    main()