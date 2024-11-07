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
# RF lab — ROE por escrito, canal/área fixos
hostapd ./lab_pmkid.conf # SSID LAB-5154a0
# capturar cred de USER_A em portal de teste; sem pulverizar o prédio
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

- OWASP wireless
- Aircrack docs ethics