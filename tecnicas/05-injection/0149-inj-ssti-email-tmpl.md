# templates de e-mail marketing

## Leitura rápida

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Foco

- Se não validar **Muito comum**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Mãos na massa

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
# se ecoa 49 → SSTI email-tmpl; sem RCE destrutivo — tag 2fc3f0
```

Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.

## Pitfall

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Detecção / remediação

RCE child processes; template render errors anômalos.

→ Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## Prova

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI