# Apache Velocity

**A03 Injection** · `T1190`

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## O que muda aqui

- Se não validar **Java RCE paths**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Como testo

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
# se ecoa 49 → SSTI velocity; sem RCE destrutivo — tag 562001
```

## Campo

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

Falso amigo em Apache Velocity: UI/log gritam, impacto não. Exijo RCE child processes.

## Já me queimei

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Blue

- Detectar: RCE child processes; template render errors anômalos.
- Fechar: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## Evidência

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI