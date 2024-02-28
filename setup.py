# Installs this tool in your system

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tornado",
    version = "1.3.5",
    author = "samogod",
    license = "MIT",
    keywords = ["Tornado", "Tor reverse shell", "reverse shell", "metasploit", "tor"],
    url = "https://github.com/samogod/tornado",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'requests',
        'wget',
        'stem',
    ],
    entry_points={
        'console_scripts': [
            'tornado = tornado.__main__:main'
        ]
    },
)
