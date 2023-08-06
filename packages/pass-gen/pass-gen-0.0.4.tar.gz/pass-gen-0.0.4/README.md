# pass_gen
Password generator

## Installation
Make sure you have installed [python](https://www.python.org/)

```bash
$ pip install -i https://test.pypi.org/simple pass-gen
```

## How to use?
### cli
You can quickly generate password by typing the following command on terminal

```bash
$ pass_gen
```

#### Options
`-l`, `--length`  Determine password length _this should be between 8-16_ __Default 12__  
`--help`  Show help and exit

### Package
You can import as package

```python
import pass_gen
```

#### Method

`generate`  Generates random password

#### Example

```python
import pass_gen

password = pass_gen.generate()
```
