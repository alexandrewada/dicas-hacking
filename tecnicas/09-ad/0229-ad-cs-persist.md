# persistência via certs

## Leitura rápida

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Foco

- Se não validar **Client auth long-lived**, a nota fica genérica.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Mãos na massa

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## No lab ficou assim

```bash
ldapsearch -H ldap://DC01.lab.local -D 'USER_A@lab.local' -w PASS_LAB -b 'DC=lab,DC=local' '(sAMAccountName=USER_A)'
# persist c32af2
```

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Pitfall

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Detecção / remediação

Monitor certificate issuance; template change audits; CA enrollment logs.

→ Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

## Prova

Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- SpecterOps Certified Pre-Owned
- MITRE T1649