from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAny

from . import items, locations
from .options import Goal

if TYPE_CHECKING:
    from .world import BitburnerWorld

# This world has no traversal or access logic yet: every check sits in the single origin region with
# nothing gating it. The only rule here is the one that decides when the run is won.


def set_all_rules(world: BitburnerWorld) -> None:
    set_victory_rule(world)
    set_completion_condition(world)


def set_victory_rule(world: BitburnerWorld) -> None:
    if world.options.goal == Goal.option_any_augmentation:
        # Naming every augmentation is what makes this goal meaningful to the generator.
        world.set_rule(world.get_location(locations.VICTORY_LOCATION), HasAny(*items.AUGMENTATION_ITEMS))
        return

    # Source Genesis deliberately carries no item requirement.
    #
    # What actually gates destroying BitNode 1 is in-game progress - hacking skill, money, programs,
    # faction access - none of which this world models yet. The earlier version required every
    # augmentation, which stopped being defensible once the pool grew to the full 136: many of them
    # sit behind BitNode content a BitNode 1 run cannot reach, so that rule would have described
    # seeds the player could never actually finish.
    #
    # Leaving it unconditional means the generator treats the run as winnable from sphere 0. That is
    # the honest description of a world with no logic, and it is what the logic pass has to replace.


def set_completion_condition(world: BitburnerWorld) -> None:
    world.set_completion_rule(Has(locations.VICTORY_ITEM))
