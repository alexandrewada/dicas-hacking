# app groups misuse

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante app groups misuse: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## No lab ficou assim

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/ipc?token=TOKEN_LAB_7a1e07'
# deep link / exported → token sink
```

## Nota de operador

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Falso amigo em app groups misuse: UI/log gritam, impacto não. Exijo MDM policies.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- OWASP MASTG iOS