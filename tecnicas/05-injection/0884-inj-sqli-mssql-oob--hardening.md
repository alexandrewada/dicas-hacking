# MSSQL out-of-band — hardening

Do PoC ao controle — MSSQL out-of-band.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **xp_dirtree / DNS se permitido.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Hotfix: quebra a exploração direta de MSSQL out-of-band.
Detectivo: WAF + DB anomaly (high row reads); prepared statement coverage.
Estrutural: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

## No lab ficou assim

```text
checklist mssql-oob:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (3e45de) falha
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