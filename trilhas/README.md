# Trilhas

Kill chains curadas — encadeiam notas do caderno fim a fim, com freio de OpSec e o que entra no relatório.

Não substituem o [índice](../indice/README.md). Servem pra quando você já tem um objetivo de engajamento e quer o caminho operacional, não a lista plana.

| Trilha | Objetivo |
|--------|----------|
| [AD: low-priv → DA](ad-lowpriv-to-da.md) | Kerberoast/AS-REP → BloodHound → DACL/ShadowCred → AD CS ESC → DCSync |
| [Web: recon → ATO](web-recon-to-ato.md) | Recon → IDOR/XSS/OAuth → session takeover |
| [API: BOLA → cross-tenant](api-bola-cross-tenant.md) | GraphQL/mass assignment/JWT → BOLA entre tenants |
| [AWS: enum → privesc IAM](aws-enum-iam-privesc.md) | S3/IMDS/SSRF → cadeia de roles |
| [Purple: do PoC à regra Sigma](purple-poc-to-sigma.md) | Técnica ofensiva → telemetria → detecção → hardening |

Cada trilha assume ROE escrito e escopo autorizado. Domínios de exemplo: `*.lab.local`.
