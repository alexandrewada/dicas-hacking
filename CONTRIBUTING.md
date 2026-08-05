# Contributing

Correção técnica, referência atualizada e PoC de lab mais claro: ok.

Malware, exploit kit ou conteúdo pra acesso sem autorização: **não**.

Leia o [DISCLAIMER.md](DISCLAIMER.md). Todo “eu testo / eu provo” assume engajamento autorizado.

## Anatomia da nota

Notas vivem em `tecnicas/<categoria>/NNNN-slug.md` (e variantes `--detecao`, `--lab`, `--evidencia`, `--path`, `--hardening`).

Seções típicas (os títulos variam um pouco por layout, o espírito é o mesmo):

1. **Título** + família / ATT&CK ou OWASP quando couber
2. **Contexto** — por que importa no engajamento
3. **Como eu faço** — passos operacionais, não tutorial genérico
4. **Sinal / query** — bloco com fence (`bash`, `http`, `yaml`, …); domínio `*.lab.local`
5. **Diferencial / pitfall / freio** — o que muda o jogo ou quando parar
6. **Entrega** — blue / fix / proof
7. **Refs** — preferir links clicáveis (MITRE, OWASP, PortSwigger, docs oficiais)

Trilhas em `trilhas/` encadeiam notas existentes; se alterar um slug, atualize os links da trilha.

## Regras de estilo

- **1ª pessoa** onde for natural (“eu enumero”, “paro se…”).
- **OpSec e ROE** explícitos; write destrutivo só com freio.
- Domínios e hosts de exemplo: `lab.local`, `DC01.lab.local` — nunca cliente real.
- **Sem dump massivo** no texto ou no PDF mental (hashes amostrados, um objeto IDOR, um TGS).
- **PII mascarada** (`user_a@lab.local`, IDs parcialmente ocultos).
- Português BR, direto; sem frase de marketing e sem “como hacker ético…” genérico.

## Como contribuir

1. Prefira **PRs pequenos** (uma família, uma trilha, um ângulo).
2. Rode localmente:

```bash
make build
make audit
```

3. Descreva no PR: o que mudou, por que, e se afetou links em `trilhas/` ou `indice/`.
4. Não commite segredos, dumps, `.env` ou `proxy.pid`.

Dúvida de escopo: abra issue antes de um PR grande.
