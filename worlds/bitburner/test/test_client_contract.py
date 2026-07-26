from ..items import AUGMENTATION_ITEMS, BASE_ID, FILLER_ITEM, ITEM_NAME_TO_ID, PROGRAM_ITEMS
from ..locations import (
    ACHIEVEMENT_LOCATIONS,
    BACKDOOR_LOCATIONS,
    BACKDOOR_PORT_REQUIREMENT,
    FACTION_LOCATIONS,
    GOAL_ACHIEVEMENT,
    LOCATION_NAME_TO_ID,
    VICTORY_LOCATION,
)
from .bases import BitburnerTestBase

# The client hardcodes these names in src/Archipelago/Data.ts, and the IDs are baked into every
# generated seed. The full lists are not repeated here -- that would just be a second copy to keep
# in step -- but their sizes and boundaries are pinned, which is what catches an accidental reorder
# or a dropped entry.
#
# Appending to either list is expected: update the counts here to match. Anything that changes an
# existing entry's position is not, and breaks seeds that already exist.
EXPECTED_ACHIEVEMENT_COUNT = 68
EXPECTED_BACKDOOR_COUNT = 70
EXPECTED_FACTION_COUNT = 27
EXPECTED_AUGMENTATION_COUNT = 136
EXPECTED_PROGRAM_COUNT = 5


class TestClientContract(BitburnerTestBase):
    # A pure data check that does not depend on options, so the generic tests would just be a slower
    # repeat of the ones the goal tests already run on default options.
    run_default_tests = False

    def test_list_sizes(self) -> None:
        self.assertEqual(len(ACHIEVEMENT_LOCATIONS), EXPECTED_ACHIEVEMENT_COUNT)
        self.assertEqual(len(BACKDOOR_LOCATIONS), EXPECTED_BACKDOOR_COUNT)
        self.assertEqual(len(FACTION_LOCATIONS), EXPECTED_FACTION_COUNT)
        self.assertEqual(len(AUGMENTATION_ITEMS), EXPECTED_AUGMENTATION_COUNT)
        self.assertEqual(len(PROGRAM_ITEMS), EXPECTED_PROGRAM_COUNT)

    def test_names_are_unique(self) -> None:
        # A duplicate name would silently collapse two entries into one ID. This is the check that
        # catches a faction join being added when an achievement already covers it.
        with self.subTest("locations"):
            expected = EXPECTED_ACHIEVEMENT_COUNT + EXPECTED_BACKDOOR_COUNT + EXPECTED_FACTION_COUNT
            self.assertEqual(len(LOCATION_NAME_TO_ID), expected)

        with self.subTest("items"):
            self.assertEqual(len(ITEM_NAME_TO_ID), EXPECTED_AUGMENTATION_COUNT + EXPECTED_PROGRAM_COUNT + 1)
            self.assertNotIn(FILLER_ITEM, AUGMENTATION_ITEMS)

    def test_every_backdoor_has_a_port_requirement(self) -> None:
        # regions.py sorts backdoors into tiers by this table, so a missing entry would KeyError
        # during generation rather than fail here.
        self.assertEqual(set(BACKDOOR_PORT_REQUIREMENT), set(BACKDOOR_LOCATIONS))
        for name, ports in BACKDOOR_PORT_REQUIREMENT.items():
            with self.subTest(name):
                self.assertIn(ports, range(0, 6))

    def test_ids_are_contiguous_from_base(self) -> None:
        # IDs come from list order, so this pins the ordering as a whole.
        self.assertEqual(sorted(LOCATION_NAME_TO_ID.values()), list(range(BASE_ID, BASE_ID + len(LOCATION_NAME_TO_ID))))
        self.assertEqual(sorted(ITEM_NAME_TO_ID.values()), list(range(BASE_ID, BASE_ID + len(ITEM_NAME_TO_ID))))

    def test_anchor_ids_are_stable(self) -> None:
        # Spot-checks at both ends of each list, so a reorder that preserved the count still fails.
        anchors = {
            "Join CyberSec": BASE_ID,
            "Acquire Source Genesis": BASE_ID + 13,
            "Backdoor ecorp": BASE_ID + EXPECTED_ACHIEVEMENT_COUNT,
            "Backdoor w0r1d_d43m0n": BASE_ID + EXPECTED_ACHIEVEMENT_COUNT + EXPECTED_BACKDOOR_COUNT - 1,
        }
        for name, expected_id in anchors.items():
            with self.subTest(name):
                self.assertEqual(LOCATION_NAME_TO_ID[name], expected_id)

        self.assertEqual(ITEM_NAME_TO_ID["Augmented Targeting I"], BASE_ID)
        self.assertEqual(ITEM_NAME_TO_ID[FILLER_ITEM], BASE_ID + EXPECTED_AUGMENTATION_COUNT)
        # Programs were appended after the filler precisely so the ids above did not move.
        self.assertEqual(ITEM_NAME_TO_ID["BruteSSH.exe"], BASE_ID + EXPECTED_AUGMENTATION_COUNT + 1)

    def test_source_genesis_is_both_a_check_and_the_goal(self) -> None:
        # SF1.1 is now a real check as well as the goal trigger, so finishing the run sends a check
        # and completes the goal. The victory event is separate and must not collide with it.
        self.assertEqual(GOAL_ACHIEVEMENT, "SF1.1")
        self.assertIn("Acquire Source Genesis", LOCATION_NAME_TO_ID)
        self.assertNotIn(VICTORY_LOCATION, LOCATION_NAME_TO_ID)
