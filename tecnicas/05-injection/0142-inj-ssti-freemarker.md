---
id: "0142"
categoria: "05-injection"
familia: "inj-ssti"
slug: "freemarker"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "base", "t1190"]
aliases: ["Freemarker", "freemarker"]
---

# Freemarker

**A03 Injection** · `T1190`

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

**Variante:** **Execute / ObjectConstructor.** Sem isso o playbook da família mente. Identifico engine com payload mínimo. Blind sem out baixa severidade.

**Método**

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## PoC mínimo

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI freemarker; sem RCE destrutivo — tag c72e96
```

**Freio:** Payloads de RCE variam; não copie blindly — adapte ao engine.

Antes de Critical em Freemarker, confiro se a telemetria que eu cobraria reagiria — RCE child processes; template render errors anômalos.

Detecto via: RCE child processes; template render errors anômalos.

Corrijo com: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

Levo no report: Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [Freemarker — lab](0522-inj-ssti-freemarker--lab.md)
- [Freemarker — hardening](0902-inj-ssti-freemarker--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)