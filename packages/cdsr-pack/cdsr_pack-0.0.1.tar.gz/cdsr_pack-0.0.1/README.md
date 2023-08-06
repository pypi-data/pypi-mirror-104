# cdsr_pack

CDSR pack is a package to store common functions from CDSR project.


## Usage

Install a specific Python version and create a virtualenv with it:

```
$ pyenv install 3.8.5 && \
    pyenv virtualenv 3.8.5 inpe_cdsr_cdsr_pack
```

Activate the virtualenv and install the dependencies inside it:

```
$ pyenv activate inpe_cdsr_cdsr_pack && \
    pip install -r requirements.txt
```

## Testing

Activate the virtualenv:

```
$ pyenv activate inpe_cdsr_cdsr_pack
```

Run the test cases:

```
$ python -m unittest discover tests "test_*.py" -v
```

Or, run the test cases and get coverage report:

```
$ coverage run -m unittest discover tests "test_*.py" -v &&
    coverage report -m &&
    coverage html
```
