---
id: "0521"
categoria: "05-injection"
familia: "inj-ssti"
slug: "jinja2"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "lab"]
aliases: ["SSTI em Jinja2", "jinja2", "jinja2-lab"]
---

# SSTI em Jinja2 — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- **MRO e config exploitation clássica.** Sem isso o playbook da família mente.
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
# se ecoa 49 → SSTI jinja2; sem RCE destrutivo — tag d68106
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

- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [SSTI em Jinja2 — hardening](0901-inj-ssti-jinja2--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)
- [Command injection cega (OOB) (path)](0131-inj-cmd-unix-blind.md)
- [sudoers misconfig (path)](../11-linux/0252-linux-privesc-sudo.md)