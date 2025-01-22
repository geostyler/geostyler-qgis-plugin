import subprocess
import os
import sys


def update_environment_path():
    # Get the current folder of the script
    current_folder = os.path.dirname(os.path.abspath(__file__))
    environment_path = os.getenv("PATH", "")

    # Check if the directory is already in PATH
    if current_folder not in environment_path:
        # Add the current folder to the PATH environment variable
        os.environ["PATH"] = current_folder + os.pathsep + os.environ.get("PATH", "")


def run_geostyler(input_file, output_file, output_format):
    update_environment_path()

    # Define the command and parameters
    # command = ["geostyler", "--version"]

    command = [
        "geostyler",
        input_file,
        "--source",
        "qgis",
        "--target",
        output_format,
        "--output",
        output_file,
    ]

    # print(" ".join(command))

    # Call the command
    # return_code = subprocess.call(command)
    # result = subprocess.run(command, capture_output=True, text=True, encoding="utf")

    # Hide the shell window on Windows
    if sys.platform == "win32":
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf", creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf")

#
#args, returncode, stdout and
#    stderr
    return result
