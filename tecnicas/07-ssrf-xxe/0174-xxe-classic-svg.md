# SVG XXE

## Contexto

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Detalhe

- **Upload image/svg+xml** — muda ruído e o que entra no PDF.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Execução

1. Identifico parsers XML (Content-Type, uploads, SOAP).
2. Injetar DOCTYPE com entity file:// e http://.
3. Se cego, parameter entities + collaborator.
4. Testo XInclude e DTD local.
5. Limitar leitura a arquivos inofensivos de prova.

## No lab ficou assim

```xml
<?xml version="1.0"?>
<!DOCTYPE r [
  <!ENTITY xxe SYSTEM "file:///etc/hostname">
]>
<r>&xxe;</r>
<!-- XXE svg lab read mínimo — tag ead3ab -->
```

## OpSec

SSRF prova alcance (IMDS, admin interno, file://) e o que voltou. Open redirect sozinho não é SSRF.

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

- OWASP XXE
- PortSwigger XXE