from filters.base_filter import BaseFilter
import cv2
import os
from datetime import datetime

class SaveFilter(BaseFilter):
    def __init__(self, output_path: str):
        super().__init__()
        self.output_path = output_path
        os.makedirs(self.output_path, exist_ok=True)

    def process(self):
        frame = self.input_queue.get()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"frame_{timestamp}.jpg"
        filepath = os.path.join(self.output_path, filename)
        cv2.imwrite(filepath, frame)
        self.output_queue.put(frame)
