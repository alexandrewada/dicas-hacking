# AD: low-priv → DA

Objetivo: a partir de uma conta de domínio de baixa privilégio, montar caminho até Domain Admin (ou equivalente tier-0) sem dump massivo e sem quebrar o ROE.

**Pré-condições:** LDAP/Kerberos no escopo; conta low-priv fornecida ou obtida de forma autorizada; BloodHound/SharpHound liberados (ou coleta LDAP equivalente); crack offline permitido; DCSync/ESC só com evidência mínima — preferir lab ou conta de teste.

[Índice](../indice/README.md) · [Trilhas](README.md)

## Cadeia

1. **Kerberoast RC4** — TGS de SPN candidata, etype 0x17, crack offline. Não assar a floresta.
   - [0201 — Kerberoasting (TGS RC4)](../tecnicas/09-ad/0201-ad-kerberoast-rc4.md)
   - [lab](../tecnicas/09-ad/0581-ad-kerberoast-rc4--lab.md) · [hardening](../tecnicas/09-ad/0961-ad-kerberoast-rc4--hardening.md)

2. **AS-REP roast** — contas `DONT_REQ_PREAUTH`; mesmo cuidado de amostragem.
   - [0203 — AS-REP roasting](../tecnicas/09-ad/0203-ad-kerberoast-asrep.md)
   - [lab](../tecnicas/09-ad/0583-ad-kerberoast-asrep--lab.md)

3. **OpSec do roast** — volume, honeypot SPN, timing; freio antes de escalar.
   - [0204 — opsec: stealthy roasting](../tecnicas/09-ad/0204-ad-kerberoast-opsec.md)

4. **BloodHound / path pós-roast** — edge exato até tier-0; sem grafo, não fecho High.
   - [0205 — path pós-roast](../tecnicas/09-ad/0205-ad-kerberoast-bloodhound.md)
   - [lab](../tecnicas/09-ad/0585-ad-kerberoast-bloodhound--lab.md)

5. **DACL: GenericAll / WriteDACL** — prova de ACE em objeto de teste; sem mudança destrutiva em prod.
   - [0211 — GenericAll](../tecnicas/09-ad/0211-ad-dacl-genericall.md)
   - [0212 — WriteDACL → escalate ACE](../tecnicas/09-ad/0212-ad-dacl-writedacl.md)
   - [lab GenericAll](../tecnicas/09-ad/0591-ad-dacl-genericall--lab.md)

6. **Shadow Credentials** — KeyCredentialLink como alternativa a RBCD clássico quando o path aponta pra isso.
   - [0220 — KeyCredentialLink / Shadow Credentials](../tecnicas/09-ad/0220-ad-dacl-shadowcred.md)
   - [lab](../tecnicas/09-ad/0600-ad-dacl-shadowcred--lab.md)

7. **AD CS ESC1** — template enrollee low-priv → cert com SAN privilegiado (conta teste / lab).
   - [0221 — AD CS ESC1](../tecnicas/09-ad/0221-ad-cs-esc1.md)
   - [lab](../tecnicas/09-ad/0601-ad-cs-esc1--lab.md) · [hardening](../tecnicas/09-ad/0981-ad-cs-esc1--hardening.md)

8. **DCSync** — direitos de replicação; evidência mínima (conta lab), nunca NTDS.dit inteiro no PDF.
   - [0213 — Direitos de DCSync](../tecnicas/09-ad/0213-ad-dacl-dcsync.md)
   - [lab](../tecnicas/09-ad/0593-ad-dacl-dcsync--lab.md) · [hardening](../tecnicas/09-ad/0973-ad-dacl-dcsync--hardening.md)

9. **Report sem dump** — o que sobra no entregável.
   - [0210 — como reportar sem dump massivo](../tecnicas/09-ad/0210-ad-kerberoast-report.md)
   - Detecção de enrollment anômalo: [0230](../tecnicas/09-ad/0230-ad-cs-detect.md)

## Freios OpSec / quando parar

- Paro se o ROE não cobre alteração de DACL, enrollment em CA ou DCSync — documento o path e peço autorização explícita.
- Não peço TGS de milhares de SPNs; priorizo candidatas (RC4, password fraca, path curto).
- Honey SPN / Event 4769 anômalo: trato como sinal de que o blue já está olhando — reduzo ruído.
- ESC/DCSync em produção: só prova mínima em conta de teste; rollback imediato se alterei ACE.
- Sem edge BloodHound (ou LDAP equivalente) até tier-0, não chamo de Domain Admin.

## O que entra no relatório

- Conta low-priv de partida + SPN/AS-REP amostrados (hash crackado de serviço lab, não dump).
- Grafo / ACE exato (GenericAll, WriteDACL, ShadowCred, ESC1) até o alvo.
- Evidência mínima de ESC1 (pfx + auth LDAP como conta teste) ou DCSync em objeto lab.
- Remediação: gMSA, AES-only, ACLs, templates AD CS, direitos de replicação.
- Referência cruzada às notas acima — peer review consegue reproduzir o path.

[Índice](../indice/README.md)
