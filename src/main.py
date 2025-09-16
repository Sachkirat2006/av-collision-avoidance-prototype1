import time
import os
import matplotlib.pyplot as plt
from sensors import get_all_sensors
from fusion import fuse_sensors
from decision import decide_action

# log file path
log_file = os.path.join("logs", "events.log")

def log_event(event):
    """Append events to a log file with timestamps"""
    with open(log_file, "a") as f:
        line = f"{time.time()} - {event}\n"
        f.write(line)
        f.flush()            # flush buffer
        os.fsync(f.fileno()) # force write to disk
    print(f"[LOGGED] {event}")  # confirmation in console

# Map decisions to numeric values for timeline plot
decision_map = {"SAFE": 0, "STEER!": 1, "BRAKE!": 2}

if __name__ == "__main__":
    print("Starting AV Collision Avoidance Simulation (press Ctrl+C to stop)...\n")

    os.makedirs("logs", exist_ok=True)  # ensure logs/ folder exists

    # data for plotting
    distances = []
    actions = []
    timestamps = []

    plt.ion()  # interactive mode
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle("Autonomous Vehicle Collision Avoidance Prototype")

    i = 0
    try:
        while True:  # continuous loop until stopped
            sensors = get_all_sensors()
            fused = fuse_sensors(sensors)
            decision = decide_action(fused)

            # log + print
            event_text = f"Distance={fused:.2f}m, Decision={decision}"
            log_event(event_text)
            print(f"[{sensors['timestamp']:.2f}] Fused Distance={fused:.2f} → {decision}")

            distances.append(fused)
            actions.append(decision)
            timestamps.append(i)

            # --- Top Plot: Distance vs Time ---
            ax1.clear()
            ax1.set_title("Fused Distance vs Time")
            ax1.set_ylabel("Distance (m)")
            ax1.axhline(y=10, color='orange', linestyle='--', label="Steer Threshold")
            ax1.axhline(y=5, color='red', linestyle='--', label="Brake Threshold")
            ax1.plot(timestamps, distances, marker="o", label="Distance")

            # mark decisions on distance plot
            for t, d, a in zip(timestamps, distances, actions):
                if a == "STEER!":
                    ax1.scatter(t, d, color="orange", s=100, marker="s",
                                label="STEER" if "STEER" not in ax1.get_legend_handles_labels()[1] else "")
                elif a == "BRAKE!":
                    ax1.scatter(t, d, color="red", s=100, marker="X",
                                label="BRAKE" if "BRAKE" not in ax1.get_legend_handles_labels()[1] else "")

            ax1.legend(loc="upper right")

            # --- Bottom Plot: Decision Timeline ---
            ax2.clear()
            ax2.set_title("Decision Timeline")
            ax2.set_xlabel("Time (s)")
            ax2.set_ylabel("Decision")
            ax2.set_yticks([0, 1, 2])
            ax2.set_yticklabels(["SAFE", "STEER", "BRAKE"])
            ax2.plot(timestamps, [decision_map[a] for a in actions],
                     marker="o", linestyle="-", color="blue")

            # refresh plots
            plt.pause(0.01)

            time.sleep(1)  # 1-second delay (realistic sensor update)

            i += 1

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
        plt.ioff()
        plt.show()
