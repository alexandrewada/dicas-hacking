---
id: "0556"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "office"
angulo: "lab"
mitre: "T1190"
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "lab", "t1190"]
aliases: ["OOXML/XLSX XXE", "office", "office-lab"]
---

# OOXML/XLSX XXE — lab

Sandbox throwaway — OOXML/XLSX XXE sem ruído de cliente.

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Variante

- Detalhe que pago pra ver: **Importadores**.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Identifico parsers XML (Content-Type, uploads, SOAP).
2. Injetar DOCTYPE com entity file:// e http://.
3. Se cego, parameter entities + collaborator.
4. Testo XInclude e DTD local.
5. Limitar leitura a arquivos inofensivos de prova.

## Exemplo

```xml
<?xml version="1.0"?>
<!DOCTYPE r [
  <!ENTITY xxe SYSTEM "file:///etc/hostname">
]>
<r>&xxe;</r>
<!-- XXE office lab read mínimo — tag 2d3289 -->
```

## Pitfall

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

DNS callback sem leitura de resposta mapeia egress; insuficiente pra claim de RCE.

## Prova do lab

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [PortSwigger — XXE](https://portswigger.net/web-security/xxe)

## Relacionadas

- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOXML/XLSX XXE — hardening](0936-xxe-classic-office--hardening.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)
- [XXE em SAML](0175-xxe-classic-saml.md)