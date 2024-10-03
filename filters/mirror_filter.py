from filters.base_filter import BaseFilter
import cv2

class MirrorFilter(BaseFilter):
    def process(self):
        frame = self.input_queue.get()
        mirrored_frame = cv2.flip(frame, 1)  # 1 for horizontal flip
        self.output_queue.put(mirrored_frame)
