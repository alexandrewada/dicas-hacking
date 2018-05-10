# SQLite em apps embarcadas — hardening

Do PoC ao controle — SQLite em apps embarcadas.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **Attached DB tricks.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

1) Bloqueio imediato
2) WAF + DB anomaly (high row reads); prepared statement coverage.
3) Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```text
antes: controle ausente para sqlite
depois: ownership check / deny default em TARGET
verificação: PoC a88d62 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Antes/depois

Payload + response diferencial; amostra de dado de teste; query log se disponível.

Aceite de risco só por escrito, com prazo.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics