# AD CS ESC1 — hardening

Do PoC ao controle — AD CS ESC1.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Detalhe que pago pra ver: **Client auth EKU**.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist esc1:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (363ee1) falha
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