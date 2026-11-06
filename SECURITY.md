# Segurança

## Modelo de ameaça

O Tocador Minimalista roda inteiramente no navegador. Não há servidor, login nem envio de dados. Os riscos relevantes são: código de terceiros, arquivos maliciosos importados pelo usuário, privacidade do microfone e dos dados guardados localmente.

## Proteções implementadas

| Área | Proteção |
|---|---|
| Código de terceiros | JSZip 3.10.1 embutido no arquivo (sem CDN); versão sem CVEs conhecidas abertas |
| Conexões externas | CSP com `connect-src 'none'`, `default-src 'none'`; apenas Google Fonts liberado |
| Injeção de HTML (XSS) | Nomes de faixas e playlists sempre inseridos como texto (`textContent`) |
| ZIP malicioso | Limites de 1.000 entradas, 512 MB por arquivo, 2 GB no total e 1 MB para a lista M3U; nada é gravado em disco, então path traversal não se aplica |
| M3U exportado | Caracteres de controle e quebras de linha removidos dos nomes |
| Microfone | Gravação só por clique; trava contra cliques repetidos; microfone fechado ao parar ou sair da página; o áudio do microfone não é enviado aos alto-falantes |
| Armazenamento | Pedido de armazenamento persistente para evitar perda de playlists |
| Hospedagem | `_headers` com CSP, `frame-ancestors 'none'`, `Permissions-Policy`, `X-Content-Type-Options`, `Referrer-Policy` e HSTS (Netlify/Cloudflare Pages) |

## Riscos conhecidos

- **Dados sem criptografia**: playlists e gravações ficam no IndexedDB do navegador. Quem tiver acesso ao seu perfil do navegador consegue lê-los.
- **Arquivo aberto do disco (`file://`)**: o navegador pode compartilhar o armazenamento entre páginas locais. O tocador exibe um aviso nesse caso. Prefira usar pela versão publicada em `https://`.
- **GitHub Pages** não permite cabeçalhos HTTP personalizados, então `frame-ancestors` (proteção contra clickjacking) não se aplica lá.
- **Google Fonts** recebe o IP de quem abre a página.

## Reportar uma vulnerabilidade

Abra uma issue privada pela aba **Security → Report a vulnerability** deste repositório, ou uma issue comum se não for sensível.
