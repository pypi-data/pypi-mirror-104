# pass-gen
A command line interface (and Python library) for generating passwords

## Installation

```bash
$ pip install pass-gen
```

## Command line usage

```bash
$ pass_gen
```

by default password length is __12__

```bash
$ pass_gen -l 10
```

or, you can set the length. _This value must be between 8-16_

## Python usage

```python
import pass_gen

# Set password length to 10. Default 12
password = pass_gen.generate(10)
```

## Contributors

- Abdulrahman M. Zaky (https://www.github.com/Aionmone)

## License
**pass_gen** is licensed under the MIT license. See the license file for details.
