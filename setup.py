from distutils.core import setup

setup(
    # Application name:
    name="uthyr",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Franck Rupin",
    author_email="frupin@tuta.io",

    # Packages
    packages=["src/packages", "src/bin"],

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="RELOAD implementation.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
    ],
)
