from typing import Any


class Parent:
    def __init__(
            self,
            eye_color:
            str, height:
            float, illnesses:
            list[str]
    ) -> None:
        self.eye_color = eye_color
        self.height = height
        self.illnesses = illnesses

    def get_info(self) -> list[Any]:
        return [
            self.eye_color,
            self.height,
            self.illnesses
        ]


class Child(Parent):
    def __init__(
            self,
            eye_color: str,
            height: float,
            illnesses: list[str],
            grade: str
    ) -> None:
        super().__init__(eye_color, height, illnesses)
        self.grade = grade

    def get_info(self) -> list[Any]:
        parent_info = super().get_info()
        parent_info.append(self.grade)
        return parent_info


parent = Parent("blue", 180.0, ["hypertension"])
child = Child("green", 150.0, ["asthma"], "5th grade")

print(parent.get_info())
print(child.get_info())
