# User guide

**English** · [Português](../pt-BR/guia-de-uso.md) · [← README](../../README.md)

The player's interface is in Portuguese (Brazil). Labels are quoted here exactly as they appear on screen, with a translation where useful.

## Contents

1. [Opening the player](#1-opening-the-player)
2. [Adding music](#2-adding-music)
3. [Playback controls](#3-playback-controls)
4. [Display and visualizer](#4-display-and-visualizer)
5. [Equalizer](#5-equalizer)
6. [Skins](#6-skins)
7. [Playlist](#7-playlist)
8. [Saving playlists](#8-saving-playlists)
9. [Exporting and importing](#9-exporting-and-importing)
10. [Recording from the microphone](#10-recording-from-the-microphone)
11. [Keyboard shortcuts](#11-keyboard-shortcuts)
12. [Privacy: where your data lives](#12-privacy-where-your-data-lives)
13. [Troubleshooting](#13-troubleshooting)

## 1. Opening the player

| Method | How | Does recording work? |
|---|---|---|
| Published site (GitHub Pages, Netlify…) | Open the `https://` address in a browser | Yes, on desktop and mobile |
| Local file | Download `index.html` and double-click it | Yes on desktop; usually not on mobile |

Tip: on a phone, use **Add to Home Screen** from the browser menu to open the player like an app.

## 2. Adding music

- Tap **+ ADD** (in the playlist) or the eject button **⏏** (main panel) and pick one or more files.
- On desktop you can also **drag files** anywhere onto the window.
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
| **REP** | Repeat the whole playlist when it ends |
| Seek bar | Drag to jump anywhere in the track |
| **VOL** | Volume |
| **BAL** | Left/right balance. Double-click to center |

## 4. Display and visualizer

- **Clock**: tap it to toggle between **elapsed** and **remaining** time (shows `REST`).
- **Status**: `▶ PLAY`, `❚❚ PAUSE`, `■ STOP` or `● REC`.
- **Title**: scrolls automatically when it does not fit.
- **kbps**: bitrate estimated from file size and duration.
- **Visualizer**: tap to cycle between **spectrum bars** (with slowly falling peaks), **oscilloscope** and **off**. While recording, it shows the microphone signal.

## 5. Equalizer

Tap **EQ** to open it.

- **10 bands**: 60 Hz, 170 Hz, 310 Hz, 600 Hz, 1 kHz, 3 kHz, 6 kHz, 12 kHz, 14 kHz and 16 kHz, from −12 dB to +12 dB.
- **PRE**: preamp. Lower it if the sound distorts after boosting several bands.
- **Presets** (`Presets…` menu): Flat, Rock, Pop, Jazz, Clássica (Classical), Eletrônica (Electronic), Grave+ (Bass+), Agudo+ (Treble+), Voz (Vocal) and Fone (Headphones).
- **ZERAR** (reset): sets everything to 0 dB. Double-clicking a single band resets only that band.
- **ON/OFF** (window title bar): bypasses the equalizer for A/B comparison.

The equalizer also applies to recordings and works in real time; it **does not change** exported files.

## 6. Skins

Tap **SKIN** and choose one of six: **Clássico** (Classic, green), **Âmbar** (Amber), **Oceano** (Ocean), **Synthwave**, **Papel** (Paper, light theme) and **Grafite** (Graphite, black and white). The `K` key cycles to the next one. Your choice is remembered by the browser.

## 7. Playlist

- Tap a track to play it. The current track is highlighted.
- Hover over a track and tap **×** to remove it.
- **LIMPAR** (clear) empties the current list (saved playlists are not affected).
- The footer shows the number of tracks and total duration.

## 8. Saving playlists

Tap **LISTAS** (lists).

1. Type a name and tap **SALVAR** (save), or press Enter. Saving with an existing name **replaces** that playlist.
2. Under *Playlists salvas* (saved playlists), use **ABRIR** (open) to load one and **×** to delete it (tap twice to confirm — the button changes to `CONFIRMA?`).

The **audio files are stored together** with the list, so you do not need to add them again. The last playlist opened or saved reopens automatically when you come back.

Everything stays **in this browser on this device only**. Clearing browsing data deletes saved playlists. To move them to another device, use ZIP export.

## 9. Exporting and importing

Tap **EXPORTAR** (export).

- **ZIP · MÚSICAS + M3U** (ZIP · music + M3U): creates a ZIP with the tracks numbered in order (`01 - name.mp3`, `02 - …`) plus a `playlist.m3u`. The ZIP works in other players and can be **imported back** with **+ ADD**, keeping order and titles.
- **SÓ A LISTA (M3U)** (list only): creates just the list, referencing the original file names. It is saved as `.m3u.txt`; rename it to `.m3u` for other players (they must find the audio files in the same folder).

When importing a ZIP, the player follows the order of the `.m3u` inside it; tracks not listed in the `.m3u` are appended in alphabetical order. For safety, ZIPs with more than 1,000 entries, tracks over 512 MB, or more than 2 GB in total are rejected.

Inside Claude, the browser asks for confirmation before saving an exported file.

## 10. Recording from the microphone

1. Tap **● REC**. The first time, the browser asks for microphone permission.
2. Playback pauses, the button becomes a blinking **■ PARAR** (stop), and the display shows the recording time.
3. Tap **■ PARAR**. The recording is appended to the playlist as `Gravação DD/MM HH:MM:SS` ("Recording" + date and time).
4. To keep it, save the playlist under **LISTAS** or export a ZIP.

Details:

- The format depends on the browser: **WEBM/Opus** (Chrome, Edge, Firefox) or **M4A/AAC** (Safari).
- Echo cancellation, noise suppression and automatic gain are disabled, so the sound is captured as-is.
- The microphone is not routed to the speakers while recording (no feedback).
- Recordings shorter than half a second are discarded.
- The microphone is released when you stop or leave the page.
- Recording is disabled when the player is embedded in another page (iframe), so a third-party site cannot trick you into clicking REC.

## 11. Keyboard shortcuts

| Key | Action | Key | Action |
|---|---|---|---|
| `Z` | Previous | `B` | Next |
| `X` | Play | `C` | Pause |
| `V` | Stop | `Space` | Play/Pause |
| `←` `→` | Seek ±5 s | `↑` `↓` | Volume |
| `S` | Shuffle | `R` | Repeat |
| `E` | Equalizer | `K` | Next skin |
| `L` | Open files | | |

Shortcuts are ignored while typing in the playlist name field.

## 12. Privacy: where your data lives

| Data | Where |
|---|---|
| Music added but not saved | Tab memory only; gone when the tab closes |
| Saved playlists and recordings | The browser's IndexedDB on this device, unencrypted |
| Chosen skin and last playlist | The browser's `localStorage` |
| Anything | **Never** sent over the internet |

When the player runs as a local file or on a `*.github.io` address, it shows a warning under **LISTAS**, because in those cases other pages from the same place can access its storage. See [SECURITY.md](../../SECURITY.md#known-risks).

## 13. Troubleshooting

| Problem | Fix |
|---|---|
| A track does not play | The browser cannot decode that format. Convert it to MP3 or try another browser |
| Duration shows `--:--` | The file is still being read or has no duration metadata; it appears once it plays |
| "Permissão do microfone negada" (microphone permission denied) | Allow the microphone for the site in the browser settings (padlock icon in the address bar) |
| "O microfone só funciona em https://" (microphone needs https) | Use the published version (GitHub Pages) or open the local file on a desktop |
| "Sem espaço no navegador" (out of browser storage) | The browser limited storage. Delete old playlists or export them as ZIP |
| Playlists disappeared | Browser data was cleared, or you opened the player from another address/browser. Each address has its own storage |
| Sound distorts with the EQ | Lower **PRE** |
| Shortcuts do not respond | Click an empty area of the player to move focus away from fields and menus |
