from setuptools import setup
from yt6 import __version__, __author__, __repo__, __info__

setup(
    name="yt6",
    packages=["yt6"],
    version=__version__,
    license="MIT",
    author=__author__,
    maintainer=__author__,
    author_email="smartwacaleb@gmail.com",
    description=__info__,
    url=__repo__,
    project_urls={"Bug Report": f"{__repo__}/issues/new"},
    python_requires=">=3.8",
    install_requires=[
        "colorama==0.4.6",
        "pytube>=15.0.0",
        "tabulate==0.9.0",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Free For Home Use",
        "Topic :: Home Automation",
        "Intended Audience :: Customer Service",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords = ['yt5','yt6','youtubedl','youtube','downloader','video-downloader'],
    entry_points={
        "console_scripts": [
            ("yt6 = yt6.yt6:launch"),
        ]
    },
)
