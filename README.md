# NIF-validator
A small Python package to validate Portuguese taxpayer numbers (NIFs). It checks if NIFs are in a correct format and if they do in fact exist.

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
import NIF_validator

# Let's try validating "123456789"
NIF_validator.validate("123456789") # Returns True

# Let's try validating "123x56789" (notice the typo 'x')
NIF_validator.validate("123x56789") # Returns False

# Let's try validating "123" (too small, must be 9 digits)
NIF_validator.validate("123") # Returns False

```
