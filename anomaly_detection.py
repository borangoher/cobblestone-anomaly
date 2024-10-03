import numpy as np

def get_drift(data):
    # attempts to compute drift from a given data series. uses simple 
    # linear regression. assumes drift is linear as a result.

    size = len(data)

    # solve for slope
    indices = np.linspace(1, size, size)
    A = np.vstack([indices, np.ones(len(indices))]).T
    slope = np.linalg.lstsq(A, data)[0][0]

    # return drift starting at 0 (without intercept)
    return np.linspace(0, slope*size, size)

def get_seasonality(data, window_size):
    # attempts to get seasonality using a moving average. convolution with a
    # constant vector of magnitude 1 is used to compute moving average. takes
    # window_size as input.

    seasonality = np.convolve(data, np.ones(window_size)/window_size, mode='same')

    # smooth over boundary effects
    seasonality[0:50] = np.average(seasonality)
    seasonality[950:1000] = np.average(seasonality)
    
    return seasonality

def detect_anomalies(data, threshold):
    # detects anomalies for a given data series and threshold. uses z-score
    # as measure of anomality. threshold is therefore the distance from mean
    # in standard deviations.

    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = (data - mean) / std_dev
    anomalies = np.abs(z_scores) > threshold 

    return anomalies

