# URL scheme hijack

**Mobile** · `Mobile ATT&CK`

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que muda aqui

- Variante URL scheme hijack: trato separado da família `mobile-ios`.

## Como testo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## PoC mínimo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/url-scheme?token=TOKEN_LAB_1e2cd7'
# deep link / exported → token sink
```

## Campo

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

URL scheme hijack: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: MDM policies; ATS force; keychain audit.

## Já me queimei

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Blue

- Detectar: MDM policies; ATS force; keychain audit.
- Fechar: Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Evidência

Artefato Keychain de teste; request API.

## Refs

- OWASP MASTG iOS