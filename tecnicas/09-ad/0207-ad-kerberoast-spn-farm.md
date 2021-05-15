# SPNs desnecessários

**Identity** · `T1558.003 Kerberoasting / T1558.004 AS-REP`

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

**Variante:** Detalhe que pago pra ver: **Attack surface**. SPN órfão (host morto) é superfície de roast de graça. Listo e peço dono. Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

**Método**

1. Enumero users com SPN / DONT_REQ_PREAUTH (LDAP autorizado).
2. Solicito tickets com usuário de domínio de baixa priv.
3. Crack offline com wordlists; foco contas de serviço.
4. Avalio caminho até Domain Admin (bloodhound).
5. Recomendo gMSA e senhas longas.

## PoC mínimo

```bash
# Kerberoast lab — amostra mínima amarrada a spn-farm
GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \
  -outputfile roast_spn-farm_d8cd31.kirbi
# crack offline em hashcat mode 13100; sem dump massivo
```

**Freio:** Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

Já abri High demais em SPNs desnecessários por sintoma sem efeito. Cruzei com: Event 4769 anômalos; honeypot SPNs; AES-only policies. Sem side-effect, baixo.

Detecto via: Event 4769 anômalos; honeypot SPNs; AES-only policies.

Corrijo com: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.

Levo no report: SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Refs: MITRE T1558, SpecterOps Kerberoasting