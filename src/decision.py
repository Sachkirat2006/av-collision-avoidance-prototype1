import time

THRESHOLD = 10  # meters
REACTION_TIME = 0.1  # 100ms

def decide_action(distance):
    """Decide whether to brake or steer based on distance"""
    if distance < THRESHOLD:
        time.sleep(REACTION_TIME)  # simulate processing delay
        if distance < 5:
            return "BRAKE!"
        else:
            return "STEER!"
    return "SAFE"

