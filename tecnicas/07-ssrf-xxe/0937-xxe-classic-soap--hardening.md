# SOAP legacy — hardening

Do PoC ao controle — SOAP legacy.

## Risco

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Controles desta variante

- Detalhe que pago pra ver: **Content-Type text/xml**.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Camadas

1) Bloqueio imediato
2) Parser errors; egress to unexpected DTD hosts.
3) Desabilitar external entities; usar JSON; patch parsers; network egress deny.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```bash
# verificação pós-hardening soap
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/soap/obj_d155e4 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag d155e4
```

## Armadilha

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

## Antes/depois

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP XXE
- PortSwigger XXE