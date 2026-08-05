---
id: "0572"
categoria: "08-network"
familia: "net-smb"
slug: "sysvol"
angulo: "lab"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "lab", "t1135"]
aliases: ["SYSVOL scripts", "sysvol", "sysvol-lab"]
---

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

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [SYSVOL scripts](0192-net-smb-sysvol.md)
- [SYSVOL scripts — hardening](0952-net-smb-sysvol--hardening.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)