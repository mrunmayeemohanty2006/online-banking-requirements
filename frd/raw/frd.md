# Functional Requirements Document

**Project Name:** Online Banking Application

**Project Code:** ONLINE-BANKING

**Version No.:** 1.0

**Date:** 2026-09-07

**Status:** RAW

**Approval Status:** NOT_APPROVED

**READY_FOR_HUMAN_REVIEW**

---

## Revision History

| Version No | Date | Prepared by / Modified by | Significant Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-09-07 | FRD Agent | Initial RAW FRD generated for human review |

---

## 1. Introduction

### 1.1 Purpose

This Functional Requirements Document specifies, at the functional-behaviour level, exactly how the approved business requirements for the Online Banking Application simulation should behave. It is derived from the approved business requirements (BR-001 through BR-023) and provides BR to FR traceability. Detailed technical implementation is out of scope.

### 1.2 Scope

This FRD covers the functional behaviour derived from the approved business requirements for the Customer and Bank Operations roles, together with a Data Specification (functional/business data, not a database schema) and an Error Catalogue. Any behaviour whose details are not specified by the approved source is preserved as an Open Question and not invented.

### 1.3 No-invention note

No APIs, databases, frameworks, programming languages, UI frameworks, cloud services, authentication technologies, implementation algorithms, deployment architecture, or technical security mechanisms are specified. Undefined business behaviour is preserved and referenced to the relevant Open Question.

### 1.4 Source basis

- brd/approved/brd.json (requested; NOT PRESENT - used brd/raw per failure-condition instructions)
- brd/approved/business_rules.json (requested; NOT PRESENT - used brd/raw per failure-condition instructions)
- brd/approved/open_questions.json (requested; NOT PRESENT - used brd/raw per failure-condition instructions)
- brd/raw/brd.json
- brd/raw/business_rules.json
- brd/raw/open_questions.json

---

## 2. Traceability (BR -> FR)

Every functional requirement traces to an approved business requirement. No orphan FRs are present.

| Business Requirement | Functional Requirement |
| :--- | :--- |
| BR-001 | FR-001 |
| BR-002 | FR-002 |
| BR-003 | FR-003 |
| BR-004 | FR-004 |
| BR-005 | FR-005 |
| BR-006 | FR-006 |
| BR-007 | FR-007 |
| BR-008 | FR-008 |
| BR-009 | FR-009 |
| BR-010 | FR-010 |
| BR-011 | FR-011 |
| BR-012 | FR-012 |
| BR-013 | FR-013 |
| BR-014 | FR-014 |
| BR-015 | FR-015 |
| BR-016 | FR-016 |
| BR-017 | FR-017 |
| BR-018 | FR-018 |
| BR-019 | FR-019 |
| BR-020 | FR-020 |
| BR-021 | FR-021 |
| BR-022 | FR-022 |
| BR-023 | FR-023 |

---

## 3. Functional Requirements

### FR-001 - Customer completes onboarding

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to complete onboarding as a customer journey within the simulation. |
| **Source business requirement** | BR-001 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer actor exists within the simulation.<br>The customer role is recognised for role-based access (OQ-009). |
| **Trigger** | A customer initiates the onboarding journey. |
| **Functional behaviour** | The system presents the onboarding journey and records its completion for the customer within the simulation. The exact onboarding workflow and validation rules are not specified by the approved source and remain open (OQ-005). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | Customer identification/identity data within the simulation.<br>Onboarding initiation by a customer. |
| **Outputs** | Recorded completion of customer onboarding. |
| **Validation** | Onboarding completion is recorded against the customer. Detailed validation rules remain OPEN (OQ-005); no validation rules are invented beyond the approved source. |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-001 |
| **Open questions** | OQ-005, OQ-009, OQ-012 |

### FR-002 - Customer provides KYC information

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to provide KYC information as part of the customer journey. |
| **Source business requirement** | BR-002 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer actor exists within the simulation. |
| **Trigger** | A customer provides KYC information. |
| **Functional behaviour** | The system accepts and records KYC information provided by the customer. The exact KYC data fields and validation constraints are not specified by the approved source and remain open (OQ-013). |
| **Business rules applied** | The simulation must not perform real identity verification; Aadhaar/PAN verification is format-only and mocked.<br>The system must not integrate with production banks, real payment gateways, or external KYC integrations. |
| **Inputs** | KYC information provided by the customer. |
| **Outputs** | Recorded KYC information for the customer. |
| **Validation** | KYC information is recorded against the customer. Field-level validation constraints remain OPEN (OQ-013). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-002 |
| **Open questions** | OQ-012, OQ-013 |

