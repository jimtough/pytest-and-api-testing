# pytest-and-api-testing


## references

* https://docs.pytest.org/en/stable/example/markers.html


## quick notes

* It appears that `pytest.ini` must be in the current ~~directory~~ module when you call `pytest`, otherwise it will be ignored
* Using the `-s` option for PyTest will allow console output from the tests to display (such as print() statements)
  * `pytest -m my_marker -s`
* If you want output from 'logging' module displayed in the console, use this:
  * `pytest -m my_marker -s --log-cli-level=DEBUG`
  * ALTERNATIVE: add some configuration to the `pytest.ini` in your unit tests module to make logging always enabled
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

## 'setuptools' module and the setup.py file

The instructor just introduced the 'setuptools' module. I believe it is a standard Python module.

We created a `setup.py` file in the root of the project.
I don't yet understand what value this provides. Hopefully it will be explained later in the course.

Command to execute the setup.py file: `python setup.py install`
