# Security policy / Política de segurança

[English](#english) · [Português](#português)

---

## English

### Threat model

Tocador Minimalista runs entirely in the browser. There is no server, no account and no network traffic. The relevant risks are: third-party code, malicious files imported by the user, microphone privacy, and data stored locally.

### Protections

| Area | Protection |
|---|---|
| Third-party code | No CDN, web fonts or external resources. JSZip 3.10.1 is embedded unmodified; its SHA-256 is in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). Version 3.10.1 includes the fixes for CVE-2021-23413 (fixed in 3.7.0) and CVE-2022-48285 (fixed in 3.8.0) |
| Content Security Policy | `default-src 'none'`; scripts allowed only by SHA-256 hash (no `'unsafe-inline'` for scripts); `connect-src 'none'` blocks any data exfiltration; `form-action`, `base-uri`, `object-src` set to `'none'` |
| HTML injection (XSS) | User-controlled strings (file names, titles, playlist names) are always rendered with `textContent` |
| Name spoofing | Control characters, line breaks and bidi override characters (e.g. U+202E) are stripped; names are capped at 200 characters |
| Malicious ZIP | Max 1,000 entries, 512 MB per file, 2 GB total, 1 MB per M3U, checked before inflating. Nothing is written to disk, so path traversal does not apply |
| Exported M3U | Names are sanitized so a crafted file name cannot inject extra lines (e.g. remote URLs) into the playlist |
| Microphone | Starts only on click (no shortcut); lock against repeated clicks; released on stop or `pagehide`; never routed to speakers; disabled when framed (clickjacking) |
| Storage | `navigator.storage.persist()` requested to avoid silent eviction; all storage calls fail safely |
| Hosting headers | `_headers` adds CSP with `frame-ancestors 'none'`, `Permissions-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, HSTS and COOP (Netlify / Cloudflare Pages) |

### Known risks

- **Unencrypted local data** — playlists and recordings are stored in the browser's IndexedDB. Anyone with access to your browser profile can read them.
- **Shared origin on GitHub Pages** — every GitHub Pages site of the same account (`<user>.github.io/<any-repo>`) shares one browser origin. Another Pages site of the same account can read the player's storage (including recordings) and reuse the microphone permission. The player shows a warning there. To isolate it, use a custom domain or a separate host (e.g. Netlify).
- **No custom headers on GitHub Pages** — `frame-ancestors` cannot be set via a meta tag. The player compensates by disabling recording when framed, but playback controls could still be framed.
- **Local file (`file://`)** — browsers may share storage between all local HTML files. The player shows a warning in this case.
- **Audio decoders** — imported media is decoded by the browser. Decoder vulnerabilities are the browser's responsibility; keep your browser up to date.
- **Commit metadata** — the e-mail address used in git commits is public on GitHub. Use your GitHub no-reply address if you prefer to keep it private.

### Reporting a vulnerability

Please use **Security → Report a vulnerability** (private advisory) on this repository. For non-sensitive issues, open a regular issue. Include steps to reproduce, browser and version, and the impact you expect.

### Supported versions

Only the latest version on the `main` branch receives security fixes.

---

## Português

### Modelo de ameaça

O Tocador Minimalista roda inteiramente no navegador. Não há servidor, conta nem tráfego de rede. Os riscos relevantes são: código de terceiros, arquivos maliciosos importados pelo usuário, privacidade do microfone e dados guardados localmente.

### Proteções

| Área | Proteção |
|---|---|
| Código de terceiros | Sem CDN, fontes da web ou recursos externos. O JSZip 3.10.1 vai embutido sem alterações; o SHA-256 está em [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). A versão 3.10.1 já tem as correções da CVE-2021-23413 (corrigida na 3.7.0) e da CVE-2022-48285 (corrigida na 3.8.0) |
| Política de segurança (CSP) | `default-src 'none'`; scripts liberados só por hash SHA-256 (sem `'unsafe-inline'` para scripts); `connect-src 'none'` impede envio de dados; `form-action`, `base-uri` e `object-src` como `'none'` |
| Injeção de HTML (XSS) | Textos controlados pelo usuário (nomes de arquivos, títulos, nomes de playlists) são sempre exibidos com `textContent` |
| Nomes falsificados | Caracteres de controle, quebras de linha e caracteres de inversão de direção (ex.: U+202E) são removidos; nomes limitados a 200 caracteres |
| ZIP malicioso | Máximo de 1.000 entradas, 512 MB por arquivo, 2 GB no total e 1 MB por M3U, verificados antes de descompactar. Nada é gravado em disco, então *path traversal* não se aplica |
| M3U exportado | Nomes higienizados para que um nome de arquivo malicioso não injete linhas extras (como URLs remotas) na playlist |
| Microfone | Só começa por clique (sem atalho); trava contra cliques repetidos; liberado ao parar ou em `pagehide`; nunca enviado aos alto-falantes; desativado dentro de iframe (clickjacking) |
| Armazenamento | Pedido de `navigator.storage.persist()` para evitar exclusão silenciosa; falhas de armazenamento não quebram o tocador |
| Cabeçalhos de hospedagem | `_headers` adiciona CSP com `frame-ancestors 'none'`, `Permissions-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, HSTS e COOP (Netlify / Cloudflare Pages) |

### Riscos conhecidos

- **Dados locais sem criptografia** — playlists e gravações ficam no IndexedDB do navegador. Quem tiver acesso ao seu perfil do navegador consegue lê-las.
- **Origem compartilhada no GitHub Pages** — todos os sites do GitHub Pages de uma mesma conta (`<usuario>.github.io/<qualquer-repo>`) compartilham a mesma origem no navegador. Outro site Pages da mesma conta pode ler o armazenamento do tocador (incluindo gravações) e reaproveitar a permissão do microfone. O tocador mostra um aviso nesse caso. Para isolar, use um domínio próprio ou outra hospedagem (ex.: Netlify).
- **GitHub Pages sem cabeçalhos personalizados** — `frame-ancestors` não pode ser definido por meta tag. O tocador compensa desativando a gravação dentro de iframes, mas os controles de reprodução ainda podem ser embutidos.
- **Arquivo local (`file://`)** — o navegador pode compartilhar o armazenamento entre todos os HTML locais. O tocador mostra um aviso nesse caso.
- **Decodificadores de áudio** — a mídia importada é decodificada pelo navegador. Falhas nos decodificadores são responsabilidade do navegador; mantenha-o atualizado.
- **Metadados dos commits** — o e-mail usado nos commits do git fica público no GitHub. Use o endereço *no-reply* do GitHub se preferir mantê-lo privado.

### Como reportar uma vulnerabilidade

Use **Security → Report a vulnerability** (aviso privado) neste repositório. Para problemas não sensíveis, abra uma issue comum. Informe os passos para reproduzir, o navegador e a versão, e o impacto esperado.

### Versões com suporte

Apenas a versão mais recente da branch `main` recebe correções de segurança.
