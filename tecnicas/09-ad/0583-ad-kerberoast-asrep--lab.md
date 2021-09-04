# AS-REP roasting — lab

Lab só pra AS-REP roasting. Se não reproduz isolado, não confio no finding de prod.

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Variante

- **Pre-auth disabled** — muda ruído e o que entra no PDF.
- DONT_REQ_PREAUTH = AS-REP roast sem SPN. Confirmo UAC no LDAP e limito amostra.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## Exemplo

```bash
# Kerberoast lab — amostra mínima amarrada a asrep
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_asrep_5ca42d.kirbi
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