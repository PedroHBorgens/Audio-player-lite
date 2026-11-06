# Contributing / Como contribuir

[English](#english) · [Português](#português)

---

## English

Thanks for your interest! Bug reports, ideas and pull requests are welcome.

### Before you start

- The project is licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE). By submitting a contribution, you agree that it will be distributed under the same license.
- Keep the core principles: **single file, no build step, no external requests, no tracking**.

### Development workflow

1. Fork and clone the repository.
2. Edit `index.html`.
3. **If you changed any `<script>` block, regenerate the Content Security Policy:**
   ```bash
   python3 tools/update-csp.py
   ```
   Scripts are allowed by SHA-256 hash, so a stale hash means the browser blocks the script and the player stops working. Use `python3 tools/update-csp.py --check` to verify (exit code 1 if out of date).
4. Test locally through a web server:
   ```bash
   python3 -m http.server 8000
   # open http://localhost:8000
   ```
5. Run through the checklist below, then open a pull request describing what changed and why.

### Test checklist

- [ ] Add files with **+ ADD**, a folder with **+ PASTA**, and files/folders by drag and drop; play, pause, stop, previous/next, seek
- [ ] Repeat: off → playlist → track; in track mode the song restarts
- [ ] Equalizer presets, PRE, ON/OFF; balance snaps to center and the label recenters it; all 6 skins (including the light **Papel** skin)
- [ ] Save, reload the page, reopen and delete a playlist
- [ ] Export ZIP and M3U; import the exported ZIP back
- [ ] Browser console shows no errors and no CSP violations
- [ ] DevTools → Network shows **no external requests**
- [ ] Mobile viewport (about 380 px wide)

### Code guidelines

- Never insert user-controlled data with `innerHTML`; use `textContent`.
- Pass every file name or title through `oneLine()`.
- Wrap storage calls (`localStorage`, `IndexedDB`) in `try/catch`.
- Do not add dependencies loaded from a CDN. If a library is essential, embed it, record its source and SHA-256 in `THIRD-PARTY-NOTICES.md`, and check its license is compatible.
- Do not add features that request device permissions (microphone, camera, location). The recorder was removed on purpose to keep the attack surface minimal.

### Adding a skin

1. CSS: add a block defining all variables:
   ```css
   [data-skin="myskin"]{--bg:#…;--panel:#…;--panel2:#…;--line:#…;--text:#…;--dim:#…;--accent:#…;--accent2:#…;--lcd:#…;--peak:#…}
   ```
2. JavaScript: add an entry to the `SKINS` array: `{id:'myskin', nome:'My Skin', c:[bg, panel, accent, accent2]}` (the four colors are the swatch).
3. Check text contrast against `--panel` and `--lcd`, then run `tools/update-csp.py`.

### Reporting bugs

Open an issue with: what you did, what you expected, what happened, browser/OS and version. For security problems, see [SECURITY.md](SECURITY.md).

---

## Português

Obrigado pelo interesse! Relatos de bugs, ideias e pull requests são bem-vindos.

### Antes de começar

- O projeto é licenciado sob a [PolyForm Noncommercial License 1.0.0](LICENSE). Ao enviar uma contribuição, você concorda que ela seja distribuída sob a mesma licença.
- Mantenha os princípios: **um único arquivo, sem etapa de build, sem requisições externas, sem rastreamento**.

### Fluxo de desenvolvimento

1. Faça um fork e clone o repositório.
2. Edite o `index.html`.
3. **Se alterou qualquer bloco `<script>`, gere de novo a política de segurança (CSP):**
   ```bash
   python3 tools/update-csp.py
   ```
   Os scripts são liberados por hash SHA-256; com o hash desatualizado, o navegador bloqueia o script e o tocador para de funcionar. Use `python3 tools/update-csp.py --check` para conferir (sai com código 1 se estiver desatualizada).
4. Teste localmente por um servidor web:
   ```bash
   python3 -m http.server 8000
   # abra http://localhost:8000
   ```
5. Siga a lista abaixo e abra um pull request explicando o que mudou e por quê.

### Lista de testes

- [ ] Adicionar arquivos pelo **+ ADD**, uma pasta pelo **+ PASTA**, e arquivos/pastas arrastando; tocar, pausar, parar, anterior/próxima, barra de progresso
- [ ] Repetir: desligado → lista → faixa; no modo faixa a música recomeça
- [ ] Presets do equalizador, PRE, ON/OFF; balanço trava no centro e o rótulo recentraliza; as 6 skins (inclusive a clara, **Papel**)
- [ ] Salvar, recarregar a página, reabrir e apagar uma playlist
- [ ] Exportar ZIP e M3U; importar de volta o ZIP exportado
- [ ] Console do navegador sem erros e sem violações de CSP
- [ ] DevTools → Network **sem requisições externas**
- [ ] Tela de celular (cerca de 380 px de largura)

### Regras de código

- Nunca insira dados do usuário com `innerHTML`; use `textContent`.
- Passe todo nome de arquivo ou título por `oneLine()`.
- Proteja acessos a armazenamento (`localStorage`, `IndexedDB`) com `try/catch`.
- Não adicione dependências carregadas de CDN. Se uma biblioteca for essencial, embuta-a, registre origem e SHA-256 em `THIRD-PARTY-NOTICES.md` e confira se a licença é compatível.
- Não adicione recursos que peçam permissões do aparelho (microfone, câmera, localização). O gravador foi removido de propósito para manter a superfície de ataque mínima.

### Criando uma skin

1. CSS: adicione um bloco com todas as variáveis:
   ```css
   [data-skin="minhaskin"]{--bg:#…;--panel:#…;--panel2:#…;--line:#…;--text:#…;--dim:#…;--accent:#…;--accent2:#…;--lcd:#…;--peak:#…}
   ```
2. JavaScript: adicione uma entrada no array `SKINS`: `{id:'minhaskin', nome:'Minha Skin', c:[bg, panel, accent, accent2]}` (as quatro cores formam a amostra).
3. Confira o contraste do texto sobre `--panel` e `--lcd` e rode `tools/update-csp.py`.

### Reportando bugs

Abra uma issue com: o que você fez, o que esperava, o que aconteceu, navegador/sistema e versão. Para problemas de segurança, veja [SECURITY.md](SECURITY.md#português).
