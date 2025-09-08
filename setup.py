#!/usr/bin/env python3
"""
Ge-ez (ግእዝ) - Amharic Programming Language
Setup script for PyPI distribution
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="geez-lang",
    version="1.0.0",
    author="Mightyshambel",
    author_email="mightyshambel@example.com",
    description="Ge-ez (ግእዝ) - The world's first complete Amharic programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mightyshambel/Ge-ez",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Amharic",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "geez=geez.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "geez": ["*.md", "examples/*.geez"],
    },
    keywords="amharic programming language interpreter ethiopia geez",
    project_urls={
        "Bug Reports": "https://github.com/Mightyshambel/Ge-ez/issues",
        "Source": "https://github.com/Mightyshambel/Ge-ez",
        "Documentation": "https://github.com/Mightyshambel/Ge-ez/blob/main/docs/",
    },
)
