# path pós-roast

**Identity** · `T1558.003 Kerberoasting / T1558.004 AS-REP`

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## O que muda aqui

- **ACL edges** — muda ruído e o que entra no PDF.
- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Como testo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## Exemplo

```bash
# Kerberoast lab — amostra mínima amarrada a bloodhound
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_bloodhound_0308ed.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
```

## Campo

RC4/AES fraco ≠ mesmo playbook. Etype e pre-auth mudam o ROI.

Falso amigo em path pós-roast: UI/log gritam, impacto não. Exijo Event 4769 anômalos.

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