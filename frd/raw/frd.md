# Functional Requirements Document

## Metadata

- **Project:** Online Banking Application
- **Project Code:** ONLINE-BANKING
- **Artifact:** Functional Requirements Document
- **Version:** 1.0
- **Status:** RAW
- **Approval Status:** NOT_APPROVED
- **Generated At:** 2026-09-07T00:00:00Z
- **Generator Agent:** FRD Agent
- **Document Status:** RAW - READY_FOR_HUMAN_REVIEW
- **Source Basis:** brd/raw/brd.json, brd/raw/business_rules.json, brd/raw/open_questions.json

## Introduction

This Functional Requirements Document (FRD) translates the approved business requirements of the Online Banking Application into precise, testable functional requirements. It is derived exclusively from the RAW BRD artifacts and maintains BR-to-FR traceability.

This FRD covers the functional behaviour required by BR-001 through BR-023. It does not prescribe technical implementation: it names no APIs, databases, authentication mechanisms, or infrastructure.

**Audience:** Architecture and Development teams, Quality Assurance and Testing teams, UAT teams, Defect Root Cause Analysis teams, Human reviewers and approvers of functional requirements

## Functional Requirements

### FR-001 — Customer Completes Onboarding

**Description:** The system shall allow a customer to complete onboarding.

**Source Business Requirement:** BR-001

**Priority:** UNSPECIFIED

**Preconditions:**
- A customer exists and has initiated the onboarding journey.

**Trigger:** The customer initiates onboarding.

**Functional Behavior:**
- The system shall make available an onboarding journey to a customer.
- The system shall accept the information required for onboarding.
- The system shall allow the customer to complete the onboarding journey.

**Inputs:**
- Customer-supplied onboarding information.

**Outputs:**
- An onboarding completion state/record for the customer.

**Error Behavior:**
- If onboarding cannot be completed, the system shall surface a relevant error. Exact error codes and messages are unresolved (see OQ-012).

**Related Open Questions:** OQ-005, OQ-012, OQ-013

### FR-002 — Customer Provides KYC Information

**Description:** The system shall allow a customer to provide KYC information.

**Source Business Requirement:** BR-002

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer is progressing through onboarding.

**Trigger:** The customer provides KYC information.

**Functional Behavior:**
- The system shall accept KYC information from the customer.
- KYC information is captured for the simulation; it is not verified against any real authority.

**Business Rules / Constraints:**
- Business rule BR-002 (simulated identity verification; Aadhaar/PAN format-only and mocked).
- Constraint CON-003 (format-only, mocked identity verification).
- Constraint CON-005 (no external KYC integration).

**Inputs:**
- Customer KYC information.

**Outputs:**
- A stored record of the customer's KYC information.

**Error Behavior:**
- If KYC information cannot be accepted, the system shall surface a relevant error. Exact validation constraints and error text are unresolved (see OQ-012, OQ-013).

**Related Open Questions:** OQ-012, OQ-013

### FR-003 — Customer Provides Aadhaar and PAN Information

**Description:** The system shall allow a customer to provide Aadhaar and PAN information. Verification of Aadhaar/PAN is format-only and mocked.

**Source Business Requirement:** BR-003

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer is providing KYC information during onboarding.

**Trigger:** The customer provides Aadhaar and/or PAN information.

**Functional Behavior:**
- The system shall accept Aadhaar and PAN information from the customer.
- Aadhaar/PAN verification performed by the system, if any, shall be format-only and mocked.
- The system shall not perform real identity verification against any external authority.

**Business Rules / Constraints:**
- Business rule BR-002 (Aadhaar/PAN verification is format-only and mocked).
- Constraint CON-003 (format-only, mocked identity verification).
- Constraint CON-005 (no external KYC integration).

**Inputs:**
- Customer Aadhaar information.
- Customer PAN information.

**Outputs:**
- A stored record of the customer's Aadhaar/PAN information.

**Error Behavior:**
- If Aadhaar/PAN information is not in the expected format, the system shall surface a relevant error. Exact format rules and error text are unresolved (see OQ-012, OQ-013).

**Related Open Questions:** OQ-012, OQ-013

### FR-004 — Customer Activates an Account

