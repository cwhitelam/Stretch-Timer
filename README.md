# Stretching Interval Timer

A simple and intuitive web-based stretching interval timer to help you manage your exercise sessions. This timer allows you to set custom durations, sets, and rest periods, with preset options for quick use. It also includes a dark mode for a better user experience in different lighting conditions.

## Features

- **Preset Timers**: Quick selection of predefined timers (30 seconds, 1 minute, 2 minutes, etc.)
- **Custom Timer**: Set your own duration, sets, and rest periods
- **Dark Mode**: Toggle between dark and light modes
- **Audio Alerts**: Sound notifications at the start and end of each interval

## Screenshots


![Screenshot 1](screenshots/wholeInterface.png)
![Screenshot 2](screenshots/timerInUse.png)

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Flask (or any web server to serve the HTML file)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stretch_timer_v2.git
    cd stretch_timer_v2
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ## On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the Flask application:
    ```bash
    python run.py
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Select a preset timer or input your custom timer settings.
2. Use the play/pause toggle to start or stop the timer.
3. Monitor the timer and listen for audio alerts indicating the start and end of intervals.
4. Switch between dark and light modes using the toggle switch at the top.