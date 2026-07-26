# Bitburner

## What does randomization do to this game?

Augmentations become Archipelago items. You receive them from the multiworld instead of buying
them, and they are applied immediately, without an install or reset.

The five port-opener programs also become items, and you can no longer write them yourself or buy
them from the darknet. Since NUKE needs open ports to root a server, and rooting is what lets you
backdoor it, which programs you have found decides how much of the network you can reach.

Earning achievements, joining factions, and installing backdoors all send checks.

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

Up to 165, from three sources:

- **68 achievements.** Everything except the secret achievements, the source file achievements for
  other BitNodes, and the challenge-run achievements.
- **70 server backdoors**, one per server in Bitburner's fixed server list.
- **27 faction joins**, for the factions whose join is not already an achievement.

A default seed has 145 of those. The rest belong to content options that are off unless you turn
them on.

## Content options

Gangs, corporations, Bladeburner, Sleeves, hacknet servers and Stanek's Gift each need a source file
from another BitNode, so a BitNode 1 run cannot reach any of them. Each has an option, off by
default, that adds its checks and any augmentations exclusive to it.

Turn one on only if your run can actually reach that content.

## Current scope

Logic covers open ports, which is what gates the backdoors. It does not yet cover required hacking
skill, money, or faction reputation, so a check can be in logic while still being a long grind
away.
