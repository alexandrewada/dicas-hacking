# ORM raw/order_by injection

## Leitura rápida

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Foco

- Se não validar **Whitelist de colunas**, a nota fica genérica.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Mãos na massa

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## No lab ficou assim

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo orm-raw; sem DROP — tag 4ceebd
```

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Pitfall

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Detecção / remediação

WAF + DB anomaly (high row reads); prepared statement coverage.

→ Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

## Prova

Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics