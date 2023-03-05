from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in service_desk/__init__.py
from service_desk import __version__ as version

setup(
	name="service_desk",
	version=version,
	description="C2N Service Desk Application",
	author="Hephzibah Technologies Inc",
	author_email="david.alexander@hephzibahtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
