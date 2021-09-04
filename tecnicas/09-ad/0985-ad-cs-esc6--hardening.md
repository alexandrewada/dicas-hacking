# ESC6 EDITF_ATTRIBUTESUBJECTALTNAME2 — hardening

Do PoC ao controle — ESC6 EDITF_ATTRIBUTESUBJECTALTNAME2.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

Hotfix: quebra a exploração direta de ESC6 EDITF_ATTRIBUTESUBJECTALTNAME2.
Detectivo: Monitor certificate issuance; template change audits; CA enrollment logs.
Estrutural: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

## PoC mínimo

```bash
# verificação pós-hardening esc6
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/esc6/usr_01HZX \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 22afc7
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