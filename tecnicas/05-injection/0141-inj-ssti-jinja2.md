# SSTI em Jinja2

## Contexto

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Detalhe

- **MRO e config exploitation clássica.** Sem isso o playbook da família mente.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Execução

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
# se ecoa 49 → SSTI jinja2; sem RCE destrutivo — tag 581a66
```

## OpSec

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Cuidados

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Fechamento

| | |
|---|---|
| Detecção | RCE child processes; template render errors anômalos. |
| Remediação | Não renderizar templates com input não confiável; sandboxes atualizados; CSP. |
| Evidência | Engine identificado; PoC `id`; trecho de código vulnerável se fornecido. |

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI