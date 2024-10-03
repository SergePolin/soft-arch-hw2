import cv2
from pipeline.frame_pipeline import FramePipeline
from filters.resize_filter import ResizeFilter
from filters.black_and_white_filter import BnWFilter
from filters.mirror_filter import MirrorFilter
from filters.save_filter import SaveFilter

def main():
    pipeline = FramePipeline()
    pipeline.add_filter(ResizeFilter(width=640, height=480))
    pipeline.add_filter(BnWFilter())
    pipeline.add_filter(MirrorFilter())
    pipeline.add_filter(SaveFilter(output_path="processed_frames/"))
    pipeline.connect_filters()

    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Original Frame', frame)
        processed_frame = pipeline.process_frame(frame)
        cv2.imshow('Processed Frame', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
