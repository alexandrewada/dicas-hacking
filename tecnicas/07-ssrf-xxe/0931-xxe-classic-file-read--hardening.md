---
id: "0931"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "file-read"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "hardening", "t1190"]
aliases: ["leitura de arquivo local", "file-read", "file-read-hardening"]
---

# leitura de arquivo local — hardening

Do PoC ao controle — leitura de arquivo local.

## Risco

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Controles desta variante

- **Prove com arquivo benigno** — muda ruído e o que entra no PDF.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Camadas

Controle que fecha: Desabilitar external entities; usar JSON; patch parsers; network egress deny.
Sinal que deveria existir: Parser errors; egress to unexpected DTD hosts.

## No lab ficou assim

```text
checklist file-read:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (1b7998) falha
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

- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [leitura de arquivo local — lab](0551-xxe-classic-file-read--lab.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)
- [XXE em SAML](0175-xxe-classic-saml.md)