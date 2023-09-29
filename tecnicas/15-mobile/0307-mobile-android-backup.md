# backup enabled

`T1420 / T1412 (mobile ATT&CK)`

## Por que importa

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## Variante

- Detalhe que pago pra ver: **adb backup data**.

## Passo a passo

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Exemplo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/backup?token=TOKEN_LAB_4a3c18'
# deep link / exported → token sink
```

## Nota de operador

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Armadilha

Não publique apps modificados. Respeite store ToS e escopo.

Falso amigo em backup enabled: UI/log gritam, impacto não. Exijo Mobile threat defense.

## Depois

Detecção — Mobile threat defense; RASP alerts; cert pinning telemetry.

Remediação — Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

No PDF — Componente explorado; dado acessado; API finding correlato.

## Refs

- OWASP MASVS/MASTG
- Frida docs