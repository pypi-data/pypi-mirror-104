from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='basicmathfunctions',
    version='0.0.55',
    description='Basic math functions',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='Isaac Cobb',
    author_email='cobbcoding@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='math',
    packages=find_packages(),
    install_requires=['']
)
