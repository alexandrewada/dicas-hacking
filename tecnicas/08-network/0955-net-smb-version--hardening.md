# SMBv1 legado — hardening

Do PoC ao controle — SMBv1 legado.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Detalhe que pago pra ver: **Finding + worm risk**.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de SMBv1 legado.
Detectivo: File server auditing; alertas de null session; DLP.
Estrutural: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## PoC mínimo

```text
checklist version:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (f7e8ed) falha
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network