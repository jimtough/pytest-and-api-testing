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

## creating a virtual environment

Creating a virtual environment on Windows 10 seems to be somewhat unreliable.

If I want to do so via the Windows Command Prompt (because I f'ing HATE Powershell), then I do the following:
* Open a Windows Command Prompt as Administrator
* Install 'virtualenv' using pip
  * `pip3 install -U pip virtualenv` (if it is already installed then this may update to a newer version)
* Create a virtual environment named 'venv01' (or whatever name you choose)
  * `cd \path\to\parent\dir` 
  * `virtualenv venv01`
  * This will create a 'venv01' subdirectory that contains all the virtual environment scripts/files/etc 
* Activate the virtual environment
  * `\path\to\parent\dir\venv01\Scripts\activate`

To deactivate the virtual environment, use the deactivate script:
* Open a Windows Command Prompt as Administrator
* Deactivate the virtual environment
  * `\path\to\parent\dir\venv01\Scripts\deactivate`
