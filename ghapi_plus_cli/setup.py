from setuptools import setup, find_packages

setup(
    name='ghapi_plus_cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'gh-api = ghapi_plus_cli.ghapi_plus:cli',
        ],
    },
)