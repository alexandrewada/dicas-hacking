# MSSQL out-of-band

`T1190`

## Por que importa

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Variante

- **xp_dirtree / DNS se permitido.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Passo a passo

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
# boolean mínimo mssql-oob; sem DROP — tag 195038
```

## Nota de operador

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Armadilha

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

Antes de Critical em MSSQL out-of-band, confiro se a telemetria que eu cobraria reagiria — WAF + DB anomaly (high row reads); prepared statement coverage.

## Depois

Detecção — WAF + DB anomaly (high row reads); prepared statement coverage.

Remediação — Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

No PDF — Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics