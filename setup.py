"""
Flask-Maintenance
-----------------

Flask Extension to enable or disable Maintenance mode.
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Flask-Maintenance',
    version='0.0.1',
    url='https://github.com/akhilharihar/Flask-Maintenance',
    license='MIT',
    author='Akhil Harihar',
    author_email='hariharakhil@gmail.com',
    description='Flask Extension to enable or disable Maintenance mode.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.0',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    entry_points={
        'flask.commands': [
            'maintenance=flask_maintenance.cli:maintenance'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Development Status :: 2 - Pre-Alpha"
    ]
)
