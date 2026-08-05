---
id: "0553"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "oob"
angulo: "lab"
mitre: "T1190"
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "lab", "t1190"]
aliases: ["OOB parameter entities", "oob", "oob-lab"]
---

# OOB parameter entities — lab

Sandbox throwaway — OOB parameter entities sem ruído de cliente.

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Variante

- **Blind XXE.** Sem isso o playbook da família mente.
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
<!-- XXE oob lab read mínimo — tag 0dcf44 -->
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

- [OOB parameter entities](0173-xxe-classic-oob.md)
- [OOB parameter entities — hardening](0933-xxe-classic-oob--hardening.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [XXE em SAML](0175-xxe-classic-saml.md)