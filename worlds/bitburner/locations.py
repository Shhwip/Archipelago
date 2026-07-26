from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import BitburnerWorld

# Every check is a Bitburner achievement. The client watches for the achievement being earned and
# sends the matching location.
#
# These six are the achievements that are reachable within the first few minutes of a fresh save,
# which is what makes them suitable for a trivial world: a whole seed can be swept quickly by hand.
# The comment on each line is the Bitburner achievement ID (src/Achievements/Achievements.ts) that
# the client maps to it — the client's ACHIEVEMENT_TO_LOCATION table must agree with this list.
#
# IMPORTANT: As with items, IDs come from this dict's insertion order and must stay stable once
# seeds exist. Only ever append.
LOCATION_NAME_TO_ID = {
    name: items.BASE_ID + index
    for index, name in enumerate(
        [
            "Purchase Your First Hacknet Node",  # FIRST_HACKNET_NODE
            "Purchase the TOR Router",  # TOR
            "Work Out at a Gym",  # WORKOUT
            "Travel to Another City",  # TRAVEL
            "Get Hospitalized",  # HOSPITALIZED
            "Write a .js Script",  # NS2
        ]
    )
}

# The event location/item pair that represents beating the world.
#
# This is not a real check and is never sent to the server as one. It exists so generation knows
# what the run requires; the client is what decides the goal is met and sends the StatusUpdate.
#
# The goal is the SF1.1 achievement, whose in-game name is "Source Genesis" and whose condition is
# Player.sourceFileLvl(1) >= 1 — that is, destroying BitNode 1. The alternative testing goal in
# options.py is satisfied by receiving an augmentation instead, and needs no achievement.
VICTORY_LOCATION = "Source Genesis"
VICTORY_ITEM = "Victory"

# The Bitburner achievement the client watches to decide the default goal is complete.
GOAL_ACHIEVEMENT = "SF1.1"


class BitburnerLocation(Location):
    game = "Bitburner"


def create_all_locations(world: BitburnerWorld) -> None:
    bitnode = world.get_region("BitNode")

    bitnode.add_locations(LOCATION_NAME_TO_ID, BitburnerLocation)

    bitnode.add_event(
        VICTORY_LOCATION,
        VICTORY_ITEM,
        location_type=BitburnerLocation,
        item_type=items.BitburnerItem,
    )
