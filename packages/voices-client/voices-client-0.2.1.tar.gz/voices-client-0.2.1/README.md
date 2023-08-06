# Python Layer Template

This is the Fondeadora Python serverless framework template.
It is intended to be used with Python v3.8 but could be updated to more recent versions.

## Contents

This template includes the following extra configurations:

- [serverless framework][1]
- [serverless-offline plugin][2]
- [serverless-plugin-git-variables][6]
- [serverless-plugin-warmup][7]
- [serverless-prune-plugin][8]
- [serverless-python-requirements][9]
- [Pylint][3] code formatter
- [Flake8][4] for code linting

It will, by default set the stage to `dev` and the region to `us-east-1`.

Pre-commit is configured to run `pyformat` and `flake8` on the pre-commit hook.

## Usage

First you should have Node.js, yarn and Python v3.8 installed on your machine.

1. Install the `serverless` framework with

```shell
npm install -g serverless
```

2. Install the serverless framework plugins required.

```shell
npm install
```

3. Create Pipenv shell environment

```shell
make venv
```

4. Install Python dependencies

```shell
make install
```

And that’s all.


## Testing

For testing you need to configure the env vars `VOICES_USER` and `VOICES_PASS`, then execute 
the command `make test`.

## Scripts

To see all available commands from Make file just run the commands `make` or `make help`.

## Suggestions

Please open an issue, so we can discuss changes to this template.

[1]: https://serverless.com/
[2]: https://github.com/dherault/serverless-offline
[3]: https://black.readthedocs.io/en/stable/
[4]: http://flake8.pycqa.org/en/latest/
[5]: https://pre-commit.com/
[6]: https://github.com/jacob-meacham/serverless-plugin-git-variables
[7]: https://github.com/FidelLimited/serverless-plugin-warmup
[8]: https://github.com/claygregory/serverless-prune-plugin
[9]: https://github.com/UnitedIncome/serverless-python-requirements
