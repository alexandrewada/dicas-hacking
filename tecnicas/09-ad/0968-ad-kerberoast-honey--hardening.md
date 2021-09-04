# honey SPN detection test — hardening

Do PoC ao controle — honey SPN detection test.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- Se não validar **Purple team**, a nota fica genérica.
- SPN órfão (host morto) é superfície de roast de graça. Listo e peço dono.
- Honey SPN só vale se 4769 daquele SPN alerta de verdade. Meço MTTD com uma request.

## Camadas

Hotfix: quebra a exploração direta de honey SPN detection test.
Detectivo: Event 4769 anômalos; honeypot SPNs; AES-only policies.
Estrutural: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.

## Exemplo

```text
checklist honey:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (a7db10) falha
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting