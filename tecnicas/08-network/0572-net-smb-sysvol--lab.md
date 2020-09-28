# SYSVOL scripts — lab

Sandbox throwaway — SYSVOL scripts sem ruído de cliente.

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Variante

- Se não validar **Passwords em VBS/bat**, a nota fica genérica.
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

## Exemplo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger sysvol; evidência: auth USER_A + ação não destrutiva tag 0fc747
```

## Pitfall

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

## Prova do lab

Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network