from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions


class Goal(Choice):
    """
    What finishes your run.

    Source Genesis: destroy BitNode 1 and acquire the SF1.1 achievement.

    Any Augmentation: receive a single augmentation. Source Genesis takes hours to reach, which
    makes it impractical for verifying that a setup works, so this exists as a fast test goal.
    """

    display_name = "Goal"

    option_source_genesis = 0
    option_any_augmentation = 1

    default = option_source_genesis


@dataclass
class BitburnerOptions(PerGameCommonOptions):
    goal: Goal


option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal],
    ),
]
