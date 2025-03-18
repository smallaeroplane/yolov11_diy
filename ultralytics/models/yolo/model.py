
from pathlib import Path

class YOLO(Model):
    """YOLO (You Only Look Once) object detection model."""

    def __init__(self, model="yolo11n.pt", task=None, verbose=False):
        path = Path(model)
        if "-world" in path.stem and path.suffix in