#          imports 
import logging
import cv2
from ppe_detection import config


logger = logging.getLogger(__name__)
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
        logger.debug(f"Created camera [{self.camera_id}] at the [{self.location}]")
        
    # Open the camera and update its status for main   
    def open(self):
        self.capture = cv2.VideoCapture(self.camera_id)
        if self.capture.isOpened():
            self.is_online = True
            self.fps = self.capture.get(cv2.CAP_PROP_FPS)
            logger.info(f"Camera [{self.camera_id}] at the [{self.location}] is online running at [{self.fps}] frames per second")
            return True
        else:
            self.capture.release()
            logger.warning(f"Camera [{self.camera_id}] at the [{self.location}] is not responding")
            return False
        
    # Read the capture after open
    def read(self):
        #  Stop if someone calls read() before open() or after the camera went offline
        if not self.is_online:
            return False, None
        ret, frame = self.capture.read()
        if not ret:
            self.is_online = False
            logger.warning(f"Camera [{self.camera_id}] at the [{self.location}] is offline")
        return ret, frame
        
        