# ORM raw/order_by injection — hardening

Do PoC ao controle — ORM raw/order_by injection.

## Risco

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Controles desta variante

- Se não validar **Whitelist de colunas**, a nota fica genérica.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Camadas

1) Bloqueio imediato
2) WAF + DB anomaly (high row reads); prepared statement coverage.
3) Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```bash
# verificação pós-hardening orm-raw
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/orm-raw/obj_29ba38 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 29ba38
```

## Armadilha

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Antes/depois

Payload + response diferencial; amostra de dado de teste; query log se disponível.

Aceite de risco só por escrito, com prazo.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics