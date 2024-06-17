import os

# Set the PWD environment variable to the correct path
os.environ["PWD"] = "../"  # Replace with the actual path to the src directory

# Verify the PWD environment variable is set correctly
print(f"PWD is set to: {os.getenv('PWD')}")

import os
import sys

DJANGO_SETTINGS_MODULE = "mechome.settings"

def init():
    PWD = os.getenv("PWD")
    if not PWD:
        raise EnvironmentError("PWD environment variable is not set.")
    print(f"Changing directory to: {PWD}")
    os.chdir(PWD)
    sys.path.insert(0, PWD)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    print("Setting up Django...")
    import django
    django.setup()
    print("Django setup complete.")

# Call the init function
init()
