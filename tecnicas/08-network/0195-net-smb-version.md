---
id: "0195"
categoria: "08-network"
familia: "net-smb"
slug: "version"
angulo: "base"
mitre: ""
owasp: ""
tags: ["08-network", "net-smb", "base"]
aliases: ["SMBv1 legado", "version"]
---

# SMBv1 legado

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Detalhe

- Detalhe que pago pra ver: **Finding + worm risk**.
- Signing/EPA/channel binding decidem se o relay vive.

## Execução

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger version; evidência: auth USER_A + ação não destrutiva tag 540c21
```

## OpSec

Não delete arquivos. Writable share ≠ ordem para ransomware demo. Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

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

- [SMBv1 legado — lab](0575-net-smb-version--lab.md)
- [SMBv1 legado — hardening](0955-net-smb-version--hardening.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)