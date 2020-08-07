# backups expostos

**Misconfiguration** · `T1135 Network Share Discovery`

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Como eu faço

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## PoC mínimo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger backup; evidência: auth USER_A + ação não destrutiva tag d630d5
```

## Diferencial desta nota

- Se não validar **VHDX/NTDS potencial**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

Já abri High demais em backups expostos por sintoma sem efeito. Cruzei com: File server auditing; alertas de null session; DLP. Sem side-effect, baixo.

## Onde já errei

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

## Entrega

- blue: File server auditing; alertas de null session; DLP.
- fix: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
- proof: Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network