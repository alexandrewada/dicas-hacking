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

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics