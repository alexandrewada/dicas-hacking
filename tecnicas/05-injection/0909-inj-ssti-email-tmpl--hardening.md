---
id: "0909"
categoria: "05-injection"
familia: "inj-ssti"
slug: "email-tmpl"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening"]
aliases: ["templates de e-mail marketing", "email-tmpl", "email-tmpl-hardening"]
---

# templates de e-mail marketing — hardening

Do PoC ao controle — templates de e-mail marketing.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Se não validar **Muito comum**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Hotfix: quebra a exploração direta de templates de e-mail marketing.
Detectivo: RCE child processes; template render errors anômalos.
Estrutural: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## No lab ficou assim

```text
antes: controle ausente para email-tmpl
depois: ownership check / deny default em TARGET
verificação: PoC 9ecdc1 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Antes/depois

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

Aceite de risco só por escrito, com prazo.

## Refs

- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [templates de e-mail marketing — lab](0529-inj-ssti-email-tmpl--lab.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)