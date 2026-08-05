---
id: "0526"
categoria: "05-injection"
familia: "inj-ssti"
slug: "thymeleaf"
angulo: "lab"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "lab", "t1190"]
aliases: ["Thymeleaf expression", "thymeleaf", "thymeleaf-lab"]
---

# Thymeleaf expression — lab

Lab só pra Thymeleaf expression. Se não reproduz isolado, não confio no finding de prod.

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- Detalhe que pago pra ver: **Spring el**.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

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
# se ecoa 49 → SSTI thymeleaf; sem RCE destrutivo — tag b5cfc4
```

## Pitfall

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Prova do lab

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [Thymeleaf expression](0146-inj-ssti-thymeleaf.md)
- [Thymeleaf expression — hardening](0906-inj-ssti-thymeleaf--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)