### FR-003 - Customer provides Aadhaar and PAN information (format-only, mocked)

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to provide Aadhaar and PAN information. Verification of Aadhaar/PAN is format-only and mocked; no real identity verification is performed. |
| **Source business requirement** | BR-003 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer actor exists within the simulation.<br>No real identity verification is performed (BR-002). |
| **Trigger** | A customer provides Aadhaar and/or PAN information. |
| **Functional behaviour** | The system captures Aadhaar and PAN information. Verification, where present, is format-only and mocked. The system must not perform real identity verification (BR-002) and must not integrate with external KYC providers (BR-004). |
| **Business rules applied** | The simulation must not perform real identity verification; Aadhaar/PAN verification is format-only and mocked.<br>The system must not integrate with production banks, real payment gateways, or external KYC integrations. |
| **Inputs** | Aadhaar information provided by the customer.<br>PAN information provided by the customer. |
| **Outputs** | Recorded Aadhaar/PAN information and any format-only verification result. |
| **Validation** | Aadhaar/PAN verification is format-only and mocked; no real identity authority is consulted. Field-level validation constraints remain OPEN (OQ-013). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-003 |
| **Open questions** | OQ-012, OQ-013 |

### FR-004 - Customer activates an account

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to activate an account within the simulation. |
| **Source business requirement** | BR-004 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer actor exists within the simulation. |
| **Trigger** | A customer activates an account. |
| **Functional behaviour** | The system allows a customer to activate an account. Account activation may also be performed by bank operations (see FR-013). Account operations and account-state rules remain open (OQ-006). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access.<br>State changes in the system must be auditable. |
| **Inputs** | Account activation requested by the customer. |
| **Outputs** | Account moved to an activated state within the simulation.<br>State change recorded for audit (BR-006). |
| **Validation** | Activation transitions the account state in the simulation. Exact account-state rules remain OPEN (OQ-006). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-004 |
| **Open questions** | OQ-006, OQ-012 |

### FR-005 - Customer logs in

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to log in to the application. |
| **Source business requirement** | BR-005 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer actor exists within the simulation.<br>Role-based access is provided (BR-005 business rule). |
| **Trigger** | A customer requests to log in. |
| **Functional behaviour** | The system allows a customer to log in, establishing role-based access for the customer journey. Authentication mechanisms are not specified by the approved source and are not invented (OQ-010). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access.<br>Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. |
| **Inputs** | Customer login request. |
| **Outputs** | Customer session established for role-based access. |
| **Validation** | A successful login establishes a customer session. Authentication/login mechanism details remain OPEN (OQ-010, OQ-009). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-005 |
| **Open questions** | OQ-009, OQ-010, OQ-012 |

### FR-006 - Customer logs out

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to log out, terminating the customer session. |
| **Source business requirement** | BR-006 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer session exists within the simulation. |
| **Trigger** | A customer requests to log out. |
| **Functional behaviour** | The system allows a customer to log out, terminating the customer session. |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | Customer logout request. |
| **Outputs** | Customer session terminated. |
| **Validation** | Logout terminates the customer session. Session/termination mechanism details remain OPEN (OQ-010). |
| **Error behaviour** | Not specified by the approved source. |
| **Acceptance reference** | BR-006 |
| **Open questions** | OQ-010 |

