# Twig PHP — lab

Sandbox throwaway — Twig PHP sem ruído de cliente.

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Variante

- Se não validar **Versões e sandbox**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Localizar reflexões em e-mails, PDFs, error pages, CMS.
2. Identifico engine com payloads diferenciadores.
3. Escapar sandbox documentado do engine.
4. Provar RCE mínimo e limpar.
5. Avalio se apenas XSS de template (impacto menor).

## Exemplo

```http
POST /render HTTP/1.1
Host: app.lab.local
Content-Type: application/x-www-form-urlencoded

name={{7*7}}
# se ecoa 49 → SSTI twig; sem RCE destrutivo — tag f6b4c4
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