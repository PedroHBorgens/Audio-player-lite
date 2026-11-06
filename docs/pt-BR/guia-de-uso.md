# Guia de uso

[English](../en/user-guide.md) · **Português** · [← README](../../README.pt-BR.md)

## Sumário

1. [Abrindo o tocador](#1-abrindo-o-tocador)
2. [Adicionando músicas](#2-adicionando-músicas)
3. [Controles de reprodução](#3-controles-de-reprodução)
4. [Display e visualizador](#4-display-e-visualizador)
5. [Equalizador](#5-equalizador)
6. [Skins](#6-skins)
7. [Playlist](#7-playlist)
8. [Salvando playlists](#8-salvando-playlists)
9. [Exportando e importando](#9-exportando-e-importando)
10. [Gravando pelo microfone](#10-gravando-pelo-microfone)
11. [Atalhos de teclado](#11-atalhos-de-teclado)
12. [Privacidade: onde ficam seus dados](#12-privacidade-onde-ficam-seus-dados)
13. [Solução de problemas](#13-solução-de-problemas)

## 1. Abrindo o tocador

| Forma | Como | Gravação funciona? |
|---|---|---|
| Site publicado (GitHub Pages, Netlify…) | Abra o endereço `https://` no navegador | Sim, no computador e no celular |
| Arquivo local | Baixe o `index.html` e abra com dois cliques | Sim no computador; no celular normalmente não |

Dica: no celular, use **Adicionar à tela de início** no menu do navegador para abrir o tocador como um app.

## 2. Adicionando músicas

- Toque em **+ ADD** (na playlist) ou no botão de ejetar **⏏** (no painel principal) e escolha um ou vários arquivos.
- No computador, você também pode **arrastar arquivos** para qualquer lugar da janela.
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
| **REP** | Repetir a playlist inteira ao chegar ao fim |
| Barra de progresso | Arraste para ir a qualquer ponto da música |
| **VOL** | Volume |
| **BAL** | Balanço esquerdo/direito. Dê dois cliques para centralizar |

## 4. Display e visualizador

- **Relógio**: toque nele para alternar entre tempo **decorrido** e **restante** (aparece `REST`).
- **Status**: `▶ PLAY`, `❚❚ PAUSE`, `■ STOP` ou `● REC`.
- **Título**: rola sozinho quando o nome não cabe.
- **kbps**: taxa de bits estimada a partir do tamanho do arquivo e da duração.
- **Visualizador**: toque para alternar entre **barras de espectro** (com picos que caem devagar), **osciloscópio** e **desligado**. Durante uma gravação, ele mostra o som do microfone.

## 5. Equalizador

Toque em **EQ** para abrir.

- **10 bandas**: 60 Hz, 170 Hz, 310 Hz, 600 Hz, 1 kHz, 3 kHz, 6 kHz, 12 kHz, 14 kHz e 16 kHz, de −12 dB a +12 dB.
- **PRE**: pré-amplificador. Abaixe se o som distorcer depois de aumentar várias bandas.
- **Presets**: Flat, Rock, Pop, Jazz, Clássica, Eletrônica, Grave+, Agudo+, Voz e Fone.
- **ZERAR**: volta tudo a 0 dB. Dois cliques em uma banda zeram só ela.
- **ON/OFF** (no título da janela): liga e desliga o equalizador para comparar.

O equalizador vale também para as gravações e é aplicado em tempo real; ele **não altera** os arquivos exportados.

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

## 10. Gravando pelo microfone

1. Toque em **● REC**. Na primeira vez, o navegador pede permissão para o microfone.
2. A música pausa, o botão vira **■ PARAR** e pisca, e o display mostra o tempo gravado.
3. Toque em **■ PARAR**. A gravação entra no fim da playlist com o nome `Gravação DD/MM HH:MM:SS`.
4. Para não perdê-la, salve a playlist em **LISTAS** ou exporte em ZIP.

Detalhes:

- O formato depende do navegador: **WEBM/Opus** (Chrome, Edge, Firefox) ou **M4A/AAC** (Safari).
- Cancelamento de eco, redução de ruído e ganho automático ficam desligados, para gravar o som como ele é.
- O som do microfone não sai nos alto-falantes durante a gravação (sem microfonia).
- Gravações com menos de meio segundo são descartadas.
- O microfone é desligado ao parar ou ao sair da página.
- A gravação fica desativada se o tocador estiver dentro de outra página (iframe), para impedir que um site engane você a clicar em REC.

## 11. Atalhos de teclado

| Tecla | Ação | Tecla | Ação |
|---|---|---|---|
| `Z` | Anterior | `B` | Próxima |
| `X` | Tocar | `C` | Pausar |
| `V` | Parar | `Espaço` | Tocar/Pausar |
| `←` `→` | Voltar/avançar 5 s | `↑` `↓` | Volume |
| `S` | Aleatório | `R` | Repetir |
| `E` | Equalizador | `K` | Próxima skin |
| `L` | Abrir arquivos | | |

Os atalhos não funcionam enquanto você digita no campo de nome da playlist.

## 12. Privacidade: onde ficam seus dados

| Dado | Onde fica |
|---|---|
| Músicas adicionadas sem salvar | Só na memória da aba; somem ao fechar |
| Playlists salvas e gravações | IndexedDB do navegador, neste aparelho, sem criptografia |
| Skin escolhida e última playlist | `localStorage` do navegador |
| Qualquer coisa | **Nunca** é enviada pela internet |

Se o tocador estiver aberto como arquivo local ou em um endereço `*.github.io`, ele mostra um aviso em **LISTAS**, porque nesses casos outras páginas do mesmo lugar podem acessar o armazenamento. Detalhes em [SECURITY.md](../../SECURITY.md#riscos-conhecidos).

## 13. Solução de problemas

| Problema | Solução |
|---|---|
| A faixa não toca | O navegador não decodifica esse formato. Converta para MP3 ou tente outro navegador |
| Duração aparece `--:--` | O arquivo ainda está sendo lido, ou não informa a duração. Ela aparece ao tocar |
| "Permissão do microfone negada" | Libere o microfone para o site nas configurações do navegador (ícone de cadeado na barra de endereço) |
| "O microfone só funciona em https://" | Use a versão publicada (GitHub Pages) ou abra o arquivo local no computador |
| "Sem espaço no navegador" | O navegador limitou o armazenamento. Apague playlists antigas ou exporte em ZIP |
| As playlists sumiram | Os dados do navegador foram limpos, ou você abriu o tocador por outro endereço/navegador. Cada endereço tem o próprio armazenamento |
| O som distorce com o EQ | Abaixe o **PRE** |
| Os atalhos não respondem | Clique em uma área vazia do tocador para tirar o foco de campos e menus |
