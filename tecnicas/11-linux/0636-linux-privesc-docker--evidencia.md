# Abuso do grupo docker / sock — evidência

Pacote pra Abuso do grupo docker / sock sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- **Container escape path** — muda ruído e o que entra no PDF.
- Leitura de host FS ou create privilegiado. Cosmético de namespace não fecha.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Vetor; id antes/depois; artefato removido.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: f879dd

{"id":"obj_f879dd","owner":"USER_A","note":"redacted-docker"}
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