# captive portal credential harvest

`T1557 AiTM`

## Por que importa

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## Variante

- Se não validar **Testers only**, a nota fica genérica.

## Passo a passo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## Exemplo

```bash
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_portal.conf # SSID LAB-b53d60
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
```

## Nota de operador

ROE de RF por escrito: potência, canal, horário, área.

## Armadilha

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

Falso amigo em captive portal credential harvest: UI/log gritam, impacto não. Exijo WIPS rogue AP detection.

## Depois

Detecção — WIPS rogue AP detection; 802.1X certificate validation training.

Remediação — WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.

No PDF — SSID teste; credencial de tester; gap de detecção WIPS.

## Refs

- OWASP wireless
- Aircrack docs ethics