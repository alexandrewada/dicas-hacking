# Purple: do PoC à regra Sigma

Objetivo: executar uma técnica ofensiva controlada, medir se a telemetria pegou, e entregar regra (Sigma/KQL) + hardening — não só o payload “passou”.

**Pré-condições:** janela purple acordada com o blue; baseline de logging (Sysmon/EDR/CloudTrail); PoC em lab ou host canary; Atomic/Sigma no escopo de entrega; sem desligar EDR pra “passar o teste”.

[Índice](../indice/README.md) · [Trilhas](README.md)

## Cadeia

1. **Escolher a técnica ofensiva** — uma família, PoC mínimo, tag de engajamento.
   - Exemplo AD: [0201 — Kerberoasting RC4](../tecnicas/09-ad/0201-ad-kerberoast-rc4.md) · [lab](../tecnicas/09-ad/0581-ad-kerberoast-rc4--lab.md) · [opsec](../tecnicas/09-ad/0204-ad-kerberoast-opsec.md)
   - Exemplo cloud: [0266 — IMDS](../tecnicas/12-aws/0266-aws-privesc-imds.md) + [0041 — SSRF IMDS](../tecnicas/02-web/0041-web-ssrf-imds.md)
   - Exemplo web ATO: [0160 — XSS ATO chain](../tecnicas/06-client/0160-client-xss-ato-chain.md) · [lab](../tecnicas/06-client/0540-client-xss-ato-chain--lab.md)

2. **Atomic / execução limpa** — um run, timestamp marcado, sem ruído paralelo.
   - [0341 — Atomic](../tecnicas/18-evasion/0341-purple-detect-atomic.md) · [evidência](../tecnicas/18-evasion/0721-purple-detect-atomic--evidencia.md)

3. **Telemetria baseline** — Sysmon/EDR; confirmar data source antes de culpar a regra.
   - [0342 — Sysmon](../tecnicas/18-evasion/0342-purple-detect-sysmon.md) · [evidência](../tecnicas/18-evasion/0722-purple-detect-sysmon--evidencia.md)
   - Cloud: [0345 — CloudTrail](../tecnicas/18-evasion/0345-purple-detect-cloudtrail.md)
   - LOLBin / ruído: [0347 — LOLBin](../tecnicas/18-evasion/0347-purple-detect-lolbin.md)

4. **Regra Sigma (ou equivalente)** — gap → draft → true positive no mesmo PoC.
   - [0344 — sugerir regra Sigma](../tecnicas/18-evasion/0344-purple-detect-sigma.md) · [evidência](../tecnicas/18-evasion/0724-purple-detect-sigma--evidencia.md)

5. **Hardening + score** — fechar o ciclo ofensivo/defensivo.
   - Hardening da técnica escolhida (ex.: [0961 — Kerberoast RC4 hardening](../tecnicas/09-ad/0961-ad-kerberoast-rc4--hardening.md) ou [0920 — XSS ATO hardening](../tecnicas/06-client/0920-client-xss-ato-chain--hardening.md))
   - [0349 — canary](../tecnicas/18-evasion/0349-purple-detect-canary.md) · [0350 — score de cobertura](../tecnicas/18-evasion/0350-purple-detect-score.md)
   - Detecção ofensiva AD CS (se o PoC foi ESC): [0230 — enrollment anômalo](../tecnicas/09-ad/0230-ad-cs-detect.md)

## Freios OpSec / quando parar

- Não desabilito EDR/AV pra forçar sucesso do Atomic.
- PoC destrutivo (ransomware sim, DCSync prod): só lab isolado; em engajamento real, evidência mínima.
- Se não houver log source, o entregável é o gap de telemetria — não uma Sigma inventada sem campo.
- Paro a reexecução em loop se o blue já confirmou TP; documento MTTA e sigo pro próximo ATT&CK.

## O que entra no relatório

- Técnica ATT&CK + comando/PoC (lab.local), timestamp UTC.
- Data sources presentes/ausentes; alerta que veio / que não veio.
- Draft Sigma (ou KQL) com `title`, `logsource`, `detection`, false-positive notes.
- Hardening acionável amarrado à nota ofensiva.
- Matriz de cobertura (score) — o valor purple, não o “exploit rodou”.

[Índice](../indice/README.md)
