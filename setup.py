from setuptools import setup, find_packages

setup(
    name='vws',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    author='Lyan',
    author_email='admin@blackcoffee.lol',
    description='Consists of three main classes: File, Directory, and Workspace. Together, these classes allow users to create, manage, and organize files and directories in a virtual workspace.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourrepository',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)