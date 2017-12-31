# Oracle SQLi

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Detalhe

- **DBA_ users e UTLs.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Execução

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## PoC mínimo

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo oracle; sem DROP — tag f508fd
```

## OpSec

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE. Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Cuidados

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Fechamento

| | |
|---|---|
| Detecção | WAF + DB anomaly (high row reads); prepared statement coverage. |
| Remediação | Parameterized queries; least privilege DB user; WAF; disable dangerous procs. |
| Evidência | Payload + response diferencial; amostra de dado de teste; query log se disponível. |

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics