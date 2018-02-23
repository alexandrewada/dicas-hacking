# Smarty PHP

**A03 Injection** · `T1190`

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## O que muda aqui

- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Como testo

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
# se ecoa 49 → SSTI smarty; sem RCE destrutivo — tag 29091c
```

## Campo

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

Smarty PHP: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: RCE child processes; template render errors anômalos.

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