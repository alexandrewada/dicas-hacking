---
id: "0522"
categoria: "05-injection"
familia: "inj-ssti"
slug: "freemarker"
angulo: "lab"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "lab", "t1190"]
aliases: ["Freemarker", "freemarker", "freemarker-lab"]
---

# Freemarker — lab

Sandbox throwaway — Freemarker sem ruído de cliente.

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- **Execute / ObjectConstructor.** Sem isso o playbook da família mente.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

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
# se ecoa 49 → SSTI freemarker; sem RCE destrutivo — tag f54e7c
```

## Pitfall

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

## Prova do lab

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [Freemarker](0142-inj-ssti-freemarker.md)
- [Freemarker — hardening](0902-inj-ssti-freemarker--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)