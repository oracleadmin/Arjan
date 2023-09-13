from typing import TypedDict, Unpack


class Movie(TypedDict):
    name: str
    year: int


def print_movie_info(**kwargs: Unpack[Movie]):
    print(type(kwargs))
    print(kwargs)


def main() -> None:
    movie: dict[str, object] = {"name": "Life of Brian", "year": 1979}
    print_movie_info(**movie)  # WRONG! Movie is of type dict[str, object]

    typed_movie: Movie = {"name": "The Meaning of Life", "year": 1983}
    print_movie_info(**typed_movie)  # OK!


if __name__ == "__main__":
    main()