### FR-007 - Customer transfers simulated money

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to transfer simulated money using synthetic data. |
| **Source business requirement** | BR-007 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer is logged in within the simulation.<br>Money movement is simulated using synthetic data (BR-001). |
| **Trigger** | A customer initiates a transfer of simulated money. |
| **Functional behaviour** | The system allows a customer to transfer simulated money. Money movement is simulated and must not involve real money (BR-001). The system must not perform credit decisioning, lending, or real financial transactions (BR-003). Exact transfer/payment rules and limits remain open (OQ-007, OQ-002, OQ-003). |
| **Business rules applied** | The simulation must not use real money; money movement is simulated using synthetic data.<br>The system must not perform credit decisioning, lending, or real financial transactions.<br>State changes in the system must be auditable. |
| **Inputs** | Transfer of simulated money initiated by the customer. |
| **Outputs** | Recorded simulated transfer.<br>Updated simulated balances.<br>State change recorded for audit (BR-006). |
| **Validation** | Transfers are simulated using synthetic data. Transfer/payment rules and limits, minimum balance, and daily transfer cap remain OPEN (OQ-007, OQ-002, OQ-003). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-007 |
| **Open questions** | OQ-002, OQ-003, OQ-007, OQ-012 |

### FR-008 - Customer receives simulated money

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to receive simulated money using synthetic data. |
| **Source business requirement** | BR-008 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer is logged in within the simulation.<br>Money movement is simulated using synthetic data (BR-001). |
| **Trigger** | A customer receives simulated money. |
| **Functional behaviour** | The system allows a customer to receive simulated money. Money movement is simulated and must not involve real money (BR-001). The system must not perform credit decisioning, lending, or real financial transactions (BR-003). Exact transfer/payment rules and limits remain open (OQ-007). |
| **Business rules applied** | The simulation must not use real money; money movement is simulated using synthetic data.<br>The system must not perform credit decisioning, lending, or real financial transactions.<br>State changes in the system must be auditable. |
| **Inputs** | Receipt of simulated money for the customer. |
| **Outputs** | Recorded simulated receipt.<br>Updated simulated balances.<br>State change recorded for audit (BR-006). |
| **Validation** | Receipts are simulated using synthetic data. Transfer/payment rules and limits remain OPEN (OQ-007). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-008 |
| **Open questions** | OQ-007, OQ-012 |

### FR-009 - Customer views statements

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to view statements. |
| **Source business requirement** | BR-009 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer is logged in within the simulation. |
| **Trigger** | A customer requests to view statements. |
| **Functional behaviour** | The system allows a customer to view statements. Statement content details remain open (OQ-008). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | Statement viewing request by the customer. |
| **Outputs** | Statements displayed to the customer. |
| **Validation** | Statements are displayed to the customer. Statement content details remain OPEN (OQ-008). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-009 |
| **Open questions** | OQ-008, OQ-012 |

### FR-010 - Customer downloads statements

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow a customer to download statements. |
| **Source business requirement** | BR-010 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A customer is logged in within the simulation. |
| **Trigger** | A customer requests to download statements. |
| **Functional behaviour** | The system allows a customer to download statements. Statement download behaviour details remain open (OQ-008). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | Statement download request by the customer. |
| **Outputs** | Statements made available for download to the customer. |
| **Validation** | Statements are downloadable by the customer. Download behaviour and content details remain OPEN (OQ-008). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-010 |
| **Open questions** | OQ-008, OQ-012 |

### FR-011 - Bank operations reviews KYC information

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to review KYC information. |
| **Source business requirement** | BR-011 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation.<br>Role-based access is provided (BR-005 business rule). |
| **Trigger** | Bank operations requests to review KYC information. |
| **Functional behaviour** | The system allows bank operations to review KYC information. The exact review workflow and data displayed remain open (OQ-005, OQ-013). |
| **Business rules applied** | The system must not integrate with production banks, real payment gateways, or external KYC integrations.<br>The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | KYC review request by bank operations. |
| **Outputs** | KYC information displayed to bank operations. |
| **Validation** | KYC information is displayed to bank operations for review. Review workflow details remain OPEN (OQ-005). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-011 |
| **Open questions** | OQ-005, OQ-012, OQ-013 |

### FR-012 - Bank operations sets KYC status

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to set KYC status. |
| **Source business requirement** | BR-012 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation. |
| **Trigger** | Bank operations sets a KYC status. |
| **Functional behaviour** | The system allows bank operations to set KYC status. The exact KYC status values are not specified by the approved source and are not invented (OQ-013). State changes are auditable (BR-006). |
| **Business rules applied** | State changes in the system must be auditable. |
| **Inputs** | KYC status set by bank operations. |
| **Outputs** | Updated KYC status.<br>State change recorded for audit (BR-006). |
| **Validation** | KYC status is updated and the state change is auditable. Allowed KYC status values remain OPEN (OQ-013). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-012 |
| **Open questions** | OQ-012, OQ-013 |

