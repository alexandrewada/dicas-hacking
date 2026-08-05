---
id: "0706"
categoria: "16-wireless"
familia: "wifi-evil-twin"
slug: "wpa3"
angulo: "evidencia"
mitre: "T1557"
owasp: ""
tags: ["16-wireless", "wifi-evil-twin", "evidencia", "t1557"]
aliases: ["WPA3 transition mode issues", "wpa3", "wpa3-evidencia"]
---

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

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [Aircrack-ng documentation](https://www.aircrack-ng.org/doku.php)
- [HackTricks — WiFi](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi)

## Relacionadas

- [WPA3 transition mode issues](0326-wifi-evil-twin-wpa3.md)
- [teste de WIPS](0327-wifi-evil-twin-detect.md)
- [Evil twin / EAP sem validar cert](0323-wifi-evil-twin-eap.md)
- [guest isolation bypass](0329-wifi-evil-twin-guest.md)
- [IoT wifi default creds](0328-wifi-evil-twin-iot.md)