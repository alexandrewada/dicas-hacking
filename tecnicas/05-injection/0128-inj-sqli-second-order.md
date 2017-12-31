# second-order SQLi

**A03 Injection** · `T1190`

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## O que muda aqui

- **Dado armazenado e reutilizado.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Como testo

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
# boolean mínimo second-order; sem DROP — tag b9beb3
```

## Campo

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

Já abri High demais em second-order SQLi por sintoma sem efeito. Cruzei com: WAF + DB anomaly (high row reads); prepared statement coverage. Sem side-effect, baixo.

## Já me queimei

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Blue

- Detectar: WAF + DB anomaly (high row reads); prepared statement coverage.
- Fechar: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

## Evidência

Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics