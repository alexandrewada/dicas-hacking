# PostgreSQL error/verbose — hardening

Do PoC ao controle — PostgreSQL error/verbose.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **Cast e XML functions.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Controle que fecha: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
Sinal que deveria existir: WAF + DB anomaly (high row reads); prepared statement coverage.

## PoC mínimo

```text
checklist pg-error:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (cd6d52) falha
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