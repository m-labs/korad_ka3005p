from setuptools import setup, find_packages

setup(
    name="korad_ka3005p",
    install_requires=["asyncserial"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_korad_ka3005p = korad_ka3005p.aqctl_korad_ka3005p:main",
        ],
    },
)
