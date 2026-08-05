# dicas-hacking

Caderno operacional de pentest autorizado — **Alexandre Riuti Wada**.

Não é curso introdutório. Cada nota assume que você já conhece a família e precisa do que muda o jogo no engajamento: variante, OpSec, falso positivo, detecção, remediação e evidência que sobrevive peer review.

Leia o [aviso](DISCLAIMER.md) antes de qualquer coisa.

## Números

| | |
|--|--|
| Notas | **1000** |
| Categorias | **20** (`tecnicas/01-recon` … `tecnicas/20-report`) |
| Ângulos | base + **detecção**, **lab**, **evidência**, **path**, **hardening** |

Recon → report, passando por web/API, auth, injection, client-side, SSRF/XXE, rede, AD, Windows/Linux, AWS/Azure, k8s, mobile, wireless, red/purple e TLS.

## Como navegar

1. **[Índice](indice/README.md)** — lista por categoria.
2. **[Trilhas](trilhas/README.md)** — kill chains fim a fim (comece por aqui se tem um objetivo claro):

| Trilha | Caminho |
|--------|---------|
| [AD: low-priv → DA](trilhas/ad-lowpriv-to-da.md) | Kerberoast/AS-REP → BloodHound → DACL/ShadowCred → AD CS → DCSync |
| [Web: recon → ATO](trilhas/web-recon-to-ato.md) | Recon → IDOR/XSS/OAuth → session takeover |
| [API: BOLA → cross-tenant](trilhas/api-bola-cross-tenant.md) | GraphQL / mass assignment / JWT → BOLA |
| [AWS: enum → privesc IAM](trilhas/aws-enum-iam-privesc.md) | S3 / IMDS / SSRF → role chain |
| [Purple: PoC → Sigma](trilhas/purple-poc-to-sigma.md) | Técnica ofensiva → telemetria → regra → hardening |

Tom de caderno de engajamento: 1ª pessoa, ROE explícito, domínios `*.lab.local`, sem dump massivo no PDF.

## Padrão de qualidade

- **OpSec** — ruído, honeypot, quando parar; não “assa a floresta”.
- **ROE** — o que está autorizado; freio antes de write destrutivo / DCSync / IMDS em prod.
- **Evidência** — prova mínima reproduzível; PII mascarada; peer review consegue seguir o path.
- **Purple** — detecção e hardening andam com a técnica ofensiva, não como apêndice decorativo.

## Contribuir

Correção técnica, referência atualizada, PoC de lab mais claro: bem-vindo.

Fluxo e anatomia da nota: **[CONTRIBUTING.md](CONTRIBUTING.md)**.

Preferência por PRs pequenos. Antes de abrir: `make build && make audit`.

Malware, exploit kit ou conteúdo pra acesso sem autorização: não.

## Autor

Alexandre Riuti Wada  
https://github.com/alexandrewada  
alexandre.rwada@gmail.com

## License

[MIT](LICENSE)
