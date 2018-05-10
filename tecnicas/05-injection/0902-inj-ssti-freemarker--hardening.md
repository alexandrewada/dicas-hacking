# Freemarker — hardening

Do PoC ao controle — Freemarker.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- **Execute / ObjectConstructor.** Sem isso o playbook da família mente.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

1) Bloqueio imediato
2) RCE child processes; template render errors anômalos.
3) Não renderizar templates com input não confiável; sandboxes atualizados; CSP.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```bash
# verificação pós-hardening freemarker
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/freemarker/10042 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag ab3f7e
```

## Armadilha

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Antes/depois

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

Aceite de risco só por escrito, com prazo.

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI