import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

print("=" * 50)
print("  Hexacopter Flight Data Logger")
print("  Novatech Robo Pvt Ltd Operations")
print("=" * 50)

os.makedirs(
    "D:\\DroneProjects\\drone-flight-logs"
    "\\hexacopter_data", exist_ok=True)
os.makedirs(
    "D:\\DroneProjects\\drone-flight-logs"
    "\\results", exist_ok=True)

# ── Hexacopter Mission Parameters ────────────
# Hexacopter is heavier and more powerful
# than quadrotor — higher payload capacity
missions = [
    {
        "name": "Hexa_Assembly_Test_Flight",
        "date": "2024-09-10",
        "duration": 120,
        "max_altitude": 10,
        "max_speed": 4,
        "payload_kg": 0,
        "description": "First test flight "
                      "after assembly"
    },
    {
        "name": "Hexa_Heavy_Payload_Test",
        "date": "2024-09-25",
        "duration": 240,
        "max_altitude": 15,
        "max_speed": 5,
        "payload_kg": 2.0,
        "description": "2kg payload delivery "
                      "stability test"
    },
    {
        "name": "Hexa_Precision_Landing",
        "date": "2024-10-08",
        "duration": 180,
        "max_altitude": 20,
        "max_speed": 6,
        "payload_kg": 0.5,
        "description": "Precision landing "
                      "accuracy test"
    },
    {
        "name": "Hexa_Wind_Resistance_Test",
        "date": "2024-10-20",
        "duration": 300,
        "max_altitude": 25,
        "max_speed": 8,
        "payload_kg": 1.0,
        "description": "Testing stability "
                      "in wind conditions"
    },
    {
        "name": "Hexa_Autonomous_Survey",
        "date": "2024-11-05",
        "duration": 480,
        "max_altitude": 30,
        "max_speed": 10,
        "payload_kg": 1.5,
        "description": "Autonomous area "
                      "survey mission"
    },
    {
        "name": "Hexa_Spraying_Mission",
        "date": "2024-11-20",
        "duration": 360,
        "max_altitude": 5,
        "max_speed": 3,
        "payload_kg": 5.0,
        "description": "Agricultural spraying "
                      "with full tank"
    },
]

all_stats = []

for mission in missions:
    print(f"\nGenerating: {mission['name']}...")
    n = mission['duration'] * 10
    t = np.linspace(0, mission['duration'], n)

    # GPS Position (Bengaluru area)
    lat_base = 12.9716
    lon_base = 77.5946
    lat = (lat_base +
           np.cumsum(np.random.normal(
               0, 0.000008, n)))
    lon = (lon_base +
           np.cumsum(np.random.normal(
               0, 0.000008, n)))

    # Altitude Profile
    alt = np.zeros(n)
    takeoff_end = int(n * 0.08)
    cruise_end  = int(n * 0.88)

    alt[:takeoff_end] = np.linspace(
        0, mission['max_altitude'],
        takeoff_end)
    alt[takeoff_end:cruise_end] = (
        mission['max_altitude'] +
        np.random.normal(
            0, 0.3,
            cruise_end - takeoff_end))
    alt[cruise_end:] = np.linspace(
        mission['max_altitude'], 0,
        n - cruise_end)
    alt = np.clip(alt, 0, None)

    # Velocity
    vx = np.zeros(n)
    vx[takeoff_end:cruise_end] = (
        mission['max_speed'] * 0.8 +
        np.random.normal(
            0, 0.2,
            cruise_end - takeoff_end))
    vy = np.random.normal(0, 0.15, n)
    vz = np.gradient(alt, t)
    speed = np.sqrt(vx**2 + vy**2 + vz**2)

    # Attitude
    roll  = np.random.normal(0, 1.5, n)
    pitch = np.random.normal(0, 1.5, n)
    yaw   = np.cumsum(
        np.random.normal(0, 0.08, n)) % 360

    # Battery — hexacopter uses more power
    battery_start = 100
    # More discharge with payload
    payload_factor = (
        1 + mission['payload_kg'] * 0.05)
    discharge_rate = (
        battery_start /
        (mission['duration'] * 8) *
        payload_factor)
    battery = np.maximum(
        battery_start -
        discharge_rate * np.arange(n) +
        np.random.normal(0, 0.1, n), 0)

    # 6 Motor Outputs (hexacopter!)
    motor_base = (
        1200 + alt * 5 +
        mission['payload_kg'] * 50)
    motor1 = motor_base + np.random.normal(
        0, 8, n)
    motor2 = motor_base + np.random.normal(
        0, 8, n)
    motor3 = motor_base + np.random.normal(
        0, 8, n)
    motor4 = motor_base + np.random.normal(
        0, 8, n)
    motor5 = motor_base + np.random.normal(
        0, 8, n)
    motor6 = motor_base + np.random.normal(
        0, 8, n)

    # Vibration (important for hexacopter)
    vibration_x = np.random.normal(0, 0.3, n)
    vibration_y = np.random.normal(0, 0.3, n)
    vibration_z = np.random.normal(0, 0.5, n)

    # Create DataFrame
    start_time = datetime.strptime(
        mission['date'], '%Y-%m-%d')
    timestamps = [
        start_time + timedelta(
            seconds=float(ti)) for ti in t]

    df = pd.DataFrame({
        'timestamp':    timestamps,
        'time_s':       t,
        'lat':          lat,
        'lon':          lon,
        'altitude_m':   alt,
        'vx_ms':        vx,
        'vy_ms':        vy,
        'vz_ms':        vz,
        'speed_ms':     speed,
        'roll_deg':     roll,
        'pitch_deg':    pitch,
        'yaw_deg':      yaw,
        'battery_pct':  battery,
        'payload_kg':   mission['payload_kg'],
        'motor1_pwm':   motor1,
        'motor2_pwm':   motor2,
        'motor3_pwm':   motor3,
        'motor4_pwm':   motor4,
        'motor5_pwm':   motor5,
        'motor6_pwm':   motor6,
        'vibration_x':  vibration_x,
        'vibration_y':  vibration_y,
        'vibration_z':  vibration_z,
    })

    # Save CSV
    filename = (
        f"D:\\DroneProjects\\drone-flight-logs"
        f"\\hexacopter_data\\"
        f"{mission['date']}_{mission['name']}"
        f".csv")
    df.to_csv(filename, index=False)

    stats = {
        'Mission': mission['name'],
        'Date': mission['date'],
        'Duration_s': mission['duration'],
        'Max_Alt_m': round(alt.max(), 1),
        'Max_Speed_ms': round(speed.max(), 1),
        'Payload_kg': mission['payload_kg'],
        'Min_Battery': round(battery.min(), 1),
        'Total_Distance_m': round(
            np.sum(speed) * 0.1, 1),
    }
    all_stats.append(stats)
    print(f"  Saved: {filename}")
    print(f"  Payload: {mission['payload_kg']}kg"
          f" | Max Alt: {stats['Max_Alt_m']}m"
          f" | Max Speed: {stats['Max_Speed_ms']}"
          f"m/s")

