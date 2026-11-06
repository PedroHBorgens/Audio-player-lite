# Changelog / Histórico de mudanças

Format based on [Keep a Changelog](https://keepachangelog.com/). / Formato baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/).

## [1.4.1] — 2026-11-06

### Changed / Alterado

- Shuffle button reads **ALEAT** (aleatório) in the Portuguese interface; **SHUF** in English / O botão de ordem aleatória mostra **ALEAT** na interface em português; **SHUF** em inglês

## [1.4.0] — 2026-11-06

### Added / Adicionado

- **?** help button (top-right, `?` key) with the player version, project link, user guide in the current language and issue reporting / Botão de ajuda **?** (canto superior direito, tecla `?`) com a versão do tocador, link do projeto, guia de uso no idioma atual e relato de problemas

### Changed / Alterado

- Site published as plain static files (`.nojekyll`) / Site publicado como arquivos estáticos (`.nojekyll`)

## [1.3.0] — 2026-11-06

### Added / Adicionado

- Interface language selector **PT / EN** (Brazilian Portuguese and English), remembered by the browser and following the browser language on the first visit / Seletor de idioma da interface **PT / EN** (português do Brasil e inglês), salvo no navegador e seguindo o idioma do navegador na primeira visita

### Fixed / Corrigido

- Track durations were not read for files added directly (regression from 1.2.0) / A duração das faixas não era lida para arquivos adicionados diretamente (regressão da 1.2.0)

### Security / Segurança

- Translations reviewed: HTML-inserted texts are fixed and placeholder-free; stored language strictly validated / Traduções revisadas: textos inseridos como HTML são fixos e sem marcadores; idioma salvo validado de forma estrita

## [1.2.1] — 2026-11-06

### Changed / Alterado

- The REP button now shows **∞** in the corner when repeating the whole playlist, just like the **1** for the current track / O botão REP agora mostra **∞** no canto ao repetir a lista inteira, assim como o **1** para a faixa atual

## [1.2.0] — 2026-11-06

### Added / Adicionado

- Repeat modes: off → whole playlist → current track (`↻` / `↻1` on the display) / Modos de repetir: desligado → lista inteira → só a faixa (`↻` / `↻1` no display)
- **+ PASTA** button and `P` key to add a whole folder, plus folder drag and drop, with subfolders and natural ordering / Botão **+ PASTA** e tecla `P` para adicionar uma pasta inteira, e arrastar pastas, com subpastas e ordem natural

### Security / Segurança

- Duration probes queued (max. 4 at a time) and batched rendering, so large folders cannot freeze the tab / Leitura de duração em fila (máx. 4 por vez) e redesenho em lote, para pastas grandes não travarem a aba
- Limits: 2,000 tracks per folder, 5,000 per playlist, 20 folder levels, 50,000 visited entries / Limites: 2.000 faixas por pasta, 5.000 por playlist, 20 níveis de pasta, 50.000 entradas visitadas
- Repeat stops after 3 tracks in a row end in under 500 ms (no endless loop) / Repetir para após 3 faixas seguidas que terminam em menos de 500 ms (sem laço infinito)

## [1.1.1] — 2026-11-06

### Security / Segurança

- ZIP import now counts the real decompressed bytes and aborts at the limit; ZIPs that forge their declared sizes are rejected / A importação de ZIP agora conta os bytes reais descompactados e aborta no limite; ZIPs que falsificam o tamanho declarado são recusados
- Saved playlists read from storage are validated and their metadata is rendered as text only / Playlists lidas do armazenamento são validadas e seus dados são exibidos só como texto

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
