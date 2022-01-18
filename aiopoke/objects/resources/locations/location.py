from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import GenerationGameIndex
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.locations import LocationArea, Region


class Location(NamedResource):
    areas: Tuple[MinimalResource["LocationArea"], ...]
    game_indices: Tuple["GenerationGameIndex", ...]
    region: MinimalResource["Region"]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.areas = tuple(MinimalResource(area_data) for area_data in data["areas"])
        self.game_indices = tuple(
            GenerationGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        )
        self.region = MinimalResource(data["region"])
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return f"<Location areas={self.areas} game_indices={self.game_indices} id_={self.id} region={self.region} name='{self.name}' names={self.names}>"
