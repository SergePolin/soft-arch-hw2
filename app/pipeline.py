class Pipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def process(self, frame):
        for filter in self.filters:
            frame = filter.execute(frame)
        return frame

def process_video(source, filters):
    import cv2
    from .filters import GrayscaleFilter, MirrorFilter, ResizeFilter, EdgeDetectionFilter

    if isinstance(source, str):
        cap = cv2.VideoCapture(source)
    else:
        cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"Error: Could not open video source {source}.")
        return

    pipeline = Pipeline()
    available_filters = {
        'grayscale': GrayscaleFilter(),
        'mirror': MirrorFilter(),
        'resize': ResizeFilter(scale=0.75),
        'edge': EdgeDetectionFilter()
    }

    if filters:
        for f in filters:
            if f in available_filters:
                pipeline.add_filter(available_filters[f])
            else:
                print(f"Warning: Unknown filter '{f}'. Skipping.")
    else:
        for f in available_filters.values():
            pipeline.add_filter(f)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream reached")
            break

        processed_frame = pipeline.process(frame)

        cv2.imshow('Processed Video', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

__all__ = ['Pipeline', 'process_video']