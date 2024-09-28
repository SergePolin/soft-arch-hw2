import cv2
import numpy as np

class Filter:
    def execute(self, frame):
        raise NotImplementedError("This method should be overridden by subclasses.")

class GrayscaleFilter(Filter):
    def execute(self, frame):
        if len(frame.shape) == 3 and frame.shape[2] == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif len(frame.shape) == 2:
            gray = frame
        else:
            raise ValueError("Input frame must have 3 channels (BGR) or be already grayscale")
        return gray

class MirrorFilter(Filter):
    def execute(self, frame):
        return cv2.flip(frame, 1)

class ResizeFilter(Filter):
    def __init__(self, scale=0.5):
        self.scale = scale

    def execute(self, frame):
        width = int(frame.shape[1] * self.scale)
        height = int(frame.shape[0] * self.scale)
        return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

class EdgeDetectionFilter(Filter):
    def execute(self, frame):
        if len(frame.shape) == 3 and frame.shape[2] == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif len(frame.shape) == 2:
            gray = frame
        else:
            raise ValueError("Input frame must have 3 channels (BGR) or be already grayscale")
        edges = cv2.Canny(gray, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def mirror(frame):
    return cv2.flip(frame, 1)

def resize(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

def edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def get_filter_function(filter_name):
    filters = {
        'grayscale': grayscale,
        'mirror': mirror,
        'resize': resize,
        'edge': edge_detection
    }
    return filters.get(filter_name.lower())