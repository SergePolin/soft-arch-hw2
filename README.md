# Video Processing Pipeline

This project implements a **Video Processing Pipeline** using the **Pipes and Filters** architectural pattern. It processes video frames from a webcam or video file in real-time, applying various filters such as resizing, black and white conversion, mirroring, and saving frames.

## Features

- **Real-time Video Processing:** Capture and process video streams from a webcam or video file.
- **Modular Filter System:** Utilize a pipes-and-filters architecture for easy management and extension of filters.
- **Implemented Filters:**
  - **Resize:** Adjust the dimensions of each video frame.
  - **Black and White:** Convert color frames to grayscale.
  - **Mirror:** Horizontally flip video frames.
  - **Save:** Save processed frames to disk for later use.
- **Extensible Design:** Easily add new filters to the pipeline with minimal effort.

## Architecture Overview

The app follows the Pipes-and-Filters pattern. Each filter applies a transformation to video frames in sequence. The system is modular and easily extensible, allowing filters to be added or removed from the pipeline with minimal changes.

### Data Flow 

1. The script captures video frames from a source (web camera or video file).
2. Captured frames are passed through the pipeline, where each filter is applied in sequence.
  - Filters include resizing, black-and-white conversion, mirroring, and saving frames.
  - If a filter is disabled, the frame bypasses that filter and proceeds to the next one in the sequence.
3. The processed frames are displayed in real-time.

### Components

- **Filters**: 
  - The `filters/` contains all the filter classes. Each filter inherits from the `BaseFilter` class defined in `base_filter.py`, ensuring that all filters have a uniform interface.
  - The current filters:
    - `black_and_white_filter.py`: Converts frames to black and white.
    - `mirror_filter.py`: Horizontally mirrors the frames.
    - `resize_filter.py`: Resizes the video frames.
    - `save_filter.py`: Saves the transformed frames to the disk.

- **Pipeline**: 
  - The `FramePipeline` class is responsible for managing the sequence of filters and ensuring that data flows correctly from one filter to the next. It uses a shared `queue` to handle the flow of frames, providing flexibility in adding, removing, or disabling filters as needed.

## Requirements

- **Python 3.10+**
- **OpenCV:** For video capture and processing.
- **NumPy:** For numerical operations on frame data.
- **Pillow:** For image processing.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SergePolin/soft-arch-hw2
   cd soft-arch-hw2
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install the Required Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### For the video from web camera:

Run the main script to start the video processing pipeline:

```bash
python main.py
```

### For the recorded video file:

To process video frames from a video file, modify the main.py file to specify the video file path:

```python
cap = cv2.VideoCapture('path/to/your/video.mp4') 
```
Then, run the script:

```bash
python main.py
```
