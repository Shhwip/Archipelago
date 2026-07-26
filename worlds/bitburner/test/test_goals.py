from ..items import FILLER_ITEM, PROGRAM_ITEMS, get_enabled_augmentations
from ..locations import VICTORY_LOCATION
from .bases import BitburnerTestBase


class TestSourceGenesisGoal(BitburnerTestBase):
    options = {
        "goal": "source_genesis",
    }

    def test_itempool_fills_every_location(self) -> None:
        with self.subTest("Test that there is exactly one of each enabled augmentation"):
            for augmentation in get_enabled_augmentations(self.world):
                self.assertEqual(len(self.get_items_by_name(augmentation)), 1)

        with self.subTest("Test that there is exactly one of each program"):
            for program in PROGRAM_ITEMS:
                self.assertEqual(len(self.get_items_by_name(program)), 1)

        with self.subTest("Test that the itempool exactly fills the world's locations"):
            self.assertEqual(
                len(self.multiworld.itempool),
                len(self.multiworld.get_unfilled_locations(self.player)),
            )

        with self.subTest("Test that the shortfall is made up with filler"):
            # There are far more locations than augmentations now that backdoors and factions are
            # checks, so filler is doing real work rather than covering a rounding error.
            self.assertGreater(len(self.get_items_by_name(FILLER_ITEM)), 0)

    def test_victory_needs_every_port_open(self) -> None:
        victory = self.world.get_location(VICTORY_LOCATION)

        with self.subTest("Test that victory is unreachable with no programs"):
            self.assertFalse(victory.can_reach(self.multiworld.state))

        with self.subTest("Test that four programs are not enough"):
            for program in PROGRAM_ITEMS[:4]:
                self.collect_by_name(program)
            self.assertFalse(victory.can_reach(self.multiworld.state))

        with self.subTest("Test that the fifth program opens the way"):
            # w0r1d_d43m0n needs all five ports, so this is the floor for destroying BitNode 1.
            self.collect_by_name(PROGRAM_ITEMS[4])
            self.assertTrue(victory.can_reach(self.multiworld.state))


class TestAnyAugmentationGoal(BitburnerTestBase):
    options = {
        "goal": "any_augmentation",
    }

    def test_victory_needs_an_augmentation(self) -> None:
        victory = self.world.get_location(VICTORY_LOCATION)

        with self.subTest("Test that victory is unreachable with nothing"):
            self.assertFalse(victory.can_reach(self.multiworld.state))

        with self.subTest("Test that a single augmentation is enough"):
            self.collect_by_name(get_enabled_augmentations(self.world)[0])
            self.assertTrue(victory.can_reach(self.multiworld.state))
