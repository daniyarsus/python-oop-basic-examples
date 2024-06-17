from dataclasses import dataclass


@dataclass(frozen=True)
class UserDTO:
    username: str
    password: str


print(
    UserDTO(
        username="Billy Harrington",
        password="qwerty12345"
    )
)
