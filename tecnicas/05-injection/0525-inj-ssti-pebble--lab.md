# Pebble — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- Se não validar **Java templates**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## No lab ficou assim

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI pebble; sem RCE destrutivo — tag 16b5c6
```

## Pitfall

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Prova do lab

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI