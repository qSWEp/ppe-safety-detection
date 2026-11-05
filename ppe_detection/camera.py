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
        
    # Open the camera and update its status for main   
    def open(self):
        self.capture = cv2.VideoCapture(self.camera_id)
        if self.capture.isOpened():
            self.is_online = True
            self.fps = self.capture.get(cv2.CAP_PROP_FPS)
            return True
        else:
            self.capture.release()
            return False
        
        
        