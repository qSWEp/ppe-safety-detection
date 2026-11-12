#          imports 
import logging , time
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
            # Heir reset capture object to Default for release()
            self.capture = None
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
     
    # Release the camera if it is in use (for example reconnection)   
    def release(self):
        if self.capture is None:
            logger.debug(f"Camera [{self.camera_id}] at the [{self.location}] is already released")
            return
        # Reset object to Default Value
        self.capture.release()
        self.capture = None
        self.is_online = False
        logger.info(f"Camera [{self.camera_id}] at the [{self.location}] was released")
    # reconnect the camera if it go offline and try to conecct based on the number in config.MAX_RETRIES     
    def reconnect(self):
        self.release()
        for attempt in range(config.MAX_RETRIES):
            logger.warning(f"Trying to reconnect camera [{self.camera_id}] at the [{self.location}] attempt [{attempt + 1} of {config.MAX_RETRIES}]")
            # Here re call open() to Check if True
            if self.open():
                return True
            time.sleep(config.RETRY_DELAY_SEC)
        # Here if thir is no respones after compeliton all attempt 
        self.offline_since = time.time()
        universal_time = time.gmtime(self.offline_since)
        readable = time.strftime("%Y-%m-%d %H:%M:%S", universal_time)
        logger.error(f"Camera [{self.camera_id}] at the [{self.location}] is offline since [{readable}] UTC after [{config.MAX_RETRIES}] attempts")
        return False