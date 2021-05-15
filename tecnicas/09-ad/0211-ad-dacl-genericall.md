# GenericAll em usuário/grupo

## Leitura rápida

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Foco

- Detalhe que pago pra ver: **Takeover direto**.

## Mãos na massa

1. Coleto dados BloodHound com credencial autorizada.
2. Analisar paths até Dualidade DA/Tier0.
3. Valido ACEs exploráveis com ação mínima.
4. Documento objeto, ACE e impacto.
5. Propor remediação (remove ACE, tiering).

## Exemplo

```bash
# DACL genericall — prova de ACE sem mudança destrutiva
bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \
  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor
# edge esperado: genericall → conta teste; tag 4627e0
```

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

## Pitfall

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Detecção / remediação

Directory Services Changes auditing; BloodHound Enterprise-like monitoring.

→ AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## Prova

Edge BloodHound; PoC controlado; ACE dump.

## Refs

- SpecterOps BloodHound docs
- MITRE AD techniques