# Bitburner

## What does randomization do to this game?

Augmentations are removed from the shops and turned into Archipelago items. You receive them from
the multiworld instead of buying them, and they are applied immediately, without an install/reset.

Earning certain Bitburner achievements sends location checks to the multiworld.

## What is the goal?

Acquire Source Genesis — destroy BitNode 1 and earn the SF1.1 achievement.

Because that takes hours, the `goal` option offers `any_augmentation` as an alternative that
finishes as soon as you receive a single augmentation. It exists to verify a setup works, not to
be played.

## Which items can be in another player's world?

All of them. Every augmentation in the pool may be placed in any world in the multiworld.

## What does another world's item look like in Bitburner?

Checks are sent when you earn the corresponding achievement. The item you found is reported by the
Archipelago server, not shown in Bitburner itself.

## What are the checks?

138 of them, from two sources:

- **68 achievements.** Everything except the secret achievements, the source file achievements for
  other BitNodes, and the challenge-run achievements.
- **70 server backdoors**, one per server in Bitburner's fixed server list.

## Current scope

The item pool is every augmentation in the game — 136 of them, plus NeuroFlux Governor as filler.

There is no logic yet. Every check sits in one region with nothing gating it, and the generator will
happily place an item behind a check you cannot reach. Some achievements in the list need BitNode
content a BitNode 1 run never sees, such as gangs, corporations, Bladeburner and Sleeves. Until
logic is added, treat those as optional and expect some checks to be out of reach in a given run.
