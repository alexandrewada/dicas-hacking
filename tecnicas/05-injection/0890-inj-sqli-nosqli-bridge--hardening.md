---
id: "0890"
categoria: "05-injection"
familia: "inj-sqli"
slug: "nosqli-bridge"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "hardening", "t1190"]
aliases: ["polyglot SQL + NoSQL", "nosqli-bridge", "nosqli-bridge-hardening"]
---

# polyglot SQL + NoSQL — hardening

Do PoC ao controle — polyglot SQL + NoSQL.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- Se não validar **Quando dual backends**, a nota fica genérica.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Controle que fecha: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
Sinal que deveria existir: WAF + DB anomaly (high row reads); prepared statement coverage.

## Exemplo

```bash
# verificação pós-hardening nosqli-bridge
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/nosqli-bridge/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 57373c
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

- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)
- [polyglot SQL + NoSQL — lab](0510-inj-sqli-nosqli-bridge--lab.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)