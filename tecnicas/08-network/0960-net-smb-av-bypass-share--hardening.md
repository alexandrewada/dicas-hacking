---
id: "0960"
categoria: "08-network"
familia: "net-smb"
slug: "av-bypass-share"
angulo: "hardening"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "hardening", "t1135"]
aliases: ["share de software deployment", "av-bypass-share", "av-bypass-share-hardening"]
---

# share de software deployment — hardening

Do PoC ao controle — share de software deployment.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Supply chain interno** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de share de software deployment.
Detectivo: File server auditing; alertas de null session; DLP.
Estrutural: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## No lab ficou assim

```bash
# verificação pós-hardening av-bypass-share
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/av-bypass-share/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag efdc13
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

- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [share de software deployment — lab](0580-net-smb-av-bypass-share--lab.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)
- [null session enum](0191-net-smb-null.md)