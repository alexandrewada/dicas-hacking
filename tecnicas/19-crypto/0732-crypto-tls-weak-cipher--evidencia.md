# CBC/RC4/3DES — evidência

Pacote pra CBC/RC4/3DES sobreviver peer review.

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## O que precisa aparecer

- RC4 ainda passa onde a policy AES existe no papel. Comparo etype do TGS com msDS-SupportedEncryptionTypes antes de chamar de hardenizado.

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

ssllabs-like summary; cipher list; exploitability note.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 4e0291

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-weak-cipher"}
# capturado como USER_B
```

## Remediação junto

TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

## Se purple

Certificate expiry monitoring; TLS policy sensors.

## Armadilha

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Refs

- OWASP Transport Layer Protection
- Mozilla TLS guidelines