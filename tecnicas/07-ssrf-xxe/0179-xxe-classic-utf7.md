---
id: "0179"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "utf7"
angulo: "base"
mitre: ""
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "base"]
aliases: ["encodings bypass", "utf7"]
---

# encodings bypass

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Detalhe

- **UTF-7 etc. em parsers antigos** — muda ruído e o que entra no PDF.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Execução

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
<!-- XXE utf7 lab read mínimo — tag e4e54b -->
```

## OpSec

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.

## Cuidados

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

## Fechamento

| | |
|---|---|
| Detecção | Parser errors; egress to unexpected DTD hosts. |
| Remediação | Desabilitar external entities; usar JSON; patch parsers; network egress deny. |
| Evidência | Entity PoC; conteúdo de arquivo não sensível; parser/versão. |

## Refs

- [OWASP XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [PortSwigger — XXE](https://portswigger.net/web-security/xxe)

## Relacionadas

- [encodings bypass — lab](0559-xxe-classic-utf7--lab.md)
- [encodings bypass — hardening](0939-xxe-classic-utf7--hardening.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)