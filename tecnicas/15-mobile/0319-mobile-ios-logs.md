# os_log secrets

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante os_log secrets: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Exemplo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/logs?token=TOKEN_LAB_1f4b79'
# deep link / exported → token sink
```

## Nota de operador

Deep link / WebView / exported: intent até token sink é o ROI.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Já abri High demais em os_log secrets por sintoma sem efeito. Cruzei com: MDM policies; ATS force; keychain audit. Sem side-effect, baixo.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- OWASP MASTG iOS