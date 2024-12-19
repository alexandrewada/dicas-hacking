# PMKID capture — evidência

Pacote pra PMKID capture sobreviver peer review.

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que precisa aparecer

- **Offline crack autorizado** — muda ruído e o que entra no PDF.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

SSID teste; credencial de tester; gap de detecção WIPS.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (pmkid)
hash_prova: dd3af0
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