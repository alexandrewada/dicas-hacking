# KARMA/known networks

`T1557 AiTM`

## Por que importa

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## Variante

- Variante KARMA/known networks: trato separado da família `wifi-evil-twin`.

## Passo a passo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## PoC mínimo

```bash
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_karma.conf # SSID LAB-24c543
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
```

## Nota de operador

Beacon spoof sem associação autenticada é demo incompleta.

## Armadilha

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

Falso amigo em KARMA/known networks: UI/log gritam, impacto não. Exijo WIPS rogue AP detection.

## Depois

Detecção — WIPS rogue AP detection; 802.1X certificate validation training.

Remediação — WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

No PDF — SSID teste; credencial de tester; gap de detecção WIPS.

## Refs

- OWASP wireless
- Aircrack docs ethics