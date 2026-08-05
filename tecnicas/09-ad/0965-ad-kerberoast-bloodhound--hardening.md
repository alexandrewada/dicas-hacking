---
id: "0965"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "bloodhound"
angulo: "hardening"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "hardening", "t1558.003"]
aliases: ["path pós-roast", "bloodhound", "bloodhound-hardening"]
---

# path pós-roast — hardening

Do PoC ao controle — path pós-roast.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- **ACL edges** — muda ruído e o que entra no PDF.
- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

Controle que fecha: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
Sinal que deveria existir: Event 4769 anômalos; honeypot SPNs; AES-only policies.

## PoC mínimo

```text
checklist bloodhound:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (a1d177) falha
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK T1558.004](https://attack.mitre.org/techniques/T1558/004/)
- [MITRE ATT&CK T1558](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps — Kerberoasting](https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91)
- [SpecterOps — BloodHound](https://bloodhound.specterops.io/)

## Relacionadas

- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [path pós-roast — lab](0585-ad-kerberoast-bloodhound--lab.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)
- [GenericAll em usuário/grupo (path)](0211-ad-dacl-genericall.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)