from ..items import BASE_ID, ITEM_NAME_TO_ID
from ..locations import GOAL_ACHIEVEMENT, LOCATION_NAME_TO_ID
from .bases import BitburnerTestBase

# The Bitburner client hardcodes these names in src/Archipelago/Data.ts, and IDs are baked into
# every generated seed. Renaming or reordering either table silently desyncs the client, or breaks
# seeds that already exist, so both are pinned here deliberately.
#
# Adding a new entry to the end of one of these lists is expected and fine — update the list here
# to match. Changing the position of an existing entry is not.
EXPECTED_ITEM_ORDER = [
    "BitWire",
    "Combat Rib I",
    "Neurotrainer I",
    "Nuoptimal Nootropic Injector Implant",
    "Speech Processor Implant",
    "Synaptic Enhancement Implant",
    "NeuroFlux Governor",
]

EXPECTED_LOCATION_ORDER = [
    "Purchase Your First Hacknet Node",
    "Purchase the TOR Router",
    "Work Out at a Gym",
    "Travel to Another City",
    "Get Hospitalized",
    "Write a .js Script",
]


class TestClientContract(BitburnerTestBase):
    # This is a pure data check that doesn't depend on options, so the generic tests would just be
    # a slower repeat of the ones the goal tests already run on default options.
    run_default_tests = False

    def test_item_ids_are_stable(self) -> None:
        expected = {name: BASE_ID + index for index, name in enumerate(EXPECTED_ITEM_ORDER)}
        self.assertEqual(ITEM_NAME_TO_ID, expected)

    def test_location_ids_are_stable(self) -> None:
        expected = {name: BASE_ID + index for index, name in enumerate(EXPECTED_LOCATION_ORDER)}
        self.assertEqual(LOCATION_NAME_TO_ID, expected)

    def test_goal_achievement_is_source_genesis(self) -> None:
        # The client watches this achievement ID to decide when to send its StatusUpdate.
        self.assertEqual(GOAL_ACHIEVEMENT, "SF1.1")

    def test_goal_achievement_is_not_also_a_check(self) -> None:
        # The goal is reported via StatusUpdate, not as a location, so SF1.1 must not appear in the
        # check list — otherwise the client would have two conflicting reasons to react to it.
        self.assertNotIn("Source Genesis", LOCATION_NAME_TO_ID)
