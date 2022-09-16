# user/machine certs — evidência

Pacote pra user/machine certs sobreviver peer review.

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## O que precisa aparecer

- Se não validar **Client auth**, a nota fica genérica.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Tipo de credencial; host; uso em lateral (sem dumps completos).

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 112672

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-cert"}
# capturado como USER_B
```

## Remediação junto

Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.

## Se purple

EDR LSASS access; Sysmon 10; Credential Guard.

## Armadilha

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

## Refs

- MITRE Credential Access
- SpecterOps DPAPI