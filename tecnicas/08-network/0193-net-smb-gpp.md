# GPP cpasswords históricos

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Detalhe

- Detalhe que pago pra ver: **Ainda em backups**.
- Signing/EPA/channel binding decidem se o relay vive.

## Execução

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## PoC mínimo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger gpp; evidência: auth USER_A + ação não destrutiva tag e3f92a
```

## OpSec

Evidência: auth capturado + ação pós-relay em conta teste. Não hash dump do prédio.

## Cuidados

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Fechamento

| | |
|---|---|
| Detecção | File server auditing; alertas de null session; DLP. |
| Remediação | Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL. |
| Evidência | Lista de shares; exemplo redigido de segredo; ACL. |

## Refs

- MITRE T1135
- WSTG network