**Description:** The system shall allow a customer to activate an account.

**Source Business Requirement:** BR-004

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has an account associated with their profile.

**Trigger:** The customer, or bank operations on the customer's behalf, initiates account activation.

**Functional Behavior:**
- The system shall allow a customer account to be activated.
- Account activation shall result in an account state that reflects the activation.

**Business Rules / Constraints:**
- Business rule BR-006 (state changes must be auditable).

**Inputs:**
- Account activation request.

**Outputs:**
- An account whose state reflects activation.
- An audit record of the state change.

**Error Behavior:**
- If account activation cannot be performed, the system shall surface a relevant error. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012).

**Related Open Questions:** OQ-006, OQ-012, OQ-013

### FR-005 — Customer Login

**Description:** The system shall allow a customer to log in.

**Source Business Requirement:** BR-005

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has a registered identity in the system.

**Trigger:** The customer initiates login.

**Functional Behavior:**
- The system shall allow a customer to log in.
- Login shall provide the customer access consistent with role-based access requirements (see FR-019).

**Business Rules / Constraints:**
- Business rule BR-005 (two distinct roles: Customer and Bank Operations, with role-based access).

**Inputs:**
- Customer login credentials/request.

**Outputs:**
- An authenticated customer session.

**Error Behavior:**
- If login fails, the system shall surface a relevant error. Exact authentication rules and error text are unresolved (see OQ-009, OQ-010, OQ-012).

**Related Open Questions:** OQ-009, OQ-010, OQ-012

### FR-006 — Customer Logout

**Description:** The system shall allow a customer to log out.

**Source Business Requirement:** BR-006

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has an active session.

**Trigger:** The customer initiates logout.

**Functional Behavior:**
- The system shall allow a customer to log out.
- Logout shall terminate the customer session.

**Inputs:**
- Customer logout request.

**Outputs:**
- A terminated customer session.

**Error Behavior:**
- If logout cannot be completed, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012).

**Related Open Questions:** OQ-012

### FR-007 — Customer Transfers Simulated Money

**Description:** The system shall allow a customer to transfer simulated money.

**Source Business Requirement:** BR-007

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has an active session and an account in a state that permits transfer.

**Trigger:** The customer initiates a transfer of simulated money.

**Functional Behavior:**
- The system shall allow a customer to initiate a transfer of simulated money.
- Money movement is simulated using synthetic data; no real money moves.

**Business Rules / Constraints:**
- Business rule BR-001 (money movement is simulated using synthetic data).
- Constraint CON-002 (real money movement is not permitted).
- Constraint CON-004 (credit decisioning is not permitted).
- Constraint CON-005 (no production bank integration or real payment gateways).

**Inputs:**
- Transfer/payment request details.

**Outputs:**
- A simulated payment/transfer record and resulting balance change.

**Error Behavior:**
- If a transfer cannot be completed, the system shall surface a relevant error. Exact transfer/payment rules, limits, and error text are unresolved (see OQ-007, OQ-012).

**Related Open Questions:** OQ-007, OQ-012, OQ-013

### FR-008 — Customer Receives Simulated Money

**Description:** The system shall allow a customer to receive simulated money.

**Source Business Requirement:** BR-008

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has an account in a state that permits receipt.

**Trigger:** Simulated money is received for the customer.

**Functional Behavior:**
- The system shall allow a customer to receive simulated money.
- Money movement is simulated using synthetic data; no real money moves.

**Business Rules / Constraints:**
- Business rule BR-001 (money movement is simulated using synthetic data).
- Constraint CON-002 (real money movement is not permitted).
- Constraint CON-005 (no production bank integration or real payment gateways).

**Inputs:**
- Incoming simulated payment/transfer details.

**Outputs:**
- A simulated payment/transfer record and resulting balance change.

**Error Behavior:**
- If receipt cannot be recorded, the system shall surface a relevant error. Exact transfer/payment rules and error text are unresolved (see OQ-007, OQ-012).

**Related Open Questions:** OQ-007, OQ-012

### FR-009 — Customer Views Statements

**Description:** The system shall allow a customer to view statements.

**Source Business Requirement:** BR-009

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has an active session and an account with statement data.

**Trigger:** The customer requests to view a statement.

