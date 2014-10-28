"""Setup file for easy installation"""
import os
from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
PIP_REQUIRES = os.path.join(ROOT, "requirements.txt")


setup(
    name="django-payzen-tester",
    version="0.9",
    description="Django project to test django-payzen app",
    author="Bertrand Svetchine",
    author_email="bertrand.svetchine@gmail.com",
    url="https://github.com/bsvetchine/django-payzen-tester",
    packages=find_packages(),
    install_requires=["django-payzen"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django", ],
    include_package_data=True,
)
