from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Toggle


class Goal(Choice):
    """
    What finishes your run.

    Source Genesis: destroy BitNode 1 and acquire the SF1.1 achievement.
    """

    display_name = "Goal"

    option_source_genesis = 0

    default = option_source_genesis


# Content options.
#
# Each of these covers a Bitburner feature that a BitNode 1 run cannot reach at all, because it
# needs a source file from another BitNode. They default to off, so a plain BitNode 1 seed contains
# only checks the player can actually send.
#
# Enabling one adds both its checks and any augmentations exclusive to it, which is what keeps the
# item pool and the location list in step.


class Gangs(Toggle):
    """
    Include gang checks. Requires SF2, or a BitNode 2 run.
    """

    display_name = "Gangs"


class Corporations(Toggle):
    """
    Include corporation checks. Requires SF3, or a BitNode 3 run.
    """

    display_name = "Corporations"


class Bladeburner(Toggle):
    """
    Include Bladeburner checks and the Bladeburner augmentations.
    Requires SF6 or SF7, or a BitNode 6 or 7 run.
    """

    display_name = "Bladeburner"


class Sleeves(Toggle):
    """
    Include duplicate sleeve checks. Requires SF10, or a BitNode 10 run.
    """

    display_name = "Sleeves"


class HacknetServers(Toggle):
    """
    Include hacknet server checks. Requires SF9, or a BitNode 9 run.
    Note that hacknet servers replace hacknet nodes, so the hacknet node checks become unobtainable
    in a run where you have them.
    """

    display_name = "Hacknet Servers"


class StaneksGift(Toggle):
    """
    Include Church of the Machine God checks and Stanek's Gift augmentations.
    Requires SF13, or a BitNode 13 run.
    """

    display_name = "Stanek's Gift"


@dataclass
class BitburnerOptions(PerGameCommonOptions):
    goal: Goal
    gangs: Gangs
    corporations: Corporations
    bladeburner: Bladeburner
    sleeves: Sleeves
    hacknet_servers: HacknetServers
    staneks_gift: StaneksGift


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal],
    ),
    OptionGroup(
        "Content Options",
        [Gangs, Corporations, Bladeburner, Sleeves, HacknetServers, StaneksGift],
    ),
]
