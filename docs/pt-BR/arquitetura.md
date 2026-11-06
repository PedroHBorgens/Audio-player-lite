# Arquitetura

[English](../en/architecture.md) · **Português** · [← README](../../README.pt-BR.md)

## Visão geral

O tocador é **um único arquivo** (`index.html`) com HTML, CSS e JavaScript puros, sem build e sem dependências externas em tempo de execução. Ele contém dois blocos `<script>`:

1. **JSZip 3.10.1** embutido (minificado, sem alterações — veja o hash em [THIRD-PARTY-NOTICES.md](../../THIRD-PARTY-NOTICES.md)).
2. **O código do tocador**, dentro de uma função autoexecutável (IIFE) para não poluir o escopo global.

```
index.html
├── <style>        visual, variáveis das skins
├── <body>         janelas: principal, skins, equalizador, playlist
├── <script> #1    JSZip (terceiro)
└── <script> #2    tocador
     ├── cadeia de áudio (Web Audio API)
     ├── playlist e transporte
     ├── armazenamento (IndexedDB / localStorage)
     ├── exportar / importar (JSZip, M3U)
     ├── equalizador, skins, letreiro, visualizador
     └── arrastar e soltar, atalhos de teclado
```

## Cadeia de áudio

A reprodução usa um único `HTMLAudioElement`. Na primeira interação do usuário (exigência dos navegadores para áudio), o tocador cria um `AudioContext` e monta:

```
<audio> → MediaElementSource → GainNode (PRE)
        → 10 × BiquadFilter → StereoPanner (BAL) → AnalyserNode → saída
```

| Banda | Tipo de filtro |
|---|---|
| 60 Hz | `lowshelf` |
| 170 Hz a 14 kHz | `peaking`, Q = 1,1 |
| 16 kHz | `highshelf` |

- O ganho do PRE é convertido de dB para linear (`10^(dB/20)`).
- O **balanço** vai de −100 a +100 e é aplicado como `pan` de −1 a +1. Valores entre −10 e +10 viram 0 (trava magnética no centro); a barra é preenchida a partir do centro e o rótulo mostra `BAL ●`, `E n` ou `D n`. No celular, uma vibração curta avisa quando ele trava no centro.
- **EQ OFF** reconecta a cadeia sem o pré-amplificador e os filtros.
- O `AnalyserNode` (FFT de 1024, suavização 0,75) alimenta o visualizador: 28 barras em escala logarítmica sobre os primeiros 70% das frequências, com picos que caem devagar, ou a forma de onda no modo osciloscópio.
- Faixas sem duração conhecida (alguns WEBM informam `Infinity`) recebem um ajuste: o tocador manda a posição para o fim, lê a duração real e volta ao início.

## Playlist e transporte

Cada faixa é um objeto `{ name, fname, blob, url, dur, size }`. O `url` é um *object URL* (`blob:`) do arquivo, revogado quando a faixa é removida ou a lista é limpa. A duração é lida por um elemento `<audio>` auxiliar só de metadados.

Nomes de arquivos e títulos passam por `oneLine()`: remove caracteres de controle, quebras de linha e caracteres de direção de texto (bidi) e limita a 200 caracteres. Tudo que aparece na tela usa `textContent`, nunca `innerHTML` com dados do usuário.

## Armazenamento

### IndexedDB — banco `tocador`, versão 1

| Store | Chave | Valor |
|---|---|---|
| `files` | `"<nome-do-arquivo>|<tamanho>"` | `{ blob, fname }` |
| `lists` | `name` (keyPath) | `{ name, updated, items: [{ key, name, dur }] }` |

- Arquivos iguais em várias playlists são guardados **uma vez só** (mesma chave).
- Salvar guarda os arquivos e a lista numa única transação.
- Apagar uma lista também apaga os arquivos que nenhuma outra lista usa.
- Depois de salvar, o tocador chama `navigator.storage.persist()` para pedir que o navegador não apague os dados sozinho.

