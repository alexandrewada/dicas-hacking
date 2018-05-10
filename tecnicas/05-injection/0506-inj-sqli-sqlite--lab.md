# SQLite em apps embarcadas — lab

Lab só pra SQLite em apps embarcadas. Se não reproduz isolado, não confio no finding de prod.

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Variante

- **Attached DB tricks.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

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
# boolean mínimo sqlite; sem DROP — tag 53d8dc
```

## Pitfall

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

## Prova do lab

Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- PortSwigger SQLi
- OWASP SQLi
- SQLMap usage ethics