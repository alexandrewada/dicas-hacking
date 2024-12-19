# Evil twin / EAP sem validar cert — evidência

Pacote pra Evil twin / EAP sem validar cert sobreviver peer review.

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que precisa aparecer

- Signing/EPA/channel binding decidem se o relay vive.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

SSID teste; credencial de tester; gap de detecção WIPS.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 8c592b

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-eap"}
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