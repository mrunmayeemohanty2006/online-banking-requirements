# Data Specification

**Project Name:** Online Banking Application

**Version No.:** 1.0

**Status:** RAW

**Approval Status:** NOT_APPROVED

**READY_FOR_HUMAN_REVIEW**

---

## 1. Introduction

This Data Specification describes business/functional data required by the approved requirements. It is NOT a database schema. No tables, engines, indexes, ORM models, or infrastructure are specified.

---

## 2. Data Entities

### DS-001 - Customer

| Field | Value |
| :--- | :--- |
| **Purpose** | A customer actor within the simulation who completes onboarding, provides KYC, activates an account, logs in/out, transfers and receives simulated money, and views/downloads statements. |
| **Source business requirement(s)** | BR-001, BR-002, BR-003, BR-004, BR-005, BR-006, BR-007, BR-008, BR-009, BR-010 |
| **Data notes** | Represented using synthetic identity data (BR-021). Exact data fields and validation constraints remain OPEN (OQ-013). |
| **Traceability (FR)** | FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010 |

### DS-002 - KYC Information

| Field | Value |
| :--- | :--- |
| **Purpose** | KYC information provided by the customer, including Aadhaar and PAN information that is format-only and mocked. |
| **Source business requirement(s)** | BR-002, BR-003, BR-011, BR-012 |
| **Data notes** | Aadhaar/PAN verification is format-only and mocked; no real identity verification is performed (BR-002). Exact data fields and validation constraints remain OPEN (OQ-013). |
| **Traceability (FR)** | FR-002, FR-003, FR-011, FR-012 |

### DS-003 - Account

| Field | Value |
| :--- | :--- |
| **Purpose** | A customer account that can be activated or frozen by the customer or bank operations, and whose state is viewable. |
| **Source business requirement(s)** | BR-004, BR-013, BR-014, BR-015 |
| **Data notes** | Account state changes are auditable (BR-006). Exact account-state rules remain OPEN (OQ-006). |
| **Traceability (FR)** | FR-004, FR-013, FR-014, FR-015 |

### DS-004 - Simulated Balance

| Field | Value |
| :--- | :--- |
| **Purpose** | Synthetic simulated balance associated with accounts within the simulation. |
| **Source business requirement(s)** | BR-007, BR-008, BR-021 |
| **Data notes** | Balances are simulated using synthetic data (BR-001, BR-021). Minimum balance value remains OPEN (OQ-002). |
| **Traceability (FR)** | FR-007, FR-008, FR-021 |

### DS-005 - Beneficiary

| Field | Value |
| :--- | :--- |
| **Purpose** | Synthetic beneficiary data used within the simulation for money movement. |
| **Source business requirement(s)** | BR-021 |
| **Data notes** | Beneficiaries are synthetic (BR-021). Beneficiary management is out of scope per the approved BRD scope of work. |
| **Traceability (FR)** | FR-021 |

### DS-006 - Simulated Payment

| Field | Value |
| :--- | :--- |
| **Purpose** | Synthetic simulated payment representing transfer/receipt of simulated money. |
| **Source business requirement(s)** | BR-007, BR-008, BR-021 |
| **Data notes** | Payments are simulated using synthetic data (BR-001, BR-021). Transfer/payment rules and limits remain OPEN (OQ-007, OQ-003). |
| **Traceability (FR)** | FR-007, FR-008, FR-021 |

### DS-007 - Statement

| Field | Value |
| :--- | :--- |
| **Purpose** | Statement data viewable and downloadable by the customer. |
| **Source business requirement(s)** | BR-009, BR-010 |
| **Data notes** | Statement content and download behaviour details remain OPEN (OQ-008). |
| **Traceability (FR)** | FR-009, FR-010 |

### DS-008 - Audit Trail

| Field | Value |
| :--- | :--- |
| **Purpose** | Record of auditable state changes accessible to bank operations. |
| **Source business requirement(s)** | BR-016, BR-020 |
| **Data notes** | State changes are auditable (BR-006). Exact audit events to be recorded remain OPEN (OQ-011). |
| **Traceability (FR)** | FR-016, FR-020 |

### DS-009 - Role

| Field | Value |
| :--- | :--- |
| **Purpose** | Roles (Customer and Bank Operations) used to keep journeys distinct via role-based access. |
| **Source business requirement(s)** | BR-019 |
| **Data notes** | Two distinct roles exist (BR-005 business rule). Exact role permissions and authorization rules remain OPEN (OQ-009). |
| **Traceability (FR)** | FR-019 |

---

## Status

- **Status:** RAW
- **Ready for human review:** READY_FOR_HUMAN_REVIEW
- **Approval status:** NOT_APPROVED
- **Version:** 1.0
