# narrativa de account takeover — evidência

Pacote pra narrativa de account takeover sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Recurso claimável + prova de controle (arquivo/challenge). Sem claim, não é Critical.

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

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 9be659

{"id":"ORD-7781","owner":"USER_A","note":"redacted-ato"}
# capturado como USER_B
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