from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from ...utility import Name
from ...utility import NamedResource

if TYPE_CHECKING:
    from ...resources import Generation, Pokedex, VersionGroup
    from . import Location


class Region(NamedResource):
    locations: Tuple[MinimalResource["Location"], ...]
    main_generation: MinimalResource["Generation"]
    pokedexes: Tuple[MinimalResource["Pokedex"], ...]
    names: Tuple["Name", ...]
    version_groups: Tuple[MinimalResource["VersionGroup"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.locations = tuple(
            MinimalResource(location_data) for location_data in data["locations"]
        )
        self.main_generation = MinimalResource(data["main_generation"])
        self.pokedexes = tuple(
            MinimalResource(pokedex_data) for pokedex_data in data["pokedexes"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.version_groups = tuple(
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        )

    def __repr__(self) -> str:
        return (
            f"<Region id_={self.id} locations={self.locations} main_generation={self.main_generation} "
            f"pokedexes={self.pokedexes} name='{self.name}' names={self.names} version_groups={self.version_groups}>"
        )
