---
id: "0328"
categoria: "16-wireless"
familia: "wifi-evil-twin"
slug: "iot"
angulo: "base"
mitre: "T1557"
owasp: ""
tags: ["16-wireless", "wifi-evil-twin", "base", "t1557"]
aliases: ["IoT wifi default creds", "iot"]
---

# IoT wifi default creds

**Wireless** · `T1557 AiTM`

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que muda aqui

- Variante IoT wifi default creds: trato separado da família `wifi-evil-twin`.

## Como testo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## Sinal / query

```bash
# RF lab — ROE escrito: canal/área/potência
# seguro: scan passivo
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon | tee wifi_50b977.log
# destrutivo só em lab isolado: hostapd evil twin SSID LAB-50b977
# NÃO pulverizar o prédio — iot
```

## Campo

ROE de RF por escrito: potência, canal, horário, área.

Falso amigo em IoT wifi default creds: UI/log gritam, impacto não. Exijo WIPS rogue AP detection.

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

- [IoT wifi default creds — evidência](0708-wifi-evil-twin-iot--evidencia.md)
- [teste de WIPS](0327-wifi-evil-twin-detect.md)
- [Evil twin / EAP sem validar cert](0323-wifi-evil-twin-eap.md)
- [guest isolation bypass](0329-wifi-evil-twin-guest.md)
- [KARMA/known networks](0322-wifi-evil-twin-karma.md)