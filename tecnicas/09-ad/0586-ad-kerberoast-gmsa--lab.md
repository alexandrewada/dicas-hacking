# detecção de ausência de gMSA — lab

Sandbox throwaway — detecção de ausência de gMSA sem ruído de cliente.

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Variante

- **Finding defensivo.** Sem isso o playbook da família mente.
- Conta de serviço com SPN e sem gMSA: higiene defensiva. Senha gerenciada > keepass de 8 chars.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## Sinal / query

```bash
# Kerberoast lab — amostra mínima amarrada a gmsa
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_gmsa_e8826e.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
```

## Pitfall

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Prova do lab

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting