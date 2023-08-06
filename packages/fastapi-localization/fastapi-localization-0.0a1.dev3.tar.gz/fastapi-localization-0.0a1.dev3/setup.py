from setuptools import (
      setup,
      find_packages,
)

import fastapi_localization


def get_long_description():
    with open("README.md", "r", encoding="utf8") as f:
        return f.read()


setup(name='fastapi-localization',
      version=fastapi_localization.__version__,
      url='https://github.com/ikasymov/fastapi-localization',
      license='MIT',
      author='Ilgiz Kasymov',
      author_email='ilgizkasymov@gmail.com',
      description='Language localization fastapi',
      packages=find_packages(include=("fastapi_localization", "fastapi_localization.*")),
      long_description=get_long_description(),
      zip_safe=False,
      install_requires="fastapi",
      python_requires=">=3.7",
)
