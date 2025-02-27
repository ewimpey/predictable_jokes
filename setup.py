from setuptools import setup, find_packages

setup(
    name='predictable_jokes',  
    version='0.1.0',  
    packages=find_packages(),  # Automatically find package directories
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[],  # no dependencies, I reckon
    entry_points={
        'console_scripts': [
            'tell-joke=predictable_jokes.jokes:tell_joke',  # Command-line tool entry point
        ],
    },
    author='Evan Wimpey',  
    author_email='evan@predictablejokes.com',  
    description='A Python package for AI, ML, data, and tech jokes.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/ewimpey/predictable_jokes',  
    classifiers=[
        'Programming Language :: Python :: 3',  
        'Operating System :: OS Independent',
    ],
    license="MIT",
    options={"metadata": {"license_files": ""}},  # Explicitly remove license_files wtf mate
    python_requires='>=3.6',  # Python version requirement
)
