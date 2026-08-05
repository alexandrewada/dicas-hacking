---
id: "0191"
categoria: "08-network"
familia: "net-smb"
slug: "null"
angulo: "base"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "base", "t1135"]
aliases: ["null session enum", "null"]
---

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

## Refs

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [null session enum — lab](0571-net-smb-null--lab.md)
- [null session enum — hardening](0951-net-smb-null--hardening.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)