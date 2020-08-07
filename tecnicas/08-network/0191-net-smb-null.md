# null session enum

**Misconfiguration** · `T1135 Network Share Discovery`

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

**Variante:** **Users/shares.** Sem isso o playbook da família mente. Signing/EPA/channel binding decidem se o relay vive.

**Método**

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger null; evidência: auth USER_A + ação não destrutiva tag 9cf7b7
```

**Freio:** Não delete arquivos. Writable share ≠ ordem para ransomware demo.

null session enum: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: File server auditing; alertas de null session; DLP.

Detecto via: File server auditing; alertas de null session; DLP.

Corrijo com: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

Levo no report: Lista de shares; exemplo redigido de segredo; ACL.

Refs: MITRE T1135, WSTG network