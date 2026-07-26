from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import BitburnerWorld

# Regions model the one thing in Bitburner that gates access discretely: open ports.
#
# Backdooring a server needs root, root needs NUKE, and NUKE needs as many open ports as the server
# demands. Each port-opener program opens exactly one port, so a server needing three ports needs
# any three of the five programs. That maps directly onto a region per port requirement.
#
# Servers needing no ports live in the origin region, since nothing gates them.
#
# The other axis, required hacking skill, is deliberately not modelled. It is grindable rather than
# unlockable, so it is soft logic, and nothing in the item pool represents it yet.
ORIGIN_REGION = "BitNode"

MAX_PORTS = 5


def region_for_ports(ports: int) -> str:
    return ORIGIN_REGION if ports == 0 else f"Port Tier {ports}"


def entrance_for_ports(ports: int) -> str:
    return f"Open {ports} Ports"


def create_and_connect_regions(world: BitburnerWorld) -> None:
    bitnode = Region(ORIGIN_REGION, world.player, world.multiworld)
    world.multiworld.regions.append(bitnode)

    # Each tier hangs directly off the origin rather than off the tier below it. Needing three ports
    # does not mean passing through the two-port servers, it just means holding three programs.
    for ports in range(1, MAX_PORTS + 1):
        tier = Region(region_for_ports(ports), world.player, world.multiworld)
        world.multiworld.regions.append(tier)
        bitnode.connect(tier, entrance_for_ports(ports))
