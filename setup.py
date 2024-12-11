from setuptools import find_packages, setup

setup(
    name='py-sarvcrm-api',
    version='1.0.0',
    description='simple sarvcrm api module',
    author='Radin System',
    author_email='Technical@rsto.ir',
    url='https://github.com/Radin-System/py-sarvcrm-api',
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)