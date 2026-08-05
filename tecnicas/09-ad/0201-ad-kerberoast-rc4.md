---
id: "0201"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "rc4"
angulo: "base"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "base", "t1558.003"]
aliases: ["Kerberoasting (TGS RC4)", "rc4"]
---

# Kerberoasting (TGS RC4)

**Identity** · `T1558.003 Kerberoasting / T1558.004 AS-REP`

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Como eu faço

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## Sinal / query

```bash
# lab.local — TGS RC4 só de SPN candidata (não assar a floresta)
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local \
  -request -outputfile tgs_rc4_66685c.kirbi
# filtrar: service_etype == rc4_hmac  (0x17)
```

## Diferencial desta nota

- Detalhe que pago pra ver: **Encryption type downgrade**.
- RC4 ainda passa onde a policy AES existe no papel. Comparo etype do TGS com msDS-SupportedEncryptionTypes antes de chamar de hardenizado.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

Já abri High demais em TGS RC4 crackável por sintoma sem efeito. Cruzei com: Event 4769 anômalos; honeypot SPNs; AES-only policies. Sem side-effect, baixo.

## Onde já errei

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

## Entrega

- blue: Event 4769 anômalos; honeypot SPNs; AES-only policies.
- fix: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
- proof: SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

## Refs

- [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK T1558.004](https://attack.mitre.org/techniques/T1558/004/)
- [MITRE ATT&CK T1558](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps — Kerberoasting](https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91)
- [SpecterOps — BloodHound](https://bloodhound.specterops.io/)

## Relacionadas

- [Kerberoasting (TGS RC4) — lab](0581-ad-kerberoast-rc4--lab.md)
- [Kerberoasting (TGS RC4) — hardening](0961-ad-kerberoast-rc4--hardening.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)