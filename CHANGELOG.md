# Changelog / Histórico de mudanças

Format based on [Keep a Changelog](https://keepachangelog.com/). / Formato baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/).

## [1.1.0] — 2026-11-06

### Removed / Removido

- Microphone recorder, to remove all device-permission risks / Gravador pelo microfone, para eliminar os riscos ligados a permissões do aparelho

### Changed / Alterado

- Balance control: center mark, magnetic snap to center (±10), fill from the center, label showing `BAL ●` / `E n` / `D n`; tap the label to recenter / Controle de balanço: marca no centro, trava magnética no centro (±10), preenchimento a partir do centro, rótulo `BAL ●` / `E n` / `D n`; toque no rótulo para recentralizar
- `Permissions-Policy` now blocks the microphone too / `Permissions-Policy` agora bloqueia também o microfone

## [1.0.0] — 2026-11-05

### Added / Adicionado

- Winamp-inspired player: playback controls, seek, volume, balance, shuffle, repeat / Tocador inspirado no Winamp: controles de reprodução, progresso, volume, balanço, aleatório, repetir
- Display with elapsed/remaining time, scrolling title and bitrate / Display com tempo decorrido/restante, título rolante e taxa de bits
- Visualizer: spectrum bars, oscilloscope, off / Visualizador: barras de espectro, osciloscópio, desligado
- 10-band equalizer with preamp and 10 presets / Equalizador de 10 bandas com pré-amplificador e 10 presets
- 6 skins / 6 skins: Clássico, Âmbar, Oceano, Synthwave, Papel, Grafite
- Named playlists saved in the browser with their audio / Playlists com nome salvas no navegador junto com o áudio
- ZIP (audio + M3U) and M3U export; ZIP import / Exportação em ZIP (áudio + M3U) e M3U; importação de ZIP
- Microphone recording into the playlist / Gravação pelo microfone direto na playlist
- Documentation in English and Portuguese / Documentação em inglês e português

### Security / Segurança

- Zero third-party requests; system font; JSZip embedded / Zero requisições a terceiros; fonte do sistema; JSZip embutido
- Hash-based CSP and `tools/update-csp.py` / CSP baseada em hash e `tools/update-csp.py`
- ZIP size/count limits, M3U and name sanitization (control and bidi characters) / Limites de tamanho/quantidade em ZIP, higienização de M3U e nomes (caracteres de controle e bidi)
- Recording: click-only, double-start lock, release on exit, disabled in iframes / Gravação: só por clique, trava contra início duplo, liberação ao sair, desativada em iframes
- Warnings for shared-origin storage (`file://`, `*.github.io`) / Avisos de armazenamento com origem compartilhada (`file://`, `*.github.io`)

### License / Licença

- PolyForm Noncommercial License 1.0.0 — free for personal use / gratuito para uso pessoal
