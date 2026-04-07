from setuptools import setup, find_packages

setup(
    name="scrapping-cli",
    version="1.0.3",
    packages=find_packages(include=["mycli", "mycli.*"]),
    include_package_data=True,
    package_data={
        "mycli": ["template/**/*"],
    },
    entry_points={
        "console_scripts": [
            "scrapping-cli=mycli.cli:main",
        ],
    },
    author="Shabbir",
    description="CLI tool to generate scraping project templates",
)