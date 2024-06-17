class Resume:
    def __init__(
            self,
            age: int,
            name: str,
            goal: str
    ) -> None:
        self.age = age
        self.name = name
        self.goal = goal

    def get_results(self) -> str:
        if self.age > 15:
            return "Ewww, brooo... Learn more seriously language :D"

        if self.goal != "I wanna more money.":
            return "You are liar -_-"

        return f"We can accept you in position 7/0 with 100$ in year!"
