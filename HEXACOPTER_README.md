\# 🚁 Hexacopter Flight Operations Data

\### Novatech Robo Pvt Ltd — Heavy Lift Operations



!\[Vehicle](https://img.shields.io/badge/Vehicle-Hexacopter-blue)

!\[Motors](https://img.shields.io/badge/Motors-6-red)

!\[Payload](https://img.shields.io/badge/Max\_Payload-5kg-green)

!\[Controller](https://img.shields.io/badge/FC-APM\_2.8-orange)

!\[Experience](https://img.shields.io/badge/Experience-2\_Years-purple)



Real flight telemetry data from hexacopter UAV

operations at Novatech Robo Pvt Ltd, Bengaluru.

Includes heavy payload delivery, agricultural

spraying, autonomous survey and stability testing.



\---



\## 📊 Hexacopter Operations Summary



| Metric | Value |

|---|---|

| Total Missions | 6 |

| Total Flight Time | 28+ minutes |

| Max Altitude | 30 meters |

| Max Speed | 10 m/s |

| Max Payload Tested | 5.0 kg |

| Period | Sep 2024 — Nov 2024 |



\---



\## 🗂️ Mission Log



| Mission | Date | Duration | Payload | Purpose |

|---|---|---|---|---|

| Assembly Test | Sep 2024 | 2 min | 0 kg | First flight after build |

| Heavy Payload | Sep 2024 | 4 min | 2.0 kg | Stability with payload |

| Precision Landing | Oct 2024 | 3 min | 0.5 kg | Landing accuracy |

| Wind Resistance | Oct 2024 | 5 min | 1.0 kg | Wind stability test |

| Autonomous Survey | Nov 2024 | 8 min | 1.5 kg | Area survey mission |

| Spraying Mission | Nov 2024 | 6 min | 5.0 kg | Agricultural spraying |



\---



\## 🛠️ Hexacopter Hardware



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



\---



\## 📁 Data Format



Each CSV contains 21 columns:



| Column | Description |

|---|---|

| timestamp | UTC datetime |

| time\_s | Mission elapsed time |

| lat/lon | GPS coordinates |

| altitude\_m | Height AGL |

| vx/vy/vz\_ms | Velocity components |

| speed\_ms | Total speed |

| roll/pitch/yaw | Attitude angles |

| battery\_pct | Battery level |

| payload\_kg | Current payload weight |

| motor1-6\_pwm | All 6 motor outputs |

| vibration\_x/y/z | Frame vibration |



\---



\## 📈 Analysis Results



!\[Hexacopter Analysis](results/hexacopter\_analysis.png)



Key findings:

\- \*\*Heavy payload\*\* (5kg) reduces battery life by 35%

\- \*\*Wind resistance\*\* maintained stability up to 8 m/s

\- \*\*Precision landing\*\* achieved within 30cm accuracy

\- \*\*Survey mission\*\* covered maximum area efficiently



\---



\## 🔑 Key Differences vs Quadrotor



| Feature | Quadrotor | Hexacopter |

|---|---|---|

| Motors | 4 | 6 |

| Max Payload | 1 kg | 5 kg |

| Redundancy | None | 1 motor failure safe |

| Flight Time | 20 min | 15 min |

| Stability | Good | Excellent |

| Wind Resistance | Moderate | High |

| Use Case | General | Heavy lift |



\---



\## 💻 Quick Start



```python

import pandas as pd

import matplotlib.pyplot as plt



\# Load hexacopter flight log

df = pd.read\_csv(

&#x20;   'hexacopter\_data/'

&#x20;   '2024-11-05\_Hexa\_Autonomous\_Survey.csv')



\# Plot altitude and speed

fig, (ax1, ax2) = plt.subplots(2, 1,

&#x20;                               figsize=(12, 6))

ax1.plot(df\['time\_s'], df\['altitude\_m'])

ax1.set\_ylabel('Altitude (m)')

ax1.grid(True)



ax2.plot(df\['time\_s'], df\['speed\_ms'],

&#x20;        color='red')

ax2.set\_ylabel('Speed (m/s)')

ax2.set\_xlabel('Time (s)')

ax2.grid(True)



plt.tight\_layout()

plt.show()



\# Payload impact analysis

print(f"Payload: {df\['payload\_kg'].mean():.1f}kg")

print(f"Max Alt: {df\['altitude\_m'].max():.1f}m")

print(f"Min Battery: "

&#x20;     f"{df\['battery\_pct'].min():.1f}%")

```



\---



\## 👨‍✈️ Author



\*\*Yogesh E S\*\*

Drone Autonomy Engineer

Novatech Robo Pvt Ltd, Bengaluru



\[!\[GitHub](https://img.shields.io/badge/GitHub-yogesh031020-black)](https://github.com/yogesh031020)

\[!\[Email](https://img.shields.io/badge/Email-Contact-red)](mailto:yogeshes376@gmail.com)



\---



\## 📜 License

MIT License



\*Real hexacopter flight data from operations

at Novatech Robo Pvt Ltd, Bengaluru, India\*

