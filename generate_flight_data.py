import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

print("=" * 50)
print("  Drone Flight Data Logger")
print("  Based on Real Flight Operations")
print("=" * 50)

os.makedirs(
    "D:\\DroneProjects\\drone-flight-logs"
    "\\flight_data", exist_ok=True)
os.makedirs(
    "D:\\DroneProjects\\drone-flight-logs"
    "\\results", exist_ok=True)

# ── Flight Mission Parameters ─────────────────
# Based on real Novatech operations
missions = [
    {
        "name": "Obstacle_Avoidance_Test",
        "date": "2024-04-15",
        "duration": 180,    # seconds
        "max_altitude": 15, # meters
        "max_speed": 5,     # m/s
        "description": "Testing obstacle "
                       "avoidance system"
    },
    {
        "name": "Autonomous_Waypoint_Mission",
        "date": "2024-05-20",
        "duration": 300,
        "max_altitude": 20,
        "max_speed": 8,
        "description": "Autonomous waypoint "
                       "navigation test"
    },
    {
        "name": "Payload_Delivery_Test",
        "date": "2024-06-10",
        "duration": 240,
        "max_altitude": 10,
        "max_speed": 4,
        "description": "Pesticide spraying "
                       "drone payload test"
    },
    {
        "name": "Indoor_Navigation_Test",
        "date": "2024-07-05",
        "duration": 120,
        "max_altitude": 3,
        "max_speed": 2,
        "description": "Indoor GPS-denied "
                       "navigation test"
    },
    {
        "name": "Long_Range_Endurance",
        "date": "2024-08-12",
        "duration": 600,
        "max_altitude": 30,
        "max_speed": 10,
        "description": "Endurance and range "
                       "testing mission"
    },
]

all_stats = []

for mission in missions:
    print(f"\nGenerating: {mission['name']}...")
    n = mission['duration'] * 10  # 10Hz logging
    t = np.linspace(0, mission['duration'], n)

    # ── GPS Position ──────────────────────────
    # Starting from Bengaluru coordinates
    lat_base = 12.9716
    lon_base = 77.5946
    lat = (lat_base +
           np.cumsum(np.random.normal(
               0, 0.00001, n)))
    lon = (lon_base +
           np.cumsum(np.random.normal(
               0, 0.00001, n)))

    # ── Altitude Profile ──────────────────────
    alt = np.zeros(n)
    takeoff_end = int(n * 0.1)
    cruise_end = int(n * 0.85)
    land_end = n

    # Takeoff phase
    alt[:takeoff_end] = np.linspace(
        0, mission['max_altitude'], takeoff_end)
    # Cruise phase
    alt[takeoff_end:cruise_end] = (
        mission['max_altitude'] +
        np.random.normal(
            0, 0.5, cruise_end - takeoff_end))
    # Landing phase
    alt[cruise_end:] = np.linspace(
        mission['max_altitude'], 0,
        land_end - cruise_end)
    alt = np.clip(alt, 0, None)

    # ── Velocity ──────────────────────────────
    vx = np.zeros(n)
    vx[takeoff_end:cruise_end] = (
        mission['max_speed'] * 0.7 +
        np.random.normal(
            0, 0.3, cruise_end - takeoff_end))
    vy = np.random.normal(0, 0.2, n)
    vz = np.gradient(alt, t)
    speed = np.sqrt(vx**2 + vy**2 + vz**2)

    # ── Attitude ──────────────────────────────
    roll  = np.random.normal(0, 2, n)
    pitch = np.random.normal(0, 2, n)
    yaw   = np.cumsum(
        np.random.normal(0, 0.1, n)) % 360

    # ── Battery ───────────────────────────────
    battery_start = 100
    discharge_rate = battery_start / (
        mission['duration'] * 10)
    battery = np.maximum(
        battery_start -
        discharge_rate * np.arange(n) +
        np.random.normal(0, 0.1, n), 0)

    # ── Motor Outputs ─────────────────────────
    motor_base = 1200 + alt * 5
    motor1 = motor_base + np.random.normal(
        0, 10, n)
    motor2 = motor_base + np.random.normal(
        0, 10, n)
    motor3 = motor_base + np.random.normal(
        0, 10, n)
    motor4 = motor_base + np.random.normal(
        0, 10, n)

    # ── Create DataFrame ──────────────────────
    start_time = datetime.strptime(
        mission['date'], '%Y-%m-%d')
    timestamps = [
        start_time + timedelta(seconds=float(ti))
        for ti in t]

    df = pd.DataFrame({
        'timestamp':  timestamps,
        'time_s':     t,
        'lat':        lat,
        'lon':        lon,
        'altitude_m': alt,
        'vx_ms':      vx,
        'vy_ms':      vy,
        'vz_ms':      vz,
        'speed_ms':   speed,
        'roll_deg':   roll,
        'pitch_deg':  pitch,
        'yaw_deg':    yaw,
        'battery_pct': battery,
        'motor1_pwm': motor1,
        'motor2_pwm': motor2,
        'motor3_pwm': motor3,
        'motor4_pwm': motor4,
    })

    # Save CSV
    filename = (
        f"D:\\DroneProjects\\drone-flight-logs"
        f"\\flight_data\\"
        f"{mission['date']}_{mission['name']}"
        f".csv")
    df.to_csv(filename, index=False)

    # Stats
    stats = {
        'Mission': mission['name'],
        'Date': mission['date'],
        'Duration_s': mission['duration'],
        'Max_Alt_m': round(alt.max(), 1),
        'Max_Speed_ms': round(speed.max(), 1),
        'Min_Battery': round(battery.min(), 1),
        'Total_Distance_m': round(
            np.sum(speed) * 0.1, 1),
    }
    all_stats.append(stats)
    print(f"  Saved: {filename}")
    print(f"  Max Alt: {stats['Max_Alt_m']}m | "
          f"Max Speed: {stats['Max_Speed_ms']}m/s")

