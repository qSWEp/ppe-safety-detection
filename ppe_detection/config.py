# Camera sources to check at startup
CAMERA_SOURCES = [0]
# Reconnect attempts before marking a camera offline
MAX_RETRIES = 3
# Seconds to wait between reconnect attempts
RETRY_DELAY_SEC = 2
# Frames to analyze per second
SAMPLES_PER_SEC = 5
# Time between analyzed frames in (seconds) Calculated, do not edit manually Used by Camera.should_sample
SAMPLE_INTERVAL_SEC = 1 / SAMPLES_PER_SEC
# Key to close the display window
EXIT_KEY = "q"  # in ord q = 113
