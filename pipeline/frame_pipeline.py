from queue import Queue
from filters.base_filter import BaseFilter
from filters.black_and_white_filter import BnWFilter
from filters.mirror_filter import MirrorFilter
from filters.resize_filter import ResizeFilter
from filters.save_filter import SaveFilter

class FramePipeline:
    def __init__(self):
        self.filters = []
        self.source_pipe = Queue()
        self.sink_pipe = Queue()

    def add_filter(self, filter: BaseFilter):
        self.filters.append(filter)

    def connect_filters(self):
        if not self.filters:
            return

        prev_output = self.source_pipe
        for filter in self.filters:
            filter.set_input(prev_output)
            prev_output = filter.get_output()

        self.sink_pipe = prev_output

    def process_frame(self, frame):
        self.source_pipe.put(frame)
        for filter in self.filters:
            filter.process()
        return self.sink_pipe.get()
