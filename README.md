# av-collision-avoidance-prototype1
Prototype collision avoidance system for SIT217 Task 6.3D
# Autonomous Vehicle Collision Avoidance Prototype

## Overview
This repository contains a **prototype collision avoidance system** for autonomous vehicles, developed as part of **SIT217 – Introduction to Software Engineering (Task 6.3D)**.

The prototype simulates **lidar, radar, and camera sensors**, fuses their data, and makes real-time decisions:
- ✅ **SAFE** when no hazards are near  
- ⚠️ **STEER** when an object is closer than 10m  
- 🛑 **BRAKE** when an object is closer than 5m  

Outputs include:
- **Console messages** (SAFE, STEER, BRAKE)  
- **Live Graphs**:
  - Distance vs Time (with thresholds + decision markers)  
  - Decision Timeline (categorical SAFE / STEER / BRAKE)  
- **Log file** saved in `logs/events.log` with timestamps of all events  

---

## Project Structure
