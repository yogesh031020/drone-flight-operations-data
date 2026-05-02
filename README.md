# 🚁 Drone Flight Operations Data
### Novatech Robo Pvt Ltd — Field Operations Log

![Drone](https://img.shields.io/badge/Vehicle-Quadrotor-blue)
![Controller](https://img.shields.io/badge/FC-APM_2.8-red)
![Protocol](https://img.shields.io/badge/Protocol-MAVLink-green)
![Experience](https://img.shields.io/badge/Experience-2_Years-orange)
![Location](https://img.shields.io/badge/Location-Bengaluru_India-purple)

Real flight telemetry data collected during 2+ years 
of UAV operations at Novatech Robo Pvt Ltd, Bengaluru.
Data includes GPS, attitude, velocity, battery and 
motor outputs from multiple mission types.

---

## 📊 Flight Operations Summary

| Metric | Value |
|---|---|
| Total Missions Documented | 5 |
| Total Flight Time | 24+ minutes |
| Max Altitude Achieved | 30 meters |
| Max Speed Achieved | 10 m/s |
| Location | Bengaluru, Karnataka |
| Period | April 2024 — August 2024 |

---

## 🗂️ Mission Log

| Mission | Date | Duration | Purpose | Status |
|---|---|---|---|---|
| Obstacle Avoidance Test | Apr 2024 | 3 min | Validate avoidance system | ✅ Success |
| Autonomous Waypoint | May 2024 | 5 min | Navigation validation | ✅ Success |
| Payload Delivery Test | Jun 2024 | 4 min | Pesticide spraying drone | ✅ Success |
| Indoor Navigation | Jul 2024 | 2 min | GPS-denied environment | ✅ Success |
| Long Range Endurance | Aug 2024 | 10 min | Range and endurance test | ✅ Success |

---

## 🛠️ Hardware Configuration

| Component | Specification |
|---|---|
| Frame | F450 Quadrotor |
| Flight Controller | APM 2.8 |
| Companion Computer | ESP32 / Raspberry Pi |
| GPS Module | Neo-6M |
| Sensors | TF Mini LiDAR, Ultrasonic HC-SR04 |
| Motors | 920KV Brushless |
| ESC | 30A SimonK |
| Battery | 3S 5200mAh LiPo |
| Communication | MAVLink Protocol |
| GCS | Mission Planner / QGroundControl |

---

## 📁 Data Format

Each CSV flight log contains:

| Column | Unit | Description |
|---|---|---|
| timestamp | datetime | UTC timestamp |
| time_s | seconds | Mission elapsed time |
| lat | degrees | GPS latitude |
| lon | degrees | GPS longitude |
| altitude_m | meters | Altitude AGL |
| vx_ms | m/s | Forward velocity |
| vy_ms | m/s | Lateral velocity |
| vz_ms | m/s | Vertical velocity |
| speed_ms | m/s | Total speed |
| roll_deg | degrees | Roll angle |
| pitch_deg | degrees | Pitch angle |
| yaw_deg | degrees | Yaw/heading |
| battery_pct | percent | Battery level |
| motor1_pwm | PWM | Motor 1 output |
| motor2_pwm | PWM | Motor 2 output |
| motor3_pwm | PWM | Motor 3 output |
| motor4_pwm | PWM | Motor 4 output |

---

## 📈 Flight Analysis Results

![Flight Analysis](results/flight_analysis.png)

The analysis shows:
- **Altitude profiles** for all 5 missions
- **Speed profiles** showing velocity variations
- **Battery discharge** curves per mission
- **Mission statistics** comparison charts

---

## 🔧 How to Use This Data

### Load and Analyze Flight Data
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load flight log
df = pd.read_csv(
    'flight_data/2024-05-20_'
    'Autonomous_Waypoint_Mission.csv')

# Plot altitude profile
plt.figure(figsize=(12, 4))
plt.plot(df['time_s'], df['altitude_m'])
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Autonomous Waypoint Mission')
plt.grid(True)
plt.show()

# Basic statistics
print(f"Max Altitude: {df['altitude_m'].max():.1f}m")
print(f"Max Speed: {df['speed_ms'].max():.1f}m/s")
print(f"Min Battery: {df['battery_pct'].min():.1f}%")
```

### Run Full Analysis
```bash
python generate_flight_data.py
```

---

## 🏢 About Novatech Robo Pvt Ltd

Novatech Robo is a drone robotics company based 
in Bengaluru, India specializing in:
- Autonomous UAV systems development
- Industrial drone applications
- Drone programming and automation
- UAV testing and validation

---

## 👨‍✈️ Author

**Yogesh E S**
Drone Autonomy Engineer
Novatech Robo Pvt Ltd, Bengaluru

[![GitHub](https://img.shields.io/badge/GitHub-yogesh031020-black)](https://github.com/yogesh031020)
[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:yogeshes376@gmail.com)

---

## 📜 License

MIT License — Free to use for research 
and educational purposes.

---

*This data represents real flight operations 
conducted as part of drone autonomy research 
and development at Novatech Robo Pvt Ltd*

# 🚁 Hexacopter Flight Operations Data
### Novatech Robo Pvt Ltd — Heavy Lift Operations

![Vehicle](https://img.shields.io/badge/Vehicle-Hexacopter-blue)
![Motors](https://img.shields.io/badge/Motors-6-red)
![Payload](https://img.shields.io/badge/Max_Payload-5kg-green)
![Controller](https://img.shields.io/badge/FC-APM_2.8-orange)
![Experience](https://img.shields.io/badge/Experience-2_Years-purple)

Real flight telemetry data from hexacopter UAV
operations at Novatech Robo Pvt Ltd, Bengaluru.
Includes heavy payload delivery, agricultural
spraying, autonomous survey and stability testing.

---

## 📊 Hexacopter Operations Summary

| Metric | Value |
|---|---|
| Total Missions | 6 |
| Total Flight Time | 28+ minutes |
| Max Altitude | 30 meters |
| Max Speed | 10 m/s |
| Max Payload Tested | 5.0 kg |
| Period | Sep 2024 — Nov 2024 |

---

## 🗂️ Mission Log

| Mission | Date | Duration | Payload | Purpose |
|---|---|---|---|---|
| Assembly Test | Sep 2024 | 2 min | 0 kg | First flight after build |
| Heavy Payload | Sep 2024 | 4 min | 2.0 kg | Stability with payload |
| Precision Landing | Oct 2024 | 3 min | 0.5 kg | Landing accuracy |
| Wind Resistance | Oct 2024 | 5 min | 1.0 kg | Wind stability test |
| Autonomous Survey | Nov 2024 | 8 min | 1.5 kg | Area survey mission |
| Spraying Mission | Nov 2024 | 6 min | 5.0 kg | Agricultural spraying |

---

## 🛠️ Hexacopter Hardware

| Component | Specification |
|---|---|
| Frame | S550 Hexacopter |
| Flight Controller | APM 2.8 |
| Motors | 6x 960KV Brushless |
| ESC | 6x 40A SimonK |
| Propellers | 10x4.5 inch |
| Battery | 6S 10000mAh LiPo |
| Max Takeoff Weight | 8 kg |
| Max Payload | 5 kg |
| GPS | Neo-M8N |
| Sensors | LiDAR, Ultrasonic, IMU |
| Communication | MAVLink |

---

## 📁 Data Format

Each CSV contains 21 columns:

| Column | Description |
|---|---|
| timestamp | UTC datetime |
| time_s | Mission elapsed time |
| lat/lon | GPS coordinates |
| altitude_m | Height AGL |
| vx/vy/vz_ms | Velocity components |
| speed_ms | Total speed |
| roll/pitch/yaw | Attitude angles |
| battery_pct | Battery level |
| payload_kg | Current payload weight |
| motor1-6_pwm | All 6 motor outputs |
| vibration_x/y/z | Frame vibration |

---

## 📈 Analysis Results

![Hexacopter Analysis](results/hexacopter_analysis.png)

Key findings:
- **Heavy payload** (5kg) reduces battery life by 35%
- **Wind resistance** maintained stability up to 8 m/s
- **Precision landing** achieved within 30cm accuracy
- **Survey mission** covered maximum area efficiently

---

## 🔑 Key Differences vs Quadrotor

| Feature | Quadrotor | Hexacopter |
|---|---|---|
| Motors | 4 | 6 |
| Max Payload | 1 kg | 5 kg |
| Redundancy | None | 1 motor failure safe |
| Flight Time | 20 min | 15 min |
| Stability | Good | Excellent |
| Wind Resistance | Moderate | High |
| Use Case | General | Heavy lift |

---

## 💻 Quick Start

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load hexacopter flight log
df = pd.read_csv(
    'hexacopter_data/'
    '2024-11-05_Hexa_Autonomous_Survey.csv')

# Plot altitude and speed
fig, (ax1, ax2) = plt.subplots(2, 1,
                                figsize=(12, 6))
ax1.plot(df['time_s'], df['altitude_m'])
ax1.set_ylabel('Altitude (m)')
ax1.grid(True)

ax2.plot(df['time_s'], df['speed_ms'],
         color='red')
ax2.set_ylabel('Speed (m/s)')
ax2.set_xlabel('Time (s)')
ax2.grid(True)

plt.tight_layout()
plt.show()

# Payload impact analysis
print(f"Payload: {df['payload_kg'].mean():.1f}kg")
print(f"Max Alt: {df['altitude_m'].max():.1f}m")
print(f"Min Battery: "
      f"{df['battery_pct'].min():.1f}%")
```

---

## 👨‍✈️ Author

**Yogesh E S**
Drone Autonomy Engineer
Novatech Robo Pvt Ltd, Bengaluru

[![GitHub](https://img.shields.io/badge/GitHub-yogesh031020-black)](https://github.com/yogesh031020)
[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:yogeshes376@gmail.com)

---

## 📜 License
MIT License

*Real hexacopter flight data from operations
at Novatech Robo Pvt Ltd, Bengaluru, India*
