from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    quote: str
    source: str
    ref: str


class UniversalLaw:
    name: str
    code: str
    uid: str
    version: str = "1.0.0-IMMUTABLE"
    sources: tuple[Source, ...]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(code={self.code!r})"

    def __str__(self) -> str:
        return f"{self.name}: {self.code}"
