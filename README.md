# Video Processing Application

This application processes video streams or files using various filters, providing a flexible and easy-to-use command-line interface for video manipulation.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Options](#options)
  - [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributors](#contributors)

## Features

- Apply multiple filters to video streams or files
- Support for the following filters:
  - **Grayscale**: Converts the video to black and white
  - **Mirror**: Flips the video horizontally
  - **Resize**: Scales the video (default: 75% of original size)
  - **Edge Detection**: Highlights edges in the video
- Command-line interface for easy usage and customization
- Real-time processing and display of filtered video
- Support for both webcam input and video file processing

## Requirements

- Python 3.6+
- OpenCV (cv2)
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SergePolin/soft-arch-hw2
   cd soft-arch-hw2
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the following command:

```bash
python app.py [options]
```

### Options

- `--source`: Specify the input source (0 for webcam, or path to a video file)
- `--filters`: Specify the filters to apply (space-separated list)

### Examples

1. Process webcam input with grayscale and mirror filters:

   ```bash
   python app.py --source 0 --filters grayscale mirror
   ```

2. Process a video file with edge detection and resize filters:

   ```bash
   python app.py --source path/to/video.mp4 --filters edge resize
   ```

3. Apply all filters to webcam input:

   ```bash
   python app.py --source 0 --filters grayscale mirror resize edge
   ```

## Project Structure

- `app.py`: Main application entry point
- `app/__init__.py`: Initializes the app module
- `app/pipeline.py`: Defines the video processing pipeline
- `app/filters.py`: Contains implementations of various filters
- `app/video_processor.py`: Handles video input and output

## Contributors

| Name            | Email                           |
| --------------- | ------------------------------- |
| Sergei Polin    | <s.polin@innopolis.university>  |
| Eleonora Pikalo | <e.pikalo@innopolis.university> |
| Sergey Katkov   | <s.katkov@innopolis.university> |
