---
id: "0198"
categoria: "08-network"
familia: "net-smb"
slug: "printer"
angulo: "base"
mitre: "T1135"
owasp: ""
tags: ["08-network", "net-smb", "base", "t1135"]
aliases: ["printer spool abuse context", "printer"]
---

# printer spool abuse context

**Misconfiguration** · `T1135 Network Share Discovery`

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Como eu faço

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger printer; evidência: auth USER_A + ação não destrutiva tag 2c5cd5
```

## Diferencial desta nota

- **Coerção relacionada** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

Antes de Critical em printer spool abuse context, confiro se a telemetria que eu cobraria reagiria — File server auditing; alertas de null session; DLP.

## Onde já errei

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Evidência: auth capturado + ação pós-relay em conta teste. Não hash dump do prédio.

## Entrega

- blue: File server auditing; alertas de null session; DLP.
- fix: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
- proof: Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [OWASP WSTG — Network testing](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [HackTricks — SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)

## Relacionadas

- [printer spool abuse context — lab](0578-net-smb-printer--lab.md)
- [printer spool abuse context — hardening](0958-net-smb-printer--hardening.md)
- [share de software deployment](0200-net-smb-av-bypass-share.md)
- [backups expostos](0199-net-smb-backup.md)
- [DFS enum](0197-net-smb-dfs.md)
- [GPP cpasswords históricos](0193-net-smb-gpp.md)