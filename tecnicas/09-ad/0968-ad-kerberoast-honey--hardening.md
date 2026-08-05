---
id: "0968"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "honey"
angulo: "hardening"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "hardening", "t1558.003"]
aliases: ["honey SPN detection test", "honey", "honey-hardening"]
---

# honey SPN detection test — hardening

Do PoC ao controle — honey SPN detection test.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- Se não validar **Purple team**, a nota fica genérica.
- SPN órfão (host morto) é superfície de roast de graça. Listo e peço dono.
- Honey SPN só vale se 4769 daquele SPN alerta de verdade. Meço MTTD com uma request.

## Camadas

Hotfix: quebra a exploração direta de honey SPN detection test.
Detectivo: Event 4769 anômalos; honeypot SPNs; AES-only policies.
Estrutural: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.

## Exemplo

```text
checklist honey:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (a7db10) falha
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

- [honey SPN detection test](0208-ad-kerberoast-honey.md)
- [honey SPN detection test — lab](0588-ad-kerberoast-honey--lab.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)