# PySAMP-Map Andreas Plugin  #


This plugin was initiali made by Kalcor and extended bv Mauzen.
It allows you to load different height maps and check the min height for x, y coordinates.
You can us it as example for an anti cheat to detect airbreaks easier or to prevent falling through the ground.


## Functions
|native|params|return|
|-------|-------|:-----:|
|map_andreas_init|mode, name: str|int (0 failed/1 success)|
|map_andreas_unload|name: str|int (0 failed/1 success)|
|map_andreas_save_current_map|name: str|int (0 failed/1 success)|
|map_andreas_find_z_for_2d_coord|x: float, y: float|int (0 failed/1 success)|
|map_andreas_find_average_z|x: float, y: float|int (0 failed/1 success)|
|map_andreas_set_z_for_2d_coord|x: float, y: float, z: float|int (0 failed/1 success)|


## Installation

Move pymapandreas to the server folder

```python
from pymapandreas.mapandreas import MapAndreas
```

### Example
Initialize MapAndreas and get a position.
```python
from pysamp import on_gamemode_init

@on_gamemode_init
def on_ready():
    map_andreas = MapAndreas(MapAndreasMode.MAP_ANDREAS_MODE_FULL, "scriptfiles/SAFull.hmap")
    if map_andreas.find_average_z(20.001, 25.006):
        print("Found")
``` 