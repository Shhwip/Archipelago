from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAny, HasFromListUnique

from . import items, locations, regions
from .options import Goal

if TYPE_CHECKING:
    from .world import BitburnerWorld


def set_all_rules(world: BitburnerWorld) -> None:
    set_all_entrance_rules(world)
    set_victory_rule(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: BitburnerWorld) -> None:
    """Gates each port tier behind holding that many port-opener programs.

    Each program opens exactly one port and they are not interchangeable duplicates, so reaching a
    server that demands three ports means holding any three distinct programs. HasFromListUnique is
    what expresses "any N of these", rather than naming a particular combination.

    The locations inside a tier need no rule of their own: a location implicitly requires its own
    region, so the entrance rule already covers them.
    """
    for ports in range(1, regions.MAX_PORTS + 1):
        entrance = world.get_entrance(regions.entrance_for_ports(ports))
        world.set_rule(entrance, HasFromListUnique(*items.PROGRAM_ITEMS, count=ports))


def set_victory_rule(world: BitburnerWorld) -> None:
    if world.options.goal == Goal.option_any_augmentation:
        # Only the augmentations actually in this seed's pool can be required.
        world.set_rule(
            world.get_location(locations.VICTORY_LOCATION),
            HasAny(*items.get_enabled_augmentations(world)),
        )
        return

    # Source Genesis means backdooring w0r1d_d43m0n, which needs all five ports open. That is a real
    # requirement rather than a guess, so unlike the previous version this goal is now gated.
    #
    # It is still not the whole story: destroying BitNode 1 also needs the hacking skill to actually
    # breach the server, and skill is not modelled. Treat this as the floor, not the full condition.
    world.set_rule(
        world.get_location(locations.VICTORY_LOCATION),
        HasFromListUnique(*items.PROGRAM_ITEMS, count=regions.MAX_PORTS),
    )


def set_completion_condition(world: BitburnerWorld) -> None:
    world.set_completion_rule(Has(locations.VICTORY_ITEM))
