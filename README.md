# pytest-and-api-testing


## references

* https://docs.pytest.org/en/stable/example/markers.html


## quick notes

* It appears that `pytest.ini` must be in the current directory when you call `pytest`, otherwise it will be ignored
* Using the `-s` option for PyTest will allow console output from the tests to display
  * `pytest -m my_marker -s`
* pytest-html is used to generate unit test reports
  * `pip install pytest-html` (you only need to do this once to install)
  * `pytest --html=demo_report.html --self-contained-html`
