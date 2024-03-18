# clipboard leaks — evidência

Pacote pra clipboard leaks sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- Variante clipboard leaks: trato separado da família `mobile-android`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Componente explorado; dado acessado; API finding correlato.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 2ad066

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-clip"}
# capturado como USER_B
```

## Remediação junto

Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

## Se purple

Mobile threat defense; RASP alerts; cert pinning telemetry.

## Armadilha

Não publique apps modificados. Respeite store ToS e escopo.

## Refs

- OWASP MASVS/MASTG
- Frida docs