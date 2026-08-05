---
id: "0145"
categoria: "05-injection"
familia: "inj-ssti"
slug: "pebble"
angulo: "base"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "base"]
aliases: ["Pebble", "pebble"]
---

# Pebble

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Detalhe

- Se não validar **Java templates**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Execução

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## PoC mínimo

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI pebble; sem RCE destrutivo — tag a7a343
```

## OpSec

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Cuidados

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Fechamento

| | |
|---|---|
| Detecção | RCE child processes; template render errors anômalos. |
| Remediação | Não renderizar templates com input não confiável; sandboxes atualizados; CSP. |
| Evidência | Engine identificado; PoC `id`; trecho de código vulnerável se fornecido. |

## Refs

- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [Pebble — lab](0525-inj-ssti-pebble--lab.md)
- [Pebble — hardening](0905-inj-ssti-pebble--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)