# XML bomb (lab controlado) — hardening

Do PoC ao controle — XML bomb (lab controlado).

## Risco

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Controles desta variante

- Detalhe que pago pra ver: **Só em ambiente dedicado**.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.

## Camadas

Controle que fecha: Desabilitar external entities; usar JSON; patch parsers; network egress deny.
Sinal que deveria existir: Parser errors; egress to unexpected DTD hosts.

## PoC mínimo

```text
checklist dos:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (fb760e) falha
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