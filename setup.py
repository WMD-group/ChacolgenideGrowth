from setuptools import setup, find_packages
version="v1.0.0"
DESCRIPTION = 'A chalcogenide package'
LONG_DESCRIPTION = 'A package that makes it easy to convert values between several units of measurement'

setup(
    name="ChacolgenideGrowthh",
    version=version,
    install_requires=[
        "tensorflow",
        "numpy",
        "monty",
        "sympy",
    ],
    description="Chalcogenide growth thermodynamics",
    author="Zhenzhu Li",
    author_email="lizhenzhupearl@gmail.com",
    download_url="https://github.com/WMD-group/ChalcogenideGrowth.git",
    license="MIT",
    packages=find_packages(),
    keywords=[
        "materials",
        "science",
        "thermodynamics"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