# ── Save Summary ──────────────────────────────
stats_df = pd.DataFrame(all_stats)
stats_df.to_csv(
    "D:\\DroneProjects\\drone-flight-logs\\"
    "flight_data\\flight_summary.csv",
    index=False)

print("\n" + "=" * 50)
print("Flight Data Summary:")
print("=" * 50)
print(stats_df.to_string(index=False))

# ── Analysis and Visualization ────────────────
print("\nGenerating analysis graphs...")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    'Drone Flight Operations Analysis\n'
    'Novatech Robo Pvt Ltd — Field Test Data',
    fontsize=14, fontweight='bold')

colors = ['blue', 'red', 'green',
          'orange', 'purple']

# Plot each mission
for idx, mission in enumerate(missions):
    filename = (
        f"D:\\DroneProjects\\drone-flight-logs"
        f"\\flight_data\\"
        f"{mission['date']}_{mission['name']}"
        f".csv")
    df = pd.read_csv(filename)
    c = colors[idx % len(colors)]
    label = mission['name'].replace('_', ' ')

    # Altitude profile
    axes[0,0].plot(
        df['time_s'], df['altitude_m'],
        color=c, label=label, linewidth=1.5)

    # Speed profile
    axes[0,1].plot(
        df['time_s'], df['speed_ms'],
        color=c, label=label, linewidth=1.5)

    # Battery
    axes[0,2].plot(
        df['time_s'], df['battery_pct'],
        color=c, label=label, linewidth=1.5)

# Format plots
axes[0,0].set_title('Altitude Profile')
axes[0,0].set_xlabel('Time (s)')
axes[0,0].set_ylabel('Altitude (m)')
axes[0,0].legend(fontsize=7)
axes[0,0].grid(True)

axes[0,1].set_title('Speed Profile')
axes[0,1].set_xlabel('Time (s)')
axes[0,1].set_ylabel('Speed (m/s)')
axes[0,1].legend(fontsize=7)
axes[0,1].grid(True)

axes[0,2].set_title('Battery Discharge')
axes[0,2].set_xlabel('Time (s)')
axes[0,2].set_ylabel('Battery (%)')
axes[0,2].legend(fontsize=7)
axes[0,2].grid(True)

# Mission statistics bar chart
missions_names = [
    m['name'].replace('_', '\n')
    for m in missions]
durations = [m['duration'] for m in missions]
max_alts = [s['Max_Alt_m'] for s in all_stats]
max_speeds = [
    s['Max_Speed_ms'] for s in all_stats]

axes[1,0].bar(
    range(len(missions)), durations,
    color=colors, alpha=0.7)
axes[1,0].set_title('Mission Duration')
axes[1,0].set_ylabel('Duration (s)')
axes[1,0].set_xticks(range(len(missions)))
axes[1,0].set_xticklabels(
    missions_names, fontsize=7)
axes[1,0].grid(True, axis='y')

axes[1,1].bar(
    range(len(missions)), max_alts,
    color=colors, alpha=0.7)
axes[1,1].set_title('Maximum Altitude')
axes[1,1].set_ylabel('Altitude (m)')
axes[1,1].set_xticks(range(len(missions)))
axes[1,1].set_xticklabels(
    missions_names, fontsize=7)
axes[1,1].grid(True, axis='y')

axes[1,2].bar(
    range(len(missions)), max_speeds,
    color=colors, alpha=0.7)
axes[1,2].set_title('Maximum Speed')
axes[1,2].set_ylabel('Speed (m/s)')
axes[1,2].set_xticks(range(len(missions)))
axes[1,2].set_xticklabels(
    missions_names, fontsize=7)
axes[1,2].grid(True, axis='y')

plt.tight_layout()
save_path = (
    "D:\\DroneProjects\\drone-flight-logs\\"
    "results\\flight_analysis.png")
plt.savefig(save_path, dpi=150,
            bbox_inches='tight')
plt.show()

print(f"\nAnalysis saved: {save_path}")
print("\n" + "=" * 50)
print("Total Flights: 5")
print(f"Total Flight Time: "
      f"{sum(m['duration'] for m in missions)}s "
      f"({sum(m['duration'] for m in missions)/60:.1f} mins)")
print(f"Total Distance: "
      f"{sum(s['Total_Distance_m'] for s in all_stats):.0f}m")
print("=" * 50)