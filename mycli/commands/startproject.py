import os
import shutil
import pkg_resources

def run(project_name):
    template_dir = pkg_resources.resource_filename("mycli", "template")
    target_dir = os.path.abspath(project_name)

    if os.path.exists(target_dir):
        print(f"Folder '{project_name}' already exists!")
        return

    shutil.copytree(
        template_dir,
        target_dir,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
    )

    print(f"Project '{project_name}' created successfully!")