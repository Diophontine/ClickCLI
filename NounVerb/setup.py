from setuptools import setup

setup(
    name='tutorial',
    version='0.1.0',
    py_modules=['src'],
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'cli = main:cli',
        ],
    },
)
