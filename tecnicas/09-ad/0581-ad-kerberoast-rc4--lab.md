---
id: "0581"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "rc4"
angulo: "lab"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "lab", "t1558.003"]
aliases: ["Kerberoasting (TGS RC4)", "rc4", "rc4-lab"]
---

# Kerberoasting (TGS RC4) — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Variante

- Detalhe que pago pra ver: **Encryption type downgrade**.
- RC4 ainda passa onde a policy AES existe no papel. Comparo etype do TGS com msDS-SupportedEncryptionTypes antes de chamar de hardenizado.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## Exemplo

```bash
# lab.local — TGS RC4 só de SPN candidata (não assar a floresta)
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local \
  -request -outputfile tgs_rc4_73c188.kirbi
# filtrar: service_etype == rc4_hmac  (0x17)
```

## Pitfall

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

## Prova do lab

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

## Refs

- [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK T1558.004](https://attack.mitre.org/techniques/T1558/004/)
- [MITRE ATT&CK T1558](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps — Kerberoasting](https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91)
- [SpecterOps — BloodHound](https://bloodhound.specterops.io/)

## Relacionadas

- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [Kerberoasting (TGS RC4) — hardening](0961-ad-kerberoast-rc4--hardening.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)