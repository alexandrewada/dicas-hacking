---
id: "0149"
categoria: "05-injection"
familia: "inj-ssti"
slug: "email-tmpl"
angulo: "base"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "base"]
aliases: ["templates de e-mail marketing", "email-tmpl"]
---

# templates de e-mail marketing

## Leitura rápida

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Foco

- Se não validar **Muito comum**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Mãos na massa

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## Exemplo

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI email-tmpl; sem RCE destrutivo — tag 2fc3f0
```

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Pitfall

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Detecção / remediação

RCE child processes; template render errors anômalos.

→ Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## Prova

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [templates de e-mail marketing — lab](0529-inj-ssti-email-tmpl--lab.md)
- [templates de e-mail marketing — hardening](0909-inj-ssti-email-tmpl--hardening.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)