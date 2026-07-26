from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items, regions

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

# Faction membership, for the factions whose join is not already an achievement check.
#
# Seven factions -- CyberSec, NiteSec, The Black Hand, BitRunners, Daedalus, The Covenant and the
# Illuminati -- are omitted here because joining them is already an achievement above, and adding
# them again would mean two locations for one action.
FACTION_LOCATIONS = [
    "Join ECorp",
    "Join MegaCorp",
    "Join Bachman & Associates",
    "Join Blade Industries",
    "Join NWO",
    "Join Clarke Incorporated",
    "Join OmniTek Incorporated",
    "Join Four Sigma",
    "Join KuaiGong International",
    "Join Fulcrum Secret Technologies",
    "Join Aevum",
    "Join Chongqing",
    "Join Ishima",
    "Join New Tokyo",
    "Join Sector-12",
    "Join Volhaven",
    "Join Speakers for the Dead",
    "Join The Dark Army",
    "Join The Syndicate",
    "Join Silhouette",
    "Join Tetrads",
    "Join Slum Snakes",
    "Join Netburners",
    "Join Tian Di Hui",
    "Join Bladeburners",
    "Join Church of the Machine God",
    "Join Shadows of Anarchy",
]

# Buying a program from the darkweb with the 'buy' command.
#
# Every item the darkweb sells, in the order src/DarkWeb/DarkWebItems.ts lists them. Unlike acquiring
# the program -- which five of these already have an achievement check for -- this is specifically the
# purchase, so the client records it where the purchase happens rather than deriving it from whether
# the player owns the file. Owning a program says nothing about how it was obtained.
#
# A player who already has a program can still get its check: 'rm <program>.exe' deletes it, and it can
# then be bought. That is the only route for DarkscapeNavigator.exe if it was taken from the Shadowed
# Walkway, which bypasses the darkweb.
#
# None of these are gated by a BitNode or Source File, so all eleven are reachable in a first BN1 run
# with the TOR router and enough money.
DARKWEB_PURCHASE_LOCATIONS = [
    "Purchase BruteSSH.exe",
    "Purchase FTPCrack.exe",
    "Purchase relaySMTP.exe",
    "Purchase HTTPWorm.exe",
    "Purchase SQLInject.exe",
    "Purchase ServerProfiler.exe",
    "Purchase DeepscanV1.exe",
    "Purchase DeepscanV2.exe",
    "Purchase AutoLink.exe",
    "Purchase DarkscapeNavigator.exe",
    "Purchase Formulas.exe",
]

# IMPORTANT: As with items, IDs come from this order and must stay stable once seeds exist.
# Appended after the backdoors rather than interleaved, so earlier ids keep their values.
LOCATION_NAME_TO_ID = {
    name: items.BASE_ID + index
    for index, name in enumerate(
        [
            *ACHIEVEMENT_LOCATIONS,
            *BACKDOOR_LOCATIONS,
            *FACTION_LOCATIONS,
            *DARKWEB_PURCHASE_LOCATIONS,
        ]
    )
}

