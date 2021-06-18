# detecção de enrollment anômalo

**Identity** · `T1649 Steal or Forge Authentication Certificates`

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## O que muda aqui

- **Purple.** Sem isso o playbook da família mente.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Como testo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## PoC mínimo

```bash
impacket-GetADUsers lab.local/USER_A:PASS_LAB -all -dc-ip DC01.lab.local | head
# detect 4d8b13
```

## Campo

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

Falso amigo em detecção de enrollment anômalo: UI/log gritam, impacto não. Exijo Monitor certificate issuance.

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