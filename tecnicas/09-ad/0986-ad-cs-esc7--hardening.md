# ESC7 ManageCA — hardening

Do PoC ao controle — ESC7 ManageCA.

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

```text
antes: controle ausente para esc7
depois: ownership check / deny default em TARGET
verificação: PoC 43fc5a retorna 403/blocked
reteste USER_A vs USER_B
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