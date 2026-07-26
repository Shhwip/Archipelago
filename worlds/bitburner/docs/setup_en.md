# Bitburner Setup Guide

## Required Software

- A build of Bitburner containing the Archipelago client module.
- Archipelago, to generate a seed and host the room.

## Configuring your YAML

Generate a template YAML from the Archipelago Launcher ("Generate Template Options"), or write one
by hand. The only Bitburner-specific option is `goal`:

```yaml
Bitburner:
  goal: source_genesis  # or: any_augmentation
```

`source_genesis` requires destroying BitNode 1 to earn the SF1.1 achievement. Use
`any_augmentation` when you just want to confirm a connection works end to end — it completes as
soon as you receive one augmentation.

## Connecting

1. Start Bitburner and load the save you want to play.
2. Open `Options` -> `Archipelago`.
3. Fill in the server address, port, slot name, and password (leave the password blank if the room
   has none), then enable the connection.
4. The character overview shows the connection status. Once it reports connected, checks you earn
   are sent automatically and items sent to you are applied as you receive them.

The client reconnects on its own if the connection drops, and re-sends any checks you earned while
disconnected the next time it connects.

## Checks

There are 138 checks: 68 Bitburner achievements, and a backdoor on each of the 70 servers in the
game's fixed server list. Earning an achievement or installing a backdoor sends its check
automatically.

You do not need to be connected at the time. The client sweeps game state every few seconds and
records what you have satisfied into your save, then sends anything outstanding the next time it
connects. This matters most for backdoors, which are wiped whenever you install augmentations —
recording them as they happen is what stops a check earned offline from being lost at your next
install.
