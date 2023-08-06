<center>
    <img width="100%" src="https://raw.githubusercontent.com/astroDimitrios/astroedu/e2d3007b867c3f5ac34d6bf4b2ca2f02aa38d824/assets/logo/astroeduLOGOtag.svg" alt='AP Logo'>
</center>

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md) 

This package is in alpha.

## Installation

To install **astroedu** run
```
>>> pip install astroedu
```
then run
```
>>> astroedu build
```
which creates the configuration file **config.ini**.

**config.ini** stores the location of your documents folder.
This is where an astroedu folder for interactive activites will me made. (not yet implemented)

## Current Functionality

### Interactives

```
>>> astroedu interactive wiens_law
```

Loads the interactive notebook file exploring Wien's Law. 
Jupyter lab arguments can be passed after the interactive name for instance:

```
>>> astroedu interactive wiens_law --port 9999
```

### Datasets

To use a data set import the utitlity function ```load_data``` from the datasets module:
```
from astroedu.datasets import load_data
```
Then you can load a data set by passing its name as a string to ```load_data```.
```
planets = load_data('planets')
```
The function returns a Pandas dataframe.