---
id: "0197"
categoria: "08-network"
familia: "net-smb"
slug: "dfs"
angulo: "base"
mitre: ""
owasp: ""
tags: ["08-network", "net-smb", "base"]
aliases: ["DFS enum", "dfs"]
---

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

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [DFS enum — lab](0577-net-smb-dfs--lab.md)
- [DFS enum — hardening](0957-net-smb-dfs--hardening.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)
- [null session enum](0191-net-smb-null.md)