# Security policy / Política de segurança

[English](#english) · [Português](#português)

---

## English

### Threat model

Tocador Minimalista runs entirely in the browser. There is no server, no account and no network traffic, and the player requests no device permissions (no microphone, camera or location). The relevant risks are: third-party code, malicious files imported by the user, and data stored locally.

### Protections

| Area | Protection |
|---|---|
| Third-party code | No CDN, web fonts or external resources. JSZip 3.10.1 is embedded unmodified; its SHA-256 is in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). Version 3.10.1 includes the fixes for CVE-2021-23413 (fixed in 3.7.0) and CVE-2022-48285 (fixed in 3.8.0) |
| Content Security Policy | `default-src 'none'`; scripts allowed only by SHA-256 hash (no `'unsafe-inline'` for scripts); `connect-src 'none'` blocks any data exfiltration; `form-action`, `base-uri`, `object-src` set to `'none'` |
| HTML injection (XSS) | User-controlled strings (file names, titles, playlist names) are always rendered with `textContent` |
| Name spoofing | Control characters, line breaks and bidi override characters (e.g. U+202E) are stripped; names are capped at 200 characters |
| Malicious ZIP | Max 1,000 entries, 512 MB per file, 2 GB total, 1 MB per M3U. Declared sizes are only a first filter: real bytes are counted while inflating and the import aborts when a limit is exceeded, so a ZIP that lies about its sizes is rejected too. Nothing is written to disk, so path traversal does not apply |
| Tampered storage | Playlists read from IndexedDB are validated (array of items, real `Blob`s, finite durations) and their metadata is rendered as text, since another page on the same origin could have written them |
| Exported M3U | Names are sanitized so a crafted file name cannot inject extra lines (e.g. remote URLs) into the playlist |
| Device permissions | The microphone recorder was removed in 1.1.0. The player asks for no permissions, and `Permissions-Policy` disables microphone, camera, geolocation, payment and USB |
| Storage | `navigator.storage.persist()` requested to avoid silent eviction; all storage calls fail safely |
| Hosting headers | `_headers` adds CSP with `frame-ancestors 'none'`, `Permissions-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, HSTS and COOP (Netlify / Cloudflare Pages) |

### Known risks

- **Unencrypted local data** — playlists (with their audio) are stored in the browser's IndexedDB. Anyone with access to your browser profile can read them.
- **Shared origin on GitHub Pages** — every GitHub Pages site of the same account (`<user>.github.io/<any-repo>`) shares one browser origin. Another Pages site of the same account can read the player's storage (saved playlists). The player shows a warning there. To isolate it, use a custom domain or a separate host (e.g. Netlify).
- **No custom headers on GitHub Pages** — `frame-ancestors` cannot be set via a meta tag. The player can therefore be embedded by other sites there; since it requests no permissions and stores nothing sensitive by default, the impact is limited to UI tricks.
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

O Tocador Minimalista roda inteiramente no navegador. Não há servidor, conta nem tráfego de rede, e o tocador não pede nenhuma permissão do aparelho (microfone, câmera ou localização). Os riscos relevantes são: código de terceiros, arquivos maliciosos importados pelo usuário e dados guardados localmente.

### Proteções

| Área | Proteção |
|---|---|
| Código de terceiros | Sem CDN, fontes da web ou recursos externos. O JSZip 3.10.1 vai embutido sem alterações; o SHA-256 está em [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). A versão 3.10.1 já tem as correções da CVE-2021-23413 (corrigida na 3.7.0) e da CVE-2022-48285 (corrigida na 3.8.0) |
| Política de segurança (CSP) | `default-src 'none'`; scripts liberados só por hash SHA-256 (sem `'unsafe-inline'` para scripts); `connect-src 'none'` impede envio de dados; `form-action`, `base-uri` e `object-src` como `'none'` |
| Injeção de HTML (XSS) | Textos controlados pelo usuário (nomes de arquivos, títulos, nomes de playlists) são sempre exibidos com `textContent` |
| Nomes falsificados | Caracteres de controle, quebras de linha e caracteres de inversão de direção (ex.: U+202E) são removidos; nomes limitados a 200 caracteres |
| ZIP malicioso | Máximo de 1.000 entradas, 512 MB por arquivo, 2 GB no total e 1 MB por M3U. O tamanho declarado no ZIP é só um primeiro filtro: os bytes reais são contados durante a descompactação e a importação é abortada ao passar do limite, então um ZIP que mente o tamanho também é recusado. Nada é gravado em disco, então *path traversal* não se aplica |
| Armazenamento adulterado | As playlists lidas do IndexedDB são validadas (lista de itens, `Blob` de verdade, durações numéricas) e os dados delas são exibidos como texto, já que outra página da mesma origem pode tê-las escrito |
| M3U exportado | Nomes higienizados para que um nome de arquivo malicioso não injete linhas extras (como URLs remotas) na playlist |
| Permissões do aparelho | O gravador pelo microfone foi removido na 1.1.0. O tocador não pede nenhuma permissão, e a `Permissions-Policy` desativa microfone, câmera, localização, pagamento e USB |
| Armazenamento | Pedido de `navigator.storage.persist()` para evitar exclusão silenciosa; falhas de armazenamento não quebram o tocador |
| Cabeçalhos de hospedagem | `_headers` adiciona CSP com `frame-ancestors 'none'`, `Permissions-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, HSTS e COOP (Netlify / Cloudflare Pages) |

### Riscos conhecidos

- **Dados locais sem criptografia** — playlists (com o áudio) ficam no IndexedDB do navegador. Quem tiver acesso ao seu perfil do navegador consegue lê-las.
- **Origem compartilhada no GitHub Pages** — todos os sites do GitHub Pages de uma mesma conta (`<usuario>.github.io/<qualquer-repo>`) compartilham a mesma origem no navegador. Outro site Pages da mesma conta pode ler o armazenamento do tocador (as playlists salvas). O tocador mostra um aviso nesse caso. Para isolar, use um domínio próprio ou outra hospedagem (ex.: Netlify).
- **GitHub Pages sem cabeçalhos personalizados** — `frame-ancestors` não pode ser definido por meta tag. Por isso, outros sites podem embutir o tocador ali; como ele não pede permissões e não guarda nada sensível por padrão, o impacto se limita a truques de interface.
- **Arquivo local (`file://`)** — o navegador pode compartilhar o armazenamento entre todos os HTML locais. O tocador mostra um aviso nesse caso.
- **Decodificadores de áudio** — a mídia importada é decodificada pelo navegador. Falhas nos decodificadores são responsabilidade do navegador; mantenha-o atualizado.
- **Metadados dos commits** — o e-mail usado nos commits do git fica público no GitHub. Use o endereço *no-reply* do GitHub se preferir mantê-lo privado.

### Como reportar uma vulnerabilidade

Use **Security → Report a vulnerability** (aviso privado) neste repositório. Para problemas não sensíveis, abra uma issue comum. Informe os passos para reproduzir, o navegador e a versão, e o impacto esperado.

### Versões com suporte

Apenas a versão mais recente da branch `main` recebe correções de segurança.
