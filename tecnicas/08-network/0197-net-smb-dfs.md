# DFS enum

## Leitura rápida

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Foco

- Se não validar **Mapa de file servers**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Mãos na massa

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger dfs; evidência: auth USER_A + ação não destrutiva tag c96f32
```

Evidência: auth capturado + ação pós-relay em conta teste. Não hash dump do prédio.

## Pitfall

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Detecção / remediação

File server auditing; alertas de null session; DLP.

→ Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## Prova

Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network