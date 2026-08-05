---
id: "0905"
categoria: "05-injection"
familia: "inj-ssti"
slug: "pebble"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening"]
aliases: ["Pebble", "pebble", "pebble-hardening"]
---

# Pebble — hardening

Do PoC ao controle — Pebble.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Se não validar **Java templates**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Controle que fecha: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.
Sinal que deveria existir: RCE child processes; template render errors anômalos.

## No lab ficou assim

```bash
# verificação pós-hardening pebble
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/pebble/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 52fa03
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

- [Pebble](0145-inj-ssti-pebble.md)
- [Pebble — lab](0525-inj-ssti-pebble--lab.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)