### localStorage

| Chave | Conteúdo |
|---|---|
| `tocador-skin` | id da skin escolhida |
| `tocador-last` | nome da última playlist aberta/salva, reaberta ao carregar |

Todo acesso a armazenamento está protegido por `try/catch`: se o navegador bloquear, o tocador continua funcionando sem salvar.

## Exportação e importação

**ZIP** — gerado com JSZip sem compressão (`STORE`), já que áudio não comprime. As faixas recebem prefixo numérico (`01 - `, `02 - `…) e um `playlist.m3u` é adicionado:

```
#EXTM3U
#EXTINF:215,Nome da faixa
01 - arquivo-original.mp3
```

A duração vai arredondada em segundos, ou `-1` se desconhecida.

**Download** — dentro do Claude, usa a capacidade `downloads` da plataforma (o usuário confirma). Fora dele, usa um link `<a download>` comum.

**Importação de ZIP** — o tocador:

1. Recusa ZIPs com mais de 1.000 entradas ou mais de 2 GB descompactados; ignora entradas acima de 512 MB e `.m3u` acima de 1 MB (usando o tamanho declarado no ZIP, antes de descompactar).
2. Ignora pastas, `__MACOSX` e arquivos ocultos.
3. Lê o `.m3u`, se houver, e ordena as faixas por ele; o resto entra em ordem alfabética.
4. Remove o prefixo numérico do nome e define o tipo MIME pela extensão.

Nada é gravado em disco, então caminhos maliciosos dentro do ZIP (`../`) não têm efeito.

## Skins

Cada skin é um conjunto de variáveis CSS aplicado por `data-skin` no elemento `<html>`:

`--bg`, `--panel`, `--panel2`, `--line`, `--text`, `--dim`, `--accent`, `--accent2`, `--lcd`, `--peak`

O visualizador (canvas) relê as cores ao trocar de skin. Para criar uma skin nova, adicione um bloco `[data-skin="id"]{…}` no CSS e uma entrada no array `SKINS` do JavaScript. Veja [CONTRIBUTING.md](../../CONTRIBUTING.md#português).

## Modelo de segurança

| Camada | Medida |
|---|---|
| CSP (meta tag) | `default-src 'none'`; scripts liberados **só por hash SHA-256**; `connect-src 'none'`; sem fontes, imagens ou mídia externas |
| Cabeçalhos HTTP (`_headers`) | Mesma CSP + `frame-ancestors 'none'`, `Permissions-Policy` (microfone, câmera e localização bloqueados), `X-Frame-Options`, `nosniff`, `no-referrer`, HSTS — aplicados no Netlify/Cloudflare Pages |
| Dados do usuário | Sempre exibidos como texto; nomes higienizados |
| Permissões | O tocador não usa microfone, câmera nem localização; `Permissions-Policy` bloqueia todos |
| Arquivos importados | Limites de tamanho e quantidade; nada escrito em disco |
| Terceiros | Nenhum recurso externo; JSZip embutido com hash documentado |

Como os scripts são liberados por hash, **qualquer alteração em um `<script>` exige recalcular a CSP** com `python3 tools/update-csp.py`. Sem isso, o navegador bloqueia o script e o tocador não funciona.

Riscos que continuam estão em [SECURITY.md](../../SECURITY.md#riscos-conhecidos).

## Compatibilidade

| Recurso | API |
|---|---|
| Equalizador e visualizador | Web Audio API (`AudioContext`, `BiquadFilterNode`, `StereoPannerNode`, `AnalyserNode`) |
| Playlists | IndexedDB, `navigator.storage.persist` |
| ZIP | JSZip (ArrayBuffer/Blob) |
| Sliders verticais do EQ | `writing-mode: vertical-lr` em `input[type=range]` |

Sem `StereoPannerNode`, o balanço é ignorado.
