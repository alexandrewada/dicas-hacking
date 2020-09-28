# SYSVOL scripts — hardening

Do PoC ao controle — SYSVOL scripts.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Se não validar **Passwords em VBS/bat**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Controle que fecha: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Sinal que deveria existir: File server auditing; alertas de null session; DLP.

## Exemplo

```text
checklist sysvol:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (fb8bd7) falha
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network