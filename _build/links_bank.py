"""Cross-links entre notas: variantes de ângulo, irmãs da família e paths curados."""
from __future__ import annotations

from typing import Any

# ângulo interno (seed/build) → sufixo de arquivo / chave frontmatter
ANGLE_META: dict[str | None, tuple[str, str]] = {
    None: ("base", ""),
    "detecção": ("detecao", "--detecao"),
    "lab": ("lab", "--lab"),
    "evidência": ("evidencia", "--evidencia"),
    "path": ("path", "--path"),
    "hardening": ("hardening", "--hardening"),
}

ANGLE_ORDER = ("base", "lab", "detecao", "evidencia", "path", "hardening")

# Paths curados: (fid, slug) → lista de (fid, slug) pivôs seguintes / irmãos de kill-chain
CURATED_PATHS: dict[tuple[str, str], list[tuple[str, str]]] = {
    # AD: roast → asrep → bloodhound → dcsync / CS
    ("ad-kerberoast", "rc4"): [
        ("ad-kerberoast", "asrep"),
        ("ad-kerberoast", "bloodhound"),
        ("ad-dacl", "dcsync"),
    ],
    ("ad-kerberoast", "aes"): [
        ("ad-kerberoast", "bloodhound"),
        ("ad-dacl", "genericall"),
    ],
    ("ad-kerberoast", "asrep"): [
        ("ad-kerberoast", "bloodhound"),
        ("ad-dacl", "dcsync"),
    ],
    ("ad-kerberoast", "bloodhound"): [
        ("ad-dacl", "dcsync"),
        ("ad-dacl", "genericall"),
        ("ad-cs", "esc1"),
    ],
    ("ad-dacl", "genericall"): [
        ("ad-dacl", "dcsync"),
        ("ad-dacl", "addmember"),
    ],
    ("ad-dacl", "writedacl"): [
        ("ad-dacl", "genericall"),
        ("ad-dacl", "dcsync"),
    ],
    ("ad-dacl", "dcsync"): [
        ("ad-cs", "esc1"),
        ("win-cred", "ntds"),
    ],
    ("ad-dacl", "writespn"): [
        ("ad-kerberoast", "rc4"),
    ],
    ("ad-dacl", "shadowcred"): [
        ("ad-cs", "esc1"),
        ("ad-dacl", "dcsync"),
    ],
    ("ad-cs", "esc1"): [
        ("ad-dacl", "dcsync"),
        ("ad-cs", "persist"),
    ],
    ("ad-cs", "esc8"): [
        ("net-llmnr-nbt", "petitpotam"),
        ("ad-dacl", "dcsync"),
    ],
    # SSRF → IMDS → AWS
    ("web-ssrf", "imds"): [
        ("aws-privesc", "imds"),
        ("aws-privesc", "passrole"),
        ("aws-s3", "public-get"),
    ],
    ("web-ssrf", "blind"): [
        ("web-ssrf", "imds"),
        ("xxe-classic", "ssrf"),
    ],
    ("web-ssrf", "file-proto"): [
        ("xxe-classic", "file-read"),
    ],
    ("aws-privesc", "imds"): [
        ("aws-privesc", "passrole"),
        ("aws-privesc", "assume-role"),
        ("aws-s3", "policy"),
    ],
    ("aws-privesc", "passrole"): [
        ("aws-privesc", "lambda-update"),
        ("aws-s3", "acl"),
    ],
    # Web IDOR / API
    ("web-idor", "numeric"): [
        ("web-idor", "batch"),
        ("api-mass-assignment", "role-flag"),
        ("api-jwt", "claim-tamper"),
    ],
    ("web-idor", "graphql"): [
        ("api-graphql", "field-authz"),
        ("api-mass-assignment", "graphql-input"),
    ],
    ("api-jwt", "alg-none"): [
        ("api-jwt", "claim-tamper"),
        ("api-mass-assignment", "role-flag"),
        ("auth-oauth-oidc", "scope-escalation"),
    ],
    ("api-jwt", "rs-hs"): [
        ("api-jwt", "alg-none"),
        ("api-jwt", "jku"),
    ],
    ("api-mass-assignment", "role-flag"): [
        ("web-idor", "numeric"),
        ("auth-oauth-oidc", "scope-escalation"),
    ],
    ("api-mass-assignment", "tenant"): [
        ("web-idor", "uuid"),
        ("api-graphql", "field-authz"),
    ],
    # Auth chains
    ("auth-password-spray", "o365"): [
        ("auth-mfa-bypass", "fatigue"),
        ("azure-entra", "ca-gap"),
    ],
    ("auth-mfa-bypass", "oauth-skip"): [
        ("auth-oauth-oidc", "redirect"),
        ("api-jwt", "claim-tamper"),
    ],
    ("auth-oauth-oidc", "redirect"): [
        ("auth-oauth-oidc", "state"),
        ("client-xss", "reflected"),
    ],
    # Injection → RCE path
    ("inj-sqli", "mysql-error"): [
        ("inj-cmd", "unix-blind"),
        ("web-upload", "webshell"),
    ],
    ("inj-ssti", "jinja2"): [
        ("inj-cmd", "unix-blind"),
        ("linux-privesc", "sudo"),
    ],
    ("inj-cmd", "unix-blind"): [
        ("linux-privesc", "suid"),
        ("k8s-escape", "sa-token"),
    ],
    # Client
    ("client-xss", "stored"): [
        ("client-csrf", "token-missing"),
        ("auth-oauth-oidc", "referrer"),
    ],
    ("client-csrf", "token-missing"): [
        ("api-mass-assignment", "role-flag"),
    ],
    # Network → AD
    ("net-llmnr-nbt", "smb-relay"): [
        ("net-smb", "signing"),
        ("ad-dacl", "dcsync"),
        ("ad-cs", "esc8"),
    ],
    ("net-llmnr-nbt", "petitpotam"): [
        ("ad-cs", "esc8"),
        ("ad-dacl", "dcsync"),
    ],
    ("net-smb", "gpp"): [
        ("win-cred", "dpapi"),
        ("ad-dacl", "genericall"),
    ],
    # Windows / Linux
    ("win-privesc", "potato"): [
        ("win-cred", "lsass"),
        ("ad-dacl", "dcsync"),
    ],
    ("win-cred", "lsass"): [
        ("ad-dacl", "dcsync"),
        ("win-cred", "ntds"),
    ],
    ("linux-privesc", "docker"): [
        ("k8s-escape", "docker-sock"),
        ("linux-privesc", "suid"),
    ],
    ("linux-privesc", "suid"): [
        ("linux-privesc", "sudo"),
        ("linux-privesc", "caps"),
    ],
    # Azure / K8s
    ("azure-entra", "consent"): [
        ("azure-entra", "app-role"),
        ("azure-entra", "prt"),
    ],
    ("azure-entra", "prt"): [
        ("azure-entra", "device-code"),
        ("auth-oauth-oidc", "implicit"),
    ],
    ("k8s-escape", "sa-token"): [
        ("k8s-escape", "rbac"),
        ("k8s-escape", "privileged"),
    ],
    ("k8s-escape", "imds"): [
        ("aws-privesc", "imds"),
        ("k8s-escape", "hostpath"),
    ],
    # Mobile / wireless / purple
    ("mobile-android", "deeplink"): [
        ("mobile-android", "webview"),
        ("mobile-android", "storage"),
    ],
    ("mobile-ios", "url-scheme"): [
        ("mobile-ios", "keychain"),
        ("mobile-ios", "ats"),
    ],
    ("wifi-evil-twin", "portal"): [
        ("auth-password-spray", "vpn"),
        ("wifi-evil-twin", "detect"),
    ],
    ("rt-c2", "https"): [
        ("purple-detect", "sigma"),
        ("rt-c2", "killswitch"),
    ],
    ("purple-detect", "atomic"): [
        ("purple-detect", "sigma"),
        ("purple-detect", "sysmon"),
    ],
    # Recon → web
    ("recon-passive-dns", "crtsh"): [
        ("recon-passive-dns", "spf-takeover"),
        ("recon-http-fingerprint", "tls-ja3"),
        ("web-idor", "numeric"),
    ],
    ("recon-passive-dns", "spf-takeover"): [
        ("recon-osint-people", "email-format"),
    ],
    ("crypto-tls", "legacy"): [
        ("crypto-tls", "weak-cipher"),
        ("recon-http-fingerprint", "tls-ja3"),
    ],
}

