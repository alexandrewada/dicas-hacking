---
id: "0907"
categoria: "05-injection"
familia: "inj-ssti"
slug: "mako"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening", "t1190"]
aliases: ["Mako Python", "mako", "mako-hardening"]
---

# Mako Python — hardening

Do PoC ao controle — Mako Python.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

1) Bloqueio imediato
2) RCE child processes; template render errors anômalos.
3) Não renderizar templates com input não confiável; sandboxes atualizados; CSP.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```text
checklist mako:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (ba937a) falha
```

## Armadilha

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Antes/depois

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [Mako Python](0147-inj-ssti-mako.md)
- [Mako Python — lab](0527-inj-ssti-mako--lab.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)