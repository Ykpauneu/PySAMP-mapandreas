from . import (
    map_andreas_init,
    map_andreas_find_z_for_2d_coord,
    map_andreas_find_average_z,
    map_andreas_unload,
    map_andreas_set_z_for_2d_coord,
    map_andreas_save_current_map
)
from .modes import MapAndreasMode

class MapAndreas():
    def __init__(self, mode: MapAndreasMode, name: str):
        self.name = name
        map_andreas_init(mode, name)


    def find_z_for_2d_coord(self, x: float, y: float):
        return map_andreas_find_z_for_2d_coord(x, y)


    def map_andreas_find_average_z(self, x: float, y: float):
        return map_andreas_find_average_z(x, y)


    def unload(self):
        return map_andreas_unload()


    def map_andreas_set_z_for_2d_coord(self, x: float, y: float, z: float):
        return map_andreas_set_z_for_2d_coord(x, y, z)
    
    
    def map_andreas_save(self):
        return map_andreas_save_current_map(self.name)
