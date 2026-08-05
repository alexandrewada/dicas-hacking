---
id: "0959"
categoria: "08-network"
familia: "net-smb"
slug: "backup"
angulo: "hardening"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "hardening", "t1135"]
aliases: ["backups expostos", "backup", "backup-hardening"]
---

# backups expostos — hardening

Do PoC ao controle — backups expostos.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Se não validar **VHDX/NTDS potencial**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) File server auditing; alertas de null session; DLP.
3) Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
antes: controle ausente para backup
depois: ownership check / deny default em TARGET
verificação: PoC 5dd1b1 retorna 403/blocked
reteste USER_A vs USER_B
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

- [backups expostos](0199-net-smb-backup.md)
- [backups expostos — lab](0579-net-smb-backup--lab.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)
- [null session enum](0191-net-smb-null.md)