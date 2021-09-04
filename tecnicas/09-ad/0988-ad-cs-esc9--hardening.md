# ESC9/ESC10 shadow + weak mapping — hardening

Do PoC ao controle — ESC9/ESC10 shadow + weak mapping.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- **Variantes recentes.** Sem isso o playbook da família mente.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist esc9:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (bbea62) falha
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