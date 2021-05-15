# como reportar sem dump massivo

**Identity** · `T1558.003 Kerberoasting / T1558.004 AS-REP`

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## O que muda aqui

- Se não validar **Amostra mínima**, a nota fica genérica.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Como testo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## PoC mínimo

```bash
# Kerberoast lab — amostra mínima amarrada a report
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_report_fac9af.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
```

## Campo

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

como reportar sem dump massivo: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Event 4769 anômalos; honeypot SPNs; AES-only policies.

## Já me queimei

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Blue

- Detectar: Event 4769 anômalos; honeypot SPNs; AES-only policies.
- Fechar: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.

## Evidência

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting