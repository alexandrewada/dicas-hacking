# ESC2 any purpose EKU — lab

Lab só pra ESC2 any purpose EKU. Se não reproduz isolado, não confio no finding de prod.

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Variante

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## PoC mínimo

```bash
# AD CS esc2 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc2 -out esc2_c372b4
```

## Pitfall

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

## Prova do lab

Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- SpecterOps Certified Pre-Owned
- MITRE T1649