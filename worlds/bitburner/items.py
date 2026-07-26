from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BitburnerWorld

# Item and location IDs share this base. IDs only need to be unique within a game, so items and
# locations are free to overlap; the offset just makes Bitburner IDs recognisable in server logs.
BASE_ID = 0xB17B00

# Every augmentation in the game, named exactly as Bitburner names it (src/Augmentation/Enums.ts).
# Matching the in-game name means the client's item -> augmentation table is an identity mapping.
#
# NeuroFlux Governor is deliberately absent: it is the filler item below, because it is the only
# augmentation that stacks rather than being rejected as already owned.
#
# Some of these are inert in a BitNode 1 run (Bladeburner, Stanek's Gift, SoA). They are included
# because the item pool has to fill every location, and because which BitNode content is reachable
# is a logic question this world does not model yet.
#
# IMPORTANT: IDs are derived from this list's order, and item IDs must stay stable across releases
# once seeds exist in the wild. Only ever append to this list; never reorder or remove.
AUGMENTATION_ITEMS = [
    "Augmented Targeting I",
    "Augmented Targeting II",
    "Augmented Targeting III",
    "Synthetic Heart",
    "Synfibril Muscle",
    "Combat Rib I",
    "Combat Rib II",
    "Combat Rib III",
    "Nanofiber Weave",
    "NEMEAN Subdermal Weave",
    "Wired Reflexes",
    "Graphene Bone Lacings",
    "Bionic Spine",
    "Graphene Bionic Spine Upgrade",
    "Bionic Legs",
    "Graphene Bionic Legs Upgrade",
    "Speech Processor Implant",
    "TITN-41 Gene-Modification Injection",
    "Enhanced Social Interaction Implant",
    "BitWire",
    "Artificial Bio-neural Network Implant",
    "Artificial Synaptic Potentiation",
    "Enhanced Myelin Sheathing",
    "Synaptic Enhancement Implant",
    "Neural-Retention Enhancement",
    "DataJack",
    "Embedded Netburner Module",
    "Embedded Netburner Module Core Implant",
    "Embedded Netburner Module Core V2 Upgrade",
    "Embedded Netburner Module Core V3 Upgrade",
    "Embedded Netburner Module Analyze Engine",
    "Embedded Netburner Module Direct Memory Access Upgrade",
    "Neuralstimulator",
    "Neural Accelerator",
    "Cranial Signal Processors - Gen I",
    "Cranial Signal Processors - Gen II",
    "Cranial Signal Processors - Gen III",
    "Cranial Signal Processors - Gen IV",
    "Cranial Signal Processors - Gen V",
    "Neuronal Densification",
    "Neuroreceptor Management Implant",
    "Nuoptimal Nootropic Injector Implant",
    "Speech Enhancement",
    "FocusWire",
    "PC Direct-Neural Interface",
    "PC Direct-Neural Interface Optimization Submodule",
    "PC Direct-Neural Interface NeuroNet Injector",
    "PCMatrix",
    "ADR-V1 Pheromone Gene",
    "ADR-V2 Pheromone Gene",
    "The Shadow's Simulacrum",
    "Hacknet Node CPU Architecture Neural-Upload",
    "Hacknet Node Cache Architecture Neural-Upload",
    "Hacknet Node NIC Architecture Neural-Upload",
    "Hacknet Node Kernel Direct-Neural Interface",
    "Hacknet Node Core Direct-Neural Interface",
    "Neurotrainer I",
    "Neurotrainer II",
    "Neurotrainer III",
    "HyperSight Corneal Implant",
    "LuminCloaking-V1 Skin Implant",
    "LuminCloaking-V2 Skin Implant",
    "HemoRecirculator",
    "SmartSonar Implant",
    "Power Recirculation Core",
    "QLink",
    "The Red Pill",
    "SPTN-97 Gene Modification",
    "ECorp HVMind Implant",
    "CordiARC Fusion Reactor",
    "SmartJaw",
    "Neotra",
    "Xanipher",
    "nextSENS Gene Modification",
    "OmniTek InfoLoad",
    "Photosynthetic Cells",
    "BitRunners Neurolink",
    "The Black Hand",
    "Unstable Circadian Modulator",
    "CRTX42-AA Gene Modification",
    "Neuregen Gene Modification",
    "CashRoot Starter Kit",
    "NutriGen Implant",
    "INFRARET Enhancement",
    "DermaForce Particle Barrier",
    "Graphene BrachiBlades Upgrade",
    "Graphene Bionic Arms Upgrade",
    "BrachiBlades",
    "Bionic Arms",
    "Social Negotiation Assistant (S.N.A)",
    "violet Congruity Implant",
    "Hydroflame Left Arm",
    "BigD's Big ... Brain",
    "Z.O.Ë.",
    "Eloquence Module",
    "Golden Tongue Module",
    "Glibness Enhancement",
    "Magnetism Amplifier",
    "The Illustrated Primer",
    "Social Dynamics Processor",
    "Neural Wit Amplifier",
    "EsperTech Bladeburner Eyewear",
    "EMS-4 Recombination",
    "ORION-MKIV Shoulder",
    "Hyperion Plasma Cannon V1",
    "Hyperion Plasma Cannon V2",
    "GOLEM Serum",
    "Vangelis Virus",
    "Vangelis Virus 3.0",
    "I.N.T.E.R.L.I.N.K.E.D",
    "Blade's Runners",
    "BLADE-51b Tesla Armor",
    "BLADE-51b Tesla Armor: Power Cells Upgrade",
    "BLADE-51b Tesla Armor: Energy Shielding Upgrade",
    "BLADE-51b Tesla Armor: Unibeam Upgrade",
    "BLADE-51b Tesla Armor: Omnibeam Upgrade",
    "BLADE-51b Tesla Armor: IPU Upgrade",
    "The Blade's Simulacrum",
    "Stanek's Gift - Genesis",
    "Stanek's Gift - Awakening",
    "Stanek's Gift - Serenity",
    "The W1ngs of Icarus",
    "The B00ts of Perseus",
    "The St4ff of Asclepius",
    "The H4mmer of Daedalus",
    "The L4w of Bayes",
    "The B1ade of Solomonoff",
    "SoA - Might of Ares",
    "SoA - Wisdom of Athena",
    "SoA - Trickery of Hermes",
    "SoA - Beauty of Aphrodite",
    "SoA - Chaos of Dionysus",
    "SoA - Flood of Poseidon",
    "SoA - Hunt of Artemis",
    "SoA - Knowledge of Apollo",
    "SoA - phyzical WKS harmonizer",
]

# AP needs one item it can create an unlimited number of, for item links and start inventory, and to
# top the pool up to the location count. NeuroFlux Governor is the natural pick: it is the one
# Bitburner augmentation that is genuinely repeatable, gaining a level on each grant.
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
    # No rule references any specific augmentation yet, so nothing has to be progression for the
    # generator to be correct. They are marked progression anyway so that fill spreads them across
    # spheres and progression balancing treats them as worth reaching, rather than dumping the whole
    # pool into late locations. Revisit once real logic exists.
    classification = ItemClassification.filler if name == FILLER_ITEM else ItemClassification.progression
    return BitburnerItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: BitburnerWorld) -> None:
    itempool: list[Item] = [world.create_item(name) for name in AUGMENTATION_ITEMS]

    # get_unfilled_locations is what we want rather than get_locations: the victory event is a
    # location too, but it already has its item and must not be counted here.
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
