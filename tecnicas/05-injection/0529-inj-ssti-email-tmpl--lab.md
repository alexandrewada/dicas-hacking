---
id: "0529"
categoria: "05-injection"
familia: "inj-ssti"
slug: "email-tmpl"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "lab"]
aliases: ["templates de e-mail marketing", "email-tmpl", "email-tmpl-lab"]
---

# templates de e-mail marketing — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- Se não validar **Muito comum**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## Sinal / query

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI email-tmpl; sem RCE destrutivo — tag dfd913
```

## Pitfall

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Prova do lab

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [templates de e-mail marketing — hardening](0909-inj-ssti-email-tmpl--hardening.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)