# XXE → SSRF — lab

Sandbox throwaway — XXE → SSRF sem ruído de cliente.

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Variante

- Se não validar **Metadata cloud**, a nota fica genérica.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
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
<!-- XXE ssrf lab read mínimo — tag 6a1f53 -->
```

## Pitfall

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

DNS callback sem leitura de resposta mapeia egress; insuficiente pra claim de RCE.

## Prova do lab

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

## Refs

- OWASP XXE
- PortSwigger XXE