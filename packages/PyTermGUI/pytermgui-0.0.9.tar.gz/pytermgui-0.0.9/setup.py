from setuptools import setup, find_packages

setup(
    name='pytermgui',
    version='0.0.9',
    packages=find_packages(exclude=['img*','tests*','examples*']),
    license='MIT',
    description='simple and robust terminal user interface library for the command line.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    python_requires=">=3.9.0",
    url='https://github.com/bczsalba/pytermgui',
    author='BcZsalba',
    author_email='bczsalba@gmail.com',
    entry_points={
        "console_scripts": [
            'ptg = pytermgui.cmd:main'
        ]
    }
)

