from abc import ABC, abstractmethod
from queue import Queue

class BaseFilter(ABC):
    def __init__(self):
        self.input_queue = None
        self.output_queue = Queue()

    def set_input(self, input_queue: Queue):
        self.input_queue = input_queue

    def get_output(self) -> Queue:
        return self.output_queue

    @abstractmethod
    def process(self):
        pass
