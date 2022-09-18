import sys

from setuptools import setup, find_packages


MINIMAL_PY_VERSION = (3, 9)
if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError(
        'pyrogram_middleware_patch works only with Python {}+'.format('.'.join(map(str, MINIMAL_PY_VERSION))))


setup(
    name='pyrogram_middleware_patch',
    version='1.1',
    license='MIT',
    author='kotttee',
    python_requires='>=3.9',
    description='This package will add middlewares for pyrogram',
    url='https://github.com/kotttee/pyrogram_middleware_patch/',
    install_requires=['pyrogram>=2.0.0'],
    classifiers=[
        'License :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages()
)
