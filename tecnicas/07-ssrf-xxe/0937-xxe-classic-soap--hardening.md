---
id: "0937"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "soap"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "hardening", "t1190"]
aliases: ["SOAP legacy", "soap", "soap-hardening"]
---

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

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [PortSwigger — XXE](https://portswigger.net/web-security/xxe)

## Relacionadas

- [SOAP legacy](0177-xxe-classic-soap.md)
- [SOAP legacy — lab](0557-xxe-classic-soap--lab.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)