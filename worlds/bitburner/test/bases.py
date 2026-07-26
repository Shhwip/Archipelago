from test.bases import WorldTestBase

from ..world import BitburnerWorld


class BitburnerTestBase(WorldTestBase):
    game = "Bitburner"
    world: BitburnerWorld
