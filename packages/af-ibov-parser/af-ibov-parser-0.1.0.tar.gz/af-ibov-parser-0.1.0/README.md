# Aerofin Ibov Parser

A CLI that parses archives from the ibovespa website into json records.

A directory will be created for each archive file (yearly) and a json file
will be created per archive record.

## Requirements

* python >= 3.6
* asyncio
* typing (type hints)

## Installation

Intalling from gitlab:

```bash
pip install -u git+https://gitlab.com/aerofin/tooling/af-ibov-parser.git@master
```

Installing from pypi:

```bash
pip install -u af-ibov-parser
```

## Usage

Once installed, the CLi will be available as `af-ibov-parser`.

Run `af-ibov-parser --help` for commands or check the [docs website](https://af-ibov-parser.readthedocs.org).

## Development

A `Makefile` is provided for common tasks, such as running tests.

The project uses poetry as "project tooling".

A `setup.py` file is generated using `dephell`.

Tests are based on `pytest` but they can be used by running `make test`.

The project also depends on `mypy` in strict mode which is used before running the actual tests.

## License

MIT