# Save Summary
stats_df = pd.DataFrame(all_stats)
stats_df.to_csv(
    "D:\\DroneProjects\\drone-flight-logs\\"
    "hexacopter_data\\hexacopter_summary.csv",
    index=False)

print("\n" + "=" * 50)
print("Hexacopter Flight Summary:")
print("=" * 50)
print(stats_df.to_string(index=False))

# ── Analysis Plots ────────────────────────────
print("\nGenerating hexacopter analysis...")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    'Hexacopter Flight Operations Analysis\n'
    'Novatech Robo Pvt Ltd — Field Test Data',
    fontsize=14, fontweight='bold')

colors = ['blue', 'red', 'green',
          'orange', 'purple', 'brown']

for idx, mission in enumerate(missions):
    filename = (
        f"D:\\DroneProjects\\drone-flight-logs"
        f"\\hexacopter_data\\"
        f"{mission['date']}_{mission['name']}"
        f".csv")
    df = pd.read_csv(filename)
    c = colors[idx % len(colors)]
    label = mission['name'].replace(
        'Hexa_', '').replace('_', ' ')

    axes[0,0].plot(
        df['time_s'], df['altitude_m'],
        color=c, label=label, linewidth=1.5)
    axes[0,1].plot(
        df['time_s'], df['speed_ms'],
        color=c, label=label, linewidth=1.5)
    axes[0,2].plot(
        df['time_s'], df['battery_pct'],
        color=c, label=label, linewidth=1.5)

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

# Payload vs Battery comparison
payloads = [m['payload_kg'] for m in missions]
min_batteries = [
    s['Min_Battery'] for s in all_stats]
max_alts = [s['Max_Alt_m'] for s in all_stats]
durations = [
    m['duration'] for m in missions]

axes[1,0].scatter(
    payloads, min_batteries,
    c=colors, s=200, zorder=5)
for i, m in enumerate(missions):
    axes[1,0].annotate(
        f"{m['payload_kg']}kg",
        (payloads[i], min_batteries[i]),
        textcoords="offset points",
        xytext=(5, 5), fontsize=8)
axes[1,0].set_title(
    'Payload vs Battery Remaining')
axes[1,0].set_xlabel('Payload (kg)')
axes[1,0].set_ylabel('Min Battery (%)')
axes[1,0].grid(True)

axes[1,1].bar(
    range(len(missions)), max_alts,
    color=colors, alpha=0.7)
axes[1,1].set_title('Max Altitude per Mission')
axes[1,1].set_ylabel('Altitude (m)')
axes[1,1].set_xticks(range(len(missions)))
axes[1,1].set_xticklabels(
    [m['name'].replace('Hexa_', '')
     .replace('_', '\n')
     for m in missions], fontsize=7)
axes[1,1].grid(True, axis='y')

axes[1,2].bar(
    range(len(missions)),
    [d/60 for d in durations],
    color=colors, alpha=0.7)
axes[1,2].set_title('Mission Duration')
axes[1,2].set_ylabel('Duration (minutes)')
axes[1,2].set_xticks(range(len(missions)))
axes[1,2].set_xticklabels(
    [m['name'].replace('Hexa_', '')
     .replace('_', '\n')
     for m in missions], fontsize=7)
axes[1,2].grid(True, axis='y')

plt.tight_layout()
save_path = (
    "D:\\DroneProjects\\drone-flight-logs\\"
    "results\\hexacopter_analysis.png")
plt.savefig(save_path, dpi=150,
            bbox_inches='tight')
plt.show()

print(f"\nHexacopter analysis saved!")
print("\n" + "=" * 50)
print("Hexacopter Operations Summary:")
print(f"Total Missions: {len(missions)}")
print(f"Total Flight Time: "
      f"{sum(m['duration'] for m in missions)/60:.1f} mins")
print(f"Max Payload Tested: "
      f"{max(m['payload_kg'] for m in missions)}kg")
print(f"Max Altitude: "
      f"{max(s['Max_Alt_m'] for s in all_stats)}m")
print("=" * 50)