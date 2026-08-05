---
id: "0957"
categoria: "08-network"
familia: "net-smb"
slug: "dfs"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["08-network", "net-smb", "hardening"]
aliases: ["DFS enum", "dfs", "dfs-hardening"]
---

# DFS enum — hardening

Do PoC ao controle — DFS enum.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Se não validar **Mapa de file servers**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) File server auditing; alertas de null session; DLP.
3) Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```text
checklist dfs:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (a35442) falha
```

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Antes/depois

Lista de shares; exemplo redigido de segredo; ACL.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [DFS enum](0197-net-smb-dfs.md)
- [DFS enum — lab](0577-net-smb-dfs--lab.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)
- [null session enum](0191-net-smb-null.md)