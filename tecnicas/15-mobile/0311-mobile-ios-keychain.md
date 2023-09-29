# Keychain fraco

**Mobile** · `Mobile ATT&CK`

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Como eu faço

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## No lab ficou assim

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/keychain?token=TOKEN_LAB_8693d8'
# deep link / exported → token sink
```

## Diferencial desta nota

- Variante Keychain accessibility fraca: trato separado da família `mobile-ios`.

Falso amigo em Keychain accessibility fraca: UI/log gritam, impacto não. Exijo MDM policies.

## Onde já errei

Não contorne DRM de terceiros fora do escopo do app do cliente.

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

## Entrega

- blue: MDM policies; ATS force; keychain audit.
- fix: Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.
- proof: Artefato Keychain de teste; request API.

## Refs

- OWASP MASTG iOS