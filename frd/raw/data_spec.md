# Data Specification

## Metadata

- **Project:** Online Banking Application
- **Project Code:** ONLINE-BANKING
- **Artifact:** Data Specification
- **Version:** 1.0
- **Status:** RAW
- **Approval Status:** NOT_APPROVED
- **Generated At:** 2026-09-07T00:00:00Z
- **Generator Agent:** FRD Agent
- **Document Status:** RAW - READY_FOR_HUMAN_REVIEW
- **Source Basis:** brd/raw/brd.json, brd/raw/business_rules.json, brd/raw/open_questions.json

## Introduction

This Data Specification describes the business/functional data used by the Online Banking Application as required by the FRD.

This specification is not a database schema. It describes functional/business data and names no tables, columns, indexes, databases, or implementation architecture.

**Audience:** Architecture and Development teams, Quality Assurance and Testing teams, Human reviewers and approvers of functional requirements

## Data Entries

### DS-001 — Customer Profile

**Description:** Business/functional identity data for a customer using the simulation.

**Purpose:** Supports onboarding and identifies the customer across journeys.

**Related Functional Requirements:** FR-001

**Notes:** Exact fields and validation constraints are unresolved (see OQ-013). Identity data is synthetic (see FR-021).

### DS-002 — KYC Information

**Description:** KYC information supplied by the customer during onboarding.

**Purpose:** Supports KYC capture and bank-operations review (see FR-002, FR-011, FR-012).

**Related Functional Requirements:** FR-002, FR-011, FR-012

**Notes:** KYC is captured for the simulation and is subject to no real verification (constraint CON-003). Exact fields and validation constraints are unresolved (see OQ-013).

### DS-003 — Aadhaar/PAN Information

**Description:** Aadhaar and PAN details provided by the customer, verified format-only and mocked.

**Purpose:** Supports capture of Aadhaar/PAN details without real identity verification.

**Related Functional Requirements:** FR-003

**Notes:** Verification is format-only and mocked (CON-003, business rule BR-002). Exact fields and format rules are unresolved (see OQ-013).

### DS-004 — Account Data

**Description:** Customer account information used in the simulation.

**Purpose:** Supports account activation, transfers, and statement journeys.

**Related Functional Requirements:** FR-004, FR-007, FR-008, FR-009, FR-010, FR-013, FR-014, FR-015

**Notes:** Accounts are synthetic (see FR-021). Exact account data fields and account-state rules are unresolved (see OQ-006, OQ-013).

### DS-005 — Account State

**Description:** The state of a customer account (for example, active or frozen) as used by bank operations and customers.

**Purpose:** Supports account activation/freezing, transfers, and state visibility.

**Related Functional Requirements:** FR-004, FR-007, FR-008, FR-013, FR-014, FR-015, FR-020

**Notes:** Exact account-state values and rules are unresolved (see OQ-006). State changes must be auditable (see FR-020).

### DS-006 — Balance Data

**Description:** Synthetic balance information associated with a customer account.

**Purpose:** Supports simulated transfer and receipt of money and balance visibility.

**Related Functional Requirements:** FR-007, FR-008

**Notes:** Balances are synthetic (see FR-021). Minimum balance and transfer-related limits are unresolved (see OQ-002, OQ-007).

### DS-007 — Beneficiary Data

**Description:** Beneficiary information used in the simulation.

**Purpose:** Supports transfer of simulated money.

**Related Functional Requirements:** FR-007, FR-021

**Notes:** Beneficiaries are synthetic (see FR-021). Beneficiary management itself is out of scope per the BRD; only the synthetic data used by the simulation is described.

### DS-008 — Payment/Transfer Data

**Description:** Records of simulated payments/transfers of money.

**Purpose:** Supports transfer and receipt of simulated money and statement generation.

**Related Functional Requirements:** FR-007, FR-008, FR-009, FR-010, FR-021

**Notes:** Payments are synthetic (see FR-021); real money movement is not permitted (CON-002). Exact transfer/payment rules and limits are unresolved (see OQ-007, OQ-013).

### DS-009 — Statement Data

**Description:** Data needed to present and download customer statements.

**Purpose:** Supports customer statement viewing and download.

**Related Functional Requirements:** FR-009, FR-010

**Notes:** Exact statement content and download behaviour are unresolved (see OQ-008).

### DS-010 — Role and Access Data

**Description:** Data representing the two roles (Customer and Bank Operations) and the actions permitted per role.

**Purpose:** Supports role-based access requirements.

**Related Functional Requirements:** FR-005, FR-011, FR-017, FR-019

**Notes:** Exact role permissions and authorization rules are unresolved (see OQ-009).

### DS-011 — Audit Trail Data

**Description:** Records of auditable state changes in the simulation.

**Purpose:** Supports auditable state changes and bank-operations access to the audit trail.

**Related Functional Requirements:** FR-016, FR-020

**Notes:** Exact audit events to be recorded are unresolved (see OQ-011).

### DS-012 — Session Data

**Description:** Data representing an authenticated session for a Customer or Bank Operations user.

**Purpose:** Supports login, logout, and role-based access.

**Related Functional Requirements:** FR-005, FR-006, FR-017, FR-018, FR-019

**Notes:** Exact authentication and session rules are unresolved (see OQ-009, OQ-010).

## Related FR Coverage

| Functional Requirement | Data Entries |
|---|---|
| FR-001 | DS-001 |
| FR-002 | DS-002 |
| FR-003 | DS-003 |
| FR-004 | DS-004, DS-005 |
| FR-005 | DS-010, DS-012 |
| FR-006 | DS-012 |
| FR-007 | DS-004, DS-005, DS-006, DS-007, DS-008 |
| FR-008 | DS-004, DS-005, DS-006, DS-008 |
| FR-009 | DS-004, DS-008, DS-009 |
| FR-010 | DS-004, DS-008, DS-009 |
| FR-011 | DS-002, DS-010 |
| FR-012 | DS-002 |
| FR-013 | DS-004, DS-005 |
| FR-014 | DS-004, DS-005 |
| FR-015 | DS-004, DS-005 |
| FR-016 | DS-011 |
| FR-017 | DS-010, DS-012 |
| FR-018 | DS-012 |
| FR-019 | DS-010, DS-012 |
| FR-020 | DS-005, DS-011 |
| FR-021 | DS-007, DS-008 |

---

**Version:** 1.0 | **Status:** RAW | **Approval Status:** NOT_APPROVED | **READY_FOR_HUMAN_REVIEW**
