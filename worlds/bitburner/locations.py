from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import BitburnerWorld

# Checks come from two sources, both of which the client derives from save state.
#
# Achievements. The comment on each line is the Bitburner achievement ID
# (src/Achievements/Achievements.ts) the client maps to it.
#
# Excluded are the secret achievements, which require exploiting or editing the game, the source
# file achievements for other BitNodes, and the challenge-run achievements. Several of those that
# remain need BitNode content that a BitNode 1 run cannot reach at all; they are here because the
# pool has to fill every location, and because that is a logic question this world does not model.
ACHIEVEMENT_LOCATIONS = [
    "Join CyberSec",  # CYBERSEC
    "Join NiteSec",  # NITESEC
    "Join The Black Hand",  # THE_BLACK_HAND
    "Join the BitRunners",  # BITRUNNERS
    "Join Daedalus",  # DAEDALUS
    "Join The Covenant",  # THE_COVENANT
    "Join the Illuminati",  # ILLUMINATI
    "Acquire BruteSSH.exe",  # BRUTESSH.EXE
    "Acquire FTPCrack.exe",  # FTPCRACK.EXE
    "Acquire relaySMTP.exe",  # RELAYSMTP.EXE
    "Acquire HTTPWorm.exe",  # HTTPWORM.EXE
    "Acquire SQLInject.exe",  # SQLINJECT.EXE
    "Acquire Formulas.exe",  # FORMULAS.EXE
    "Acquire Source Genesis",  # SF1.1
    "Hold $1Q",  # MONEY_1Q
    "Install Your First Augmentation",  # INSTALL_1
    "Install 100 Augmentations",  # INSTALL_100
    "Queue 40 Augmentations",  # QUEUE_40
    "Reach 100,000 Hacking Skill",  # HACKING_100000
    "Reach 3000 in All Combat Stats",  # COMBAT_3000
    "Install NeuroFlux Governor Level 255",  # NEUROFLUX_255
    "Write a .js Script",  # NS2
    "Freeze the Game With an Infinite Loop",  # FROZE
    "Run 1000 Scripts Simultaneously",  # RUNNING_SCRIPTS_1000
    "Drain a Server of All Its Money",  # DRAIN_SERVER
    "Maximize Home Computer RAM",  # MAX_RAM
    "Maximize Home Computer Cores",  # MAX_CORES
    "Keep 30 Scripts on Home",  # SCRIPTS_30
    "Make $1q on the Stock Market",  # STOCK_1q
    "Earn the Powerhouse Gym Discount",  # DISCOUNT
    "Write a 32GB Script",  # SCRIPT_32GB
    "Purchase Your First Hacknet Node",  # FIRST_HACKNET_NODE
    "Own 30 Hacknet Nodes",  # 30_HACKNET_NODE
    "Maximize a Hacknet Node",  # MAX_HACKNET_NODE
    "Earn $10m From Hacknet Nodes",  # HACKNET_NODE_10M
    "Reach 10m Faction Reputation",  # REPUTATION_10M
    "Unlock Faction Donations",  # DONATION
    "Travel to Another City",  # TRAVEL
    "Work Out at a Gym",  # WORKOUT
    "Purchase the TOR Router",  # TOR
    "Get Hospitalized",  # HOSPITALIZED
    "Form a Gang",  # GANG
    "Recruit All Gang Members",  # FULL_GANG
    "Control All Gang Territory",  # GANG_TERRITORY
    "Train a Gang Member to 10,000 in a Skill",  # GANG_MEMBER_POWER
    "Create a Corporation",  # CORPORATION
    "Lower Corporation Tribute by Lobbying",  # CORPORATION_BRIBE
    "Reach a 1000x Division Production Multiplier",  # CORPORATION_PROD_1000
    "Employ 3000 in a Division",  # CORPORATION_EMPLOYEE_3000
    "Expand Into Real Estate",  # CORPORATION_REAL_ESTATE
    "Reach Intelligence 255",  # INTELLIGENCE_255
    "Join the Bladeburner Division",  # BLADEBURNER_DIVISION
    "Max Out Bladeburner Overclock",  # BLADEBURNER_OVERCLOCK
    "Bank 100,000 Bladeburner Skill Points",  # BLADEBURNER_UNSPENT_100000
    "Purchase 4S Market Data",  # 4S
    "Purchase Your First Hacknet Server",  # FIRST_HACKNET_SERVER
    "Buy All Hacknet Servers",  # ALL_HACKNET_SERVER
    "Maximize a Hacknet Server",  # MAX_HACKNET_SERVER
    "Earn $1b From Hacknet Servers",  # HACKNET_SERVER_1B
    "Cap Your Hashes",  # MAX_CACHE
    "Acquire All 8 Sleeves",  # SLEEVE_8
    "Spend an Hour in the BitVerse",  # INDECISIVE
    "Destroy a BitNode in Under 2 Days",  # FAST_BN
    "Reach SF x.3 in Every BitNode",  # BN_DESTROYER
    "Get Ejected From an IPvGO Subnet",  # IPVGO_ANTICHEAT
    "Win 10 IPvGO Games in a Row",  # IPVGO_WINNING_STREAK
    "Backdoor 50 Darknet Servers at Once",  # DARKNET_BACKDOOR
    "Install the Augment From the Deepest Server",  # DARKNET_DEPTHS
]