**Functional Behavior:**
- The system shall allow a customer to view statements.

**Business Rules / Constraints:**
- Constraint CON-001 (educational simulation, not a production banking system).

**Inputs:**
- Statement-viewing request.

**Outputs:**
- A statement presented to the customer.

**Error Behavior:**
- If a statement cannot be presented, the system shall surface a relevant error. Exact statement content and error text are unresolved (see OQ-008, OQ-012).

**Related Open Questions:** OQ-008, OQ-012

### FR-010 — Customer Downloads Statements

**Description:** The system shall allow a customer to download statements.

**Source Business Requirement:** BR-010

**Priority:** UNSPECIFIED

**Preconditions:**
- The customer has an active session and an account with statement data.

**Trigger:** The customer requests to download a statement.

**Functional Behavior:**
- The system shall allow a customer to download statements.

**Business Rules / Constraints:**
- Constraint CON-001 (educational simulation, not a production banking system).

**Inputs:**
- Statement-download request.

**Outputs:**
- A downloadable statement artifact for the customer.

**Error Behavior:**
- If a statement cannot be downloaded, the system shall surface a relevant error. Exact download behaviour and error text are unresolved (see OQ-008, OQ-012).

**Related Open Questions:** OQ-008, OQ-012

### FR-011 — Bank Operations Reviews KYC

**Description:** The system shall allow bank operations to review KYC information.

**Source Business Requirement:** BR-011

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session and the required role-based access.

**Trigger:** Bank operations requests to review a customer's KYC information.

**Functional Behavior:**
- The system shall allow bank operations to review KYC information.

**Business Rules / Constraints:**
- Business rule BR-005 (two distinct roles with role-based access).

**Inputs:**
- A KYC review request identifying the customer.

**Outputs:**
- KYC information presented to bank operations.

**Error Behavior:**
- If KYC information cannot be presented, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012).

**Related Open Questions:** OQ-009, OQ-012

### FR-012 — Bank Operations Sets KYC Status

**Description:** The system shall allow bank operations to set KYC status.

**Source Business Requirement:** BR-012

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session, the required role-based access, and has reviewed the KYC information.

**Trigger:** Bank operations sets the KYC status for a customer.

**Functional Behavior:**
- The system shall allow bank operations to set the KYC status of a customer.

**Business Rules / Constraints:**
- Business rule BR-006 (state changes must be auditable).

**Inputs:**
- A KYC status update for a customer.

**Outputs:**
- An updated KYC status for the customer.
- An audit record of the state change.

**Error Behavior:**
- If the KYC status cannot be updated, the system shall surface a relevant error. Exact status values and error text are unresolved (see OQ-012, OQ-013).

**Related Open Questions:** OQ-009, OQ-012, OQ-013

### FR-013 — Bank Operations Activates Customer Accounts

**Description:** The system shall allow bank operations to activate customer accounts.

**Source Business Requirement:** BR-013

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session and the required role-based access.

**Trigger:** Bank operations initiates activation of a customer account.

**Functional Behavior:**
- The system shall allow bank operations to activate a customer account.

**Business Rules / Constraints:**
- Business rule BR-006 (state changes must be auditable).

**Inputs:**
- An account-activation request from bank operations.

**Outputs:**
- A customer account whose state reflects activation.
- An audit record of the state change.

**Error Behavior:**
- If the account cannot be activated, the system shall surface a relevant error. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012).

**Related Open Questions:** OQ-006, OQ-009, OQ-012

### FR-014 — Bank Operations Freezes Customer Accounts

**Description:** The system shall allow bank operations to freeze customer accounts.

**Source Business Requirement:** BR-014

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session and the required role-based access.

**Trigger:** Bank operations initiates a freeze of a customer account.

**Functional Behavior:**
- The system shall allow bank operations to freeze a customer account.
- A frozen account shall reflect the frozen state.

**Business Rules / Constraints:**
- Business rule BR-006 (state changes must be auditable).

**Inputs:**
- An account-freeze request from bank operations.

**Outputs:**
- A customer account whose state reflects a freeze.
- An audit record of the state change.

**Error Behavior:**
- If the account cannot be frozen, the system shall surface a relevant error. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012).

