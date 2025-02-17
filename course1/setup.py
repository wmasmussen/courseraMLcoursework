import subprocess
import sys
import os

def create_venv(venv_name):
    try:
        subprocess.check_call([sys.executable, "-m", "venv", venv_name])
        print(f"Virtual environment '{venv_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")

def activate_venv(venv_name):
     if os.name == 'nt': # Windows
        activate_script = os.path.join(venv_name, "Scripts", "activate")
     else: # macOS and Linux
        activate_script = os.path.join(venv_name, "bin", "activate")
     print(f"Activate the virtual environment with: source {activate_script}")

if __name__ == "__main__":
    venv_name = "../.virtualenvs/course_one"
    create_venv(venv_name)
    activate_venv(venv_name)