---
id: "0141"
categoria: "05-injection"
familia: "inj-ssti"
slug: "jinja2"
angulo: "base"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "base"]
aliases: ["SSTI em Jinja2", "jinja2"]
---

# SSTI em Jinja2

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Detalhe

- **MRO e config exploitation clássica.** Sem isso o playbook da família mente.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Execução

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## No lab ficou assim

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI jinja2; sem RCE destrutivo — tag 581a66
```

## OpSec

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

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

- [SSTI em Jinja2 — lab](0521-inj-ssti-jinja2--lab.md)
- [SSTI em Jinja2 — hardening](0901-inj-ssti-jinja2--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)
- [Command injection cega (OOB) (path)](0131-inj-cmd-unix-blind.md)
- [sudoers misconfig (path)](../11-linux/0252-linux-privesc-sudo.md)