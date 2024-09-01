from setuptools import find_packages, setup

import OfficialNezuNotify

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=OfficialNezuNotify.__project_name__,
    version=OfficialNezuNotify.__version__,
    author=OfficialNezuNotify.__author__,
    author_email=OfficialNezuNotify.__email__,
    description=OfficialNezuNotify.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=OfficialNezuNotify.__url__,
    packages=find_packages(),
    classifiers=OfficialNezuNotify.__classifiers__,
    keywords=OfficialNezuNotify.__keywords__,
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.1",
    ],
)