# Which server each backdoor check belongs to, and how many ports that server needs opened. This is
# what regions.py uses to sort the backdoors into port tiers.
BACKDOOR_PORT_REQUIREMENT = {
    "Backdoor n00dles": 0,
    "Backdoor foodnstuff": 0,
    "Backdoor sigma-cosmetics": 0,
    "Backdoor joesguns": 0,
    "Backdoor nectar-net": 0,
    "Backdoor hong-fang-tea": 0,
    "Backdoor harakiri-sushi": 0,
    "Backdoor zer0": 1,
    "Backdoor neo-net": 1,
    "Backdoor max-hardware": 1,
    "Backdoor iron-gym": 1,
    "Backdoor CSEC": 1,
    "Backdoor the-hub": 2,
    "Backdoor johnson-ortho": 2,
    "Backdoor silver-helix": 2,
    "Backdoor phantasy": 2,
    "Backdoor omega-net": 2,
    "Backdoor crush-fitness": 2,
    "Backdoor avmnite-02h": 2,
    "Backdoor rho-construction": 3,
    "Backdoor rothman-uni": 3,
    "Backdoor summit-uni": 3,
    "Backdoor catalyst": 3,
    "Backdoor computek": 3,
    "Backdoor netlink": 3,
    "Backdoor millenium-fitness": 3,
    "Backdoor I.I.I.I": 3,
    "Backdoor univ-energy": 4,
    "Backdoor zb-def": 4,
    "Backdoor applied-energetics": 4,
    "Backdoor global-pharm": 4,
    "Backdoor nova-med": 4,
    "Backdoor unitalife": 4,
    "Backdoor lexo-corp": 4,
    "Backdoor alpha-ent": 4,
    "Backdoor aevum-police": 4,
    "Backdoor syscore": 4,
    "Backdoor snap-fitness": 4,
    "Backdoor run4theh111z": 4,
    "Backdoor .": 4,
    "Backdoor ecorp": 5,
    "Backdoor megacorp": 5,
    "Backdoor b-and-a": 5,
    "Backdoor blade": 5,
    "Backdoor nwo": 5,
    "Backdoor clarkinc": 5,
    "Backdoor omnitek": 5,
    "Backdoor 4sigma": 5,
    "Backdoor kuai-gong": 5,
    "Backdoor fulcrumtech": 5,
    "Backdoor fulcrumassets": 5,
    "Backdoor stormtech": 5,
    "Backdoor defcomm": 5,
    "Backdoor infocomm": 5,
    "Backdoor helios": 5,
    "Backdoor vitalife": 5,
    "Backdoor icarus": 5,
    "Backdoor titan-labs": 5,
    "Backdoor microdyne": 5,
    "Backdoor taiyang-digital": 5,
    "Backdoor galactic-cyber": 5,
    "Backdoor aerocorp": 5,
    "Backdoor omnia": 5,
    "Backdoor solaris": 5,
    "Backdoor deltaone": 5,
    "Backdoor zeus-med": 5,
    "Backdoor zb-institute": 5,
    "Backdoor powerhouse-fitness": 5,
    "Backdoor The-Cave": 5,
    "Backdoor w0r1d_d43m0n": 5,
}

# Locations that only exist when their content option is enabled. A BitNode 1 run cannot reach any
# of this, so including it unconditionally would mean checks the player can never send.
CONTENT_LOCATIONS = {
    "gangs": [
        "Form a Gang",
        "Recruit All Gang Members",
        "Control All Gang Territory",
        "Train a Gang Member to 10,000 in a Skill",
    ],
    "corporations": [
        "Create a Corporation",
        "Lower Corporation Tribute by Lobbying",
        "Reach a 1000x Division Production Multiplier",
        "Employ 3000 in a Division",
        "Expand Into Real Estate",
    ],
    "bladeburner": [
        "Join the Bladeburner Division",
        "Max Out Bladeburner Overclock",
        "Bank 100,000 Bladeburner Skill Points",
        "Join Bladeburners",
    ],
    "sleeves": [
        "Acquire All 8 Sleeves",
    ],
    "hacknet_servers": [
        "Purchase Your First Hacknet Server",
        "Buy All Hacknet Servers",
        "Maximize a Hacknet Server",
        "Earn $1b From Hacknet Servers",
        "Cap Your Hashes",
    ],
    "staneks_gift": [
        "Join Church of the Machine God",
    ],
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


def get_disabled_locations(world: BitburnerWorld) -> set[str]:
    """Locations left out of this seed because their content option is off."""
    disabled: set[str] = set()

    for option_name, location_names in CONTENT_LOCATIONS.items():
        if not getattr(world.options, option_name):
            disabled.update(location_names)

    return disabled


def create_all_locations(world: BitburnerWorld) -> None:
    disabled = get_disabled_locations(world)
    bitnode = world.get_region(regions.ORIGIN_REGION)

    # Achievements, faction joins and darkweb purchases have no port requirement, so they sit in the
    # origin region. The purchases need the TOR router and money, neither of which is modelled.
    ungated = [
        name
        for name in (*ACHIEVEMENT_LOCATIONS, *FACTION_LOCATIONS, *DARKWEB_PURCHASE_LOCATIONS)
        if name not in disabled
    ]
    bitnode.add_locations({name: LOCATION_NAME_TO_ID[name] for name in ungated}, BitburnerLocation)

    # Backdoors go to the region for the number of ports their server needs.
    for name in BACKDOOR_LOCATIONS:
        region = world.get_region(regions.region_for_ports(BACKDOOR_PORT_REQUIREMENT[name]))
        region.add_locations({name: LOCATION_NAME_TO_ID[name]}, BitburnerLocation)

    bitnode.add_event(
        VICTORY_LOCATION,
        VICTORY_ITEM,
        location_type=BitburnerLocation,
        item_type=items.BitburnerItem,
    )
