import numpy as np

def generate_normal_data(mean, std_dev, size):
    # generates normally distributed data of given mean, standard deviation
    # and array size. 
    return np.random.normal(loc=mean, scale=std_dev, size=size)

def generate_seasonality(mag, phase, size):
    # generates seasonality to add on to base data. The seasonality is
    # a sinusoidal with specified magnitude and phase.
    
    x = np.linspace(0, 4 * np.pi, size)
    return mag * np.sin(x + phase)

def generate_drift(mag, size):
    # generates drift to add on to base data. The drift is a linear
    # shift in mean of given magnitude.
    return np.linspace(0, mag, size)

