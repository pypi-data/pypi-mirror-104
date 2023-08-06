[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

voices-client
===========

A library for accessing Voices for python.


## Installation
Use the package manager [pipenv](https://pypi.org/project/pipenv/2020.6.2/) to install.

    pipenv install voices-client

## Usage
Use your own Voices credentials.
* **user** - Voices user
* **password** - Voices password

```python
from voices import Voices

client = Voices(
    user='user',
    password='password',
)
```


## Test
Tested with [mamba](https://mamba-framework.readthedocs.io/en/latest/), install pipenv dev packages and then run tests.

    pipenv install --dev
    pipenv run make test

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
