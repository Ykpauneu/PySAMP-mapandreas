from pysamp import call_native_function
from .modes import MapAndreasMode


def map_andreas_init(mode: MapAndreasMode, name: str):
    return call_native_function("MapAndreas_Init", mode, name)


def map_andreas_find_z_for_2d_coord(x: float, y: float):
    z = 0.0
    z = call_native_function("MapAndreas_FindZ_For2DCoord", x, y, z)
    return z


def map_andreas_find_average_z(x: float, y: float):
    z = 0.0
    z = call_native_function("MapAndreas_FindAverageZ", x, y, z)
    return z


def map_andreas_unload():
    return call_native_function("MapAndreas_Unload")


def map_andreas_set_z_for_2d_coord(x: float, y: float, z: float):
    return ("MapAndreas_SetZ_For2DCoord", x, y, z)


def map_andreas_save_current_map(name: str):
    return call_native_function("MapAndreas_SaveCurrentHMap", name)
