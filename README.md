# qte-popups

Random quick-time events for Linux Mint (GTK3 / Python). A sprite flashes on
screen at a random spot; **mash the space bar 10-30 times** before the timer runs out.

- **Success:** the success sprite shows for a few seconds, then disappears.
- **Fail:** the fail sprite shows for a few seconds, then disappears.
- Holding the key doesn't count (auto-repeat is ignored); you have to mash.
- **Esc** dismisses an event.

## Build and install
```
./build.sh
sudo apt install ./qte-popups_1.2.0_all.deb
```

## Try it
```
qte-popups --now                                   # first event in 2 seconds
qte-popups --min-interval 5 --max-interval 15      # fast testing
```
Run straight from the repo (no install): `python3 src/usr/bin/qte-popups --now`

## Options
| Option | Default | Meaning |
|---|---|---|
| `--min-interval` / `--max-interval` | 120 / 900 | seconds between events |
| `--min-presses` / `--max-presses` | 10 / 30 | presses required (random per event) |
| `--seconds-per-press` | 0.3 | time allowed per required press |
| `--min-time` | 3 | minimum time limit (seconds) |
| `--flash-ms` | 150 | milliseconds between the two flash sprites |
| `--success-seconds` / `--fail-seconds` | 3 / 3 | how long the result sprite stays |
| `--size` | 256 | max sprite size in pixels |
| `--no-hud` | off | hide the counter and timer bar |
| `--no-grab` | off | don't grab the keyboard (popup needs focus instead) |
| `--sprites DIR` | – | sprite folder to try first |
| `--now` | off | fire the first event after 2 seconds |

Autostart options live in `/etc/xdg/autostart/qte-popups.desktop` (`Exec=` line).

## Sprites
Four PNGs in `src/usr/share/qte-popups/sprites/`: `flash_a.png`, `flash_b.png`,
`success.png`, `fail.png`. Replace the placeholders, keeping the filenames.
See that folder's `README.md`. Missing sprites fall back to text.

Try sprites without rebuilding: drop PNGs into `~/.local/share/qte-popups/sprites/`
or run with `--sprites /path/to/dir`.

Regenerate placeholders (needs Pillow): `python3 tools/make_placeholders.py --force`

## Layout
- `src/usr/bin/qte-popups` – the program
- `src/usr/share/qte-popups/sprites/` – PNG sprites
- `src/etc/xdg/autostart/` – autostart entry
- `src/usr/share/applications/` – app-menu test launcher
- `src/DEBIAN/control` – package metadata
- `tools/make_placeholders.py` – placeholder sprite generator
