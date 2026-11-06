# User guide

**English** · [Português](../pt-BR/guia-de-uso.md) · [← README](../../README.md)

The interface is available in **English and Brazilian Portuguese** (see [Language](#language)). Labels below are the English ones; the Portuguese label follows in parentheses where it differs.

## Contents

- [Language](#language)
1. [Opening the player](#1-opening-the-player)
2. [Adding music](#2-adding-music)
3. [Playback controls](#3-playback-controls)
4. [Display and visualizer](#4-display-and-visualizer)
5. [Equalizer](#5-equalizer)
6. [Skins](#6-skins)
7. [Playlist](#7-playlist)
8. [Saving playlists](#8-saving-playlists)
9. [Exporting and importing](#9-exporting-and-importing)
10. [Keyboard shortcuts](#10-keyboard-shortcuts)
11. [Privacy: where your data lives](#11-privacy-where-your-data-lives)
12. [Troubleshooting](#12-troubleshooting)

## Language

Tap **PT** or **EN** in the top-right corner of the main window to switch the whole interface between Brazilian Portuguese and English — buttons, tips, messages, skin and preset names. The choice is remembered by the browser; on the first visit the player follows your browser's language (Portuguese if it is set to Portuguese, English otherwise).

## 1. Opening the player

| Method | How |
|---|---|
| Published site (GitHub Pages, Netlify…) | Open the `https://` address in a browser, on desktop or mobile |
| Local file | Download `index.html` and double-click it |

Tip: on a phone, use **Add to Home Screen** from the browser menu to open the player like an app.

## 2. Adding music

- Tap **+ ADD** (in the playlist) or the eject button **⏏** (main panel) and pick one or more files.
- Tap **+ FOLDER** (*+ PASTA*, or press `P`) and pick a **whole folder**: every audio file inside it, including subfolders, is added in **natural order** by path (`2 - …` before `10 - …`). Non-audio files and hidden files or folders (starting with `.`) are skipped. Up to 2,000 tracks per folder.
- On desktop you can also **drag files or folders** anywhere onto the window.

When you pick a folder, some browsers ask whether you want to "upload" the files to the site. **Nothing is uploaded**: the player only reads the files on your device. On phones, folder picking depends on the browser; if it is not offered, use **+ ADD** and select several files.

The playlist holds up to 5,000 tracks.
- You can also add a **ZIP exported by the player** (or any ZIP containing music) — see [section 9](#9-exporting-and-importing).

Accepted formats: MP3, WAV, OGG, FLAC, M4A, AAC, OPUS and WEBM. If the browser cannot decode a file, the track is listed but will not play.

## 3. Playback controls

| Button | Function |
|---|---|
| ⏮ | Previous track. If the current track is past 3 seconds, restarts it instead |
| ▶ / ❚❚ | Play / pause |
| ■ | Stop and rewind |
| ⏭ | Next track |
| **SHUF** | Shuffle (lit = on) |
| **REP** | Each tap changes the mode: **off** → **whole playlist** (lit with an **∞** in the corner, `↻` on the display) → **current track only** (lit with a **1** in the corner, `↻1` on the display). In track mode the song restarts when it ends; ⏮ ⏭ still change tracks |
| Seek bar | Drag to jump anywhere in the track |
| **VOL** | Volume |
| **BAL** | Left/right balance. It has a center mark and a magnetic center: near the middle it snaps to center. The label shows `BAL ●` (center), `L 40` (left) or `R 25` (right) — `E`/`D` in Portuguese; **tap the label** or double-click the control to recenter |

## 4. Display and visualizer

- **Clock**: tap it to toggle between **elapsed** and **remaining** time (shows `REM`, *REST* in Portuguese).
- **Status**: `▶ PLAY`, `❚❚ PAUSE` or `■ STOP`.
- **Title**: scrolls automatically when it does not fit.
- **kbps**: bitrate estimated from file size and duration.
- **Visualizer**: tap to cycle between **spectrum bars** (with slowly falling peaks), **oscilloscope** and **off**.

## 5. Equalizer

Tap **EQ** to open it.

- **10 bands**: 60 Hz, 170 Hz, 310 Hz, 600 Hz, 1 kHz, 3 kHz, 6 kHz, 12 kHz, 14 kHz and 16 kHz, from −12 dB to +12 dB.
- **PRE**: preamp. Lower it if the sound distorts after boosting several bands.
- **Presets** (`Presets…` menu): Flat, Rock, Pop, Jazz, Classical, Electronic, Bass+, Treble+, Vocal and Headphones.
- **RESET** (*ZERAR*): sets everything to 0 dB. Double-clicking a single band resets only that band.
- **ON/OFF** (window title bar): bypasses the equalizer for A/B comparison.

The equalizer works in real time; it **does not change** exported files.

## 6. Skins

Tap **SKIN** and choose one of six: **Classic** (green), **Amber**, **Ocean**, **Synthwave**, **Paper** (light theme) and **Graphite** (black and white). The `K` key cycles to the next one. Your choice is remembered by the browser.

## 7. Playlist

- Tap a track to play it. The current track is highlighted.
- Hover over a track and tap **×** to remove it.
- **CLEAR** (*LIMPAR*) empties the current list (saved playlists are not affected).
- The footer shows the number of tracks and total duration.

## 8. Saving playlists

Tap **LISTS** (*LISTAS*).

1. Type a name and tap **SAVE** (*SALVAR*), or press Enter. Saving with an existing name **replaces** that playlist.
2. Under *saved playlists*, use **OPEN** to load one and **×** to delete it (tap twice to confirm — the button changes to `SURE?`).

The **audio files are stored together** with the list, so you do not need to add them again. The last playlist opened or saved reopens automatically when you come back.

Everything stays **in this browser on this device only**. Clearing browsing data deletes saved playlists. To move them to another device, use ZIP export.

## 9. Exporting and importing

Tap **EXPORT** (*EXPORTAR*).

- **ZIP · MUSIC + M3U**: creates a ZIP with the tracks numbered in order (`01 - name.mp3`, `02 - …`) plus a `playlist.m3u`. The ZIP works in other players and can be **imported back** with **+ ADD**, keeping order and titles.
- **LIST ONLY (M3U)**: creates just the list, referencing the original file names. It is saved as `.m3u.txt`; rename it to `.m3u` for other players (they must find the audio files in the same folder).

When importing a ZIP, the player follows the order of the `.m3u` inside it; tracks not listed in the `.m3u` are appended in alphabetical order. For safety, ZIPs with more than 1,000 entries, tracks over 512 MB, or more than 2 GB in total are rejected.

Inside Claude, the browser asks for confirmation before saving an exported file.

## 10. Keyboard shortcuts

| Key | Action | Key | Action |
|---|---|---|---|
| `Z` | Previous | `B` | Next |
| `X` | Play | `C` | Pause |
| `V` | Stop | `Space` | Play/Pause |
| `←` `→` | Seek ±5 s | `↑` `↓` | Volume |
| `S` | Shuffle | `R` | Repeat: off → playlist → track |
| `E` | Equalizer | `K` | Next skin |
| `L` | Open files | `P` | Add a folder |

Shortcuts are ignored while typing in the playlist name field.

## 11. Privacy: where your data lives

| Data | Where |
|---|---|
| Music added but not saved | Tab memory only; gone when the tab closes |
| Saved playlists | The browser's IndexedDB on this device, unencrypted |
| Chosen skin and last playlist | The browser's `localStorage` |
| Anything | **Never** sent over the internet |

When the player runs as a local file or on a `*.github.io` address, it shows a warning under **LISTS**, because in those cases other pages from the same place can access its storage. See [SECURITY.md](../../SECURITY.md#known-risks).

## 12. Troubleshooting

| Problem | Fix |
|---|---|
| A track does not play | The browser cannot decode that format. Convert it to MP3 or try another browser |
| Duration shows `--:--` | The file is still being read or has no duration metadata; it appears once it plays |
| "Not enough browser storage" | The browser limited storage. Delete old playlists or export them as ZIP |
| Playlists disappeared | Browser data was cleared, or you opened the player from another address/browser. Each address has its own storage |
| Sound distorts with the EQ | Lower **PRE** |
| "Playback stopped: tracks are ending too quickly to repeat" | Protection against endless repeat loops: if 3 tracks in a row end in under half a second, the player stops. It happens with empty or corrupted files |
| **+ FOLDER** does not open a folder on my phone | Not every mobile browser supports picking folders. Use **+ ADD** and select several files |
| I can't set a small balance value (1–10) | That is the magnetic center: values up to 10 on either side snap back to the middle, by design |
| Shortcuts do not respond | Click an empty area of the player to move focus away from fields and menus |
