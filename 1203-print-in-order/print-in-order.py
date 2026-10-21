from threading import Lock

class Foo:
    def __init__(self):
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock2:
            printSecond()
            self.lock3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock3:
            printThird()