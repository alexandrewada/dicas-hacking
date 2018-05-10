# Apache Velocity — hardening

Do PoC ao controle — Apache Velocity.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Se não validar **Java RCE paths**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Hotfix: quebra a exploração direta de Apache Velocity.
Detectivo: RCE child processes; template render errors anômalos.
Estrutural: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## No lab ficou assim

```bash
# verificação pós-hardening velocity
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/velocity/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag e31ddf
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