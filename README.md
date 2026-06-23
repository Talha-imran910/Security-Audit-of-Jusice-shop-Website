# Security Audit Report: OWASP Juice Shop

## 📋 Project Overview
This repository contains the documentation, logs, and findings from a comprehensive security audit of the OWASP Juice Shop application. The audit was conducted to identify vulnerabilities and assess the overall security posture of the target application.

## 👤 Auditor
**Name:** Ahmed Imran  
**Date:** June 23, 2026

## 🛠️ Tools Used
* **OWASP Juice Shop:** Target application.
* **Nikto:** Web server reconnaissance and info leakage detection.
* **sqlmap:** Automated SQL injection testing and data exfiltration.
* **Firefox (Manual Testing):** Verification of client-side vulnerabilities (XSS, CSRF).
* **Python:** Custom script used to generate the final audit report.

## 🔍 Vulnerability Summary
| Vulnerability | Category (OWASP 2021) | Severity |
| :--- | :--- | :--- |
| SQL Injection | A03: Injection | CRITICAL |
| Broken Authentication | A07: Identification & Auth Failures | CRITICAL |
| Cross-Site Scripting (XSS) | A03: Injection | HIGH |
| CSRF | A05: Security Misconfiguration | HIGH |
| Sensitive Data Exposure | A02: Cryptographic Failures | HIGH |

## 📁 Repository Contents
* `audit_report.py`: The script used to generate the final findings.
* `nikto_results.txt.txt`: Raw recon data from the server scan.
* `csrf_test.html`: Proof-of-concept file used for CSRF testing.
* `screenshots/`: Evidence folder containing proof of XSS and SQLi exploits.

## 🚀 How to Run the Audit Report
1. Ensure you are in the Kali environment.
2. Navigate to the project directory: `cd ~/security-audit/`
3. Execute the report generator:
```bash
   python3 audit_report.py
