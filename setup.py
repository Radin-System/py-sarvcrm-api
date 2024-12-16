from setuptools import find_packages, setup

from sarvcrm_api import version

setup(
    name='py-sarvcrm-api',
    version=version,
    description='simple sarvcrm api module',
    author='Radin-System',
    author_email='technical@rsto.ir',
    url='https://github.com/Radin-System/py-sarvcrm-api',
    install_requires=[
        'requests==2.32.3',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)