---
id: "0908"
categoria: "05-injection"
familia: "inj-ssti"
slug: "smarty"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening", "t1190"]
aliases: ["Smarty PHP", "smarty", "smarty-hardening"]
---

# Smarty PHP — hardening

Do PoC ao controle — Smarty PHP.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Hotfix: quebra a exploração direta de Smarty PHP.
Detectivo: RCE child processes; template render errors anômalos.
Estrutural: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## Exemplo

```bash
# verificação pós-hardening smarty
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/smarty/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 1828fa
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

- [Smarty PHP](0148-inj-ssti-smarty.md)
- [Smarty PHP — lab](0528-inj-ssti-smarty--lab.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)