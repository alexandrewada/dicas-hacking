# Smarty PHP — hardening

Do PoC ao controle — Smarty PHP.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Hotfix: quebra a exploração direta de Smarty PHP.
Detectivo: RCE child processes; template render errors anômalos.
Estrutural: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## Exemplo

```bash
# verificação pós-hardening smarty
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/smarty/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 1828fa
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