### FR-013 - Bank operations activates customer accounts

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to activate customer accounts. |
| **Source business requirement** | BR-013 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation. |
| **Trigger** | Bank operations activates a customer account. |
| **Functional behaviour** | The system allows bank operations to activate customer accounts. Account-state rules remain open (OQ-006). State changes are auditable (BR-006). |
| **Business rules applied** | State changes in the system must be auditable. |
| **Inputs** | Account activation performed by bank operations. |
| **Outputs** | Customer account moved to an activated state.<br>State change recorded for audit (BR-006). |
| **Validation** | Account activation by bank operations transitions account state. Exact account-state rules remain OPEN (OQ-006). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-013 |
| **Open questions** | OQ-006, OQ-012 |

### FR-014 - Bank operations freezes customer accounts

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to freeze customer accounts. |
| **Source business requirement** | BR-014 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation. |
| **Trigger** | Bank operations freezes a customer account. |
| **Functional behaviour** | The system allows bank operations to freeze customer accounts. Account-state rules remain open (OQ-006). State changes are auditable (BR-006). |
| **Business rules applied** | State changes in the system must be auditable. |
| **Inputs** | Account freeze performed by bank operations. |
| **Outputs** | Customer account moved to a frozen state.<br>State change recorded for audit (BR-006). |
| **Validation** | Account freezing by bank operations transitions account state. Exact account-state rules remain OPEN (OQ-006). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-014 |
| **Open questions** | OQ-006, OQ-012 |

### FR-015 - Bank operations views customer account state

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to view customer account state. |
| **Source business requirement** | BR-015 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation. |
| **Trigger** | Bank operations requests to view customer account state. |
| **Functional behaviour** | The system allows bank operations to view customer account state. Account-state details remain open (OQ-006). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | Account state viewing request by bank operations. |
| **Outputs** | Customer account state displayed to bank operations. |
| **Validation** | Customer account state is displayed to bank operations. Account-state details remain OPEN (OQ-006). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-015 |
| **Open questions** | OQ-006, OQ-012 |

### FR-016 - Bank operations accesses the audit trail

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to access the audit trail. |
| **Source business requirement** | BR-016 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation.<br>State changes are auditable (BR-006). |
| **Trigger** | Bank operations requests to access the audit trail. |
| **Functional behaviour** | The system allows bank operations to access the audit trail. The exact audit events to be recorded remain open (OQ-011). |
| **Business rules applied** | State changes in the system must be auditable. |
| **Inputs** | Audit trail access request by bank operations. |
| **Outputs** | Audit trail displayed to bank operations. |
| **Validation** | The audit trail is accessible to bank operations. Exact audit events to be recorded remain OPEN (OQ-011). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-016 |
| **Open questions** | OQ-011, OQ-012 |

### FR-017 - Bank operations logs in

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to log in to the application. |
| **Source business requirement** | BR-017 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations actor exists within the simulation.<br>Role-based access is provided (BR-005 business rule). |
| **Trigger** | Bank operations requests to log in. |
| **Functional behaviour** | The system allows bank operations to log in, establishing role-based access for the bank-operations journey. Authentication mechanisms are not specified by the approved source and are not invented (OQ-010). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access.<br>Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. |
| **Inputs** | Bank-operations login request. |
| **Outputs** | Bank-operations session established for role-based access. |
| **Validation** | A successful login establishes a bank-operations session. Authentication/login mechanism details remain OPEN (OQ-010, OQ-009). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-017 |
| **Open questions** | OQ-009, OQ-010, OQ-012 |

### FR-018 - Bank operations logs out

| Field | Value |
| :--- | :--- |
| **Description** | The system shall allow bank operations to log out, terminating the session. |
| **Source business requirement** | BR-018 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | A bank-operations session exists within the simulation. |
| **Trigger** | Bank operations requests to log out. |
| **Functional behaviour** | The system allows bank operations to log out, terminating the bank-operations session. |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access. |
| **Inputs** | Bank-operations logout request. |
| **Outputs** | Bank-operations session terminated. |
| **Validation** | Logout terminates the bank-operations session. Session/termination mechanism details remain OPEN (OQ-010). |
| **Error behaviour** | Not specified by the approved source. |
| **Acceptance reference** | BR-018 |
| **Open questions** | OQ-010 |

