# XInclude

**A03 / A05** · `T1190`

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

**Variante:** Se não validar **Quando entities bloqueadas**, a nota fica genérica. OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

**Método**

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
<!-- XXE xinclude lab read mínimo — tag 66fa3e -->
```

**Freio:** Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.

Falso amigo em XInclude: UI/log gritam, impacto não. Exijo Parser errors.

Detecto via: Parser errors; egress to unexpected DTD hosts.

Corrijo com: Desabilitar external entities; usar JSON; patch parsers; network egress deny.

Levo no report: Entity PoC; conteúdo de arquivo não sensível; parser/versão.

Refs: OWASP XXE, PortSwigger XXE