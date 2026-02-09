# critérios de reteste

## Leitura rápida

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Foco

- Variante critérios de reteste: trato separado da família `report-quality`.

## Mãos na massa

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## Exemplo

```text
finding_id: F-6dc548
variant: retest
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto 10042; reteste path anexado
cvss: environmental justificado (não só base)
```

Finding sem reteste path e cleanup vira pingue-pongue.

## Pitfall

Não inclua dados reais de clientes em material público — redija.

## Detecção / remediação

N/A

→ Templates de relatório; peer review; threat model alinhado.

## Prova

Exemplo de finding redigido; CVSS; remediação.

## Refs

- PTES
- OSSTMM
- CVSS