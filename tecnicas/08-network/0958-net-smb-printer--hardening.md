---
id: "0958"
categoria: "08-network"
familia: "net-smb"
slug: "printer"
angulo: "hardening"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "hardening", "t1135"]
aliases: ["printer spool abuse context", "printer", "printer-hardening"]
---

# printer spool abuse context — hardening

Do PoC ao controle — printer spool abuse context.

## Risco

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Controles desta variante

- **Coerção relacionada** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) File server auditing; alertas de null session; DLP.
3) Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening printer
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/printer/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag f16162
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

- [printer spool abuse context](0198-net-smb-printer.md)
- [printer spool abuse context — lab](0578-net-smb-printer--lab.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)