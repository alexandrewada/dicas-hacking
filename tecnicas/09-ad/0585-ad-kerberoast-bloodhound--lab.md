---
id: "0585"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "bloodhound"
angulo: "lab"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "lab", "t1558.003"]
aliases: ["path pós-roast", "bloodhound", "bloodhound-lab"]
---

# path pós-roast — lab

Sandbox throwaway — path pós-roast sem ruído de cliente.

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Variante

- **ACL edges** — muda ruído e o que entra no PDF.
- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## PoC mínimo

```bash
# Kerberoast lab — amostra mínima amarrada a bloodhound
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_bloodhound_cd8a9d.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
```

## Pitfall

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

RC4/AES fraco ≠ mesmo playbook. Etype e pre-auth mudam o ROI.

## Prova do lab

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

## Refs

- [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK T1558.004](https://attack.mitre.org/techniques/T1558/004/)
- [MITRE ATT&CK T1558](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps — Kerberoasting](https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91)
- [SpecterOps — BloodHound](https://bloodhound.specterops.io/)

## Relacionadas

- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [path pós-roast — hardening](0965-ad-kerberoast-bloodhound--hardening.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)
- [GenericAll em usuário/grupo (path)](0211-ad-dacl-genericall.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)