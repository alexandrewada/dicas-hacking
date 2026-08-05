---
id: "0147"
categoria: "05-injection"
familia: "inj-ssti"
slug: "mako"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "base", "t1190"]
aliases: ["Mako Python", "mako"]
---

# Mako Python

**A03 Injection** · `T1190`

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Como eu faço

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
# se ecoa 49 → SSTI mako; sem RCE destrutivo — tag 4fa602
```

## Diferencial desta nota

- Identifico engine com payload mínimo. Blind sem out baixa severidade.

Já abri High demais em Mako Python por sintoma sem efeito. Cruzei com: RCE child processes; template render errors anômalos. Sem side-effect, baixo.

## Onde já errei

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Entrega

- blue: RCE child processes; template render errors anômalos.
- fix: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.
- proof: Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SSTI](https://portswigger.net/web-security/server-side-template-injection)
- [PayloadsAllTheThings — SSTI](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Relacionadas

- [Mako Python — lab](0527-inj-ssti-mako--lab.md)
- [Mako Python — hardening](0907-inj-ssti-mako--hardening.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)