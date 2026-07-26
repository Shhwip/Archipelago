from ..items import AUGMENTATION_ITEMS
from ..locations import LOCATION_NAME_TO_ID, VICTORY_LOCATION
from .bases import BitburnerTestBase


class TestSourceGenesisGoal(BitburnerTestBase):
    options = {
        "goal": "source_genesis",
    }

    def test_every_augmentation_is_required_for_victory(self) -> None:
        # Checking each augmentation on its own, rather than all six in one call, is what proves
        # that every single one is actually required. A single call listing all six would still
        # pass if the goal rule had accidentally dropped one of them.
        for augmentation in AUGMENTATION_ITEMS:
            with self.subTest(f"Test that victory requires {augmentation}"):
                self.assertAccessDependency([VICTORY_LOCATION], [[augmentation]], only_check_listed=True)

    def test_itempool_matches_locations(self) -> None:
        with self.subTest("Test that there is exactly one of each augmentation"):
            for augmentation in AUGMENTATION_ITEMS:
                self.assertEqual(len(self.get_items_by_name(augmentation)), 1)

        with self.subTest("Test that the itempool exactly fills the world's locations"):
            number_of_unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))
            self.assertEqual(len(self.multiworld.itempool), number_of_unfilled_locations)

        with self.subTest("Test that the checks, but not the victory event, are the unfilled locations"):
            self.assertEqual(number_of_unfilled_locations, len(LOCATION_NAME_TO_ID))

    def test_augmentations_are_progression(self) -> None:
        # Every augmentation is named by the goal rule, so all of them must be progression.
        for augmentation in AUGMENTATION_ITEMS:
            with self.subTest(f"Test that {augmentation} is progression"):
                self.assertTrue(all(item.advancement for item in self.get_items_by_name(augmentation)))


class TestAnyAugmentationGoal(BitburnerTestBase):
    options = {
        "goal": "any_augmentation",
    }

    def test_a_single_augmentation_is_enough(self) -> None:
        # With this goal any one augmentation wins, so each of them is independently sufficient,
        # and having none of them must leave victory unreachable.
        self.assertAccessDependency(
            [VICTORY_LOCATION],
            [[augmentation] for augmentation in AUGMENTATION_ITEMS],
            only_check_listed=True,
        )
