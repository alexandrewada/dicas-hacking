---
id: "0705"
categoria: "16-wireless"
familia: "wifi-evil-twin"
slug: "wps"
angulo: "evidencia"
mitre: "T1557"
owasp: ""
tags: ["16-wireless", "wifi-evil-twin", "evidencia", "t1557"]
aliases: ["WPS PIN", "wps", "wps-evidencia"]
---

# WPS PIN — evidência

Pacote pra WPS PIN sobreviver peer review.

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que precisa aparecer

- Se não validar **Se habilitado**, a nota fica genérica.

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

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (wps)
hash_prova: f4d161
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

- [WPS PIN](0325-wifi-evil-twin-wps.md)
- [teste de WIPS](0327-wifi-evil-twin-detect.md)
- [Evil twin / EAP sem validar cert](0323-wifi-evil-twin-eap.md)
- [guest isolation bypass](0329-wifi-evil-twin-guest.md)
- [IoT wifi default creds](0328-wifi-evil-twin-iot.md)