### FR-019 - Role-based access keeps journeys distinct

| Field | Value |
| :--- | :--- |
| **Description** | The system shall provide role-based access so that customer and bank-operations journeys are kept distinct. |
| **Source business requirement** | BR-019 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | Two distinct roles exist: Customer and Bank Operations (BR-005 business rule). |
| **Trigger** | A user acts within either the customer or bank-operations journey. |
| **Functional behaviour** | The system provides role-based access so that customer and bank-operations journeys are kept distinct. The exact role permissions and authorization rules remain open (OQ-009). |
| **Business rules applied** | The system supports two distinct roles: Customer and Bank Operations, with role-based access.<br>Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. |
| **Inputs** | Role definition and activation of a journey. |
| **Outputs** | Customer and bank-operations journeys kept distinct via role-based access. |
| **Validation** | Role-based access keeps the customer and bank-operations journeys distinct. Exact role permissions and authorization rules remain OPEN (OQ-009). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-019 |
| **Open questions** | OQ-009, OQ-012 |

### FR-020 - State changes are auditable

| Field | Value |
| :--- | :--- |
| **Description** | The system shall make state changes auditable. |
| **Source business requirement** | BR-020 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | The system records state changes (BR-006 business rule). |
| **Trigger** | A state change occurs within the simulation. |
| **Functional behaviour** | The system makes state changes auditable. The exact audit events to be recorded remain open (OQ-011). |
| **Business rules applied** | State changes in the system must be auditable.<br>Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. |
| **Inputs** | State changes occurring in the simulation. |
| **Outputs** | Audit trail capturing state changes.<br>Audit trail accessible to bank operations (FR-016). |
| **Validation** | State changes are captured as auditable events. Exact audit events to be recorded remain OPEN (OQ-011). |
| **Error behaviour** | Not specified by the approved source. Error messages/codes remain OPEN (OQ-012). |
| **Acceptance reference** | BR-020 |
| **Open questions** | OQ-011, OQ-012 |

### FR-021 - Use of synthetic data for the simulation

| Field | Value |
| :--- | :--- |
| **Description** | The system shall use synthetic identities, accounts, balances, beneficiaries, and payments for the simulation. |
| **Source business requirement** | BR-021 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | The project is an educational simulation using synthetic data (CON-001, CON-002). |
| **Trigger** | The simulation operates using synthetic data. |
| **Functional behaviour** | The system uses synthetic identities, accounts, balances, beneficiaries, and payments. Real money movement and real financial transactions are not permitted (BR-001, BR-003). |
| **Business rules applied** | The simulation must not use real money; money movement is simulated using synthetic data.<br>The system must not perform credit decisioning, lending, or real financial transactions.<br>The system must not integrate with production banks, real payment gateways, or external KYC integrations. |
| **Inputs** | Synthetic identities, accounts, balances, beneficiaries, and payments. |
| **Outputs** | Simulation operating on synthetic data only. |
| **Validation** | All simulation data is synthetic; no real money or real financial transactions are used. Data fields and validation constraints remain OPEN (OQ-013). |
| **Error behaviour** | Not specified by the approved source. |
| **Acceptance reference** | BR-021 |
| **Open questions** | OQ-013 |

### FR-022 - Agent-produced artifacts are governed

| Field | Value |
| :--- | :--- |
| **Description** | Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval. |
| **Source business requirement** | BR-022 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | The project uses reusable AI-assisted engineering agents. |
| **Trigger** | An agent produces an artifact. |
| **Functional behaviour** | The system (and its governing process) requires agent-produced artifacts to be reviewable, reproducible, schema-valid, source-linked, and subject to human approval. Every project handoff must carry version, source IDs, assumptions, open questions, and approval status (BR-008 business rule). |
| **Business rules applied** | Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. |
| **Inputs** | Agent-produced artifacts. |
| **Outputs** | Artifacts that are reviewable, reproducible, schema-valid, source-linked, and subject to human approval. |
| **Validation** | Agent output satisfies the governance conditions (reviewable, reproducible, schema-valid, source-linked, human-approved). |
| **Error behaviour** | Not specified by the approved source. |
| **Acceptance reference** | BR-022 |
| **Open questions** | None |

