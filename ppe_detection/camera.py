#          imports 
import cv2
from ppe_detection import config


class Camera:
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self.is_online = False
        self.capture = None
        self.fps = None
        self.last_sample_time = None
        self.offline_since = None
        self.retry_count = 0
        
        