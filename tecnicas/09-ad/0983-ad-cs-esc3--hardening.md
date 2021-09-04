# ESC3 enrollment agent — hardening

Do PoC ao controle — ESC3 enrollment agent.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

Controle que fecha: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Sinal que deveria existir: Monitor certificate issuance; template change audits; CA enrollment logs.

## No lab ficou assim

```bash
# verificação pós-hardening esc3
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/esc3/10042 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 722288
```

## Armadilha

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Antes/depois

Template vulnerável; cert de teste; auth proof; revogação.

Aceite de risco só por escrito, com prazo.

## Refs

- SpecterOps Certified Pre-Owned
- MITRE T1649