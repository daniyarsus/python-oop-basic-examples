import inspect


class FirstObject:
    @staticmethod
    def first_phone(number: int) -> str:
        return f"1 number: {number}"


class SecondObject(FirstObject):
    @staticmethod
    def second_phone(number: int) -> str:
        return f"2 number {number}"


obj = SecondObject()
print(obj.first_phone(877781119999))
print(obj.second_phone(933329991111))

