---
id: "0901"
categoria: "05-injection"
familia: "inj-ssti"
slug: "jinja2"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening"]
aliases: ["SSTI em Jinja2", "jinja2", "jinja2-hardening"]
---

# SSTI em Jinja2 — hardening

Do PoC ao controle — SSTI em Jinja2.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- **MRO e config exploitation clássica.** Sem isso o playbook da família mente.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Hotfix: quebra a exploração direta de SSTI em Jinja2.
Detectivo: RCE child processes; template render errors anômalos.
Estrutural: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## No lab ficou assim

```text
antes: controle ausente para jinja2
depois: ownership check / deny default em TARGET
verificação: PoC 6c79e4 retorna 403/blocked
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

- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [SSTI em Jinja2 — lab](0521-inj-ssti-jinja2--lab.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)
- [Command injection cega (OOB) (path)](0131-inj-cmd-unix-blind.md)
- [sudoers misconfig (path)](../11-linux/0252-linux-privesc-sudo.md)