from setuptools import setup,find_packages
setup(
    name='gitback',
    version='1.0.9',
    description='Makes a backup of all your repositories and gists from GitHub',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/gitback',
    packages=find_packages(),
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    install_requires=['six==1.14.0'],
    entry_points={ 'console_scripts': [ 'gitback=gitback.__init__:backup' ] }
)
