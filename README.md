# indian-names <small> (v0.2) </small> 
Python module to generate random names of Indian origin.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/indian-names?label=Python) ![PyPI - License](https://img.shields.io/pypi/l/indian-names?label=License&color=red) ![Maintenance](https://img.shields.io/maintenance/yes/2022?label=Maintained) ![PyPI](https://img.shields.io/pypi/v/indian-names?label=PyPi) ![PyPI - Status](https://img.shields.io/pypi/status/indian-names?label=Status)


Installation
------------

You can install it using pip from the repository as:

    pip install indian-names


Usage
-----

Indian-names can be used as a command line utility or imported as a Python module.

#### Command Line Usage

To use the script from the command line:

```
    $ indian-names
    Anand Dubey
```
#### Python Module Usage

Here are examples of all current features:

```
    >>> import indian_names
    >>> indian_names.get_full_name()
    'Nisha Asthana'
    >>> indian_names.get_full_name(gender='male')
    'Manish Gupta'
    >>> indian_names.get_first_name()
    'Siddhant'
    >>> indian_names.get_first_name(gender='female')
    'Kajal'
    >>> indian_names.get_last_name()
    'Tripathi'
```

The module can currently generate 550+ first names for male and female each, and 350+ last names. Overall 400,000+ full names can be generated.

### TODO (Future):
- Increase the number of names possible.
- Implement first/last name pairs for regional names as well. Emphasis on handling first names that are compatible with only certain last names & vice-versa.


License
-------

This project is released under a [BSD 3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html).

Names are compiled in the following files through various online sources available publically:

- `first.male.names`
- `first.female.names`
- `last.names`
