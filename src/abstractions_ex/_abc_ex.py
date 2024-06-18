from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self, velocity: float) -> str:
        ...

    def color(self, name: str) -> str:
        ...


class Bugatti(Car):
    def drive(self, velocity: float) -> float:
        return f"Bugatti's velocity is {velocity}"

    def color(self, name: str) -> str:
        return f"Bugatti's color is {name}"


bugatti = Bugatti()
print(bugatti.drive(100))
print(bugatti.color("black"))
