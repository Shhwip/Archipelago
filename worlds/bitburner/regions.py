from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import BitburnerWorld

# A Bitburner run takes place inside a single BitNode, and this trivial world has no traversal logic
# at all — every check is reachable from the moment the save exists. So there is exactly one region,
# and it is the origin region (see BitburnerWorld.origin_region_name).
#
# Real logic — gating checks behind hacking skill, money, programs, or faction access — will mean
# splitting this into several regions with entrance rules between them.
ORIGIN_REGION = "BitNode"


def create_and_connect_regions(world: BitburnerWorld) -> None:
    bitnode = Region(ORIGIN_REGION, world.player, world.multiworld)
    world.multiworld.regions.append(bitnode)

    # With only the origin region there is nothing to connect yet.
