---
id: "0171"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "file-read"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "base", "t1190"]
aliases: ["leitura de arquivo local", "file-read"]
---

# leitura de arquivo local

`T1190`

## Por que importa

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Variante

- **Prove com arquivo benigno** — muda ruído e o que entra no PDF.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Passo a passo

1. Identifico parsers XML (Content-Type, uploads, SOAP).
2. Injetar DOCTYPE com entity file:// e http://.
3. Se cego, parameter entities + collaborator.
4. Testo XInclude e DTD local.
5. Limitar leitura a arquivos inofensivos de prova.

## Sinal / query

```xml
<?xml version="1.0"?>
<!DOCTYPE r [
  <!ENTITY xxe SYSTEM "file:///etc/hostname">
]>
<r>&xxe;</r>
<!-- XXE file-read lab read mínimo — tag fab08e -->
```

## Nota de operador

DNS callback sem leitura de resposta mapeia egress; insuficiente pra claim de RCE.

## Armadilha

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

Antes de Critical em leitura de arquivo local, confiro se a telemetria que eu cobraria reagiria — Parser errors; egress to unexpected DTD hosts.

## Depois

Detecção — Parser errors; egress to unexpected DTD hosts.

Remediação — Desabilitar external entities; usar JSON; patch parsers; network egress deny.

No PDF — Entity PoC; conteúdo de arquivo não sensível; parser/versão.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [PortSwigger — XXE](https://portswigger.net/web-security/xxe)

## Relacionadas

- [leitura de arquivo local — lab](0551-xxe-classic-file-read--lab.md)
- [leitura de arquivo local — hardening](0931-xxe-classic-file-read--hardening.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)
- [XXE em SAML](0175-xxe-classic-saml.md)