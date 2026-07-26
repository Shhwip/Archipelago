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

  # Content that needs a source file from another BitNode. Leave these off for a BitNode 1 run,
  # or you will have checks you cannot reach.
  gangs: false
  corporations: false
  bladeburner: false
  sleeves: false
  hacknet_servers: false
  staneks_gift: false
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

Checks come from Bitburner achievements, backdoors on each of the game's fixed servers, and joining
factions. Earning, backdooring or joining sends the check automatically.

You cannot write the port-opener programs or buy them from the darknet — they arrive as items. A
server needs as many open ports as it demands before you can NUKE and then backdoor it, so early on
you will only be able to reach the servers requiring no ports.

You do not need to be connected at the time. The client sweeps game state every few seconds and
records what you have satisfied into your save, then sends anything outstanding the next time it
connects. This matters most for backdoors, which are wiped whenever you install augmentations —
recording them as they happen is what stops a check earned offline from being lost at your next
install.
