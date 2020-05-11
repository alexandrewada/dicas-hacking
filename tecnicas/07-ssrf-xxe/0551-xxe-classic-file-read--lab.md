# leitura de arquivo local — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Variante

- **Prove com arquivo benigno** — muda ruído e o que entra no PDF.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

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
<!-- XXE file-read lab read mínimo — tag fc37de -->
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