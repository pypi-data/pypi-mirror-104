# cdsr_pack

CDSR pack is a package to store common functions from CDSR project.


## Installation

```
$ pip install cdsr-pack==0.0.dev2
```

## Usage

```
>>> from cdsr_pack import build_collection, decode_path

>>> image = ('/TIFF/AMAZONIA1/2021_03/AMAZONIA_1_WFI_DRD_2021_03_03.12_57_40_CB11/'
             '217_015_0/2_BC_LCC_WGS84/AMAZONIA_1_WFI_20210303_217_015_L2_BAND4.tif')

>>> decoded_image = decode_path(image)

>>> decoded_image
{
    'satellite': 'AMAZONIA1', 'sensor': 'WFI',
    'path': '217', 'row': '015',
    'geo_processing': '2', 'radio_processing': 'DN'
}

>>> build_collection(decoded_image)
'AMAZONIA1_WFI_L2_DN'
```

## Development

Install a specific Python version and create a virtualenv with it. For example:

```
$ pyenv install 3.8.5 && \
    pyenv virtualenv 3.8.5 inpe_cdsr_cdsr_pack
```

Activate the virtualenv and install the dependencies inside it:

```
$ pyenv activate inpe_cdsr_cdsr_pack && \
    pip install -r requirements.txt
```


### Testing

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
