#!/usr/bin/env python3
"""
Setup script for Goyard Product Scraper
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="goyard-product-scraper",
    version="1.0.0",
    author="Daniel Peggy",
    author_email="danielpeggy@gmail.com",
    description="A web scraping tool for extracting product metadata from Goyard website using Amazon Nova Act",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielpeggy/goyard-product-scraper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "goyard-scraper=goyard_scraper_secure:main",
        ],
    },
    keywords="web-scraping, goyard, product-metadata, nova-act, automation",
    project_urls={
        "Bug Reports": "https://github.com/danielpeggy/goyard-product-scraper/issues",
        "Source": "https://github.com/danielpeggy/goyard-product-scraper",
        "Documentation": "https://github.com/danielpeggy/goyard-product-scraper#readme",
    },
)
