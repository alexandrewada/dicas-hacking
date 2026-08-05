---
id: "0951"
categoria: "08-network"
familia: "net-smb"
slug: "null"
angulo: "hardening"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "hardening", "t1135"]
aliases: ["null session enum", "null", "null-hardening"]
---

# null session enum — hardening

Do PoC ao controle — null session enum.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Users/shares.** Sem isso o playbook da família mente.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Controle que fecha: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Sinal que deveria existir: File server auditing; alertas de null session; DLP.

## Exemplo

```text
antes: controle ausente para null
depois: ownership check / deny default em TARGET
verificação: PoC ca759b retorna 403/blocked
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

- [null session enum](0191-net-smb-null.md)
- [null session enum — lab](0571-net-smb-null--lab.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)