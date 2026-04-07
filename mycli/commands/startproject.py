import os
import shutil
from importlib.resources import files


def run(project_name):
    template_dir = files("mycli").joinpath("template")
    target_dir = os.path.abspath(project_name)

    if os.path.exists(target_dir):
        print(f"Folder '{project_name}' already exists!")
        return

    shutil.copytree(
        template_dir,
        target_dir,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )

    print(f"Project '{project_name}' created successfully!")