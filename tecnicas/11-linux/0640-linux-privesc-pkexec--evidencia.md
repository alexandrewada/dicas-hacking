# polkit histórico — evidência

Pacote pra polkit histórico sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- Detalhe que pago pra ver: **Patch status**.

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
X-Request-Id: 165902

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-pkexec"}
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