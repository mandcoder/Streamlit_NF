from setuptools import setup, find_packages

setup(
    name="netflix",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
