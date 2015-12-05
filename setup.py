import os
from setuptools import setup, find_packages
import sys

BASE_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(BASE_DIR, 'shecodes_ciphers'))

install_require = [
    "clint==0.5.1"
]

test_require = [
    # Testing
    'pytest==2.7.2',
    'pytest-cache==1.0',

    # Code quality
    'flake8==2.4.1',
    'radon==1.2.2',
]

setup(
    name="shecodes-ciphers",
    version="0.0.1",
    author="Ben Emery",
    author_email="willcodefortea@gmail.com",
    description="Simple examples of a few ciphers.",
    url="https://github.com/willcodefortea/shecodes-ciphers",
    package_dir={'': 'shecodes_ciphers'},
    packages=find_packages('shecodes_ciphers'),
    install_requires=install_require,
    extras_require={
        'tests': test_require
    }
)