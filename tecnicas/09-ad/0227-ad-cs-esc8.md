# AD CS ESC8 (relay HTTP)

**Identity** · `T1649 Steal or Forge Authentication Certificates`

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

**Variante:** Signing/EPA/channel binding decidem se o relay vive. Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

**Método**

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## No lab ficou assim

```bash
# AD CS esc8 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc8 -out esc8_fb9311
```

**Freio:** Certificados são persistência — revogo sempre ao final.

Já abri High demais em ESC8 NTLM relay to HTTP por sintoma sem efeito. Cruzei com: Monitor certificate issuance; template change audits; CA enrollment logs. Sem side-effect, baixo.

Detecto via: Monitor certificate issuance; template change audits; CA enrollment logs.

Corrijo com: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

Levo no report: Template vulnerável; cert de teste; auth proof; revogação.

Refs: SpecterOps Certified Pre-Owned, MITRE T1649