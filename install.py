import subprocess
import os
import sys

# Function to run pip commands
def run_pip(*args):
    subprocess.run([sys.executable, "-m", "pip", "install", *args])

# Path to the requirements.txt file
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

# Installing packages from requirements.txt
with open(req_file) as file:
    for package in file:
        package = package.strip()
        if package:  # Ignore empty lines
            run_pip(package)

print("Dependencies installed successfully.")