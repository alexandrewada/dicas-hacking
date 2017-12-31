# MySQL error-based

**A03 Injection** · `T1190`

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Como eu faço

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## Sinal / query

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo mysql-error; sem DROP — tag f863d5
```

## Diferencial desta nota

- **Extractvalue/updatexml clássicos.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

MySQL error-based: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: WAF + DB anomaly (high row reads); prepared statement coverage.

## Onde já errei

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

## Entrega

- blue: WAF + DB anomaly (high row reads); prepared statement coverage.
- fix: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
- proof: Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics