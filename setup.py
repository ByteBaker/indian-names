from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='indian-names',
    version='0.3',
    author='ByteBaker',
    url="https://github.com/ByteBaker/indian-names",
    description="Generate random names of Indian origin",
    long_description=readme,
    long_description_content_type='text/markdown',
    license='BSD 3-Clause License',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'indian-names = indian_names.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ]
)
