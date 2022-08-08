# LegitExersice

This is a solution for Legit's exercise.

This Flask-based app waits for webhooks from GitHub, and monitors the events.
The following events will be notified to the user:
1. pushing code between 14:00-16:00
2. create a team with the prefix “hacker”
3. creating a repository and deleting it in less than 10 minutes

In order to use it, webhooks must be set on GitHub manually.

## Installation

Enter the project directory and run:

```bash
python3 -m pip install -e .
```

## Usage

Run the following commands:

```bash
export FLASK_APP=LegitMonitor
python3 -m flask run
```
