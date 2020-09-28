# GPP cpasswords históricos — lab

Sandbox throwaway — GPP cpasswords históricos sem ruído de cliente.

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Variante

- Detalhe que pago pra ver: **Ainda em backups**.
- Signing/EPA/channel binding decidem se o relay vive.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger gpp; evidência: auth USER_A + ação não destrutiva tag 0b248a
```

## Pitfall

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Evidência: auth capturado + ação pós-relay em conta teste. Não hash dump do prédio.

## Prova do lab

Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network