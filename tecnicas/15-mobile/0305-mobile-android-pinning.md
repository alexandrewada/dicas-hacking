# pinning bypass lab

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

**Variante:** **Para testar API** — muda ruído e o que entra no PDF. Bypass em debug build ≠ ausência de pin na store.

**Método**

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## PoC mínimo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/pinning?token=TOKEN_LAB_5cd37a'
# deep link / exported → token sink
```

**Freio:** Não publique apps modificados. Respeite store ToS e escopo.

Já abri High demais em pinning bypass lab por sintoma sem efeito. Cruzei com: Mobile threat defense; RASP alerts; cert pinning telemetry. Sem side-effect, baixo.

Detecto via: Mobile threat defense; RASP alerts; cert pinning telemetry.

Corrijo com: Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

Levo no report: Componente explorado; dado acessado; API finding correlato.

Refs: OWASP MASVS/MASTG, Frida docs