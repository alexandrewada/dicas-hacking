# SSL kill switch lab

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante SSL kill switch lab: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Sinal / query

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/ssl?token=TOKEN_LAB_eada08'
# deep link / exported → token sink
```

## Nota de operador

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Antes de Critical em SSL kill switch lab, confiro se a telemetria que eu cobraria reagiria — MDM policies; ATS force; keychain audit.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- OWASP MASTG iOS