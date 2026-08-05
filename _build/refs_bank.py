"""Banco de referências curadas → URLs clicáveis (2–5 por nota)."""
from __future__ import annotations

import re
from typing import Iterable

# (regex case-insensitive no texto da ref do seed) → (título, url)
SEED_REF_MAP: list[tuple[str, str, str]] = [
    (r"MITRE ATT&CK T1590|MITRE ATT&CK\b(?!\s*T)", "MITRE ATT&CK", "https://attack.mitre.org/"),
    (r"MITRE T1590", "MITRE ATT&CK T1590", "https://attack.mitre.org/techniques/T1590/"),
    (r"MITRE T1589", "MITRE ATT&CK T1589", "https://attack.mitre.org/techniques/T1589/"),
    (r"MITRE T1558", "MITRE ATT&CK T1558", "https://attack.mitre.org/techniques/T1558/"),
    (r"MITRE T1557\.001|MITRE T1557", "MITRE ATT&CK T1557.001", "https://attack.mitre.org/techniques/T1557/001/"),
    (r"MITRE T1110\.003", "MITRE ATT&CK T1110.003", "https://attack.mitre.org/techniques/T1110/003/"),
    (r"MITRE T1135", "MITRE ATT&CK T1135", "https://attack.mitre.org/techniques/T1135/"),
    (r"MITRE T1621", "MITRE ATT&CK T1621", "https://attack.mitre.org/techniques/T1621/"),
    (r"MITRE T1649", "MITRE ATT&CK T1649", "https://attack.mitre.org/techniques/T1649/"),
    (r"MITRE AD techniques|MITRE Credential Access|MITRE PrivEsc|MITRE Cloud|MITRE C2|MITRE ATT&CK",
     "MITRE ATT&CK", "https://attack.mitre.org/"),
    (r"OWASP Testing Guide WSTG-INFO|WSTG-INFO(?!-)",
     "OWASP WSTG — Information Gathering",
     "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README"),
    (r"WSTG-INFO-02", "OWASP WSTG-INFO-02 Fingerprint Web Server",
     "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server"),
    (r"WSTG-ATHZ-04", "OWASP WSTG — Bypassing Authorization Schema",
     "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema"),
    (r"WSTG-BUSL-08", "OWASP WSTG-BUSL-08 Testing for HTTP Uploading",
     "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types"),
    (r"WSTG-INPV-01|WSTG-INPV-01/02", "OWASP WSTG-INPV-01 Reflected XSS",
     "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting"),
    (r"WSTG-INPV-12", "OWASP WSTG-INPV-12 Testing for Command Injection",
     "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection"),
    (r"WSTG network", "OWASP WSTG — Network testing",
     "https://owasp.org/www-project-web-security-testing-guide/latest/"),
    (r"OWASP SSRF", "OWASP SSRF Prevention Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html"),
    (r"OWASP XSS", "OWASP XSS Prevention Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html"),
    (r"OWASP CSRF", "OWASP CSRF Prevention Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"),
    (r"OWASP XXE", "OWASP XXE Prevention Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html"),
    (r"OWASP SQLi", "OWASP SQL Injection",
     "https://owasp.org/www-community/attacks/SQL_Injection"),
    (r"OWASP Command Injection", "OWASP OS Command Injection Defense",
     "https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html"),
    (r"OWASP Unrestricted File Upload", "OWASP File Upload Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html"),
    (r"OWASP JWT", "OWASP JWT Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html"),
    (r"OWASP GraphQL", "OWASP GraphQL Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html"),
    (r"OWASP API Top 10 API1|OWASP API3|API Top 10", "OWASP API Security Top 10",
     "https://owasp.org/API-Security/editions/2023/en/0x11-t10/"),
    (r"OWASP MFA", "OWASP Multifactor Authentication Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html"),
    (r"OWASP OAuth", "OWASP OAuth 2.0 Cheat Sheet",
     "https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html"),
    (r"OWASP Secure Headers", "OWASP Secure Headers Project",
     "https://owasp.org/www-project-secure-headers/"),
    (r"OWASP Transport Layer|OWASP TLS", "OWASP Transport Layer Protection",
     "https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html"),
    (r"OWASP MASVS|OWASP MASTG iOS|OWASP MASTG", "OWASP MASTG",
     "https://mas.owasp.org/MASTG/"),
    (r"OWASP wireless", "OWASP Testing Guide",
     "https://owasp.org/www-project-web-security-testing-guide/latest/"),
    (r"PortSwigger Access Control", "PortSwigger — Access control",
     "https://portswigger.net/web-security/access-control"),
    (r"PortSwigger SSRF", "PortSwigger — SSRF",
     "https://portswigger.net/web-security/ssrf"),
    (r"PortSwigger JWT", "PortSwigger — JWT attacks",
     "https://portswigger.net/web-security/jwt"),
    (r"PortSwigger Mass Assignment", "PortSwigger — Mass assignment",
     "https://portswigger.net/web-security/access-control"),
    (r"PortSwigger SQLi", "PortSwigger — SQL injection",
     "https://portswigger.net/web-security/sql-injection"),
    (r"PortSwigger SSTI", "PortSwigger — SSTI",
     "https://portswigger.net/web-security/server-side-template-injection"),
    (r"PortSwigger XSS", "PortSwigger — XSS",
     "https://portswigger.net/web-security/cross-site-scripting"),
    (r"PortSwigger CSRF", "PortSwigger — CSRF",
     "https://portswigger.net/web-security/csrf"),
    (r"PortSwigger XXE", "PortSwigger — XXE",
     "https://portswigger.net/web-security/xxe"),
    (r"SpecterOps Kerberoasting", "SpecterOps — Kerberoasting",
     "https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91"),
    (r"SpecterOps Certified Pre-Owned", "SpecterOps — Certified Pre-Owned (AD CS)",
     "https://posts.specterops.io/certified-pre-owned-d95910965cd2"),
    (r"SpecterOps BloodHound", "SpecterOps — BloodHound docs",
     "https://bloodhound.specterops.io/"),
    (r"SpecterOps DPAPI", "SpecterOps — DPAPI",
     "https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107"),
    (r"SpecterOps AD", "SpecterOps — AD security",
     "https://posts.specterops.io/"),
    (r"HackTricks Linux PrivEsc", "HackTricks — Linux Privilege Escalation",
     "https://book.hacktricks.xyz/linux-hardening/privilege-escalation"),
    (r"PayloadsAllTheThings GraphQL", "PayloadsAllTheThings — GraphQL",
     "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection"),
    (r"PayloadsAllTheThings SSTI", "PayloadsAllTheThings — SSTI",
     "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection"),
    (r"PayloadsAllTheThings Windows", "PayloadsAllTheThings — Methodology and Resources",
     "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources"),
    (r"AWS IMDSv2", "AWS — IMDSv2",
     "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html"),
    (r"AWS S3", "AWS — S3 security best practices",
     "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"),
    (r"Rhino Security Labs AWS", "Rhino Security Labs — AWS privilege escalation",
     "https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/"),
    (r"MSFT Entra|Microsoft Password Spray|RoadTools",
     "Microsoft Learn — Entra ID security",
     "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health"),
    (r"Kubernetes Attack Matrix", "Microsoft — Kubernetes attack matrix",
     "https://microsoft.github.io/Threat-Matrix-for-Kubernetes/"),
    (r"NSA/CISA k8s", "NSA/CISA — Kubernetes hardening",
     "https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF"),
    (r"GTFOBins", "GTFOBins", "https://gtfobins.github.io/"),
    (r"Frida docs", "Frida documentation", "https://frida.re/docs/home/"),
    (r"Atomic Red Team", "Atomic Red Team", "https://github.com/redcanaryco/atomic-red-team"),
    (r"Mozilla TLS", "Mozilla SSL Configuration Generator",
     "https://ssl-config.mozilla.org/"),
    (r"RFC 1035", "RFC 1035 — DNS", "https://www.rfc-editor.org/rfc/rfc1035"),
    (r"RFC 9110", "RFC 9110 — HTTP Semantics", "https://www.rfc-editor.org/rfc/rfc9110"),
    (r"RFC 7519", "RFC 7519 — JWT", "https://www.rfc-editor.org/rfc/rfc7519"),
    (r"RFC 6749", "RFC 6749 — OAuth 2.0", "https://www.rfc-editor.org/rfc/rfc6749"),
    (r"RFC 8252", "RFC 8252 — OAuth for Native Apps", "https://www.rfc-editor.org/rfc/rfc8252"),
    (r"NIST SP 800-63", "NIST SP 800-63", "https://pages.nist.gov/800-63-3/"),
    (r"OSINT Framework", "OSINT Framework", "https://osintframework.com/"),
    (r"CVSS", "FIRST — CVSS", "https://www.first.org/cvss/"),
    (r"PTES", "PTES", "http://www.pentest-standard.org/"),
    (r"OSSTMM", "OSSTMM", "https://www.isecom.org/research.html"),
    (r"CREST", "CREST guides", "https://www.crest-approved.org/"),
    (r"Aircrack", "Aircrack-ng documentation", "https://www.aircrack-ng.org/doku.php"),
    (r"SQLMap", "sqlmap — usage", "https://sqlmap.org/"),
    (r"Red Team Field Manual", "Red team ethics / ROE", "https://attack.mitre.org/"),
]

