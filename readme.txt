
# CNN-Based Crowd Density Estimation

## Project Overview
This project aims to estimate crowd density using Deep Learning
and Computer Vision.

## Objectives
- Upload and display crowd images.
- Develop a CNN-based density-map regression model.
- Estimate crowd counts from predicted density maps.
- Visualize crowd density for safety monitoring.

## Technologies Used
- Python
- Deep Learning
- Convolutional Neural Networks (CNN)
- Streamlit
- NumPy
- Matplotlib
- Pillow

## Current Features
- Crowd image upload
- Image preview
- Streamlit dashboard interface

## Future Enhancements
- Train a CNN using an annotated crowd-counting dataset.
- Generate predicted density maps.
- Estimate crowd counts.
- Add crowd-level indicators and video support.

## Run Locally
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run crowd_density_app.py
```

## Note
Actual crowd-count predictions require a trained CNN model.
The current interface does not generate verified crowd counts.
