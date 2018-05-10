# Twig PHP — hardening

Do PoC ao controle — Twig PHP.

## Risco

SSTI permite sair de template sandbox para RCE (Jinja2, Freemarker, Velocity, Twig, Pebble).
Detecção começa com polyglots `{{7*7}}` / `${7*7}` e fingerprint do engine antes do payload ofensivo.

## Controles desta variante

- Se não validar **Versões e sandbox**, a nota fica genérica.
- Identifico engine com payload mínimo. Blind sem out baixa severidade.

## Camadas

Hotfix: quebra a exploração direta de Twig PHP.
Detectivo: RCE child processes; template render errors anômalos.
Estrutural: Não renderizar templates com input não confiável; sandboxes atualizados; CSP.

## PoC mínimo

```text
antes: controle ausente para twig
depois: ownership check / deny default em TARGET
verificação: PoC 3527fb retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Payloads de RCE variam; não copie blindly — adapte ao engine.
Ambientes prod: minimize.

## Antes/depois

Engine identificado; PoC `id`; trecho de código vulnerável se fornecido.

Aceite de risco só por escrito, com prazo.

## Refs

- PortSwigger SSTI
- PayloadsAllTheThings SSTI