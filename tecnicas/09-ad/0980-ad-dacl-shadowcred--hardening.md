# KeyCredentialLink / Shadow Credentials — hardening

Do PoC ao controle — KeyCredentialLink / Shadow Credentials.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- **PKINIT abuse** — muda ruído e o que entra no PDF.

## Camadas

Controle que fecha: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Sinal que deveria existir: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.

## No lab ficou assim

```text
antes: controle ausente para shadowcred
depois: ownership check / deny default em TARGET
verificação: PoC 5ca9c4 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Antes/depois

Edge BloodHound; PoC controlado; ACE dump.

Aceite de risco só por escrito, com prazo.

## Refs

- SpecterOps BloodHound docs
- MITRE AD techniques