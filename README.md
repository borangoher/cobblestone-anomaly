# Anomaly Detection Demo

This small project generates a data series with simulated seasonality and drift
effects and performs anomaly detection on the result. A short explanation of
each part is contained in this document, please consult relevant files for more
details.

## Data Generation

The dataset is generated in three steps. First, we generate an array of normally
distributed values with given distribution properties. Then, a sinusoidal of
given magnitude is generated to simulate seasonality. Finally, a line from 0 to
a given magnitude is generated to simulate mean drift. When all are added
together, we get a data series with seasonal and drift effects. This part of
the project resides in `data_generation.py`.

## Anomaly Detection

Anomaly detection is also performed in three steps. In the first step, we assume
that drift is linear. To calculate drift we use simple linear regression and fit
a line to the data. This line is taken as the computed drift. Afterwards,
we compute a moving average of the data in order to catch seasonality effects.
When both drift and seasonality are removed, we are left with the residual data.
We use z-scores to detect any anomalies in the residual. These functions
are contained in `anomaly_detection.py`.

## Simulation

The `simulation.py` file puts together both steps and plots the results.
Several constants that are necessary for the simulation are also defined in this
file. You can manipulate these constants and see how the results change
if you wish.

## Running the Project

Simply run

`python simulation.py`

in the shell. You might have to install dependencies provided in the
`requirements.txt` file.

The script outputs an image containing plots relevant to the simulation. This
file is named `output_plot.png` and is placed in the working directory by default.
