# Load-Order-Sentinel
 
A CLI tool that audits Skyrim/Bethesda plugin load orders — catches duplicate plugins and known mod conflicts before you boot the game.
 
## What it does
 
Point it at a `plugins.txt` (or similar load order file), and it checks for:
 
- **Duplicate plugins** — the same plugin listed more than once in your load order
- **Known conflicts** — plugins that are flagged in a small, hand-maintained list of mods known to cause trouble together
It prints a clean, grouped report of anything it finds — or nothing at all if your load order is clean.
 
## Why this exists
 
Tools like [LOOT](https://loot.github.io/) and [xEdit](https://tes5edit.github.io/) already do this, and do it far more thoroughly — LOOT sorts your load order using a community-maintained masterlist, and xEdit can inspect actual plugin dependency data at the binary level.
 
Load-Order-Sentinel isn't trying to replace either of those. It's a small, personal, terminal-first tool built to practice Python fundamentals (parsing, OOP, exceptions, testing) on a real problem I actually care about — and to have something fast and scriptable that checks the handful of things I personally care about, without needing a GUI or a community database.
 
## Installation
 
Requires Python 3.10+. No external dependencies to run the tool itself.
 
```bash
git clone https://github.com/<your-username>/Load-Order-Sentinel.git
cd Load-Order-Sentinel
```
 
## Usage
 
```bash
python3 main.py --path path/to/plugins.txt
```
 
If `--path` is omitted, it defaults to looking for `plugins.txt` in the current directory.
 
### Example output
 
```
DuplicateRule:
  SomeMod.esp
 
ConflictRule:
  Ordinator.esp: Conflicts with Apocalypse.
```
 
## How it works
 
Each check is a `Rule` — a small class implementing a shared `check(plugins)` interface. This means adding a new check is just writing a new `Rule` subclass and adding it to the rule list; nothing else in the program needs to change.
 
Currently implemented rules:
 
| Rule | What it checks |
|---|---|
| `DuplicateRule` | Plugin names that appear more than once |
| `ConflictRule` | Plugin names matching a hardcoded `KNOWN_CONFLICTS` dictionary |
 
Known conflicts are maintained by hand in `main.py` — this isn't a community masterlist, just mods I've personally flagged.
 
## Running tests
 
```bash
python3 -m pip install pytest
python3 -m pytest
```
 
## Roadmap
 
Ideas for future versions:
 
- [ ] Malformed-line detection (unexpected characters, bad formatting)
- [ ] Missing-master detection (would require parsing plugin headers directly, not just the load order text file)
- [ ] Config file support for `KNOWN_CONFLICTS` instead of hardcoding it in `main.py`
- [ ] More test coverage, including edge cases like empty files and blank lines
## License
 
No license has been chosen yet — all rights reserved by default until one is added.