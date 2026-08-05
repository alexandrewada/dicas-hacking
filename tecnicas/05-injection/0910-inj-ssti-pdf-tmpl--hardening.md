---
id: "0910"
categoria: "05-injection"
familia: "inj-ssti"
slug: "pdf-tmpl"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-ssti", "hardening", "t1190"]
aliases: ["HTML templates → PDF", "pdf-tmpl", "pdf-tmpl-hardening"]
---

# HTML templates → PDF — hardening

Do PoC ao controle — HTML templates → PDF.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- **Encadeia XSS/SSTI** — muda ruído e o que entra no PDF.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

1) Bloqueio imediato
2) RCE child processes; template render errors anômalos.
3) Não renderizar templates com input não confiável; sandboxes atualizados; CSP.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```bash
# verificação pós-hardening pdf-tmpl
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/pdf-tmpl/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 67d6a5
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

- [HTML templates → PDF](0150-inj-ssti-pdf-tmpl.md)
- [HTML templates → PDF — lab](0530-inj-ssti-pdf-tmpl--lab.md)
- [templates de e-mail marketing](0149-inj-ssti-email-tmpl.md)
- [Freemarker](0142-inj-ssti-freemarker.md)
- [SSTI em Jinja2](0141-inj-ssti-jinja2.md)
- [Mako Python](0147-inj-ssti-mako.md)