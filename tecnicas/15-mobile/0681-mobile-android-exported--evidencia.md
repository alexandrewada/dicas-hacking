# activity/service exported — evidência

Pacote pra activity/service exported sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- **IPC abuse.** Sem isso o playbook da família mente.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Componente explorado; dado acessado; API finding correlato.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (exported)
hash_prova: fb6a0f
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