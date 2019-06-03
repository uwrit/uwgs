from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='uwgs',
    version='0.1.0',
    description='Flexible http client for UW Groups API v3.',
    long_description=readme,
    author='UW Medicine Research IT',
    url='https://github.com/uwrit/uwgs',
    packages=['uwgs']
)
