# guest isolation bypass

**Wireless** · `T1557 AiTM`

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

**Variante:** Variante guest isolation bypass: trato separado da família `wifi-evil-twin`.

**Método**

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## PoC mínimo

```bash
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_guest.conf # SSID LAB-9a8833
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
```

**Freio:** Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

Falso amigo em guest isolation bypass: UI/log gritam, impacto não. Exijo WIPS rogue AP detection.

Detecto via: WIPS rogue AP detection; 802.1X certificate validation training.

Corrijo com: WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

Levo no report: SSID teste; credencial de tester; gap de detecção WIPS.

Refs: OWASP wireless, Aircrack docs ethics