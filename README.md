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
