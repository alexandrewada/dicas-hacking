# WPA3 transition mode issues — evidência

Pacote pra WPA3 transition mode issues sobreviver peer review.

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que precisa aparecer

- Variante WPA3 transition mode issues: trato separado da família `wifi-evil-twin`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

SSID teste; credencial de tester; gap de detecção WIPS.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: a2cc36

{"id":"10042","owner":"USER_A","note":"redacted-wpa3"}
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