**Related Open Questions:** OQ-006, OQ-009, OQ-012

### FR-015 — Bank Operations Views Customer Account State

**Description:** The system shall allow bank operations to view customer account state.

**Source Business Requirement:** BR-015

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session and the required role-based access.

**Trigger:** Bank operations requests to view a customer's account state.

**Functional Behavior:**
- The system shall allow bank operations to view the state of a customer account.

**Business Rules / Constraints:**
- Business rule BR-005 (two distinct roles with role-based access).

**Inputs:**
- An account-state view request identifying the customer/account.

**Outputs:**
- Customer account state presented to bank operations.

**Error Behavior:**
- If the account state cannot be presented, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012).

**Related Open Questions:** OQ-006, OQ-009, OQ-012

### FR-016 — Bank Operations Accesses the Audit Trail

**Description:** The system shall allow bank operations to access the audit trail.

**Source Business Requirement:** BR-016

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session and the required role-based access.

**Trigger:** Bank operations requests access to the audit trail.

**Functional Behavior:**
- The system shall allow bank operations to access the audit trail.

**Business Rules / Constraints:**
- Business rule BR-006 (state changes must be auditable).
- Business rule BR-005 (two distinct roles with role-based access).

**Inputs:**
- An audit-trail access request.

**Outputs:**
- Audit trail information presented to bank operations.

**Error Behavior:**
- If the audit trail cannot be accessed, the system shall surface a relevant error. Exact audit events and error text are unresolved (see OQ-011, OQ-012).

**Related Open Questions:** OQ-011, OQ-009, OQ-012

### FR-017 — Bank Operations Login

**Description:** The system shall allow bank operations to log in.

**Source Business Requirement:** BR-017

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has a registered identity in the system.

**Trigger:** Bank operations initiates login.

**Functional Behavior:**
- The system shall allow bank operations to log in.
- Login shall provide bank operations access consistent with role-based access requirements (see FR-019).

**Business Rules / Constraints:**
- Business rule BR-005 (two distinct roles: Customer and Bank Operations, with role-based access).

**Inputs:**
- Bank-operations login credentials/request.

**Outputs:**
- An authenticated bank-operations session.

**Error Behavior:**
- If login fails, the system shall surface a relevant error. Exact authentication rules and error text are unresolved (see OQ-009, OQ-010, OQ-012).

**Related Open Questions:** OQ-009, OQ-010, OQ-012

### FR-018 — Bank Operations Logout

**Description:** The system shall allow bank operations to log out.

**Source Business Requirement:** BR-018

**Priority:** UNSPECIFIED

**Preconditions:**
- Bank operations has an active session.

**Trigger:** Bank operations initiates logout.

**Functional Behavior:**
- The system shall allow bank operations to log out.
- Logout shall terminate the bank-operations session.

**Inputs:**
- Bank-operations logout request.

**Outputs:**
- A terminated bank-operations session.

**Error Behavior:**
- If logout cannot be completed, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012).

**Related Open Questions:** OQ-012

### FR-019 — Role-Based Access

**Description:** The system shall provide role-based access so that customer and bank-operations journeys are kept distinct.

**Source Business Requirement:** BR-019

**Priority:** UNSPECIFIED

**Preconditions:**
- The system has defined roles for Customer and Bank Operations.

**Trigger:** A user (Customer or Bank Operations) attempts to perform an action in the system.

**Functional Behavior:**
- The system shall keep customer and bank-operations journeys distinct through role-based access.
- Actions available to a user shall be consistent with the user's role.

**Business Rules / Constraints:**
- Business rule BR-005 (two distinct roles: Customer and Bank Operations, with role-based access).

**Inputs:**
- A user action request carrying role context.

**Outputs:**
- Access granted or denied consistent with the user's role.

**Error Behavior:**
- If a user attempts an action not permitted for their role, the system shall surface a relevant error. Exact role permissions and error text are unresolved (see OQ-009, OQ-012).

**Related Open Questions:** OQ-009, OQ-012

### FR-020 — Auditable State Changes

**Description:** The system shall make state changes auditable.

**Source Business Requirement:** BR-020

**Priority:** UNSPECIFIED

**Preconditions:**
- A state change occurs in the system.

