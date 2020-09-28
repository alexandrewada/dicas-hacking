# share gravável — lab

Lab só pra share gravável. Se não reproduz isolado, não confio no finding de prod.

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Variante

- **Plantio de teste aprovado** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger writable; evidência: auth USER_A + ação não destrutiva tag 7f75a4
```

## Pitfall

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

## Prova do lab

Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network