---
id: "0582"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "aes"
angulo: "lab"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "lab", "t1558.003"]
aliases: ["AES ainda fraco se password ruim", "aes", "aes-lab"]
---

# AES ainda fraco se password ruim — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Variante

- **Não assume AES=safe** — muda ruído e o que entra no PDF.
- AES não salva password fraca — TGS AES cracka offline igual, só mais lento. Controle de verdade: gMSA / complexidade.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## No lab ficou assim

```bash
# Kerberoast lab — amostra mínima amarrada a aes
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_aes_92bffa.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
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

- [AES ainda fraco se password ruim](0202-ad-kerberoast-aes.md)
- [AES ainda fraco se password ruim — hardening](0962-ad-kerberoast-aes--hardening.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)
- [GenericAll em usuário/grupo (path)](0211-ad-dacl-genericall.md)