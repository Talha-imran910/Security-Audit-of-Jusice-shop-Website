import datetime

print("=" * 65)
print("   SECURITY AUDIT REPORT — INTERNEE.PK")
print("   Conducted using OWASP Juice Shop + OWASP ZAP")
print("=" * 65)
print(f"   Date: {datetime.datetime.now().strftime('%B %d, %Y')}")
print(f"   Auditor: Talha Imran")
print(f"   Target: http://localhost:3000 (OWASP Juice Shop)")
print("=" * 65)

vulnerabilities = [
    {
        "id": "VULN-001",
        "name": "SQL Injection",
        "owasp": "A03:2021",
        "severity": "CRITICAL",
        "location": "/rest/user/login — email field",
        "payload": "' OR 1=1--",
        "impact": "Authentication bypass, full DB access",
        "mitre": "T1190 - Exploit Public-Facing Application",
        "fix": "Use parameterized queries / prepared statements"
    },
    {
        "id": "VULN-002", 
        "name": "Cross-Site Scripting (XSS)",
        "owasp": "A03:2021",
        "severity": "HIGH",
        "location": "Search bar, Customer Feedback form",
        "payload": "<script>alert('XSS')</script>",
        "impact": "Session hijacking, credential theft",
        "mitre": "T1059.007 - JavaScript",
        "fix": "Input validation + Content Security Policy"
    },
    {
        "id": "VULN-003",
        "name": "Cross-Site Request Forgery (CSRF)",
        "owasp": "A05:2021",
        "severity": "HIGH",
        "location": "/api/BasketItems/ and other endpoints",
        "payload": "Cross-origin POST without token",
        "impact": "Unauthorized actions on behalf of users",
        "mitre": "T1185 - Browser Session Hijacking",
        "fix": "Implement CSRF tokens on all state-changing requests"
    },
    {
        "id": "VULN-004",
        "name": "Broken Authentication",
        "owasp": "A07:2021",
        "severity": "CRITICAL",
        "location": "/rest/user/login",
        "payload": "SQLi bypass without valid credentials",
        "impact": "Complete account takeover",
        "mitre": "T1110 - Brute Force",
        "fix": "MFA implementation + account lockout"
    },
    {
        "id": "VULN-005",
        "name": "Sensitive Data Exposure",
        "owasp": "A02:2021",
        "severity": "HIGH",
        "location": "/api/Users/ endpoint",
        "payload": "GET request returns user data",
        "impact": "PII exposure, credential leakage",
        "mitre": "T1552 - Unsecured Credentials",
        "fix": "Implement proper authorization + data masking"
    }
]

severity_count = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}

for vuln in vulnerabilities:
    severity_count[vuln["severity"]] += 1
    print(f"\n{'='*65}")
    print(f"  [{vuln['id']}] {vuln['name']}")
    print(f"{'='*65}")
    print(f"  OWASP Category : {vuln['owasp']}")
    print(f"  Severity       : {vuln['severity']}")
    print(f"  Location       : {vuln['location']}")
    print(f"  Payload Used   : {vuln['payload']}")
    print(f"  Impact         : {vuln['impact']}")
    print(f"  MITRE ATT&CK   : {vuln['mitre']}")
    print(f"  Recommendation : {vuln['fix']}")

print(f"\n{'='*65}")
print("  SUMMARY")
print(f"{'='*65}")
print(f"  Total Vulnerabilities Found : {len(vulnerabilities)}")
print(f"  Critical : {severity_count['CRITICAL']}")
print(f"  High     : {severity_count['HIGH']}")
print(f"  Medium   : {severity_count['MEDIUM']}")
print(f"  Low      : {severity_count['LOW']}")
print(f"\n  Overall Risk Level : CRITICAL")
print(f"  Immediate Action Required : YES")
print(f"{'='*65}")
print("\n  Tools Used:")
print("  - OWASP ZAP (Automated Scanner)")
print("  - sqlmap (SQL Injection)")
print("  - OWASP Juice Shop (Target)")
print("  - Manual Testing (XSS, CSRF)")
print(f"\n  Audit completed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

