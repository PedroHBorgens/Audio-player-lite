# Tocador Minimalista

Tocador de áudio para o navegador com visual minimalista, inspirado no Winamp. É um único arquivo HTML: não precisa instalar nada, não tem servidor nem conta, e suas músicas nunca saem do seu aparelho.

![Tocador Minimalista](docs/screenshot.png)

## Recursos

- **Reprodução**: tocar, pausar, parar, anterior/próxima, aleatório, repetir, barra de progresso, volume e balanço
- **Display estilo Winamp**: tempo decorrido/restante, título rolante, kbps estimado
- **Visualizador**: barras de espectro com picos, osciloscópio ou desligado (clique para alternar)
- **Equalizador de 10 bandas** com pré-amplificador e presets (Rock, Pop, Jazz, Clássica, Eletrônica, Grave+, Agudo+, Voz, Fone)
- **6 skins**: Clássico, Âmbar, Oceano, Synthwave, Papel (claro) e Grafite
- **Playlists salvas** no navegador (com as músicas), com reabertura automática da última
- **Exportação** em ZIP (músicas + `playlist.m3u`) ou só a lista M3U; o ZIP pode ser importado de volta
- **Gravação pelo microfone**: a gravação entra direto na playlist
- Arrastar e soltar arquivos · formatos MP3, WAV, OGG, FLAC, M4A, AAC, OPUS, WEBM

## Como usar

**Online:** acesse a página do GitHub Pages deste repositório (veja abaixo como ativar).

**Local:** baixe o `index.html` e abra no Chrome, Edge ou Firefox.

> A gravação pelo microfone exige `https://` (GitHub Pages serve) ou o arquivo aberto direto do disco no computador.

### Atalhos de teclado

| Tecla | Ação | Tecla | Ação |
|---|---|---|---|
| `Z` | Anterior | `B` | Próxima |
| `X` | Tocar | `C` | Pausar |
| `V` | Parar | `Espaço` | Tocar/Pausar |
| `←` `→` | ±5 segundos | `↑` `↓` | Volume |
| `S` | Aleatório | `R` | Repetir |
| `E` | Equalizador | `K` | Próxima skin |
| `L` | Abrir arquivos | | |

A gravação só é iniciada por clique no botão **● REC**, de propósito.

## Publicar com GitHub Pages

1. No repositório, vá em **Settings → Pages**
2. Em *Source*, escolha **Deploy from a branch**, branch `main`, pasta `/ (root)` e salve
3. Em alguns minutos o tocador estará em `https://<seu-usuario>.github.io/<nome-do-repositorio>/`

O arquivo `_headers` não tem efeito no GitHub Pages; ele aplica cabeçalhos de segurança extras se você publicar no Netlify ou Cloudflare Pages.

## Privacidade e segurança

- **Zero contato com terceiros**: a página não carrega nada de fora (nem fontes, nem bibliotecas) e bloqueia qualquer conexão externa por política de segurança (CSP)
- Usa a fonte monoespaçada do próprio sistema
- As playlists e gravações ficam no armazenamento local do navegador (IndexedDB), sem criptografia

Detalhes e como reportar problemas: [SECURITY.md](SECURITY.md).

## Tecnologia

HTML, CSS e JavaScript puros, Web Audio API (equalizador e visualizador), MediaRecorder (gravação), IndexedDB (playlists) e [JSZip](https://stuk.github.io/jszip/) 3.10.1 embutido para os arquivos ZIP.

## Licença

[MIT](LICENSE). O JSZip embutido é distribuído sob a licença MIT (dupla licença MIT/GPLv3).
