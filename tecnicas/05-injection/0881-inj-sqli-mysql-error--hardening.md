---
id: "0881"
categoria: "05-injection"
familia: "inj-sqli"
slug: "mysql-error"
angulo: "hardening"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "hardening", "t1190"]
aliases: ["MySQL error-based", "mysql-error", "mysql-error-hardening"]
---

# MySQL error-based — hardening

Do PoC ao controle — MySQL error-based.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- **Extractvalue/updatexml clássicos.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

Hotfix: quebra a exploração direta de MySQL error-based.
Detectivo: WAF + DB anomaly (high row reads); prepared statement coverage.
Estrutural: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

## Exemplo

```bash
# verificação pós-hardening mysql-error
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/mysql-error/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 61ffc2
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

- [MySQL error-based](0121-inj-sqli-mysql-error.md)
- [MySQL error-based — detecção](0501-inj-sqli-mysql-error--detecao.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)
- [Command injection cega (OOB) (path)](0131-inj-cmd-unix-blind.md)
- [web shell via extensão (path)](../02-web/0051-web-upload-webshell.md)