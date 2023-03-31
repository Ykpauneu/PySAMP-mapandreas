from dataclasses import dataclass

@dataclass
class MapAndreasMode:
    MAP_ANDREAS_MODE_NONE: int = 0
    MAP_ANDREAS_MODE_MINIMAL: int = 1
    MAP_ANDREAS_MODE_MEDIUM: int = 2
    MAP_ANDREAS_MODE_FULL: int = 3
    MAP_ANDREAS_MODE_NOBUFFER: int = 4
    