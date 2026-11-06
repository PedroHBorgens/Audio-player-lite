# Architecture

**English** · [Português](../pt-BR/arquitetura.md) · [← README](../../README.md)

## Overview

The player is **a single file** (`index.html`) of plain HTML, CSS and JavaScript — no build step and no external runtime dependencies. It contains two `<script>` blocks:

1. **JSZip 3.10.1**, embedded unmodified (minified — the hash is listed in [THIRD-PARTY-NOTICES.md](../../THIRD-PARTY-NOTICES.md)).
2. **The player code**, wrapped in an immediately invoked function (IIFE) so nothing leaks into the global scope.

```
index.html
├── <style>        layout, skin variables
├── <body>         windows: main, skins, equalizer, playlist
├── <script> #1    JSZip (third party)
└── <script> #2    player
     ├── audio graph (Web Audio API)
     ├── playlist and transport
     ├── storage (IndexedDB / localStorage)
     ├── export / import (JSZip, M3U)
     ├── equalizer, skins, marquee, visualizer
     └── drag and drop, keyboard shortcuts
```

Code identifiers and comments are mostly in Portuguese. The UI is translated (see [Interface language](#interface-language)).

## Audio graph

Playback uses one `HTMLAudioElement`. On the first user interaction (browsers require a gesture before audio), the player creates an `AudioContext` and wires:

```
<audio> → MediaElementSource → GainNode (PRE)
        → 10 × BiquadFilter → StereoPanner (BAL) → AnalyserNode → destination
```

| Band | Filter type |
|---|---|
| 60 Hz | `lowshelf` |
| 170 Hz – 14 kHz | `peaking`, Q = 1.1 |
| 16 kHz | `highshelf` |

- PRE gain is converted from dB to linear (`10^(dB/20)`).
- **Balance** ranges from −100 to +100 and is applied as `pan` from −1 to +1. Values between −10 and +10 become 0 (magnetic center); the track fills from the center and the label shows `BAL ●`, `E n` (left) or `D n` (right). On phones, a short vibration signals the snap to center.
- **EQ OFF** rewires the graph without the preamp and filters.
- The `AnalyserNode` (FFT size 1024, smoothing 0.75) drives the visualizer: 28 log-spaced bars over the lowest 70% of the bins, with slowly falling peaks, or the raw waveform in oscilloscope mode.
- Tracks with unknown duration (some WEBM files report `Infinity`) get a fix-up: the player seeks to the end, reads the real duration, and seeks back to the start.

## Playlist and transport

Each track is an object `{ name, fname, blob, url, dur, size }`.

- **Repeat** has three modes (`repeat = 'off' | 'all' | 'one'`). In `one`, the `ended` event seeks to 0 and plays again; in `all`, the track after the last one is the first. If 3 tracks in a row end less than 500 ms after starting, playback stops (prevents endless loops with empty files).
- **Folders**: `+ FOLDER` (`+ PASTA`) uses an `<input type="file" webkitdirectory>`; dropped folders are walked with `webkitGetAsEntry()` / `readEntries()` (up to 20 levels deep and 50,000 visited entries). Only files with an audio extension are kept, hidden items are skipped, and files are sorted with `localeCompare` and `numeric: true`, up to 2,000 per folder. The whole playlist is capped at 5,000 tracks.
- **Duration** is read through a queue with at most 4 metadata-only `<audio>` elements at a time (10 s timeout each), and the list is re-rendered at most once per frame. Without this, a large folder opened thousands of readers at once and froze the tab. `url` is an object URL (`blob:`) for the file, revoked when the track is removed or the list is cleared. Duration is read by a helper metadata-only `<audio>` element.

File names and titles go through `oneLine()`, which strips control characters, line breaks and bidirectional-text override characters, and truncates to 200 characters. Everything shown on screen is set with `textContent`, never `innerHTML` with user data.

## Interface language

- All UI text lives in the `I18N` dictionary (`pt` and `en`, same keys) at the top of the player script, read through `T(key, vars)`. `{name}`-style placeholders are filled with a replacer function, so values are inserted once and never re-parsed.
- Static elements carry `data-i18n` (text), `data-i18n-title`, `data-i18n-ph` (placeholder), `data-i18n-aria` or `data-i18n-html`. `applyLang()` refreshes them plus everything drawn by code (playlist, saved lists, skins, presets, repeat and balance labels, warnings) and clears transient messages.
- `data-i18n-html` and every string concatenated into `innerHTML` are fixed dictionary texts **without placeholders**; anything that includes user data goes through `textContent`.
- The language is stored in `localStorage` (`tocador-lang`) and accepted only if it is exactly `pt` or `en`; otherwise the browser language decides. `<html lang>` follows the choice.
- The Claude-hosted version is generated from `index.html` by removing the CSP meta tag (the host applies its own policy), so both versions share the same code.

## Version and help card

`VERSION` and `REPO_URL` are constants at the top of the player script; the **?** card reads them, and the user-guide link switches with the language. Bump `VERSION` together with `CHANGELOG.md` on every release.

## Storage

### IndexedDB — database `tocador`, version 1

| Store | Key | Value |
|---|---|---|
| `files` | `"<file-name>|<size>"` | `{ blob, fname }` |
| `lists` | `name` (keyPath) | `{ name, updated, items: [{ key, name, dur }] }` |

- Identical files shared by several playlists are stored **once** (same key).
- Saving writes files and list in a single transaction.
- Deleting a list also deletes files no other list references.
- After saving, the player calls `navigator.storage.persist()` to ask the browser not to evict the data.

### localStorage

| Key | Content |
|---|---|
| `tocador-skin` | id of the chosen skin |
| `tocador-last` | name of the last opened/saved playlist, reopened on load |

All storage access is wrapped in `try/catch`: if the browser blocks it, the player keeps working without persistence. Data read back from storage is treated as untrusted (another page on the same origin could have written it): lists must have an `items` array, files must be real `Blob`s, durations must be finite numbers, and list metadata is rendered as text.

## Export and import

**ZIP** — built with JSZip without compression (`STORE`), since audio does not compress. Tracks get a numeric prefix (`01 - `, `02 - `…) and a `playlist.m3u` is added:

```
#EXTM3U
#EXTINF:215,Track title
01 - original-file.mp3
```

Duration is rounded to seconds, or `-1` when unknown.

**Download** — inside Claude it uses the platform's `downloads` capability (the user confirms). Elsewhere it uses a regular `<a download>` link.

**ZIP import** — the player:

1. Rejects ZIPs with more than 1,000 entries or more than 2 GB uncompressed; skips entries over 512 MB and `.m3u` files over 1 MB using the sizes declared in the ZIP as a quick first filter. Because those declared sizes can be forged, every entry is then inflated through a stream (`inflateLimited`) that counts the real bytes and aborts as soon as a per-file or total limit is exceeded.
2. Ignores directories, `__MACOSX` and hidden files.
3. Reads the `.m3u`, if any, and orders tracks by it; the rest are appended alphabetically.
4. Strips the numeric prefix from names and sets the MIME type from the extension.

Nothing is written to disk, so malicious paths inside the ZIP (`../`) have no effect.

## Skins

Each skin is a set of CSS custom properties applied through `data-skin` on the `<html>` element:

`--bg`, `--panel`, `--panel2`, `--line`, `--text`, `--dim`, `--accent`, `--accent2`, `--lcd`, `--peak`

The canvas visualizer re-reads the colors when the skin changes. To add a skin, add a `[data-skin="id"]{…}` block to the CSS and an entry to the `SKINS` array in the JavaScript. See [CONTRIBUTING.md](../../CONTRIBUTING.md#english).

## Security model

| Layer | Measure |
|---|---|
| CSP (meta tag) | `default-src 'none'`; scripts allowed **only by SHA-256 hash**; `connect-src 'none'`; no external fonts, images or media |
| HTTP headers (`_headers`) | Same CSP + `frame-ancestors 'none'`, `Permissions-Policy` (microphone, camera and location blocked), `X-Frame-Options`, `nosniff`, `no-referrer`, HSTS — applied on Netlify/Cloudflare Pages |
| User data | Always rendered as text; names sanitized |
| Permissions | The player uses no microphone, camera or location; `Permissions-Policy` blocks them all |
| Imported files | Size and count limits; nothing written to disk |
| Third parties | No external resources; JSZip embedded with a documented hash |

Because scripts are allowed by hash, **any change to a `<script>` block requires regenerating the CSP** with `python3 tools/update-csp.py`. Otherwise the browser blocks the script and the player stops working.

Remaining risks are listed in [SECURITY.md](../../SECURITY.md#known-risks).

## Compatibility

| Feature | API |
|---|---|
| Equalizer and visualizer | Web Audio API (`AudioContext`, `BiquadFilterNode`, `StereoPannerNode`, `AnalyserNode`) |
| Playlists | IndexedDB, `navigator.storage.persist` |
| ZIP | JSZip (ArrayBuffer/Blob) |
| Vertical EQ sliders | `writing-mode: vertical-lr` on `input[type=range]` |

Without `StereoPannerNode`, balance is ignored.
