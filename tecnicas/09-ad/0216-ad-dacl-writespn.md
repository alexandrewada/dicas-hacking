# WriteSPN → targeted roast

## Contexto

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Detalhe

- Variante WriteSPN → targeted roast: trato separado da família `ad-dacl`.

## Execução

1. Coleto dados BloodHound com credencial autorizada.
2. Analisar paths até Dualidade DA/Tier0.
3. Valido ACEs exploráveis com ação mínima.
4. Documento objeto, ACE e impacto.
5. Propor remediação (remove ACE, tiering).

## No lab ficou assim

```bash
# DACL writespn — prova de ACE sem mudança destrutiva
bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \
  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor
# edge esperado: writespn → conta teste; tag db5664
```

## OpSec

DCSync em produção é sensível — alinhe com cliente. Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Cuidados

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Fechamento

| | |
|---|---|
| Detecção | Directory Services Changes auditing; BloodHound Enterprise-like monitoring. |
| Remediação | AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos. |
| Evidência | Edge BloodHound; PoC controlado; ACE dump. |

## Refs

- SpecterOps BloodHound docs
- MITRE AD techniques