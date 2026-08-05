---
id: "0884"
categoria: "05-injection"
familia: "inj-sqli"
slug: "mssql-oob"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "hardening", "t1190"]
aliases: ["MSSQL out-of-band", "mssql-oob", "mssql-oob-hardening"]
---

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

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [MSSQL out-of-band — detecção](0504-inj-sqli-mssql-oob--detecao.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)
- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)