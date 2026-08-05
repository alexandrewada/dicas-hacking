---
id: "0956"
categoria: "08-network"
familia: "net-smb"
slug: "signing"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["08-network", "net-smb", "hardening"]
aliases: ["signing disabled", "signing", "signing-hardening"]
---

# signing disabled — hardening

Do PoC ao controle — signing disabled.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- Detalhe que pago pra ver: **Pré-requisito de relay**.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de signing disabled.
Detectivo: File server auditing; alertas de null session; DLP.
Estrutural: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## PoC mínimo

```text
checklist signing:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (cb32af) falha
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

- [signing disabled](0196-net-smb-signing.md)
- [signing disabled — lab](0576-net-smb-signing--lab.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)