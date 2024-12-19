# como reportar risco RF — evidência

Pacote pra como reportar risco RF sobreviver peer review.

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que precisa aparecer

- **Sem dados de terceiros** — muda ruído e o que entra no PDF.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

SSID teste; credencial de tester; gap de detecção WIPS.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 047276

{"id":"ORD-7781","owner":"USER_A","note":"redacted-report"}
# capturado como USER_B
```

## Remediação junto

WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

## Se purple

WIPS rogue AP detection; 802.1X certificate validation training.

## Armadilha

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

## Refs

- OWASP wireless
- Aircrack docs ethics