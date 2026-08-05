---
id: "0324"
categoria: "16-wireless"
familia: "wifi-evil-twin"
slug: "pmkid"
angulo: "base"
mitre: "T1557"
owasp: ""
tags: ["16-wireless", "wifi-evil-twin", "base", "t1557"]
aliases: ["PMKID capture", "pmkid"]
---

# PMKID capture

`T1557 AiTM`

## Por que importa

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## Variante

- **Offline crack autorizado** — muda ruído e o que entra no PDF.

## Passo a passo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## PoC mínimo

```bash
# RF lab — ROE escrito: canal/área/potência
# seguro: scan passivo
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon | tee wifi_5154a0.log
# destrutivo só em lab isolado: hostapd evil twin SSID LAB-5154a0
# NÃO pulverizar o prédio — pmkid
```

## Nota de operador

ROE de RF por escrito: potência, canal, horário, área.

## Armadilha

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

PMKID capture: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: WIPS rogue AP detection; 802.1X certificate validation training.

## Depois

Detecção — WIPS rogue AP detection; 802.1X certificate validation training.

Remediação — WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

No PDF — SSID teste; credencial de tester; gap de detecção WIPS.

## Refs

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [Aircrack-ng documentation](https://www.aircrack-ng.org/doku.php)
- [HackTricks — WiFi](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi)

## Relacionadas

- [PMKID capture — evidência](0704-wifi-evil-twin-pmkid--evidencia.md)
- [teste de WIPS](0327-wifi-evil-twin-detect.md)
- [Evil twin / EAP sem validar cert](0323-wifi-evil-twin-eap.md)
- [guest isolation bypass](0329-wifi-evil-twin-guest.md)
- [IoT wifi default creds](0328-wifi-evil-twin-iot.md)