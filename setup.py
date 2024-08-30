from setuptools import setup, find_packages

setup(
    name='predictable_jokes',  
    version='0.1.0',  
    packages=find_packages(),  # Automatically find package directories
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[],  # List dependencies if any, otherwise leave it empty
    entry_points={
        'console_scripts': [
            'tell-a-joke=predictable_jokes.jokes:get_random_joke',  # Command-line tool entry point
        ],
    },
    author='Evan Wimpey',  
    author_email='evan@predictablejokes.com',  
    description='A Python package for AI, ML, data, and techjokes.',
    long_description=open('README.md').read(),  
    long_description_content_type='markdown',  
    url='https://github.com/ewimpey/predictable_jokes',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python version requirement
)
