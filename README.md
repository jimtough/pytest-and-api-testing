# pytest-and-api-testing


## references

* https://docs.pytest.org/en/stable/example/markers.html


## quick notes

* It appears that `pytest.ini` must be in the current directory when you call `pytest`, otherwise it will be ignored
* Using the `-s` option for PyTest will allow console output from the tests to display
  * `pytest -m my_marker -s`
