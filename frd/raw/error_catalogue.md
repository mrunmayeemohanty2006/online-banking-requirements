# Error Catalogue

## Metadata

- **Project:** Online Banking Application
- **Project Code:** ONLINE-BANKING
- **Artifact:** Error Catalogue
- **Version:** 1.0
- **Status:** RAW
- **Approval Status:** NOT_APPROVED
- **Generated At:** 2026-09-07T00:00:00Z
- **Generator Agent:** FRD Agent
- **Document Status:** RAW - READY_FOR_HUMAN_REVIEW
- **Source Basis:** brd/raw/brd.json, brd/raw/business_rules.json, brd/raw/open_questions.json

## Introduction

This Error Catalogue documents validation and business errors derived from the FRD and the underlying BRD.

Each error traces to a functional requirement and, through it, to a business requirement. Exact error codes and messages are treated as unresolved because the source material leaves them open (OQ-012).

**Audience:** Architecture and Development teams, Quality Assurance and Testing teams, Defect Root Cause Analysis teams, Human reviewers and approvers of functional requirements

## Errors

### ERR-001 — Onboarding cannot be completed

**Description:** A customer is unable to complete the onboarding journey.

**Related Functional Requirement:** FR-001

**Source Business Requirement:** BR-001

**Severity:** UNSPECIFIED

**Condition:** Onboarding cannot be completed or accepted by the system.

**Expected Behavior:** The system shall surface a relevant error to the customer.

**Notes:** Exact error codes/messages are unresolved (see OQ-012); exact onboarding workflow and validation rules are unresolved (see OQ-005).

### ERR-002 — KYC information cannot be accepted

**Description:** KYC information provided by a customer cannot be accepted.

**Related Functional Requirement:** FR-002

**Source Business Requirement:** BR-002

**Severity:** UNSPECIFIED

**Condition:** KYC information cannot be accepted or recorded.

**Expected Behavior:** The system shall surface a relevant error to the customer.

**Notes:** Exact validation constraints and error text are unresolved (see OQ-012, OQ-013).

### ERR-003 — Aadhaar/PAN information fails format validation

**Description:** Aadhaar/PAN information provided by a customer does not conform to the expected format.

**Related Functional Requirement:** FR-003

**Source Business Requirement:** BR-003

**Severity:** UNSPECIFIED

**Condition:** Aadhaar/PAN information fails format-only, mocked validation.

**Expected Behavior:** The system shall surface a relevant error to the customer.

**Notes:** Format is format-only and mocked (CON-003). Exact format rules and error text are unresolved (see OQ-012, OQ-013).

### ERR-004 — Account activation cannot be performed

**Description:** A customer account cannot be activated.

**Related Functional Requirement:** FR-004

**Source Business Requirement:** BR-004

**Severity:** UNSPECIFIED

**Condition:** Account activation fails or is not permitted.

**Expected Behavior:** The system shall surface a relevant error to the requesting user.

**Notes:** Exact account-state rules and error text are unresolved (see OQ-006, OQ-012).

### ERR-005 — Customer login fails

**Description:** A customer cannot log in.

**Related Functional Requirement:** FR-005

**Source Business Requirement:** BR-005

**Severity:** UNSPECIFIED

**Condition:** Customer login fails, including invalid credentials or unauthorized access.

**Expected Behavior:** The system shall surface a relevant error to the customer.

**Notes:** Exact authentication and authorization rules and error text are unresolved (see OQ-009, OQ-010, OQ-012).

### ERR-006 — Transfer of simulated money cannot be completed

**Description:** A customer cannot complete a transfer of simulated money.

**Related Functional Requirement:** FR-007

**Source Business Requirement:** BR-007

**Severity:** UNSPECIFIED

**Condition:** A simulated transfer cannot be completed (for example, blocked by account state or unresolved limits).

**Expected Behavior:** The system shall surface a relevant error to the customer.

**Notes:** Exact transfer/payment rules and limits are unresolved (see OQ-007, OQ-012). Minimum balance and daily caps are open (see OQ-002, OQ-003).

### ERR-007 — Receipt of simulated money cannot be recorded

**Description:** Incoming simulated money cannot be recorded for a customer.

**Related Functional Requirement:** FR-008

**Source Business Requirement:** BR-008

**Severity:** UNSPECIFIED

**Condition:** A simulated receipt cannot be recorded.

**Expected Behavior:** The system shall surface a relevant error.

**Notes:** Exact transfer/payment rules and error text are unresolved (see OQ-007, OQ-012).

### ERR-008 — Statement cannot be presented or downloaded

**Description:** A customer cannot view or download a statement.

**Related Functional Requirement:** FR-009

**Source Business Requirement:** BR-009

**Severity:** UNSPECIFIED

**Condition:** A statement cannot be presented or downloaded.

**Expected Behavior:** The system shall surface a relevant error to the customer.

**Notes:** Statement content/download behaviour is unresolved (see OQ-008); error text is unresolved (see OQ-012). Relates to FR-010 for download behaviour.

### ERR-009 — KYC review or status update fails

**Description:** Bank operations cannot review KYC or set KYC status.

**Related Functional Requirement:** FR-012

**Source Business Requirement:** BR-012

