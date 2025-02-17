import os
import virtualenv

def activate_env_command():
    PROJECT_NAME = 'course_one'
    virtualenvs_folder = os.path.expanduser("../.virtualenvs")
    command = "source {}/{}/bin/activate && pip install -r requirements.txt".format(virtualenvs_folder, PROJECT_NAME)
    print('Activate Environment with: ',command)

if __name__ == "__main__":
    activate_env_command()