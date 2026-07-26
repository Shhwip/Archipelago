from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as bitburner_options  # renamed to avoid clashing with World.options


class BitburnerWorld(World):
    """
    Bitburner is an incremental programming game where you write JavaScript to hack servers,
    climb factions, and buy the augmentations that let you reset into a stronger run.
    """

    game = "Bitburner"

    web = web_world.BitburnerWebWorld()

    options_dataclass = bitburner_options.BitburnerOptions
    options: bitburner_options.BitburnerOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    item_name_groups = items.ITEM_NAME_GROUPS

    origin_region_name = regions.ORIGIN_REGION

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BitburnerItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # The client needs the goal to know when to send its StatusUpdate.
        return self.options.as_dict("goal")
