import os

os.system('sudo chmod 777 -R /usr/local/bin')
os.system('sudo chmod 777 -R /usr/local/lib')
os.system('sudo chmod 777 /dev/ttyS3')

import re
import setuptools


def get_packages():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, 'src')


def get_install_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith("#")]
    return reqs


def get_version():
    with open("./HandController/__init__.py", "r") as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return version


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setuptools.setup(
    name="HandController",
    version=get_version(),
    author="LSH9832",
    author_email="bitshliu@qq.com",
    url="https://github.com/LSH9832/HandController",
    python_requires=">=3.6",
    install_requires=get_install_requirements(),
    packages=setuptools.find_packages(exclude=["*test"]),
    project_urls={
        "Source": "https://github.com/LSH9832/HandController",
    },
)
