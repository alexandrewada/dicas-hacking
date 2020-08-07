# share gravável

**Misconfiguration** · `T1135 Network Share Discovery`

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## O que muda aqui

- **Plantio de teste aprovado** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Como testo

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## Exemplo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger writable; evidência: auth USER_A + ação não destrutiva tag 3167ec
```

## Campo

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

Já abri High demais em share gravável por sintoma sem efeito. Cruzei com: File server auditing; alertas de null session; DLP. Sem side-effect, baixo.

## Já me queimei

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

## Blue

- Detectar: File server auditing; alertas de null session; DLP.
- Fechar: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.

## Evidência

Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network