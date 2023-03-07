# Stopwatch

Simple stopwatch based on PySide6 with QML. The whole design is based on a svg vector graphic
that is organized in multiple layers. These layers are extracted and saved in separate files.
In QML these layers are stacked and animated to create the result below.

[![Video](frontend/images/svg/stopwatch.svg)](doc/demo.mp4)

## Setup environment

To setup a development environment and install all requirements run the following commands (example for windows):

    python -m venv venv
    venv/Scripts/activate
    python -m pip install -r requirements.txt

## Run

    python stopwatch_backend/main.py