**Trigger:** A state change is performed (for example, account activation, account freeze, or KYC status update).

**Functional Behavior:**
- The system shall record state changes so that they are auditable.

**Business Rules / Constraints:**
- Business rule BR-006 (state changes in the system must be auditable).

**Inputs:**
- State change event information.

**Outputs:**
- An audit record of the state change, accessible via the audit trail (see FR-016).

**Error Behavior:**
- If a state change cannot be recorded for audit, the system shall surface a relevant error. Exact audit events and error text are unresolved (see OQ-011, OQ-012).

**Related Open Questions:** OQ-011, OQ-012

### FR-021 — Synthetic Data Simulation

**Description:** The system shall use synthetic identities, accounts, balances, beneficiaries, and payments for the simulation.

**Source Business Requirement:** BR-021

**Priority:** UNSPECIFIED

**Preconditions:**
- The simulation operates with synthetic data.

**Trigger:** The simulation instantiates identities, accounts, balances, beneficiaries, or payments.

**Functional Behavior:**
- The system shall use synthetic identities, accounts, balances, beneficiaries, and payments.
- The system shall not use real money, real identity verification, or real banking integration.

**Business Rules / Constraints:**
- Business rule BR-001 (money movement is simulated using synthetic data).
- Business rule BR-002 (Aadhaar/PAN verification is format-only and mocked).
- Business rule BR-004 (no production bank, real payment gateway, or external KYC integration).
- Constraints CON-001 through CON-005.

**Inputs:**
- Synthetic simulation data.

**Outputs:**
- A coherent simulation populated with synthetic data.

### FR-022 — Agent Artifact Quality

**Description:** Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval.

**Source Business Requirement:** BR-022

**Priority:** UNSPECIFIED

**Preconditions:**
- An agent produces an artifact.

**Trigger:** An agent produces or delivers an artifact.

**Functional Behavior:**
- Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval.

**Business Rules / Constraints:**
- Business rule BR-007 (out-of-scope requirements go through change control).
- Business rule BR-008 (each handoff carries version, source IDs, assumptions, open questions, and approval status).

**Inputs:**
- Artifact content and metadata.

**Outputs:**
- A reviewable, reproducible, schema-valid, source-linked artifact.

**Validation:**
- Artifact is schema-valid.
- Artifact is source-linked.
- Artifact records version, status, and approval status.

### FR-023 — Requirements Traceability

**Description:** Approved business rules shall remain traceable through requirements and downstream evidence.

**Source Business Requirement:** BR-023

**Priority:** UNSPECIFIED

**Preconditions:**
- BRD artifacts record source-to-requirement mappings.

**Trigger:** Downstream requirements or evidence are produced from business requirements.

**Functional Behavior:**
- Approved business rules shall remain traceable through requirements, design, implementation, test, defect decision, and final evidence record.

**Business Rules / Constraints:**
- Business rule BR-008 (every handoff carries version, source IDs, assumptions, open questions, and approval status).

**Inputs:**
- Tracing information linking downstream artifacts to approved business requirements/rules.

**Outputs:**
- Traceable downstream artifacts (FRD, UAT, evidence records).

**Validation:**
- Every functional requirement traces to an approved business requirement.
- No orphan functional requirements exist.
- No unknown business-requirement references exist.

## BR -> FR Traceability

| Business Requirement | Functional Requirement |
|---|---|
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

## Carried-Forward Open Questions

| ID | Question | Status | Source |
|---|---|---|---|
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

## Consistency Notes

- The BRD business-rule artifact and the BRD document both use the ID prefix BR- for business rules (BR-001..BR-008), which is distinct from but identical-in-prefix to the business-requirement IDs (BR-001..BR-023). The convention is preserved verbatim from the approved source; no rewrite was made.
- All open questions OQ-001 through OQ-013 are carried forward from the BRD; none were silently resolved.
- ERR-016 intentionally traces to FR-006 (source BR-006, customer logout), which is noted because it also covers FR-018 (bank-operations logout). This is an explicit consistency note, not an invented requirement.
- No missing FR references were detected in the approved source material.

---

**Version:** 1.0 | **Status:** RAW | **Approval Status:** NOT_APPROVED | **READY_FOR_HUMAN_REVIEW**
