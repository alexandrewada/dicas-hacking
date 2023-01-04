# LD_PRELOAD / hijack — evidência

Pacote pra LD_PRELOAD / hijack sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- Variante LD_PRELOAD / hijack: trato separado da família `linux-privesc`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Vetor; id antes/depois; artefato removido.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: dc4e2d

{"id":"obj_dc4e2d","owner":"USER_A","note":"redacted-ld-preload"}
# capturado como USER_B
```

## Remediação junto

Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

## Se purple

Auditd execve; sudo logs; file integrity.

## Armadilha

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Refs

- GTFOBins
- HackTricks Linux PrivEsc