**Severity:** UNSPECIFIED

**Condition:** KYC review fails or a KYC status update cannot be recorded.

**Expected Behavior:** The system shall surface a relevant error to bank operations.

**Notes:** See also FR-011 for KYC review. Exact status values and error text are unresolved (see OQ-012, OQ-013).

### ERR-010 — Account activation or freeze fails

**Description:** Bank operations cannot activate or freeze a customer account.

**Related Functional Requirement:** FR-013

**Source Business Requirement:** BR-013

**Severity:** UNSPECIFIED

**Condition:** An account activation or freeze cannot be performed.

**Expected Behavior:** The system shall surface a relevant error to bank operations.

**Notes:** See also FR-014 for account freeze. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012).

### ERR-011 — Customer account state cannot be viewed

**Description:** Bank operations cannot view a customer account's state.

**Related Functional Requirement:** FR-015

**Source Business Requirement:** BR-015

**Severity:** UNSPECIFIED

**Condition:** Account state cannot be presented to bank operations.

**Expected Behavior:** The system shall surface a relevant error to bank operations.

**Notes:** Exact error text is unresolved (see OQ-012).

### ERR-012 — Audit trail access fails

**Description:** Bank operations cannot access the audit trail.

**Related Functional Requirement:** FR-016

**Source Business Requirement:** BR-016

**Severity:** UNSPECIFIED

**Condition:** The audit trail cannot be accessed or returned.

**Expected Behavior:** The system shall surface a relevant error to bank operations.

**Notes:** Exact audit events are unresolved (see OQ-011); error text is unresolved (see OQ-012).

### ERR-013 — Bank-operations login fails

**Description:** Bank operations cannot log in.

**Related Functional Requirement:** FR-017

**Source Business Requirement:** BR-017

**Severity:** UNSPECIFIED

**Condition:** Bank-operations login fails, including invalid credentials or unauthorized access.

**Expected Behavior:** The system shall surface a relevant error to bank operations.

**Notes:** Exact authentication and authorization rules and error text are unresolved (see OQ-009, OQ-010, OQ-012).

### ERR-014 — Action not permitted by role

**Description:** A user attempts an action that is not permitted for their role.

**Related Functional Requirement:** FR-019

**Source Business Requirement:** BR-019

**Severity:** UNSPECIFIED

**Condition:** A user requests an action inconsistent with their role's permissions.

**Expected Behavior:** The system shall deny the action and surface a relevant error.

**Notes:** Exact role permissions and authorization rules are unresolved (see OQ-009); error text is unresolved (see OQ-012).

### ERR-015 — State change cannot be recorded for audit

**Description:** A state change cannot be recorded as an auditable event.

**Related Functional Requirement:** FR-020

**Source Business Requirement:** BR-020

**Severity:** UNSPECIFIED

**Condition:** An auditable state change cannot be recorded.

**Expected Behavior:** The system shall surface a relevant error and preserve auditable state-change behaviour.

**Notes:** Exact audit events are unresolved (see OQ-011); error text is unresolved (see OQ-012).

### ERR-016 — Logout cannot be completed

**Description:** A customer or bank-operations user cannot log out.

**Related Functional Requirement:** FR-006

**Source Business Requirement:** BR-006

**Severity:** UNSPECIFIED

**Condition:** Session termination cannot be completed for a customer or bank-operations user.

**Expected Behavior:** The system shall surface a relevant error.

**Notes:** Applies to FR-006 (customer) and FR-018 (bank operations). Exact error text is unresolved (see OQ-012).

## Error Traceability

| Error | Functional Requirement | Business Requirement |
|---|---|---|
| ERR-001 | FR-001 | BR-001 |
| ERR-002 | FR-002 | BR-002 |
| ERR-003 | FR-003 | BR-003 |
| ERR-004 | FR-004 | BR-004 |
| ERR-005 | FR-005 | BR-005 |
| ERR-006 | FR-007 | BR-007 |
| ERR-007 | FR-008 | BR-008 |
| ERR-008 | FR-009 | BR-009 |
| ERR-009 | FR-012 | BR-012 |
| ERR-010 | FR-013 | BR-013 |
| ERR-011 | FR-015 | BR-015 |
| ERR-012 | FR-016 | BR-016 |
| ERR-013 | FR-017 | BR-017 |
| ERR-014 | FR-019 | BR-019 |
| ERR-015 | FR-020 | BR-020 |
| ERR-016 | FR-006 | BR-006 |

## Consistency Notes

- The BRD business-rule artifact and the BRD document both use the ID prefix BR- for business rules (BR-001..BR-008), which is distinct from but identical-in-prefix to the business-requirement IDs (BR-001..BR-023). The convention is preserved verbatim from the approved source; no rewrite was made.
- All open questions OQ-001 through OQ-013 are carried forward from the BRD; none were silently resolved.
- ERR-016 intentionally traces to FR-006 (source BR-006, customer logout), which is noted because it also covers FR-018 (bank-operations logout). This is an explicit consistency note, not an invented requirement.
- No missing FR references were detected in the approved source material.

---

**Version:** 1.0 | **Status:** RAW | **Approval Status:** NOT_APPROVED | **READY_FOR_HUMAN_REVIEW**
