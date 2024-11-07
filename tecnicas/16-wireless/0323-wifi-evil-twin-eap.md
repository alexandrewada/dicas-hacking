# Evil twin / EAP sem validar cert

**Wireless** · `T1557 AiTM`

## Contexto

Evil twin captura credenciais de portais captivos e força downgrade.
Somente com autorização de RF e isolamento — pode afetar usuários reais.

## Como eu faço

1. Confirmar ROE RF e canal.
2. Levantar AP clone em lab/área isolada.
3. Capturo handshakes ou portal creds de **testers**.
4. Avalio EAP inadequado (PEAP sem validação).
5. Desligar AP e reportar.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger eap; evidência: auth USER_A + ação não destrutiva tag 6cf2a8
```

## Diferencial desta nota

- Signing/EPA/channel binding decidem se o relay vive.

EAP downgrade / relay: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: WIPS rogue AP detection; 802.1X certificate validation training.

## Onde já errei

Não opere jammers ilegais. Não capture tráfego de terceiros fora do escopo.

Capturo handshake/credencial de conta teste — não pulverizo o prédio.

## Entrega

- blue: WIPS rogue AP detection; 802.1X certificate validation training.
- fix: WPA2/3-Enterprise com validação de cert; PMF; disable auto-join guest.
- proof: SSID teste; credencial de tester; gap de detecção WIPS.

## Refs

- OWASP wireless
- Aircrack docs ethics