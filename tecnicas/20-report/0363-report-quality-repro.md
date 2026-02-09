# passos de reprodução perfeitos

**Methodology** · `N/A`

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Como eu faço

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## Exemplo

```text
finding_id: F-46859a
variant: repro
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
cvss: environmental justificado (não só base)
```

## Diferencial desta nota

- Variante passos de reprodução perfeitos: trato separado da família `report-quality`.

passos de reprodução perfeitos: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: N/A.

## Onde já errei

Não inclua dados reais de clientes em material público — redija.

Executivo: risco em 3 frases. Técnico: PoC redigido. Misturar perde os dois públicos.

## Entrega

- blue: N/A
- fix: Templates de relatório; peer review; threat model alinhado.
- proof: Exemplo de finding redigido; CVSS; remediação.

## Refs

- PTES
- OSSTMM
- CVSS