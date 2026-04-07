from setuptools import setup, find_packages

setup(
    author="Shabbir",
    description="CLI tool to generate scraping projects",
    name="scrapping-cli",
    version="1.0.1",   
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "mycli": ["template/**/*"],
    },
    entry_points={
        'console_scripts': [
            'scrapping-cli=mycli.cli:main',
        ],
    },
)