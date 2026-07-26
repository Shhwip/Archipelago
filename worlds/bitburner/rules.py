from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, HasAny, Rule

from . import items, locations
from .options import Goal

if TYPE_CHECKING:
    from .world import BitburnerWorld

# This world is deliberately trivial: none of the six checks is gated behind anything, so there are
# no entrance rules and no location rules. The only rule is the one that decides when the run is won.


def set_all_rules(world: BitburnerWorld) -> None:
    set_victory_rule(world)
    set_completion_condition(world)


def set_victory_rule(world: BitburnerWorld) -> None:
    # Both branches name every augmentation, which is why all of them are progression items.
    goal_rule: Rule[BitburnerWorld]
    if world.options.goal == Goal.option_any_augmentation:
        goal_rule = HasAny(*items.AUGMENTATION_ITEMS)
    else:
        # Placeholder logic for destroying BitNode 1. Nothing about six cheap augmentations really
        # gates the Bitverse, but requiring all of them keeps the seed from being beatable before
        # any items are received, and keeps every augmentation a progression item.
        # Replace this with real requirements once the world grows past the trivial stage.
        goal_rule = HasAll(*items.AUGMENTATION_ITEMS)

    world.set_rule(world.get_location(locations.VICTORY_LOCATION), goal_rule)


def set_completion_condition(world: BitburnerWorld) -> None:
    # The run is won once the Victory event is reachable, which set_victory_rule defines above.
    world.set_completion_rule(Has(locations.VICTORY_ITEM))
