from typing import override


class Base:
    def get_color(self) -> str:
        return "blue"


class GoodChild(Base):
    @override  # ok: overrides Base.get_color
    def get_color(self) -> str:
        return "yellow"


class BadChild(Base):
    @override  # type checker error: does not override Base.get_color
    def get_colour(self) -> str:
        return "red"
