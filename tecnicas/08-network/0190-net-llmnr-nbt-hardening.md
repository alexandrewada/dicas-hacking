# playbook de hardening GPO

`T1557 Adversary-in-the-Middle`

## Por que importa

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Variante

- Se não validar **Entrega defensiva**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Passo a passo

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger hardening; evidência: auth USER_A + ação não destrutiva tag 5ee710
```

## Nota de operador

Responder/ntlmrelayx em segmento acordado — sem poisoning do floor inteiro.

## Armadilha

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

Já abri High demais em playbook de hardening GPO por sintoma sem efeito. Cruzei com: Detectar Rogue WPAD/LLMNR responders; SMB signing compliance. Sem side-effect, baixo.

## Depois

Detecção — Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.

Remediação — Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.

No PDF — Hash de conta de teste / relay success; GPO recomendada.

## Refs

- MITRE T1557.001
- SpecterOps AD guides