from setuptools import find_packages, setup
def get_requirements():
    requirements = []
    try:
        with open("requirements.txt", "r") as f:
            requirements = f.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if "-e ." in requirements:
                requirements.remove("-e .")
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirements

setup(
    name="network_security",
    version="0.0.1",
    author="uvan rishee",
    author_email="uvanrishee123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)