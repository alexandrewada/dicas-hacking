# printer spool abuse context

**Misconfiguration** · `T1135 Network Share Discovery`

## Contexto

Shares SMB expõem scripts de logon, credenciais em cleartext, backups e SYSVOL artifacts.
Null/guest sessions e enumeração de usuários via SAMR ainda aparecem em ambientes legados.

## Como eu faço

1. Enumero shares autorizados (smbclient/netexec).
2. Testo null session e guest.
3. Caçar scripts, web.config, unattend, chaves.
4. Avalio writable shares para plantio controlado (com permissão).
5. Documento dados sensíveis sem exfiltrar em massa.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger printer; evidência: auth USER_A + ação não destrutiva tag 2c5cd5
```

## Diferencial desta nota

- **Coerção relacionada** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

Antes de Critical em printer spool abuse context, confiro se a telemetria que eu cobraria reagiria — File server auditing; alertas de null session; DLP.

## Onde já errei

Não delete arquivos. Writable share ≠ ordem para ransomware demo.

Evidência: auth capturado + ação pós-relay em conta teste. Não hash dump do prédio.

## Entrega

- blue: File server auditing; alertas de null session; DLP.
- fix: Desabilitar guest/null; least privilege ACLs; SMB signing; remove secrets de SYSVOL.
- proof: Lista de shares; exemplo redigido de segredo; ACL.

## Refs

- MITRE T1135
- WSTG network