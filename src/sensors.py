import random
import time

def get_lidar():
    return random.uniform(2, 100)  # distance in meters

def get_radar():
    return random.uniform(2, 100)

def get_camera():
    return random.uniform(2, 100)

def get_all_sensors():
    """Return simulated sensor readings"""
    return {
        "lidar": get_lidar(),
        "radar": get_radar(),
        "camera": get_camera(),
        "timestamp": time.time()
    }
