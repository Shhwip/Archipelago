from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BitburnerWorld

# Item and location IDs share this base. IDs only need to be unique within a game, so items and
# locations are free to overlap; the offset just makes Bitburner IDs recognisable in server logs.
BASE_ID = 0xB17B00

# Every item is an augmentation, named exactly as Bitburner names it (src/Augmentation/Enums.ts).
# Matching the in-game name means the client's item -> augmentation table is an identity mapping
# for everything except deliberate exceptions.
#
# All six are cheap, non-special augmentations whose only effect is a stat multiplier, so granting
# one is immediately visible on the character overview and cannot alter game state in surprising ways.
#
# IMPORTANT: IDs are derived from this list's order, and item IDs must stay stable across releases
# once seeds exist in the wild. Only ever append to this list; never reorder or remove.
AUGMENTATION_ITEMS = [
    "BitWire",
    "Combat Rib I",
    "Neurotrainer I",
    "Nuoptimal Nootropic Injector Implant",
    "Speech Processor Implant",
    "Synaptic Enhancement Implant",
]

# AP needs one item it can create an unlimited number of, for item links and start inventory.
# NeuroFlux Governor is the natural pick: it is the one Bitburner augmentation that is genuinely
# repeatable, gaining a level on each purchase rather than being rejected as already-owned.
FILLER_ITEM = "NeuroFlux Governor"

ITEM_NAME_TO_ID = {name: BASE_ID + index for index, name in enumerate([*AUGMENTATION_ITEMS, FILLER_ITEM])}

# Item groups let players write "!hint augmentations" and let other worlds reference our items.
ITEM_NAME_GROUPS = {
    "Augmentations": {*AUGMENTATION_ITEMS, FILLER_ITEM},
}


class BitburnerItem(Item):
    game = "Bitburner"


def get_filler_item_name(world: BitburnerWorld) -> str:
    return FILLER_ITEM


def create_item_with_correct_classification(world: BitburnerWorld, name: str) -> BitburnerItem:
    # Every augmentation in the pool is named by the goal rule in rules.py, and anything a rule
    # references must be progression. NeuroFlux Governor is never referenced, so it stays filler.
    classification = ItemClassification.filler if name == FILLER_ITEM else ItemClassification.progression
    return BitburnerItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: BitburnerWorld) -> None:
    # One of each augmentation. With the current location list this exactly fills the world, but the
    # filler top-up below keeps the counts correct if either list changes.
    itempool: list[Item] = [world.create_item(name) for name in AUGMENTATION_ITEMS]

    # get_unfilled_locations is what we want rather than get_locations: the victory event is a
    # location too, but it already has its item and must not be counted here.
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
