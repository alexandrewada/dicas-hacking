# critérios de reteste — evidência

Pacote pra critérios de reteste sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Variante critérios de reteste: trato separado da família `report-quality`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/usr_01HZX Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (retest)
hash_prova: 6d7011
```

## Remediação junto

Templates de relatório; peer review; threat model alinhado.

## Se purple

N/A

## Armadilha

Não inclua dados reais de clientes em material público — redija.

## Refs

- PTES
- OSSTMM
- CVSS