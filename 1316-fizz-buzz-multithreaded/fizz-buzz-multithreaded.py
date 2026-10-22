from threading import Condition

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.condition = Condition()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printFizz()
                self.current += 1
                self.condition.notify_all()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printBuzz()
                self.current += 1
                self.condition.notify_all()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and self.current % 15 != 0:
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printFizzBuzz()
                self.current += 1
                self.condition.notify_all()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.condition:
            while self.current <= self.n:
                while self.current <= self.n and self.current % 3 == 0 or self.current <= self.n and self.current % 5 == 0:
                    self.condition.wait()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                printNumber(self.current)
                self.current += 1
                self.condition.notify_all()