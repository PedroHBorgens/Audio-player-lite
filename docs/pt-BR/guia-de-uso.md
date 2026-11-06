# Guia de uso

[English](../en/user-guide.md) · **Português** · [← README](../../README.pt-BR.md)

## Sumário

- [Idioma](#idioma)
1. [Abrindo o tocador](#1-abrindo-o-tocador)
2. [Adicionando músicas](#2-adicionando-músicas)
3. [Controles de reprodução](#3-controles-de-reprodução)
4. [Display e visualizador](#4-display-e-visualizador)
5. [Equalizador](#5-equalizador)
6. [Skins](#6-skins)
7. [Playlist](#7-playlist)
8. [Salvando playlists](#8-salvando-playlists)
9. [Exportando e importando](#9-exportando-e-importando)
10. [Atalhos de teclado](#10-atalhos-de-teclado)
11. [Privacidade: onde ficam seus dados](#11-privacidade-onde-ficam-seus-dados)
12. [Solução de problemas](#12-solução-de-problemas)

## Idioma

Toque em **PT** ou **EN** no canto superior direito da janela principal para trocar toda a interface entre português do Brasil e inglês — botões, dicas, mensagens, nomes de skins e de presets. A escolha fica salva no navegador; na primeira visita, o tocador segue o idioma do navegador (português se ele estiver em português, inglês nos demais casos).

## 1. Abrindo o tocador

| Forma | Como |
|---|---|
| Site publicado (GitHub Pages, Netlify…) | Abra o endereço `https://` no navegador, no computador ou no celular |
| Arquivo local | Baixe o `index.html` e abra com dois cliques |

Dica: no celular, use **Adicionar à tela de início** no menu do navegador para abrir o tocador como um app.

## 2. Adicionando músicas

- Toque em **+ ADD** (na playlist) ou no botão de ejetar **⏏** (no painel principal) e escolha um ou vários arquivos.
- Toque em **+ PASTA** (ou tecla `P`) e escolha uma **pasta inteira**: todos os arquivos de áudio dentro dela, inclusive em subpastas, entram na playlist em **ordem natural** pelo caminho (`2 - …` antes de `10 - …`). Arquivos que não são áudio e pastas ou arquivos ocultos (começando com `.`) são ignorados. Até 2.000 faixas por pasta.
- No computador, você também pode **arrastar arquivos ou pastas** para qualquer lugar da janela.

Ao escolher uma pasta, alguns navegadores perguntam se você quer "enviar" os arquivos ao site. **Nada é enviado**: o tocador só lê os arquivos no seu aparelho. Em celulares, a escolha de pasta depende do navegador; se a opção não aparecer, use **+ ADD** e selecione vários arquivos.

A playlist aceita até 5.000 faixas.
- Também é possível adicionar um **ZIP exportado pelo tocador** (ou qualquer ZIP com músicas) — veja a [seção 9](#9-exportando-e-importando).

Formatos aceitos: MP3, WAV, OGG, FLAC, M4A, AAC, OPUS e WEBM. Se o navegador não conseguir decodificar um arquivo, a faixa aparece na lista mas não toca.

## 3. Controles de reprodução

| Botão | Função |
|---|---|
| ⏮ | Faixa anterior. Se a música já passou de 3 segundos, volta ao início dela |
| ▶ / ❚❚ | Tocar / pausar |
| ■ | Parar e voltar ao início |
| ⏭ | Próxima faixa |
| **SHUF** | Ordem aleatória (aceso = ligado) |
| **REP** | Cada toque troca o modo: **desligado** → **lista inteira** (aceso com um **∞** no canto, `↻` no display) → **só esta faixa** (aceso com um **1** no canto, `↻1` no display). Em "só esta faixa", a música recomeça ao terminar; os botões ⏮ ⏭ continuam trocando de faixa |
| Barra de progresso | Arraste para ir a qualquer ponto da música |
| **VOL** | Volume |
| **BAL** | Balanço esquerdo/direito. Tem uma marca no centro e uma trava magnética: perto do meio, ele "gruda" no centro. O rótulo mostra `BAL ●` (centro), `E 40` (esquerda) ou `D 25` (direita); **toque no rótulo** ou dê dois cliques no controle para voltar ao centro |

## 4. Display e visualizador

- **Relógio**: toque nele para alternar entre tempo **decorrido** e **restante** (aparece `REST`).
- **Status**: `▶ PLAY`, `❚❚ PAUSE` ou `■ STOP`.
- **Título**: rola sozinho quando o nome não cabe.
- **kbps**: taxa de bits estimada a partir do tamanho do arquivo e da duração.
- **Visualizador**: toque para alternar entre **barras de espectro** (com picos que caem devagar), **osciloscópio** e **desligado**.

## 5. Equalizador

Toque em **EQ** para abrir.

- **10 bandas**: 60 Hz, 170 Hz, 310 Hz, 600 Hz, 1 kHz, 3 kHz, 6 kHz, 12 kHz, 14 kHz e 16 kHz, de −12 dB a +12 dB.
- **PRE**: pré-amplificador. Abaixe se o som distorcer depois de aumentar várias bandas.
- **Presets**: Flat, Rock, Pop, Jazz, Clássica, Eletrônica, Grave+, Agudo+, Voz e Fone.
- **ZERAR**: volta tudo a 0 dB. Dois cliques em uma banda zeram só ela.
- **ON/OFF** (no título da janela): liga e desliga o equalizador para comparar.

O equalizador é aplicado em tempo real; ele **não altera** os arquivos exportados.

## 6. Skins

Toque em **SKIN** e escolha uma das seis: **Clássico** (verde), **Âmbar**, **Oceano**, **Synthwave**, **Papel** (tema claro) e **Grafite** (preto e branco). A tecla `K` passa para a próxima. A escolha fica salva no navegador.

## 7. Playlist

- Toque em uma faixa para tocá-la. A faixa atual fica destacada.
- Passe o mouse sobre uma faixa e toque em **×** para removê-la.
- **LIMPAR** esvazia a lista atual (não apaga playlists salvas).
- O rodapé mostra o número de faixas e a duração total.

## 8. Salvando playlists

Toque em **LISTAS**.

1. Digite um nome e toque em **SALVAR** (ou Enter). Salvar com um nome que já existe **substitui** aquela playlist.
2. Em *Playlists salvas*, use **ABRIR** para carregar e **×** para apagar (toque duas vezes para confirmar).

As **músicas são guardadas junto** com a lista, então você não precisa adicioná-las de novo. A última playlist aberta ou salva reabre sozinha quando você volta ao tocador.

Tudo fica **apenas neste navegador e neste aparelho**. Limpar os dados de navegação apaga as playlists. Para levar para outro aparelho, use a exportação em ZIP.

## 9. Exportando e importando

Toque em **EXPORTAR**.

- **ZIP · MÚSICAS + M3U**: gera um ZIP com as músicas numeradas na ordem (`01 - nome.mp3`, `02 - …`) e um `playlist.m3u`. Esse ZIP abre em outros players e pode ser **importado de volta** pelo **+ ADD**, mantendo ordem e títulos.
- **SÓ A LISTA (M3U)**: gera só a lista, com os nomes dos arquivos originais. É salva como `.m3u.txt`; renomeie para `.m3u` para usar em outros players (eles precisam encontrar os arquivos de áudio na mesma pasta).

Ao importar um ZIP, o tocador segue a ordem do `.m3u` dentro dele; faixas que não estão no `.m3u` entram depois, em ordem alfabética. Por segurança, ZIPs com mais de 1.000 arquivos, músicas acima de 512 MB ou mais de 2 GB no total são recusados.

Dentro do Claude, o navegador pede confirmação antes de salvar o arquivo exportado.

## 10. Atalhos de teclado

| Tecla | Ação | Tecla | Ação |
|---|---|---|---|
| `Z` | Anterior | `B` | Próxima |
| `X` | Tocar | `C` | Pausar |
| `V` | Parar | `Espaço` | Tocar/Pausar |
| `←` `→` | Voltar/avançar 5 s | `↑` `↓` | Volume |
| `S` | Aleatório | `R` | Repetir: desligado → lista → faixa |
| `E` | Equalizador | `K` | Próxima skin |
| `L` | Abrir arquivos | `P` | Adicionar pasta |

Os atalhos não funcionam enquanto você digita no campo de nome da playlist.

## 11. Privacidade: onde ficam seus dados

| Dado | Onde fica |
|---|---|
| Músicas adicionadas sem salvar | Só na memória da aba; somem ao fechar |
| Playlists salvas | IndexedDB do navegador, neste aparelho, sem criptografia |
| Skin escolhida e última playlist | `localStorage` do navegador |
| Qualquer coisa | **Nunca** é enviada pela internet |

Se o tocador estiver aberto como arquivo local ou em um endereço `*.github.io`, ele mostra um aviso em **LISTAS**, porque nesses casos outras páginas do mesmo lugar podem acessar o armazenamento. Detalhes em [SECURITY.md](../../SECURITY.md#riscos-conhecidos).

## 12. Solução de problemas

| Problema | Solução |
|---|---|
| A faixa não toca | O navegador não decodifica esse formato. Converta para MP3 ou tente outro navegador |
| Duração aparece `--:--` | O arquivo ainda está sendo lido, ou não informa a duração. Ela aparece ao tocar |
| "Sem espaço no navegador" | O navegador limitou o armazenamento. Apague playlists antigas ou exporte em ZIP |
| As playlists sumiram | Os dados do navegador foram limpos, ou você abriu o tocador por outro endereço/navegador. Cada endereço tem o próprio armazenamento |
| O som distorce com o EQ | Abaixe o **PRE** |
| "Reprodução parada: as faixas estão terminando rápido demais" | Proteção contra repetição sem fim: se 3 faixas seguidas terminam em menos de meio segundo, o tocador para. Acontece com arquivos vazios ou corrompidos |
| O botão **+ PASTA** não abre a pasta no celular | Nem todo navegador de celular permite escolher pastas. Use **+ ADD** e selecione vários arquivos |
| Não consigo deixar o balanço em um valor pequeno (1 a 10) | É a trava magnética do centro: valores até 10 para cada lado voltam para o meio, de propósito |
| Os atalhos não respondem | Clique em uma área vazia do tocador para tirar o foco de campos e menus |
