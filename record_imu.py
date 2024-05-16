from mpu6050 import mpu6050
import time
import pandas as pd

data = []
sensor = mpu6050(0x68)
start = time.time()
for i in range(5000):
    t = time.time()
    acc_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    tmp = {
            't':t-start,
            'x':acc_data['x'],
            'y':acc_data['y'],
            'z':acc_data['z'],
            'xr':gyro_data['x'],
            'yr':gyro_data['y'],
            'zr':gyro_data['z']
            }
    data.append(tmp)
    time.sleep(0.05)
df = pd.DataFrame(data)
df.to_csv("imu_data.csv", index=False)
