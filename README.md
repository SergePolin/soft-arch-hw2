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

Run the main script to start the video processing pipeline:

```bash
python main.py
```
