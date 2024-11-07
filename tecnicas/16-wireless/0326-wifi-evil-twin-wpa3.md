# WPA3 transition mode issues

**Wireless** · `T1557 AiTM`

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que muda aqui

- Variante WPA3 transition mode issues: trato separado da família `wifi-evil-twin`.

## Como testo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## Sinal / query

```bash
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_wpa3.conf # SSID LAB-18503f
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
```

## Campo

Beacon spoof sem associação autenticada é demo incompleta.

Falso amigo em WPA3 transition mode issues: UI/log gritam, impacto não. Exijo WIPS rogue AP detection.

## Já me queimei

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

## Blue

- Detectar: WIPS rogue AP detection; 802.1X certificate validation training.
- Fechar: WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

## Evidência

SSID teste; credencial de tester; gap de detecção WIPS.

## Refs

- OWASP wireless
- Aircrack docs ethics