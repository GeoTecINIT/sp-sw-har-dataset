# Smartphone and smartwatch inertial measurements from heterogeneous subjects for human activity recognition

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/GeoTecINIT/sp-sw-har-dataset/)
[![Paper DOI](https://img.shields.io/badge/PaperDOI-10.1016%2Fj.dib.2023.109809-yellow.svg)](https://doi.org/10.1016/j.dib.2023.109809)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8398688.svg)](https://doi.org/10.5281/zenodo.8398688)

This repository contains the dataset and contents described in the _"Dataset of inertial measurements of smartphones and smartwatches for human activity recognition"_ data article. 

> Matey-Sanz, M., Casteleyn, S., & Granell, C. (2023). Dataset of inertial measurements of smartphones and smartwatches for human activity recognition. Data in Brief, 109809.

## Repository structure

**Dataset:** the [`DATA`](./DATA) directory contains the dataset collected and described in the article. It contains:

- `sXX`: directory containing the data collected by the subject `sXX`. A total of 23 subjects participated in the data collection.
  - `sXX_YY_{sp|sw}.csv`: file containing the accelerometer and gyroscope samples collected by the subject `sXX` in the execution `YY` with the smartphone (`sp`) or the smartwatch (`sw`). Each file row (sample) has the following fields:
    - _x_acc_: X-axis value of the accelerometer.
    - _y_acc_: Y-axis value of the accelerometer.
    - _z_acc_: Z-axis value of the accelerometer.
    - _x_acc_: X-axis value of the gyroscope.
    - _y_acc_: Y-axis value of the gyroscope.
    - _z_acc_: Z-axis value of the gyroscope.
    - _timestamp_: when the sample was collected, UNIX timestamp.
    - _label_: activity associated to the sample.
- [`executions_info.csv`](./DATA/executions_info.csv): file with information about the activity sequences executions (phone orientation, first turn and second turn direction).
- [`subjects_info.csv`](./DATA/subjects_info.csv): file with information about the subjects (age, gender, height (cm), weight (kg), dominand hand and number of activity sequences executed).

**Code:**

- [`utils`](./utils): Python package containing modules with some util functions.
  - [`data_loading`](./utils/data_loading): module with functions to load the dataset and associated files.
  - [`exploration`](./utils/exploration): module with functions to obtain insights about the subjects and executions.
  - [`visualization`](./utils/visualization): module with the `plot_execution()` function, which plots the accelerometer and gyroscope samples of a certain execution and device.
- [`example-usage.ipynb`](./example-usage.ipynb): Jupyter Notebook that shows the usage of the provided utility functions.

**Common files:**

- [`requirements.txt`](./requirements.txt): Python dependencies required to use the provided functions. Install Python if it is not installed in your system and execute the following command to install the dependecies:

  ```bash
  pip install -r requirements.txt
  ```
    

## License 

### Dataset

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

The dataset in this repository is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

### Code

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

All contained code in the `utils` package is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).

