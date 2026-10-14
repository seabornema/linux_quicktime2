# Sprites

Replace any placeholder with your own PNG, keeping the same filename.
Transparent PNGs are supported. Images larger than the size box are shrunk
to fit (aspect ratio kept); smaller images are shown at their own size.

| File          | Shown when                                              |
|---------------|---------------------------------------------------------|
| `flash_a.png` | During the event: frame 1 (flashes with frame 2)        |
| `flash_b.png` | During the event: frame 2                               |
| `success.png` | You hit the press count in time (stays a few seconds)   |
| `fail.png`    | Time ran out (stays a few seconds, then disappears)     |

Default size box is 256x256 (change with `--size`). Flash speed is
`--flash-ms` (default 150). If a file is missing, plain text is shown
instead, so you can add sprites a few at a time.

Lookup order (first match wins):
1. `--sprites DIR` on the command line
2. `~/.local/share/qte-popups/sprites/`   (per-user override, no sudo needed)
3. `/usr/share/qte-popups/sprites/`       (installed by the package)
4. `../share/qte-popups/sprites/` next to the script (running from the repo)
