# backups expostos — hardening

Do PoC ao controle — backups expostos.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Se não validar **VHDX/NTDS potencial**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) File server auditing; alertas de null session; DLP.
3) Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
antes: controle ausente para backup
depois: ownership check / deny default em TARGET
verificação: PoC 5dd1b1 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1135
- WSTG network