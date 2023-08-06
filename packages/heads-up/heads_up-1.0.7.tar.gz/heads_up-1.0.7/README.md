# heads_up

headsup is a Python library for getting local and remote alerts about your code execution process.

https://github.com/heads-up-org/heads-up

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install heads-up.

```bash
pip install heads-up
```

## Usage

```python
# local
from headsup.local import headsup

headsup()

# remote
from headsup.remote import watch, notify
watch_code = watch()

## ...
## Here comes your long-running code
## ...

notify(watch_code, "Success!!")

```

## Contributing
Pull requests are welcome. For major changes, contact the project owner. 

## License
[GNU General Public License v3.0]