### FR-023 - Approved business rules remain traceable

| Field | Value |
| :--- | :--- |
| **Description** | Approved business rules shall remain traceable through requirements and downstream evidence. |
| **Source business requirement** | BR-023 |
| **Priority** | UNSPECIFIED |
| **Preconditions** | The project maintains governance and traceability (CHARTER-2, SCOPE-6). |
| **Trigger** | An approved business rule is carried through the lifecycle. |
| **Functional behaviour** | The system and its governing process maintain traceability of approved business rules through requirements and downstream evidence, so that an approved business rule can be traced through requirement, design element, implementation, test, defect decision, and final evidence record. |
| **Business rules applied** | Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. |
| **Inputs** | Approved business rules and downstream artifacts. |
| **Outputs** | Traceability chain from approved business rule through requirements and downstream evidence. |
| **Validation** | Approved business rules remain traceable through requirements and downstream evidence. |
| **Error behaviour** | Not specified by the approved source. |
| **Acceptance reference** | BR-023 |
| **Open questions** | None |

---

## 4. Business Rules

| ID | Business Rule | Source |
| :--- | :--- | :--- |
| BR-001 | The simulation must not use real money; money movement is simulated using synthetic data. | CHARTER-6, SCOPE-5 |
| BR-002 | The simulation must not perform real identity verification; Aadhaar/PAN verification is format-only and mocked. | CHARTER-6, SCOPE-5 |
| BR-003 | The system must not perform credit decisioning, lending, or real financial transactions. | CHARTER-6, SCOPE-5 |
| BR-004 | The system must not integrate with production banks, real payment gateways, or external KYC integrations. | CHARTER-6, SCOPE-5 |
| BR-005 | The system supports two distinct roles: Customer and Bank Operations, with role-based access. | CHARTER-3.2, SCOPE-3 |
| BR-006 | State changes in the system must be auditable. | CHARTER-3.2 |
| BR-007 | Any requirement outside the approved scope must be handled through the project's change-control process rather than silently added to the baseline. | SCOPE-8 |
| BR-008 | Every project handoff must carry version, source IDs, assumptions, open questions, and approval status. | CHARTER-5 |

---

## 5. Open Questions carried forward

These open questions from the approved BRD are carried forward. They are not silently resolved.

| ID | Open Question | Status | Source |
| :--- | :--- | :--- | :--- |
| OQ-001 | Who executes UAT and signs off business acceptance? | OPEN | CHARTER-8, SCOPE-7 |
| OQ-002 | What is the minimum balance value? | OPEN | CHARTER-8, SCOPE-7 |
| OQ-003 | What is the daily transfer cap? | OPEN | CHARTER-8, SCOPE-7 |
| OQ-004 | Is the data-testid convention confirmed with the development team? | OPEN | AGENTS (Open Questions) |
| OQ-005 | What are the exact onboarding workflow and validation rules? | OPEN | SCOPE-7 |
| OQ-006 | What are the exact account operations and account-state rules? | OPEN | SCOPE-7 |
| OQ-007 | What are the exact transfer/payment rules and limits? | OPEN | SCOPE-7 |
| OQ-008 | What are the statement content and download behaviour details? | OPEN | SCOPE-7 |
| OQ-009 | What are the exact role permissions and authorization rules? | OPEN | SCOPE-3, SCOPE-7 |
| OQ-010 | What are the detailed security, privacy, accessibility, and testability requirements? | OPEN | CHARTER-8, SCOPE-7 |
| OQ-011 | What are the exact audit events to be recorded? | OPEN | SCOPE-7 |
| OQ-012 | What are the error codes and error messages? | OPEN | SCOPE-7 |
| OQ-013 | What are the data fields and validation constraints? | OPEN | SCOPE-7 |

---

## 6. Source inconsistencies detected

No inconsistencies detected in the approved source references.

---

## Status

- **Status:** RAW
- **Ready for human review:** READY_FOR_HUMAN_REVIEW
- **Approval status:** NOT_APPROVED
- **Version:** 1.0
