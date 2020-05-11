# XXE em SAML — hardening

Do PoC ao controle — XXE em SAML.

## Risco

XXE explora parsers XML com external entities habilitadas: leitura de arquivos,
SSRF e DoS (billion laughs). Em SOAP, SAML, office docs e uploads SVG/XML ainda é frequente.
OOB XXE (parameter entities) cobre casos cegos.

## Controles desta variante

- Detalhe que pago pra ver: **Auth surface crítica**.
- OOB/error em lab. Em prod: file read mínimo, sem exfil de segredo de cliente.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Camadas

1) Bloqueio imediato
2) Parser errors; egress to unexpected DTD hosts.
3) Desabilitar external entities; usar JSON; patch parsers; network egress deny.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
antes: controle ausente para saml
depois: ownership check / deny default em TARGET
verificação: PoC d353b9 retorna 403/blocked
reteste USER_A vs USER_B
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