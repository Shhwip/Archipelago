from ..items import AUGMENTATION_ITEMS, FILLER_ITEM
from ..locations import LOCATION_NAME_TO_ID, VICTORY_LOCATION
from .bases import BitburnerTestBase


class TestSourceGenesisGoal(BitburnerTestBase):
    options = {
        "goal": "source_genesis",
    }

    def test_itempool_fills_every_location(self) -> None:
        with self.subTest("Test that there is exactly one of each augmentation"):
            for augmentation in AUGMENTATION_ITEMS:
                self.assertEqual(len(self.get_items_by_name(augmentation)), 1)

        with self.subTest("Test that the itempool exactly fills the world's locations"):
            number_of_unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))
            self.assertEqual(len(self.multiworld.itempool), number_of_unfilled_locations)
            self.assertEqual(number_of_unfilled_locations, len(LOCATION_NAME_TO_ID))

        with self.subTest("Test that the shortfall is made up with filler"):
            # The augmentations do not quite fill the location list on their own, so the remainder
            # has to arrive as repeatable NeuroFlux Governor.
            expected_filler = len(LOCATION_NAME_TO_ID) - len(AUGMENTATION_ITEMS)
            self.assertEqual(len(self.get_items_by_name(FILLER_ITEM)), expected_filler)

    def test_victory_is_not_gated_on_items(self) -> None:
        # This world models nothing about what destroying BitNode 1 requires, so victory carries no
        # item requirement. When real logic arrives this test should be replaced, not deleted.
        self.assertTrue(self.world.get_location(VICTORY_LOCATION).can_reach(self.multiworld.state))


class TestAnyAugmentationGoal(BitburnerTestBase):
    options = {
        "goal": "any_augmentation",
    }

    def test_victory_needs_an_augmentation(self) -> None:
        victory = self.world.get_location(VICTORY_LOCATION)

        with self.subTest("Test that victory is unreachable with nothing"):
            self.assertFalse(victory.can_reach(self.multiworld.state))

        with self.subTest("Test that a single augmentation is enough"):
            self.collect_by_name(AUGMENTATION_ITEMS[0])
            self.assertTrue(victory.can_reach(self.multiworld.state))
