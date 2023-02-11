from setuptools import setup, find_packages
import os


def get_requirements(*file_paths):
    """Get requirements which are needed for installation"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    reqs = []
    for line in open(filename).readlines():
        req = line.strip()
        if req and not req.startswith("-"):
            reqs.append(req)
    return reqs


setup(
    name="shop-be",
    version='0.1.0',
    description="Shop API (Rest)",
    author="Victor",
    url="https://github.com/vwjugow/shop_be_juiceIT",
    packages=find_packages() + ['project.envs'],
    package_data={'project': ['envs/flask.cfg']},
    include_package_data=True,
    install_requires=get_requirements("requirements/core.txt"),
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
)
