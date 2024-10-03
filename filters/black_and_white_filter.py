from filters.base_filter import BaseFilter
import cv2

class BnWFilter(BaseFilter):
    def process(self):
        frame = self.input_queue.get()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.output_queue.put(gray_frame)
