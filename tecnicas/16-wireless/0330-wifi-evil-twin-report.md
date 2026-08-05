---
id: "0330"
categoria: "16-wireless"
familia: "wifi-evil-twin"
slug: "report"
angulo: "base"
mitre: "T1557"
owasp: ""
tags: ["16-wireless", "wifi-evil-twin", "base", "t1557"]
aliases: ["como reportar risco RF", "report"]
---

# como reportar risco RF

**Wireless** · `T1557 AiTM`

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que muda aqui

- **Sem dados de terceiros** — muda ruído e o que entra no PDF.

## Como testo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## Sinal / query

```bash
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_report.conf # SSID LAB-728c88
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
```

## Campo

Beacon spoof sem associação autenticada é demo incompleta.

como reportar risco RF: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: WIPS rogue AP detection; 802.1X certificate validation training.

## Já me queimei

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

## Blue

- Detectar: WIPS rogue AP detection; 802.1X certificate validation training.
- Fechar: WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

## Evidência

SSID teste; credencial de tester; gap de detecção WIPS.

## Refs

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [Aircrack-ng documentation](https://www.aircrack-ng.org/doku.php)
- [HackTricks — WiFi](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi)

## Relacionadas

- [como reportar risco RF — evidência](0710-wifi-evil-twin-report--evidencia.md)
- [teste de WIPS](0327-wifi-evil-twin-detect.md)
- [Evil twin / EAP sem validar cert](0323-wifi-evil-twin-eap.md)
- [guest isolation bypass](0329-wifi-evil-twin-guest.md)
- [IoT wifi default creds](0328-wifi-evil-twin-iot.md)