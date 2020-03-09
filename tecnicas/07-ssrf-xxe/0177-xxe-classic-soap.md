# SOAP legacy

**A03 / A05** · `T1190`

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## O que muda aqui

- Detalhe que pago pra ver: **Content-Type text/xml**.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Como testo

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
<!-- XXE soap lab read mínimo — tag 853bcc -->
```

## Campo

DNS callback sem leitura de resposta mapeia egress; insuficiente pra claim de RCE.

Já abri High demais em SOAP legacy por sintoma sem efeito. Cruzei com: Parser errors; egress to unexpected DTD hosts. Sem side-effect, baixo.

## Já me queimei

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

## Blue

- Detectar: Parser errors; egress to unexpected DTD hosts.
- Fechar: Desabilitar external entities; usar JSON; patch parsers; network egress deny.

## Evidência

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

## Refs

- OWASP XXE
- PortSwigger XXE