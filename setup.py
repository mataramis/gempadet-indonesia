
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'this is an package of latest indonesian earthquake'
LONG_DESCRIPTION = 'this package uses beautifulsoup4 and request, the result of this package is the latest earthquake update information in the Indonesian region'
# Setting up
setup(
    name="gempadet-indonesian",
    version=VERSION,
    author="Muhammad Afrizal",
    author_email="muhamadafrizal5@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    # install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'scream'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)