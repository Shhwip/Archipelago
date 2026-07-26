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

All six checks are Bitburner achievements:

| Check | How to earn it |
|---|---|
| Purchase Your First Hacknet Node | Buy a node from the Hacknet menu |
| Purchase the TOR Router | Buy the TOR router at the Sector-12 Alpha Enterprises |
| Work Out at a Gym | Begin any gym workout |
| Travel to Another City | Travel out of Sector-12 |
| Get Hospitalized | Take enough damage to be hospitalized |
| Write a .js Script | Create a `.js` script on your home computer |
