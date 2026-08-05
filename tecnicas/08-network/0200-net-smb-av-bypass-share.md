---
id: "0200"
categoria: "08-network"
familia: "net-smb"
slug: "av-bypass-share"
angulo: "base"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "base", "t1135"]
aliases: ["share de software deployment", "av-bypass-share"]
---

# share de software deployment

`T1135 Network Share Discovery`

## Por que importa

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Variante

- **Supply chain interno** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Passo a passo

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger av-bypass-share; evidência: auth USER_A + ação não destrutiva tag aa4232
```

## Nota de operador

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

## Armadilha

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Antes de Critical em share de software deployment, confiro se a telemetria que eu cobraria reagiria — File server auditing; alertas de null session; DLP.

## Depois

Detecção — File server auditing; alertas de null session; DLP.

Remediação — Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

No PDF — Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [share de software deployment — lab](0580-net-smb-av-bypass-share--lab.md)
- [share de software deployment — hardening](0960-net-smb-av-bypass-share--hardening.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)
- [null session enum](0191-net-smb-null.md)