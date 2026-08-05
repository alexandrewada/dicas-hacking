---
id: "0902"
categoria: "05-injection"
familia: "inj-ssti"
slug: "freemarker"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening", "t1190"]
aliases: ["Freemarker", "freemarker", "freemarker-hardening"]
---

# Freemarker — hardening

Do PoC ao controle — Freemarker.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- **Execute / ObjectConstructor.** Sem isso o playbook da família mente.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

1) Bloqueio imediato
2) RCE child processes; template render errors anômalos.
3) Não renderizar templates com input não confiável; sandboxes atualizados; CSP.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```bash
# verificação pós-hardening freemarker
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/freemarker/10042 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag ab3f7e
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

- [Freemarker](0142-inj-ssti-freemarker.md)
- [Freemarker — lab](0522-inj-ssti-freemarker--lab.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)