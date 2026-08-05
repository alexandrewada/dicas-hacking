---
id: "0502"
categoria: "05-injection"
familia: "inj-sqli"
slug: "mysql-blind"
angulo: "detecao"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "detecao", "t1190"]
aliases: ["SQLi blind em MySQL", "mysql-blind", "mysql-blind-detecao"]
---

# SQLi blind em MySQL — detecção

Se o SOC não vê SQLi blind em MySQL, o finding é de cobertura, não de ego ofensivo.

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Hipótese

- **SLEEP com benchmark cuidadoso.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## Sinal / query

```text
db_audit: syntax error OR atypical query from app_user
pattern mysql-blind tag 86a4c9
```

## Sinal

WAF + DB anomaly (high row reads); prepared statement coverage.

## Freio

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Evidência

Payload + response diferencial; amostra de dado de teste; query log se disponível.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [SQLi blind em MySQL — hardening](0882-inj-sqli-mysql-blind--hardening.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)
- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)