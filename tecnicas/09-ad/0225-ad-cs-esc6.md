# ESC6 EDITF_ATTRIBUTESUBJECTALTNAME2

**Identity** · `T1649 Steal or Forge Authentication Certificates`

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

**Variante:** Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

**Método**

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## PoC mínimo

```bash
# AD CS esc6 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc6 -out esc6_4dd35d
```

**Freio:** Certificados são persistência — revogo sempre ao final.

ESC6 EDITF_ATTRIBUTESUBJECTALTNAME2: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Monitor certificate issuance; template change audits; CA enrollment logs.

Detecto via: Monitor certificate issuance; template change audits; CA enrollment logs.

Corrijo com: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

Levo no report: Template vulnerável; cert de teste; auth proof; revogação.

Refs: SpecterOps Certified Pre-Owned, MITRE T1649