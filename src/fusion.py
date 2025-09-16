def fuse_sensors(data):
    """Simple fusion: take the minimum distance (worst-case)"""
    return min(data["lidar"], data["radar"], data["camera"])
