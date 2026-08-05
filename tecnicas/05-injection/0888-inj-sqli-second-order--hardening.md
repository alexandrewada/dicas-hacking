---
id: "0888"
categoria: "05-injection"
familia: "inj-sqli"
slug: "second-order"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "hardening", "t1190"]
aliases: ["second-order SQLi", "second-order", "second-order-hardening"]
---

# second-order SQLi — hardening

Do PoC ao controle — second-order SQLi.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **Dado armazenado e reutilizado.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Controle que fecha: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
Sinal que deveria existir: WAF + DB anomaly (high row reads); prepared statement coverage.

## PoC mínimo

```text
antes: controle ausente para second-order
depois: ownership check / deny default em TARGET
verificação: PoC 02d46f retorna 403/blocked
reteste USER_A vs USER_B
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

- [second-order SQLi](0128-inj-sqli-second-order.md)
- [second-order SQLi — lab](0508-inj-sqli-second-order--lab.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)