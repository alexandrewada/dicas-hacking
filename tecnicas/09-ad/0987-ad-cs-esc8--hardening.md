# AD CS ESC8 (relay HTTP) — hardening

Do PoC ao controle — AD CS ESC8 (relay HTTP).

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Signing/EPA/channel binding decidem se o relay vive.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```bash
# verificação pós-hardening esc8
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/esc8/obj_c248ac \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag c248ac
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