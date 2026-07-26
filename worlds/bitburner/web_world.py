from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups


class BitburnerWebWorld(WebWorld):
    game = "Bitburner"

    theme = "ice"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Bitburner for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["shhwip"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
