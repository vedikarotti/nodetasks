from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nodetasks",
    version="0.0.8",
    author="Vedika Rotti",
    author_email="vedika.rotti@gmail.com",
    description="Simple CLI script for listing and running npm tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vedikarotti/nodetasks.git",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    install_requires=[
        'iterfzf'
    ],
    license='MIT',
    packages=['nodetasks'],
    entry_points={
        'console_scripts': [
            'nodetasks=nodetasks:main'
        ]
    }
)
