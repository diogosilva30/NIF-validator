[![PyPI version](https://badge.fury.io/py/NIF-validator.svg)](https://badge.fury.io/py/NIF-validator)

# NIF-validator
A small Python package to validate Portuguese taxpayer numbers (NIFs). It checks if NIFs are in a **correct format** and if they do in fact **exist**.

# Installation :package: 

From PyPi repository:

```
pip install NIF-validator
```

From source code:

```
git clone https://github.com/spamz23/NIF-validator.git
virtualenv venv
pip install -r requirements.txt
```

# How to use it?
It's very simple! :fire:

```
import nif_validator

# Let's try validating "123456789"
nif_validator.validate("123456789") # Returns True

# Let's try validating "123x56789" (notice the typo 'x')
nif_validator.validate("123x56789") # Returns False

# Let's try validating "123" (too small, must be 9 digits)
nif_validator.validate("123") # Returns False

```
