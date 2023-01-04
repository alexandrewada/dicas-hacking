# kernel exploit (lab) — evidência

Pacote pra kernel exploit (lab) sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- **CVE específico** — muda ruído e o que entra no PDF.

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

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: f101de

{"id":"ORD-7781","owner":"USER_A","note":"redacted-kernel"}
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