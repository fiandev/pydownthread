# pydownthread
Multiple files downloader for python

## installation
```sh
pip install pydownthread
```

## how to usage
```python
from pydownthread import pydownthread

downloader = PyDownThread([
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/242px-Python-logo-notext.svg.png",
], output="./images")

downloader.start()
```

> built with ♥️ by fiandev