from setuptools import setup

setup(
    name="devconnect",
    packages=["devconnect"],
    include_package_data=True, 
    install_requires=[
        'flask',
    ],
)