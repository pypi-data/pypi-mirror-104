import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = os.getenv('VERSION', '0.0.1')

setuptools.setup(
    name="apigee-trace-apim", # Replace with your own username
    version=version,
    author="NHS Digital APIM",
    author_email="apim@nhs.net",
    description="A package to provide apigee trace functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artronics/apigee-trace",
    project_urls={
        "Bug Tracker": "https://github.com/artronics/apigee-trace/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
