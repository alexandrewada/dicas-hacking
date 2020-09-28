# printer spool abuse context — hardening

Do PoC ao controle — printer spool abuse context.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Coerção relacionada** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) File server auditing; alertas de null session; DLP.
3) Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening printer
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/printer/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag f16162
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network