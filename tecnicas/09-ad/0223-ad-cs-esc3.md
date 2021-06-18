# ESC3 enrollment agent

**Identity** · `T1649 Steal or Forge Authentication Certificates`

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## O que muda aqui

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Como testo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## No lab ficou assim

```bash
# AD CS esc3 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc3 -out esc3_2a59a9
```

## Campo

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

Antes de Critical em ESC3 enrollment agent, confiro se a telemetria que eu cobraria reagiria — Monitor certificate issuance; template change audits; CA enrollment logs.

## Já me queimei

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Blue

- Detectar: Monitor certificate issuance; template change audits; CA enrollment logs.
- Fechar: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

## Evidência

Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- SpecterOps Certified Pre-Owned
- MITRE T1649