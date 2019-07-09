from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='uwgs',
    version='0.2.0',
    description='Flexible http client for reading UW Groups API v3.',
    long_description=readme,
    author='UW Medicine Research IT',
    url='https://github.com/uwrit/uwgs',
    packages=['uwgs']
)
