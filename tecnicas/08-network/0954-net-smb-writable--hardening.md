# share gravável — hardening

Do PoC ao controle — share gravável.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Plantio de teste aprovado** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Controle que fecha: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Sinal que deveria existir: File server auditing; alertas de null session; DLP.

## No lab ficou assim

```bash
# verificação pós-hardening writable
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/writable/obj_1afc72 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 1afc72
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network