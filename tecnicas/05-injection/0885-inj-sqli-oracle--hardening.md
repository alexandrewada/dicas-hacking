---
id: "0885"
categoria: "05-injection"
familia: "inj-sqli"
slug: "oracle"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["05-injection", "inj-sqli", "hardening"]
aliases: ["Oracle SQLi", "oracle", "oracle-hardening"]
---

# Oracle SQLi — hardening

Do PoC ao controle — Oracle SQLi.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **DBA_ users e UTLs.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Controle que fecha: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
Sinal que deveria existir: WAF + DB anomaly (high row reads); prepared statement coverage.

## PoC mínimo

```bash
# verificação pós-hardening oracle
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/oracle/10042 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag cdbbe5
```

## Armadilha

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Antes/depois

Payload + response diferencial; amostra de dado de teste; query log se disponível.

Aceite de risco só por escrito, com prazo.

## Refs

- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [Oracle SQLi](0125-inj-sqli-oracle.md)
- [Oracle SQLi — lab](0505-inj-sqli-oracle--lab.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)