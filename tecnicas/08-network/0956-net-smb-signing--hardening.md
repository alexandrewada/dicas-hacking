# signing disabled — hardening

Do PoC ao controle — signing disabled.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Detalhe que pago pra ver: **Pré-requisito de relay**.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de signing disabled.
Detectivo: File server auditing; alertas de null session; DLP.
Estrutural: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## PoC mínimo

```text
checklist signing:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (cb32af) falha
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network