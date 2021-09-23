```
  ____  ____    _    ____ ___     _____           _ _    _ _   
 | __ )| __ )  / \  |  _ \_ _|   |_   _|__   ___ | | | _(_) |_ 
 |  _ \|  _ \ / _ \ | |_) | |      | |/ _ \ / _ \| | |/ / | __|
 | |_) | |_) / ___ \|  __/| |______| | (_) | (_) | |   <| | |_ 
 |____/|____/_/   \_\_|  |___|_____|_|\___/ \___/|_|_|\_\_|\__|
```
---
## Description
BBAPI_Toolkit is a Python package for easily accessing data via Blackbaud’s ON API and SKY API.


## Requirements
This package is written for Python 3.8 and later. Prior versions of Python may work, but have not been tested. The requests and requests_oauthlib packages need to be installed in your system.
```bash
pip3 install requests requests_oauthlib
```


## Installation
Clone this repository into your project directory:
```bash
cd </path/to/your/project>
git clone https://github.com/Lugal-PCZ/bbapi_toolkit.git
```

Or, if your project is already version controlled with git, add it as a submodule into your project directory:
```bash
cd </path/to/your/project>
git submodule add https://github.com/Lugal-PCZ/bbapi_toolkit.git
```


## Configuration
Duplicate the _config.ini.example_ file into your project directory (or a config subdirectory, if desired), rename it something sensible (like _config.ini_), and modify the settings to match the needs of your current project. Each config file can contain connection settings for ON API and/or SKY API. You can, however, make multiple config files, each with its own settings, if you intend to connect to the API applications with multiple accounts concurrently.


## Usage
Create an instance of the _Client_ class, with the name of your config file as its only parameter, to create a client connection to Blackbaud’s APIs. Once created, pre-built functions provide a consistent interface to the API. The modules and functions in this package mirror the organization of Blackbaud’s API documentation: ```category/group/function``` _or_ ```category/function```.

The following code snippet provides an example of how to use the onapi module to issue two API calls, one to get a list of Blackbaud roles, and the other to retrieve the results of a pre-built list:
```python
from bbapi_toolkit import onapi

client = onapi.Client('config.ini')
roles = onapi.constituents.role.get_roles(client)
listresults = onapi.list.get_list(client, 12345)  # Change this id to that of a list which you can access.
```

The following code snippet provides an example provides the same example using the SKY API:
```python
from bbapi_toolkit import skyapi

client = skyapi.Client('config.ini')
roles = skyapi.school.core_roles.get(client)
listresults = skyapi.school.legacy_list.get(client, 12345)  # Change this id to that of a list which you can access.
```
