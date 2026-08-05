---
id: "0932"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "ssrf"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "hardening", "t1190"]
aliases: ["XXE → SSRF", "ssrf", "ssrf-hardening"]
---

# XXE → SSRF — hardening

Do PoC ao controle — XXE → SSRF.

## Risco

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Controles desta variante

- Se não validar **Metadata cloud**, a nota fica genérica.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Camadas

Hotfix: quebra a exploração direta de XXE → SSRF.
Detectivo: Parser errors; egress to unexpected DTD hosts.
Estrutural: Desabilitar external entities; usar JSON; patch parsers; network egress deny.

## No lab ficou assim

```bash
# verificação pós-hardening ssrf
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/ssrf/obj_f26aa2 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag f26aa2
```

## Armadilha

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

## Antes/depois

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [PortSwigger — XXE](https://portswigger.net/web-security/xxe)

## Relacionadas

- [XXE → SSRF](0172-xxe-classic-ssrf.md)
- [XXE → SSRF — lab](0552-xxe-classic-ssrf--lab.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)