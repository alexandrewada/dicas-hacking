# share de software deployment — hardening

Do PoC ao controle — share de software deployment.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Supply chain interno** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de share de software deployment.
Detectivo: File server auditing; alertas de null session; DLP.
Estrutural: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## No lab ficou assim

```bash
# verificação pós-hardening av-bypass-share
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/av-bypass-share/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag efdc13
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network