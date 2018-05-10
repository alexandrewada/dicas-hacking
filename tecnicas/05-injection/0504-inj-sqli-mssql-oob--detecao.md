# MSSQL out-of-band — detecção

Purple em MSSQL out-of-band: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Hipótese

- **xp_dirtree / DNS se permitido.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1190`.

### PoC

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## Sinal / query

```text
db_audit: syntax error OR atypical query from app_user
pattern mssql-oob tag cb6d85
```

## Sinal

WAF + DB anomaly (high row reads); prepared statement coverage.

## Freio

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Evidência

Payload + response diferencial; amostra de dado de teste; query log se disponível.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics