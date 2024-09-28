import cv2
from .pipeline import Pipeline
from .filters import GrayscaleFilter, MirrorFilter, ResizeFilter, EdgeDetectionFilter

def capture_video(source=0, filters=None):
    if isinstance(source, str):
        cap = cv2.VideoCapture(source)
    else:
        cap = cv2.VideoCapture(source)  # Default webcam

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
        # Default to all filters if none specified
        for f in available_filters.values():
            pipeline.add_filter(f)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream reached")
            break

        processed_frame = pipeline.apply_filters(frame)

        cv2.imshow('Processed Video', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()