# refs extras por família (fid) — completam quando o seed não traz URL suficiente
FAMILY_REFS: dict[str, list[tuple[str, str]]] = {
    "recon-passive-dns": [
        ("crt.sh — Certificate Transparency", "https://crt.sh/"),
        ("HackTricks — DNS enumeration", "https://book.hacktricks.xyz/network-services-pentesting/pentesting-dns"),
    ],
    "recon-http-fingerprint": [
        ("PortSwigger — HTTP information gathering", "https://portswigger.net/web-security"),
        ("OWASP WSTG-INFO-02", "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server"),
    ],
    "recon-osint-people": [
        ("OSINT Framework", "https://osintframework.com/"),
        ("MITRE ATT&CK T1589", "https://attack.mitre.org/techniques/T1589/"),
    ],
    "web-idor": [
        ("PortSwigger — Access control", "https://portswigger.net/web-security/access-control"),
        ("OWASP API1 BOLA", "https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/"),
    ],
    "web-ssrf": [
        ("PortSwigger — SSRF", "https://portswigger.net/web-security/ssrf"),
        ("AWS IMDSv2", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html"),
    ],
    "web-upload": [
        ("PortSwigger — File upload vulnerabilities", "https://portswigger.net/web-security/file-upload"),
        ("OWASP File Upload Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html"),
    ],
    "api-jwt": [
        ("PortSwigger — JWT attacks", "https://portswigger.net/web-security/jwt"),
        ("RFC 7519 — JWT", "https://www.rfc-editor.org/rfc/rfc7519"),
    ],
    "api-graphql": [
        ("OWASP GraphQL Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html"),
        ("PayloadsAllTheThings — GraphQL", "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection"),
    ],
    "api-mass-assignment": [
        ("OWASP API3 BOPLA", "https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/"),
        ("PortSwigger — Mass assignment", "https://portswigger.net/web-security/access-control"),
    ],
    "auth-password-spray": [
        ("MITRE ATT&CK T1110.003", "https://attack.mitre.org/techniques/T1110/003/"),
        ("Microsoft — Compromised credentials alerts", "https://learn.microsoft.com/en-us/defender-for-identity/compromised-credentials-alerts"),
    ],
    "auth-mfa-bypass": [
        ("OWASP MFA Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html"),
        ("MITRE ATT&CK T1621", "https://attack.mitre.org/techniques/T1621/"),
    ],
    "auth-oauth-oidc": [
        ("RFC 6749 — OAuth 2.0", "https://www.rfc-editor.org/rfc/rfc6749"),
        ("PortSwigger — OAuth authentication", "https://portswigger.net/web-security/oauth"),
    ],
    "inj-sqli": [
        ("PortSwigger — SQL injection", "https://portswigger.net/web-security/sql-injection"),
        ("OWASP SQL Injection", "https://owasp.org/www-community/attacks/SQL_Injection"),
    ],
    "inj-cmd": [
        ("OWASP OS Command Injection Defense", "https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html"),
        ("PortSwigger — OS command injection", "https://portswigger.net/web-security/os-command-injection"),
    ],
    "inj-ssti": [
        ("PortSwigger — SSTI", "https://portswigger.net/web-security/server-side-template-injection"),
        ("PayloadsAllTheThings — SSTI", "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection"),
    ],
    "client-xss": [
        ("PortSwigger — XSS", "https://portswigger.net/web-security/cross-site-scripting"),
        ("OWASP XSS Prevention", "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html"),
    ],
    "client-csrf": [
        ("PortSwigger — CSRF", "https://portswigger.net/web-security/csrf"),
        ("OWASP CSRF Prevention", "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"),
    ],
    "xxe-classic": [
        ("PortSwigger — XXE", "https://portswigger.net/web-security/xxe"),
        ("OWASP XXE Prevention", "https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html"),
    ],
    "net-llmnr-nbt": [
        ("MITRE ATT&CK T1557.001", "https://attack.mitre.org/techniques/T1557/001/"),
        ("HackTricks — LLMNR/NBT-NS spoofing", "https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks"),
    ],
    "net-smb": [
        ("MITRE ATT&CK T1135", "https://attack.mitre.org/techniques/T1135/"),
        ("HackTricks — SMB", "https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb"),
    ],
    "ad-kerberoast": [
        ("SpecterOps — Kerberoasting", "https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91"),
        ("MITRE ATT&CK T1558.003", "https://attack.mitre.org/techniques/T1558/003/"),
        ("SpecterOps — BloodHound", "https://bloodhound.specterops.io/"),
    ],
    "ad-dacl": [
        ("SpecterOps — BloodHound edges", "https://bloodhound.specterops.io/"),
        ("MITRE ATT&CK T1484", "https://attack.mitre.org/techniques/T1484/"),
    ],
    "ad-cs": [
        ("SpecterOps — Certified Pre-Owned", "https://posts.specterops.io/certified-pre-owned-d95910965cd2"),
        ("MITRE ATT&CK T1649", "https://attack.mitre.org/techniques/T1649/"),
    ],
    "win-privesc": [
        ("HackTricks — Windows Privilege Escalation", "https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation"),
        ("PayloadsAllTheThings — Methodology and Resources", "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources"),
    ],
    "win-cred": [
        ("SpecterOps — DPAPI", "https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107"),
        ("MITRE ATT&CK T1003", "https://attack.mitre.org/techniques/T1003/"),
    ],
    "linux-privesc": [
        ("HackTricks — Linux Privilege Escalation", "https://book.hacktricks.xyz/linux-hardening/privilege-escalation"),
        ("GTFOBins", "https://gtfobins.github.io/"),
    ],
    "aws-privesc": [
        ("Rhino Security Labs — AWS privEsc", "https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/"),
        ("AWS IAM best practices", "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"),
    ],
    "aws-s3": [
        ("AWS — S3 security best practices", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"),
        ("HackTricks — AWS S3", "https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3"),
    ],
    "azure-entra": [
        ("Microsoft Learn — Entra ID", "https://learn.microsoft.com/en-us/entra/identity/"),
        ("MITRE ATT&CK T1078.004", "https://attack.mitre.org/techniques/T1078/004/"),
    ],
    "k8s-escape": [
        ("NSA/CISA — Kubernetes hardening", "https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF"),
        ("Kubernetes Attack Matrix", "https://microsoft.github.io/Threat-Matrix-for-Kubernetes/"),
    ],
    "mobile-android": [
        ("OWASP MASTG — Android", "https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/"),
        ("Frida documentation", "https://frida.re/docs/home/"),
    ],
    "mobile-ios": [
        ("OWASP MASTG — iOS", "https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/"),
        ("Frida documentation", "https://frida.re/docs/home/"),
    ],
    "wifi-evil-twin": [
        ("Aircrack-ng documentation", "https://www.aircrack-ng.org/doku.php"),
        ("HackTricks — WiFi", "https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi"),
    ],
    "rt-c2": [
        ("MITRE ATT&CK — Command and Control", "https://attack.mitre.org/tactics/TA0011/"),
        ("Atomic Red Team", "https://github.com/redcanaryco/atomic-red-team"),
    ],
    "purple-detect": [
        ("SigmaHQ rules", "https://github.com/SigmaHQ/sigma"),
        ("Atomic Red Team", "https://github.com/redcanaryco/atomic-red-team"),
    ],
    "crypto-tls": [
        ("Mozilla SSL Configuration Generator", "https://ssl-config.mozilla.org/"),
        ("OWASP Transport Layer Protection", "https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html"),
    ],
    "report-quality": [
        ("FIRST — CVSS", "https://www.first.org/cvss/"),
        ("PTES", "http://www.pentest-standard.org/"),
    ],
    "method-scope": [
        ("PTES Pre-engagement", "http://www.pentest-standard.org/index.php/Pre-engagement"),
        ("CREST guides", "https://www.crest-approved.org/"),
    ],
}

# slug → refs extras (sobrescreve/complementa família)
SLUG_REFS: dict[str, list[tuple[str, str]]] = {
    "esc1": [
        ("SpecterOps — Certified Pre-Owned (ESC1)", "https://posts.specterops.io/certified-pre-owned-d95910965cd2"),
    ],
    "imds": [
        ("AWS — Instance metadata", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html"),
    ],
    "dcsync": [
        ("MITRE ATT&CK T1003.006", "https://attack.mitre.org/techniques/T1003/006/"),
    ],
    "alg-none": [
        ("PortSwigger — JWT algorithm confusion", "https://portswigger.net/web-security/jwt"),
    ],
}

MITRE_ID_RE = re.compile(r"T\d{4}(?:\.\d{3})?")
WSTG_ID_RE = re.compile(r"WSTG-[A-Z]+-\d+(?:/\d+)?")


def mitre_url(tid: str) -> str:
    tid = tid.strip().upper()
    if "." in tid:
        base, sub = tid.split(".", 1)
        return f"https://attack.mitre.org/techniques/{base}/{sub}/"
    return f"https://attack.mitre.org/techniques/{tid}/"


def extract_mitre_ids(text: str) -> list[str]:
    seen: list[str] = []
    for m in MITRE_ID_RE.findall(text or ""):
        if m not in seen:
            seen.append(m)
    return seen


def extract_wstg_ids(text: str) -> list[str]:
    seen: list[str] = []
    for m in WSTG_ID_RE.findall(text or ""):
        # normaliza WSTG-INPV-01/02 → WSTG-INPV-01
        base = m.split("/")[0]
        if base not in seen:
            seen.append(base)
    return seen


# páginas oficiais WSTG mais comuns
WSTG_URLS: dict[str, str] = {
    "WSTG-INFO-01": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/01-Conduct_Search_Engine_Discovery_Reconnaissance_for_Information_Leakage",
    "WSTG-INFO-02": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server",
    "WSTG-INFO-05": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Web_Page_Content_for_Information_Leakage",
    "WSTG-ATHZ-01": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include",
    "WSTG-ATHZ-04": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema",
    "WSTG-BUSL-08": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types",
    "WSTG-INPV-01": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting",
    "WSTG-INPV-02": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting",
    "WSTG-INPV-12": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection",
    "WSTG-INPV-19": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery",
}


def _match_seed_ref(text: str) -> tuple[str, str] | None:
    for pat, title, url in SEED_REF_MAP:
        if re.search(pat, text, re.I):
            return title, url
    # MITRE genérico com id no texto
    ids = extract_mitre_ids(text)
    if ids and re.search(r"MITRE", text, re.I):
        return f"MITRE ATT&CK {ids[0]}", mitre_url(ids[0])
    wstg = extract_wstg_ids(text)
    if wstg and wstg[0] in WSTG_URLS:
        return wstg[0], WSTG_URLS[wstg[0]]
    return None


def _dedupe(refs: Iterable[tuple[str, str]], limit: int = 5) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    for title, url in refs:
        if not url or url in seen_urls:
            continue
        if title in seen_titles:
            continue
        seen_urls.add(url)
        seen_titles.add(title)
        out.append((title, url))
        if len(out) >= limit:
            break
    return out


def resolve_refs(row: dict) -> list[tuple[str, str]]:
    """Retorna 2–5 pares (título, url) para a nota."""
    collected: list[tuple[str, str]] = []

    # 1) MITRE a partir do campo mitre
    for tid in extract_mitre_ids(row.get("mitre") or ""):
        collected.append((f"MITRE ATT&CK {tid}", mitre_url(tid)))

    # 2) WSTG a partir de owasp/refs
    blob = " ".join([row.get("owasp") or ""] + list(row.get("refs") or []))
    for wid in extract_wstg_ids(blob):
        if wid in WSTG_URLS:
            collected.append((wid, WSTG_URLS[wid]))

    # 3) refs do seed → URL
    for raw in row.get("refs") or []:
        hit = _match_seed_ref(raw)
        if hit:
            collected.append(hit)
        else:
            # mantém como link âncora local? melhor pular texto sem URL
            # tenta MITRE id solto
            ids = extract_mitre_ids(raw)
            if ids:
                collected.append((raw.strip(), mitre_url(ids[0])))

    # 4) slug / família
    slug = row.get("slug") or ""
    fid = row.get("fid") or ""
    for item in SLUG_REFS.get(slug, []):
        collected.append(item)
    for item in FAMILY_REFS.get(fid, []):
        collected.append(item)

    refs = _dedupe(collected, limit=5)
    # garante mínimo 2 quando possível
    if len(refs) < 2:
        refs = _dedupe(refs + [("MITRE ATT&CK", "https://attack.mitre.org/")], limit=5)
    return refs


def format_refs_md(row: dict) -> str:
    """Lista Markdown `- [título](url)`."""
    refs = resolve_refs(row)
    if not refs:
        return "- (sem refs curadas)"
    return "\n".join(f"- [{t}]({u})" for t, u in refs)
