---
id: "0934"
categoria: "07-ssrf-xxe"
familia: "xxe-classic"
slug: "svg"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["07-ssrf-xxe", "xxe-classic", "hardening"]
aliases: ["SVG XXE", "svg", "svg-hardening"]
---

# SVG XXE — hardening

Do PoC ao controle — SVG XXE.

## Risco

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Controles desta variante

- **Upload image/svg+xml** — muda ruído e o que entra no PDF.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Camadas

Hotfix: quebra a exploração direta de SVG XXE.
Detectivo: Parser errors; egress to unexpected DTD hosts.
Estrutural: Desabilitar external entities; usar JSON; patch parsers; network egress deny.

## No lab ficou assim

```text
antes: controle ausente para svg
depois: ownership check / deny default em TARGET
verificação: PoC 46cce3 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Evito ler `/etc/shadow` se não necessário — `/etc/hostname` basta.
Billion laughs pode derrubar serviço: combine com SOC.

## Antes/depois

Entity PoC; conteúdo de arquivo não sensível; parser/versão.

Aceite de risco só por escrito, com prazo.

## Refs

- [OWASP XXE Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [PortSwigger — XXE](https://portswigger.net/web-security/xxe)

## Relacionadas

- [SVG XXE](0174-xxe-classic-svg.md)
- [SVG XXE — lab](0554-xxe-classic-svg--lab.md)
- [XML bomb (lab controlado)](0180-xxe-classic-dos.md)
- [leitura de arquivo local](0171-xxe-classic-file-read.md)
- [OOXML/XLSX XXE](0176-xxe-classic-office.md)
- [OOB parameter entities](0173-xxe-classic-oob.md)