---
id: "0122"
categoria: "05-injection"
familia: "inj-sqli"
slug: "mysql-blind"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "base", "t1190"]
aliases: ["SQLi blind em MySQL", "mysql-blind"]
---

# SQLi blind em MySQL

**A03 Injection** · `T1190`

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## O que muda aqui

- **SLEEP com benchmark cuidadoso.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Como testo

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## Exemplo

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo mysql-blind; sem DROP — tag dbac26
```

## Campo

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

Falso amigo em MySQL boolean/time: UI/log gritam, impacto não. Exijo WAF + DB anomaly (high row reads).

## Já me queimei

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Blue

- Detectar: WAF + DB anomaly (high row reads); prepared statement coverage.
- Fechar: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

## Evidência

Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [SQLi blind em MySQL — detecção](0502-inj-sqli-mysql-blind--detecao.md)
- [SQLi blind em MySQL — hardening](0882-inj-sqli-mysql-blind--hardening.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)
- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)