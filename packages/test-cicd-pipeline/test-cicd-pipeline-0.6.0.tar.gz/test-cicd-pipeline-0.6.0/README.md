# testcicd

In master, change version number of pip package manually in setup.py (this is because merges to master should only
happen when a new stable and improved version of the code is available). Package is pushed to PyPi
In develop, package version is automatically updated based on angular commit style messages and package is pushed to TestPyPi