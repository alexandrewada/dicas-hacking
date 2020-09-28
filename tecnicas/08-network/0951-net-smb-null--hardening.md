# null session enum — hardening

Do PoC ao controle — null session enum.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Users/shares.** Sem isso o playbook da família mente.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Controle que fecha: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Sinal que deveria existir: File server auditing; alertas de null session; DLP.

## Exemplo

```text
antes: controle ausente para null
depois: ownership check / deny default em TARGET
verificação: PoC ca759b retorna 403/blocked
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