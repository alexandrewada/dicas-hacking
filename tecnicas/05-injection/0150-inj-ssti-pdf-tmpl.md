# HTML templates → PDF

**A03 Injection** · `T1190`

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

**Variante:** **Encadeia XSS/SSTI** — muda ruído e o que entra no PDF. Identifico engine com payload mínimo. Blind sem out baixa severidade.

**Método**

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
# se ecoa 49 → SSTI pdf-tmpl; sem RCE destrutivo — tag 52ae6a
```

**Freio:** Payloads de RCE variam; não copie blindly — adapte ao engine.

Antes de Critical em HTML templates → PDF, confiro se a telemetria que eu cobraria reagiria — RCE child processes; template render errors anômalos.

Detecto via: RCE child processes; template render errors anômalos.

Corrijo com: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

Levo no report: Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

Refs: PortSwigger SSTI, PayloadsAllTheThings SSTI