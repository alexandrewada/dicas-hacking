---
id: "0150"
categoria: "05-injection"
familia: "inj-ssti"
slug: "pdf-tmpl"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "base", "t1190"]
aliases: ["HTML templates → PDF", "pdf-tmpl"]
---

# HTML templates → PDF

**A03 Injection** · `T1190`

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

**Variante:** **Encadeia XSS/SSTI** — muda ruído e o que entra no PDF. Identifico engine com payload mínimo. Blind sem out baixa severidade.

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
# se ecoa 49 → SSTI pdf-tmpl; sem RCE destrutivo — tag 52ae6a
```

**Freio:** Payloads de RCE variam; não copie blindly — adapte ao engine.

Antes de Critical em HTML templates → PDF, confiro se a telemetria que eu cobraria reagiria — RCE child processes; template render errors anômalos.

Detecto via: RCE child processes; template render errors anômalos.

Corrijo com: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

Levo no report: Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [HTML templates → PDF — lab](0530-inj-ssti-pdf-tmpl--lab.md)
- [HTML templates → PDF — hardening](0910-inj-ssti-pdf-tmpl--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)