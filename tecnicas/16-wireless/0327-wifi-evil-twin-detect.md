# teste de WIPS

**Wireless** · `T1557 AiTM`

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## O que muda aqui

- **Purple.** Sem isso o playbook da família mente.

## Como testo

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## No lab ficou assim

```bash
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_detect.conf # SSID LAB-2ee6aa
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
```

## Campo

Capturo handshake/credencial de conta teste — não pulverizo o prédio.

Falso amigo em teste de WIPS: UI/log gritam, impacto não. Exijo WIPS rogue AP detection.

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