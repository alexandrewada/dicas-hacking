# ESC4 template ACL write

`T1649 Steal or Forge Authentication Certificates`

## Por que importa

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Passo a passo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## Sinal / query

```bash
# AD CS esc4 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc4 -out esc4_f403bb
```

## Nota de operador

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Armadilha

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

ESC4 template ACL write: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Monitor certificate issuance; template change audits; CA enrollment logs.

## Depois

Detecção — Monitor certificate issuance; template change audits; CA enrollment logs.

Remediação — Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

No PDF — Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- SpecterOps Certified Pre-Owned
- MITRE T1649