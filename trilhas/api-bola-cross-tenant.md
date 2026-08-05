# API: BOLA → cross-tenant

Objetivo: a partir de um token de tenant A, ler ou mutar recurso de tenant B (Broken Object Level Authorization / mass assignment / claim JWT) — evidência mínima, sem varrer IDs em massa.

**Pré-condições:** API no escopo; dois tenants de teste (A/B); GraphQL/REST documentados ou introspection liberada; JWT próprio para análise offline; sem rate-limit abusivo além do ROE.

[Índice](../indice/README.md) · [Trilhas](README.md)

## Cadeia

1. **Mapear o grafo da API** — introspection / schema / campos privilegiados.
   - [0071 — GraphQL introspection](../tecnicas/03-api/0071-api-graphql-introspection.md) · [path](../tecnicas/03-api/0831-api-graphql-introspection--path.md) · [detecção](../tecnicas/03-api/0451-api-graphql-introspection--detecao.md)
   - [0074 — field-level authZ](../tecnicas/03-api/0074-api-graphql-field-authz.md) · [path](../tecnicas/03-api/0834-api-graphql-field-authz--path.md)

2. **Mass assignment cross-tenant** — `tenantId` / `org_id` / role no body.
   - [0063 — mass assignment tenant](../tecnicas/03-api/0063-api-mass-assignment-tenant.md) · [path](../tecnicas/03-api/0823-api-mass-assignment-tenant--path.md) · [detecção](../tecnicas/03-api/0443-api-mass-assignment-tenant--detecao.md)
   - [0061 — role flag](../tecnicas/03-api/0061-api-mass-assignment-role-flag.md) · [path](../tecnicas/03-api/0821-api-mass-assignment-role-flag--path.md)
   - [0067 — GraphQL input](../tecnicas/03-api/0067-api-mass-assignment-graphql-input.md) (se o input type aceitar campos privilegiados)

3. **JWT: claim / alg** — subir `tid`/`sub`/`role` ou quebrar verificação.
   - [0086 — claim tamper](../tecnicas/03-api/0086-api-jwt-claim-tamper.md) · [path](../tecnicas/03-api/0846-api-jwt-claim-tamper--path.md)
   - [0081 — alg:none](../tecnicas/03-api/0081-api-jwt-alg-none.md) · [path](../tecnicas/03-api/0841-api-jwt-alg-none--path.md)
   - [0088 — aud / iss](../tecnicas/03-api/0088-api-jwt-aud-iss.md) · [path](../tecnicas/03-api/0848-api-jwt-aud-iss--path.md)

4. **Fechar BOLA** — mesmo object ID com token do outro tenant; um objeto basta.
   - Volto em [0074 — field authZ](../tecnicas/03-api/0074-api-graphql-field-authz.md) e [0063 — tenant](../tecnicas/03-api/0063-api-mass-assignment-tenant.md) com request A→B documentado.
   - Paralelo web (objeto HTTP): [0035 — IDOR GraphQL](../tecnicas/02-web/0035-web-idor-graphql.md) · [path](../tecnicas/02-web/0795-web-idor-graphql--path.md)

## Freios OpSec / quando parar

- Não faço enum massivo de UUIDs / tenant IDs; um par A/B de teste fecha o finding.
- Introspection em prod: só se ROE permitir; caso contrário schema do lab ou docs.
- JWT: não publico secret crackado no PDF; mostro claim alterado e resposta 200 no recurso B.
- Paro se a mutação cross-tenant for destrutiva (delete/billing) — leio primeiro, peço ok pra write.

## O que entra no relatório

- Schema/campo ou endpoint + parâmetro que carrega `tenantId`/`id`.
- Request com token A, object ID de B, resposta (dados mascarados).
- Se JWT: header/payload alterados (sem secret) + prova de aceite.
- Fix: authZ server-side por tenant, deny-list de campos, alg allowlist, aud/iss binding.
- Detecção: logs de acesso cross-tenant e queries GraphQL anômalas (notas `--detecao`).

[Índice](../indice/README.md)
