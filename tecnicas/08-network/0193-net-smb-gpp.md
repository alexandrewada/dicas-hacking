---
id: "0193"
categoria: "08-network"
familia: "net-smb"
slug: "gpp"
angulo: "base"
mitre: ""
owasp: ""
tags: ["08-network", "net-smb", "base"]
aliases: ["GPP cpasswords históricos", "gpp"]
---

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

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [GPP cpasswords históricos — lab](0573-net-smb-gpp--lab.md)
- [GPP cpasswords históricos — hardening](0953-net-smb-gpp--hardening.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [null session enum](0191-net-smb-null.md)
- [DPAPI masterkey abuse (path)](../10-windows/0242-win-cred-dpapi.md)
- [GenericAll em usuário/grupo (path)](../09-ad/0211-ad-dacl-genericall.md)