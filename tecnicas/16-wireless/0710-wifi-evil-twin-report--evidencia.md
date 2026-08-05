---
id: "0710"
categoria: "16-wireless"
familia: "wifi-evil-twin"
slug: "report"
angulo: "evidencia"
mitre: "T1557"
owasp: ""
tags: ["16-wireless", "wifi-evil-twin", "evidencia", "t1557"]
aliases: ["como reportar risco RF", "report", "report-evidencia"]
---

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

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [Aircrack-ng documentation](https://www.aircrack-ng.org/doku.php)
- [HackTricks — WiFi](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi)

## Relacionadas

- [como reportar risco RF](0330-wifi-evil-twin-report.md)
- [teste de WIPS](0327-wifi-evil-twin-detect.md)
- [Evil twin / EAP sem validar cert](0323-wifi-evil-twin-eap.md)
- [guest isolation bypass](0329-wifi-evil-twin-guest.md)
- [IoT wifi default creds](0328-wifi-evil-twin-iot.md)