# Backdoors, one per server in Bitburner's fixed server list (src/Server/data/servers.ts).
#
# Unlike achievements these are not permanent: installing augmentations resets every server, so a
# backdoor check cannot be re-derived afterwards. The client therefore persists which checks it has
# sent rather than recomputing them, which is what keeps them idempotent across a reset.
BACKDOOR_LOCATIONS = [
    "Backdoor ecorp",
    "Backdoor megacorp",
    "Backdoor b-and-a",
    "Backdoor blade",
    "Backdoor nwo",
    "Backdoor clarkinc",
    "Backdoor omnitek",
    "Backdoor 4sigma",
    "Backdoor kuai-gong",
    "Backdoor fulcrumtech",
    "Backdoor fulcrumassets",
    "Backdoor stormtech",
    "Backdoor defcomm",
    "Backdoor infocomm",
    "Backdoor helios",
    "Backdoor vitalife",
    "Backdoor icarus",
    "Backdoor univ-energy",
    "Backdoor titan-labs",
    "Backdoor microdyne",
    "Backdoor taiyang-digital",
    "Backdoor galactic-cyber",
    "Backdoor aerocorp",
    "Backdoor omnia",
    "Backdoor zb-def",
    "Backdoor applied-energetics",
    "Backdoor solaris",
    "Backdoor deltaone",
    "Backdoor global-pharm",
    "Backdoor nova-med",
    "Backdoor zeus-med",
    "Backdoor unitalife",
    "Backdoor lexo-corp",
    "Backdoor rho-construction",
    "Backdoor alpha-ent",
    "Backdoor aevum-police",
    "Backdoor rothman-uni",
    "Backdoor zb-institute",
    "Backdoor summit-uni",
    "Backdoor syscore",
    "Backdoor catalyst",
    "Backdoor the-hub",
    "Backdoor computek",
    "Backdoor netlink",
    "Backdoor johnson-ortho",
    "Backdoor n00dles",
    "Backdoor foodnstuff",
    "Backdoor sigma-cosmetics",
    "Backdoor joesguns",
    "Backdoor zer0",
    "Backdoor nectar-net",
    "Backdoor neo-net",
    "Backdoor silver-helix",
    "Backdoor hong-fang-tea",
    "Backdoor harakiri-sushi",
    "Backdoor phantasy",
    "Backdoor max-hardware",
    "Backdoor omega-net",
    "Backdoor crush-fitness",
    "Backdoor iron-gym",
    "Backdoor millenium-fitness",
    "Backdoor powerhouse-fitness",
    "Backdoor snap-fitness",
    "Backdoor run4theh111z",
    "Backdoor I.I.I.I",
    "Backdoor avmnite-02h",
    "Backdoor .",
    "Backdoor CSEC",
    "Backdoor The-Cave",
    "Backdoor w0r1d_d43m0n",
]

# IMPORTANT: As with items, IDs come from this order and must stay stable once seeds exist.
# Only ever append.
LOCATION_NAME_TO_ID = {
    name: items.BASE_ID + index for index, name in enumerate([*ACHIEVEMENT_LOCATIONS, *BACKDOOR_LOCATIONS])
}

# The event location/item pair that represents beating the world.
#
# This is not a real check and is never sent to the server as one; the client reports the goal with
# a StatusUpdate. Acquiring Source Genesis is also a location in its own right, so finishing the run
# both completes the goal and sends a check.
VICTORY_LOCATION = "Ascension"
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
