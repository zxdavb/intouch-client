import os
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install

VERSION = "0.4.0.post1"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our VERSION."""

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {tag} does not match the version of this pkg: {VERSION}"
            sys.exit(info)


setup(
    name="incomfort-client",
    version=VERSION,
    packages=find_packages(),
    install_requires=["aiohttp>=3.6.1", "docopt>=0.6.2"],

    # metadata to display on PyPI
    author="David Bonnes",
    author_email="zxdavb@gmail.com",

    description="A aiohttp-based client for Intergas InComfort/InTouch Lan2RF systems",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    url="https://github.com/zxdavb/incomfort-client",
    download_url="{url}tarball/{VERSION}",

    keywords=["intergas", "incomfort", "intouch", "lan2rf"],
    license="XXX",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Topic :: Home Automation",
    ],
    cmdclass={"verify": VerifyVersionCommand},
)
