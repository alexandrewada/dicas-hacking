# honey SPN detection test

**Identity** · `T1558.003 Kerberoasting / T1558.004 AS-REP`

## Contexto

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## O que muda aqui

- Se não validar **Purple team**, a nota fica genérica.
- SPN órfão (host morto) é superfície de roast de graça. Listo e peço dono.
- Honey SPN só vale se 4769 daquele SPN alerta de verdade. Meço MTTD com uma request.

## Como testo

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## No lab ficou assim

```bash
# Kerberoast lab — amostra mínima amarrada a honey
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_honey_62796b.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
```

## Campo

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

Antes de Critical em honey SPN detection test, confiro se a telemetria que eu cobraria reagiria — Event 4769 anômalos; honeypot SPNs; AES-only policies.

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