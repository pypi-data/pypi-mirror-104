from setuptools import find_packages, setup

setup(
    name="qpq",
    version="0.1",
    description="Really nice lib",
    author="Mathieu Moalic",
    author_email="matmoa@pm.me",
    platforms=["any"],
    license="GPL-3.0",
    url="https://github.com/MathieuMoalic/qpq",
    packages=find_packages(),
    # install_requires=[i.strip() for i in open("requirements.txt").readlines()],
)
