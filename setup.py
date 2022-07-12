import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="remecap",
    version="1.0.0",
    author="jiroawesome",
    description="A simple python library that bypasses H-Captcha automatically using yolov5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiroawesome/remecap",
    project_urls={
        "Bug Tracker": "https://github.com/jiroawesome/remecap/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={'': ['**/*']},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=required
)