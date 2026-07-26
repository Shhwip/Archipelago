import itertools
import unittest

from ..items import (
    AUGMENTATION_ITEMS,
    BLADEBURNER_AUGMENTATIONS,
    PROGRAM_ITEMS,
    STANEK_AUGMENTATIONS,
)
from ..locations import (
    ACHIEVEMENT_LOCATIONS,
    BACKDOOR_LOCATIONS,
    BACKDOOR_PORT_REQUIREMENT,
    CONTENT_LOCATIONS,
    DARKWEB_PURCHASE_LOCATIONS,
    FACTION_LOCATIONS,
    PROGRAM_CREATION_LOCATIONS,
)
from .bases import BitburnerTestBase


def backdoors_needing(ports: int) -> list[str]:
    return [name for name, required in BACKDOOR_PORT_REQUIREMENT.items() if required == ports]


class TestPortLogic(BitburnerTestBase):
    options = {
        "goal": "source_genesis",
    }

    def test_unported_backdoors_are_free(self) -> None:
        # Seven servers need no ports at all. If these were gated the seed would have an empty
        # sphere one, so this doubles as a check that the player always has somewhere to start.
        for name in backdoors_needing(0):
            with self.subTest(name):
                self.assertTrue(self.world.get_location(name).can_reach(self.multiworld.state))

    def test_ported_backdoors_start_locked(self) -> None:
        for ports in range(1, 6):
            name = backdoors_needing(ports)[0]
            with self.subTest(f"{ports} ports: {name}"):
                self.assertFalse(self.world.get_location(name).can_reach(self.multiworld.state))

    def test_each_program_opens_the_next_tier(self) -> None:
        # Programs are interchangeable: what matters is how many you hold, not which. Collecting
        # them in order should unlock the tiers in order.
        for held, program in enumerate(PROGRAM_ITEMS, start=1):
            self.collect_by_name(program)

            with self.subTest(f"{held} programs unlocks tier {held}"):
                for name in backdoors_needing(held):
                    self.assertTrue(self.world.get_location(name).can_reach(self.multiworld.state))

            if held < 5:
                with self.subTest(f"{held} programs does not unlock tier {held + 1}"):
                    for name in backdoors_needing(held + 1):
                        self.assertFalse(self.world.get_location(name).can_reach(self.multiworld.state))


class TestContentOptions(BitburnerTestBase):
    options = {
        "bladeburner": True,
    }

    def test_enabling_content_adds_its_checks_and_items(self) -> None:
        # The point of the content toggles is that checks and items move together, so that enabling
        # a feature cannot leave the pool the wrong size.
        with self.subTest("Bladeburner checks exist"):
            self.world.get_location("Join the Bladeburner Division")
            self.world.get_location("Join Bladeburners")

        with self.subTest("Bladeburner augmentations are in the pool"):
            self.assertEqual(len(self.get_items_by_name("The Blade's Simulacrum")), 1)

        with self.subTest("Disabled content is still absent"):
            self.assertRaises(KeyError, self.world.get_location, "Form a Gang")
            self.assertEqual(len(self.get_items_by_name("Stanek's Gift - Genesis")), 0)


class TestItemBudget(unittest.TestCase):
    """The pool must never be larger than the locations it has to fill.

    Archipelago requires the two to be exactly equal, and the shortfall is made up with filler --
    but filler only absorbs surplus *locations*. Surplus items cannot be placed at all, and the
    failure surfaces as a generation error rather than anything readable. Content toggles move both
    sides at once, so every combination needs checking, not just the default.

    Plain arithmetic rather than a generated world per combination, so all 64 stay cheap.
    """

    CONTENT_AUGMENTATIONS = {
        "bladeburner": BLADEBURNER_AUGMENTATIONS,
        "staneks_gift": STANEK_AUGMENTATIONS,
    }

    def test_every_content_combination_fits(self) -> None:
        toggles = sorted(CONTENT_LOCATIONS)

        for enabled_flags in itertools.product([False, True], repeat=len(toggles)):
            enabled = {name for name, on in zip(toggles, enabled_flags) if on}

            locations = (
                len(ACHIEVEMENT_LOCATIONS)
                + len(BACKDOOR_LOCATIONS)
                + len(FACTION_LOCATIONS)
                + len(DARKWEB_PURCHASE_LOCATIONS)
                + len(PROGRAM_CREATION_LOCATIONS)
            )
            for toggle, names in CONTENT_LOCATIONS.items():
                if toggle not in enabled:
                    locations -= len(names)

            items = len(PROGRAM_ITEMS) + len(AUGMENTATION_ITEMS)
            for toggle, names in self.CONTENT_AUGMENTATIONS.items():
                if toggle not in enabled:
                    items -= len(names)

            with self.subTest(enabled=",".join(sorted(enabled)) or "none"):
                self.assertLessEqual(items, locations)


class TestContentDisabledByDefault(BitburnerTestBase):
    run_default_tests = False

    def test_bitnode_locked_content_is_absent(self) -> None:
        # A plain BitNode 1 seed should contain only checks the player can actually send.
        for name in ["Form a Gang", "Create a Corporation", "Acquire All 8 Sleeves", "Cap Your Hashes"]:
            with self.subTest(name):
                self.assertRaises(KeyError, self.world.get_location, name)
