# JSON operators injection

**A03 Injection** · `T1190`

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

**Variante:** **MySQL/PG JSON path.** Sem isso o playbook da família mente. Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

**Método**

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
# boolean mínimo json-sql; sem DROP — tag 447c8c
```

**Freio:** Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.

Já abri High demais em JSON operators injection por sintoma sem efeito. Cruzei com: WAF + DB anomaly (high row reads); prepared statement coverage. Sem side-effect, baixo.

Detecto via: WAF + DB anomaly (high row reads); prepared statement coverage.

Corrijo com: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

Levo no report: Payload + response diferencial; amostra de dado de teste; query log se disponível.

Refs: PortSwigger SQLi, OWASP SQLi, SQLMap usage ethics