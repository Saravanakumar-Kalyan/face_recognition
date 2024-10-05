# Face Recognition Based Attendance System

## Overview

This project implements a face recognition-based attendance system using Python. The system captures images of individuals and recognizes their faces to mark attendance automatically.

## Features

- Capture and store images of individuals
- Recognize faces in real-time
- Mark attendance based on recognized faces
- Save attendance to a CSV file

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/)
- Python 3.9

### Setting Up the Environment

1. Clone this repository:

   ```bash
   git clone https://github.com/Saravanakumar-Kalyan/face_recognition.git
   ```
   ```bash
   cd face_recognition
   ```
2. Create a Conda environment and activate it:
    ```bash
    conda create --name face-recognition-env python=3.9
    ```
    ```bash
    conda activate face-recognition-env
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    
4. For installing dlib on windows refer to this [link](https://github.com/z-mahmud22/Dlib_Windows_Python3.x)

## Usage
1. Run the script to capture images:
    ```bash
    python run.py -a <name>
2. Run the script to recognise faces and mark attendance:
    ```bash
    python run.py -r
    ```
    ```bash
    # Attendance will be stored in attendance/ folder
