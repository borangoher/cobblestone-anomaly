import numpy as np
import matplotlib.pyplot as plt
from anomaly_detection import get_drift, get_seasonality, detect_anomalies
from data_generation import generate_normal_data, generate_seasonality, generate_drift 

MEAN = 100
STD_DEV = 10
SIZE = 1000
SEASONALITY_MAG = 2 * STD_DEV
DRIFT_MAG = 3 * STD_DEV
WINDOW_SIZE = 50
THRESHOLD = 2


# generate data series
base_data = generate_normal_data(MEAN, STD_DEV, SIZE)
seasonality = generate_seasonality(SEASONALITY_MAG, 0, SIZE)
drift = generate_drift(DRIFT_MAG, SIZE)
final_data = base_data + seasonality + drift 

# compute drift from data 
computed_drift = get_drift(final_data)
drift_corrected = final_data - computed_drift

# compute seasonality from data
computed_seasonality = get_seasonality(drift_corrected-MEAN, WINDOW_SIZE)
seasonality_corrected = drift_corrected - computed_seasonality

# detect anomalies in corrected data
data_indices = np.arange(SIZE)
anomaly_indices = detect_anomalies(seasonality_corrected, THRESHOLD)

# plot results
plt.rcParams['figure.constrained_layout.use'] = True

plt.subplot(2, 4, 1)
plt.plot(base_data)
plt.title('Base Data')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 2)
plt.plot(seasonality)
plt.title('Seasonality')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 3)
plt.plot(drift)
plt.title('Drift')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 4)
plt.plot(final_data)
plt.title('Adjusted Data')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 5)
plt.plot(computed_drift)
plt.title('Comp. Drift')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 6)
plt.plot(computed_seasonality)
plt.title('Comp. Seasonality')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 7)
plt.plot(seasonality_corrected)
plt.title('Corrected Data')
plt.xlabel('Index')
plt.ylabel('Value')

plt.subplot(2, 4, 8)
plt.plot(data_indices, seasonality_corrected)
plt.scatter(data_indices[anomaly_indices], seasonality_corrected[anomaly_indices], color='red')
plt.title('Anomalies')
plt.xlabel('Index')
plt.ylabel('Value')

plt.savefig('./output_plot.png')
