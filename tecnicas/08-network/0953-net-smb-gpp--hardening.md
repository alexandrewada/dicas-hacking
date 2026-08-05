---
id: "0953"
categoria: "08-network"
familia: "net-smb"
slug: "gpp"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["08-network", "net-smb", "hardening"]
aliases: ["GPP cpasswords históricos", "gpp", "gpp-hardening"]
---

# GPP cpasswords históricos — hardening

Do PoC ao controle — GPP cpasswords históricos.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Detalhe que pago pra ver: **Ainda em backups**.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Controle que fecha: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Sinal que deveria existir: File server auditing; alertas de null session; DLP.

## No lab ficou assim

```text
checklist gpp:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (f4bb33) falha
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

- [GPP cpasswords históricos](0193-net-smb-gpp.md)
- [GPP cpasswords históricos — lab](0573-net-smb-gpp--lab.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [null session enum](0191-net-smb-null.md)
- [DPAPI masterkey abuse (path)](../10-windows/0242-win-cred-dpapi.md)
- [GenericAll em usuário/grupo (path)](../09-ad/0211-ad-dacl-genericall.md)