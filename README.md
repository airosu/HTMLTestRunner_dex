# Description

This is a modified version of the HTMLTestRunner created by Wai Yip Tung, http://tungwaiyip.info/software/HTMLTestRunner.html

HTMLTestRunner is an extension to the Python standard library's unittest module. It generates easy to use HTML test reports.


## Updates / Features

* Python 3.x support
  - This version is for python version 3.x and upwards
  
* Slight Visual Changes
  - Small changes to color palette
  - Alignment changes, containers have fixed widths
  - Test groups are expanded by default

* Docstring Description Support
  - Adding a docstring in the test group / test will output it in the report
  - Not adding a docstring will output the test group / test method name instead
  - Docstrings need to be on the firs line in a class / method (unittest behavior)
  
* Automatically Generated Reports
  - Every time a test is ran, a new report will be created in a 'reports' folder
  
* Specified Report Output
  - A report will also be generated in the specified output .html file
  - When running the script, specify the output file using > in the terminal (e.g. "python my_suite.py > my_report.html")


![Report Screenshot](/screenshot_01.png)


## Installation

Only a single file module HTMLTestRunner_dex.py is needed to generate your report. Either copy the file from this repository, or copy / paste the content in your own .py file

## Usage

```
Runner must be configured in the main script file:
--> runner = HTMLTestRunner_dex.HTMLTestRunner()

When executed, the test or suite must be passed to the runner:
--> runner.run(my_test_suite)

A full example can be seen in "sample_test_report.py" file
```

## Running

```
python script.py > report.html
```