# irmãs preferidas por família (quando não há path curado específico)
FAMILY_SISTERS: dict[str, list[str]] = {
    "ad-kerberoast": ["rc4", "asrep", "bloodhound", "gmsa"],
    "ad-dacl": ["genericall", "dcsync", "shadowcred", "writespn"],
    "ad-cs": ["esc1", "esc8", "persist", "detect"],
    "web-ssrf": ["imds", "blind", "dns-rebind"],
    "web-idor": ["numeric", "batch", "graphql"],
    "api-jwt": ["alg-none", "rs-hs", "claim-tamper"],
    "aws-privesc": ["imds", "passrole", "assume-role"],
    "linux-privesc": ["suid", "sudo", "docker", "caps"],
    "k8s-escape": ["sa-token", "rbac", "privileged", "imds"],
    "azure-entra": ["consent", "prt", "ca-gap"],
}


def angle_frontmatter(ang: str | None) -> str:
    return ANGLE_META.get(ang, ("base", ""))[0]


def angle_suffix(ang: str | None) -> str:
    return ANGLE_META.get(ang, ("base", ""))[1]


def catalog_key(fid: str, slug: str, ang_key: str) -> str:
    return f"{fid}/{slug}/{ang_key}"


def build_catalog(entries: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """entries: {fid, slug, ang_key, cat, fname, title, idx}"""
    return {catalog_key(e["fid"], e["slug"], e["ang_key"]): e for e in entries}


def _rel_path(from_cat: str, to_cat: str, to_fname: str) -> str:
    if from_cat == to_cat:
        return to_fname
    return f"../{to_cat}/{to_fname}"


def _link_line(from_cat: str, entry: dict[str, Any], label: str | None = None) -> str:
    title = label or entry["title"]
    href = _rel_path(from_cat, entry["cat"], entry["fname"])
    return f"- [{title}]({href})"


def related_md(
    row: dict,
    ang: str | None,
    catalog: dict[str, dict[str, Any]],
    *,
    max_links: int = 12,
) -> str:
    """Seção Relacionadas: variantes → irmãs → paths curados."""
    fid, slug = row["fid"], row["slug"]
    cat = row["cat"]
    self_key = catalog_key(fid, slug, angle_frontmatter(ang))
    lines: list[str] = []
    seen: set[str] = set()

    def add_entry(entry: dict[str, Any] | None, label: str | None = None) -> None:
        if not entry:
            return
        k = catalog_key(entry["fid"], entry["slug"], entry["ang_key"])
        if k == self_key or k in seen:
            return
        seen.add(k)
        lines.append(_link_line(cat, entry, label))

    # 1) variantes da mesma técnica (ângulos)
    for ak in ANGLE_ORDER:
        e = catalog.get(catalog_key(fid, slug, ak))
        if not e:
            continue
        if ak == angle_frontmatter(ang):
            continue
        label = f"{e['title']} ({ak})" if ak != "base" else e["title"]
        # title do ângulo já costuma trazer " — lab"; evita duplicar
        if ak != "base" and e["title"].endswith(tuple(f" — {x}" for x in ("lab", "detecção", "evidência", "path", "hardening"))):
            label = e["title"]
        add_entry(e, label)

    # 2) irmãs da família (base)
    sisters = FAMILY_SISTERS.get(fid, [])
    if not sisters:
        # qualquer outro slug da mesma família presente no catálogo
        sisters = sorted({e["slug"] for e in catalog.values() if e["fid"] == fid and e["slug"] != slug})[:4]
    for s in sisters:
        if s == slug:
            continue
        e = catalog.get(catalog_key(fid, s, "base"))
        add_entry(e)

    # 3) paths curados (sempre base do alvo)
    for tfid, tslug in CURATED_PATHS.get((fid, slug), []):
        e = catalog.get(catalog_key(tfid, tslug, "base"))
        if e:
            add_entry(e, f"{e['title']} (path)")

    if not lines:
        # fallback: 2 irmãs quaisquer da categoria
        for e in catalog.values():
            if e["cat"] == cat and e["ang_key"] == "base" and e["fid"] == fid and e["slug"] != slug:
                add_entry(e)
            if len(lines) >= 3:
                break

    return "\n".join(lines[:max_links]) if lines else "- (sem relacionadas no índice atual)"
