from filters.base_filter import BaseFilter
import cv2

class ResizeFilter(BaseFilter):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height

    def process(self):
        frame = self.input_queue.get()
        resized_frame = cv2.resize(frame, (self.width, self.height))
        self.output_queue.put(resized_frame)
