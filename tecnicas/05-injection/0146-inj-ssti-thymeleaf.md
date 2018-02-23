# Thymeleaf expression

`T1190`

## Por que importa

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- Detalhe que pago pra ver: **Spring el**.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Passo a passo

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## PoC mínimo

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI thymeleaf; sem RCE destrutivo — tag ee14ae
```

## Nota de operador

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Armadilha

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

Já abri High demais em Thymeleaf expression por sintoma sem efeito. Cruzei com: RCE child processes; template render errors anômalos. Sem side-effect, baixo.

## Depois

Detecção — RCE child processes; template render errors anômalos.

Remediação — Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

No PDF — Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI