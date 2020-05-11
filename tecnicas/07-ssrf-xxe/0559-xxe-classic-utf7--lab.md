# encodings bypass — lab

Sandbox throwaway — encodings bypass sem ruído de cliente.

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Variante

- **UTF-7 etc. em parsers antigos** — muda ruído e o que entra no PDF.
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

## PoC mínimo

```xml
<?xml version="1.0"?>
<!DOCTYPE r [
  <!ENTITY xxe SYSTEM "file:///etc/hostname">
]>
<r>&xxe;</r>
<!-- XXE utf7 lab read mínimo — tag d8bc33 -->
```

## Pitfall

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

SSRF prova alcance (IMDS, admin interno, file://) e o que voltou. Open redirect sozinho não é SSRF.

## Prova do lab

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

## Refs

- OWASP XXE
- PortSwigger XXE