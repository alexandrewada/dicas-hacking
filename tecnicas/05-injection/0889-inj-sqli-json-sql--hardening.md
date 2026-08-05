---
id: "0889"
categoria: "05-injection"
familia: "inj-sqli"
slug: "json-sql"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "hardening", "t1190"]
aliases: ["JSON operators injection", "json-sql", "json-sql-hardening"]
---

# JSON operators injection — hardening

Do PoC ao controle — JSON operators injection.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **MySQL/PG JSON path.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Hotfix: quebra a exploração direta de JSON operators injection.
Detectivo: WAF + DB anomaly (high row reads); prepared statement coverage.
Estrutural: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

## Exemplo

```text
checklist json-sql:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (ad7bfc) falha
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

- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [JSON operators injection — lab](0509-inj-sqli-json-sql--lab.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)
- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)