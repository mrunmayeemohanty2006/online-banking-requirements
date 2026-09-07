# Business Requirements Document

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
| 1.0 | 2026-09-07 | BRD Agent | Initial RAW BRD generated for human review |

---

## Glossary

### Abbreviation Description

| Abbreviation | Description |
| :--- | :--- |
| BRD | Business Requirements Document |
| FRD | Functional Requirements Document |
| UAT | User Acceptance Testing |
| KYC | Know Your Customer |
| SDLC | Software Development Life Cycle |
| AI | Artificial Intelligence |

---

## Table Of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Audience](#13-audience)
  - [1.4 References](#14-references)
- [2. Project Drivers](#2-project-drivers)
- [3. Constraints](#3-constraints)
- [4. Assumptions and Dependencies](#4-assumptions-and-dependencies)
- [5. Current State](#5-current-state)
- [6. Stakeholder Profiles](#6-stakeholder-profiles)
- [7. Scope of Work](#7-scope-of-work)
- [8. Functional and Data Requirements](#8-functional-and-data-requirements)
  - [8.1 Requirements summary](#81-requirements-summary)
  - [8.2 Requirement priorities](#82-requirement-priorities)
  - [8.3 Functional Requirements](#83-functional-requirements)
  - [8.4 Business Rules](#84-business-rules)
  - [8.5 Traceability](#85-traceability)
  - [8.6 Open Questions](#86-open-questions)
- [9. Business Implementation Requirements](#9-business-implementation-requirements)
- [10. Issues](#10-issues)

---

# 1. Introduction

## 1.1 Purpose

The Online Banking Application is an educational simulation developed to demonstrate a coherent, traceable software development lifecycle. This Business Requirements Document specifies, in user/business language, what the business wants the system to do. It is the primary deliverable of the business-analysis stage and forms the basis for the Functional Requirements Document (FRD) and User Acceptance Testing (UAT).

## 1.2 Scope

This BRD covers the business requirements for the Online Banking Application educational simulation as bounded by the project charter and the scope agreement. It defines the business capabilities, business rules, constraints, assumptions, and open questions. It does not specify technical implementation.

## 1.3 Audience

- Business Analysts
- Requirements Analysts
- Architecture and Development teams
- Quality Assurance and Testing teams
- Defect Root Cause Analysis teams
- Human reviewers and approvers of business requirements

## 1.4 References

- Project2_Online_Banking_Student_Development_Project.docx (source basis)
- sources/charter.md
- sources/scope_agreement.md
- sources/brd_template.md

---

# 2. Project Drivers

## 2.1 The purpose of the application

Customers expect secure digital access to banking capabilities, including accounts, transfers, and statements. The project delivers a coherent online-banking simulation using synthetic data, coordinated across business analysis, architecture, development, testing, and defect root-cause analysis, supported by reusable AI-assisted engineering agents. Success requires demonstrating that an approved business rule can be traced through requirement, design element, implementation, test, defect decision, and final evidence record.

## 2.2 Client, Customer and other Stakeholders

- **Business Analysis** (Ritu & Team (Group 2)): Turn approved needs into a Business Requirements Document.
- **Architecture, Build and Unit Test (Development)** (Mohit & Team): Technical design, build, and unit testing.
- **Quality Assurance and Testing** (Mandeep & Team): System testing and automation.
- **Defect Root Cause Analysis** (Adiba & Team): Defect root-cause analysis.

## 2.3 Users of the Application

- **Customer**: Completes onboarding, provides KYC and Aadhaar/PAN information, activates an account, logs in/out, transfers and receives simulated money, and views/downloads statements.
- **Bank Operations**: Reviews KYC, sets KYC status, activates/freezes accounts, views customer account state, accesses the audit trail, and logs in/out.

## 2.4 Key success factors

- A coherent banking simulation using synthetic identities, accounts, balances, beneficiaries, and payments.
- Role-based customer and bank-operations journeys with auditable state changes.
- Agent output that is reviewable, reproducible, schema-valid, source-linked, and subject to human approval.
- Traceability of approved business rules through requirement, design, implementation, test, and evidence.
- Application of security, privacy, accessibility, reliability, and testability as acceptance conditions.
- Governance through baselines, versioning, change control, traceability, evidence, risk management, and retrospectives.

---

# 3. Constraints

## 3.1 Constraints

| ID | Constraint | Source |
| :--- | :--- | :--- |
| CON-001 | The system is an educational simulation, not a production banking system. | CHARTER-6 |
| CON-002 | Real money movement is not permitted; money movement is simulated using synthetic data. | CHARTER-6, SCOPE-5 |
| CON-003 | Real identity verification is not permitted; Aadhaar/PAN verification is format-only and mocked. | CHARTER-6, SCOPE-5 |
| CON-004 | Credit decisioning is not permitted. | CHARTER-6, SCOPE-5 |
| CON-005 | Production bank integration is not permitted, including real payment gateways and external KYC integrations. | CHARTER-6, SCOPE-5 |
| CON-006 | Business requirements must not invent business decisions not present in the source material. | AGENTS (BRD Rules) |

---

# 4. Assumptions and Dependencies

- **ASM-001**: The project uses synthetic identities, accounts, balances, beneficiaries, and payments throughout the simulation. (Source: CHARTER-3.1, SCOPE-4)
- **ASM-002**: The system supports two user roles: Customer and Bank Operations. (Source: CHARTER-3.2, SCOPE-3)
- **ASM-003**: All agent-produced artifacts are reviewable, reproducible, schema-valid, source-linked, and subject to human approval. (Source: CHARTER-5)
- **ASM-004**: Candidate in-scope business areas are subject to detailed requirement confirmation and human approval before being treated as approved requirements. (Source: SCOPE-2)
- **ASM-005**: Aadhaar/PAN verification is format-only and mocked; no real identity verification is performed. (Source: AGENTS (Business Scope))

---

# 5. Current State

## 5.1 Stakeholder Problem and Desired State Capture

Customers expect secure digital access to onboarding, accounts, transfers, statements, and related banking functions. Student projects can treat business analysis, architecture, engineering, testing, evidence management, and defect triage as isolated activities, which can result in ambiguous requirements, untestable designs, weak handoffs, and disagreement over whether a failure is a defect or a new request.

## 5.2 Overview of current business environment

### 5.2.1 Existing business environment

No detailed description of an existing business environment is provided in the source material. The project is a new educational simulation and is not based on an existing production banking system.

### 5.2.2 Existing application environment

No existing application environment is described in the source material. The application is greenfield for the purposes of this simulation.

---

# 6. Stakeholder Profiles

## 6.1 Customer (STK-001)

| Attribute | Details |
| :--- | :--- |
| **Description** | An end user of the online banking simulation who manages their own onboarding, KYC, account activation, transactions, and statements. |
| **Success Criteria** | Can complete onboarding and provide KYC and Aadhaar/PAN information.<br>Can activate an account and log in/out.<br>Can transfer and receive simulated money.<br>Can view and download statements. |
| **Deliverables** | Completion of onboarding.<br>Provision of KYC and Aadhaar/PAN information.<br>Activation of an account. |

## 6.2 Bank Operations (STK-002)

| Attribute | Details |
| :--- | :--- |
| **Description** | A bank-operations user who administers customer accounts and KYC within the simulation. |
| **Success Criteria** | Can review KYC and set KYC status.<br>Can activate and freeze customer accounts.<br>Can view customer account state.<br>Can access the audit trail.<br>Can log in/out. |
| **Deliverables** | Review and update of KYC status.<br>Activation and freezing of customer accounts.<br>Access to the audit trail. |

---

# 7. Scope of Work

## 7.1 Scope of the Application

| Is included | Is not included |
| :--- | :--- |
| - Customer onboarding<br>- KYC information capture (format-only, mocked for Aadhaar/PAN)<br>- Account activation<br>- Customer login/logout<br>- Transfer of simulated money<br>- Receipt of simulated money<br>- Viewing and downloading of statements<br>- Bank operations: review KYC, set KYC status, activate/freeze accounts, view customer account state, access audit trail, login/logout<br>- Role-based access for customer and bank-operations journeys<br>- Auditable state changes<br>- Traceable requirements and evidence<br>- Reusable AI-assisted engineering agents | - Beneficiary management<br>- Notifications<br>- Service requests<br>- Real Aadhaar verification<br>- Real PAN verification<br>- Real banking integrations<br>- Real payment gateways<br>- Real money movement<br>- Credit decisioning<br>- Lending<br>- Real financial transactions<br>- External KYC integrations |

---

# 8. Functional and Data Requirements

## 8.1 Requirements summary

This section lists the business requirements for the Online Banking Application simulation, grouped by business function for the Customer and Bank Operations roles. Formal technical implementation is out of scope for this document and belongs to the FRD stage. Each requirement is identified by a unique ID (BR-###) and carries source traceability.

## 8.2 Requirement priorities

The priority for delivering each requirement is listed to the right of the requirement statement using the following codes:

| Code | Priority |
| :--- | :--- |
| 1 | Must |
| 2 | Should |
| 3 | Could |
| F | Future |
| BP | Business Process |

Where the source material does not explicitly establish a priority, the priority is recorded as **UNSPECIFIED**. No priority is invented.

## 8.3 Functional Requirements

### Customer - Onboarding

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-001** — The system shall allow a customer to complete onboarding. | UNSPECIFIED | AGENTS (Customer scope), SCOPE-2 |

### Customer - KYC

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-002** — The system shall allow a customer to provide KYC information. | UNSPECIFIED | AGENTS (Customer scope) |
| **BR-003** — The system shall allow a customer to provide Aadhaar and PAN information. Verification of Aadhaar/PAN is format-only and mocked. | UNSPECIFIED | AGENTS (Customer scope), AGENTS (Out of scope) |

### Customer - Account

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-004** — The system shall allow a customer to activate an account. | UNSPECIFIED | AGENTS (Customer scope) |

### Customer - Access

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-005** — The system shall allow a customer to log in. | UNSPECIFIED | AGENTS (Customer scope) |
| **BR-006** — The system shall allow a customer to log out. | UNSPECIFIED | AGENTS (Customer scope) |

### Customer - Transactions

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-007** — The system shall allow a customer to transfer simulated money. | UNSPECIFIED | AGENTS (Customer scope) |
| **BR-008** — The system shall allow a customer to receive simulated money. | UNSPECIFIED | AGENTS (Customer scope) |

### Customer - Statements

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-009** — The system shall allow a customer to view statements. | UNSPECIFIED | AGENTS (Customer scope) |
| **BR-010** — The system shall allow a customer to download statements. | UNSPECIFIED | AGENTS (Customer scope) |

### Bank Operations - KYC

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-011** — The system shall allow bank operations to review KYC information. | UNSPECIFIED | AGENTS (Bank operations scope) |
| **BR-012** — The system shall allow bank operations to set KYC status. | UNSPECIFIED | AGENTS (Bank operations scope) |

### Bank Operations - Account

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-013** — The system shall allow bank operations to activate customer accounts. | UNSPECIFIED | AGENTS (Bank operations scope) |
| **BR-014** — The system shall allow bank operations to freeze customer accounts. | UNSPECIFIED | AGENTS (Bank operations scope) |
| **BR-015** — The system shall allow bank operations to view customer account state. | UNSPECIFIED | AGENTS (Bank operations scope) |

### Bank Operations - Audit

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-016** — The system shall allow bank operations to access the audit trail. | UNSPECIFIED | AGENTS (Bank operations scope), CHARTER-3.2 |

### Bank Operations - Access

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-017** — The system shall allow bank operations to log in. | UNSPECIFIED | AGENTS (Bank operations scope) |
| **BR-018** — The system shall allow bank operations to log out. | UNSPECIFIED | AGENTS (Bank operations scope) |

### Cross-cutting - Access

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-019** — The system shall provide role-based access so that customer and bank-operations journeys are kept distinct. | UNSPECIFIED | CHARTER-3.2 |

### Cross-cutting - Audit

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-020** — The system shall make state changes auditable. | UNSPECIFIED | CHARTER-3.2, CHARTER-7 |

### Cross-cutting - Simulation

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-021** — The system shall use synthetic identities, accounts, balances, beneficiaries, and payments for the simulation. | UNSPECIFIED | CHARTER-3.1, SCOPE-4 |

### Cross-cutting - Governance

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-022** — Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval. | UNSPECIFIED | CHARTER-3.4, CHARTER-5 |

### Cross-cutting - Traceability

| Detailed requirement | Priority | Source |
| :--- | :--- | :--- |
| **BR-023** — Approved business rules shall remain traceable through requirements and downstream evidence. | UNSPECIFIED | CHARTER-2, SCOPE-6 |

## 8.4 Business Rules

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

## 8.5 Traceability

The following SOURCE → BUSINESS REQUIREMENT chain is maintained:

| Source | Business Requirement |
| :--- | :--- |
| AGENTS (Customer scope) | BR-001 |
| SCOPE-2 | BR-001 |
| AGENTS (Customer scope) | BR-002 |
| AGENTS (Customer scope) | BR-003 |
| AGENTS (Out of scope) | BR-003 |
| AGENTS (Customer scope) | BR-004 |
| AGENTS (Customer scope) | BR-005 |
| AGENTS (Customer scope) | BR-006 |
| AGENTS (Customer scope) | BR-007 |
| AGENTS (Customer scope) | BR-008 |
| AGENTS (Customer scope) | BR-009 |
| AGENTS (Customer scope) | BR-010 |
| AGENTS (Bank operations scope) | BR-011 |
| AGENTS (Bank operations scope) | BR-012 |
| AGENTS (Bank operations scope) | BR-013 |
| AGENTS (Bank operations scope) | BR-014 |
| AGENTS (Bank operations scope) | BR-015 |
| AGENTS (Bank operations scope) | BR-016 |
| CHARTER-3.2 | BR-016 |
| AGENTS (Bank operations scope) | BR-017 |
| AGENTS (Bank operations scope) | BR-018 |
| CHARTER-3.2 | BR-019 |
| CHARTER-3.2 | BR-020 |
| CHARTER-7 | BR-020 |
| CHARTER-3.1 | BR-021 |
| SCOPE-4 | BR-021 |
| CHARTER-3.4 | BR-022 |
| CHARTER-5 | BR-022 |
| CHARTER-2 | BR-023 |
| SCOPE-6 | BR-023 |

## 8.6 Open Questions

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

# 9. Business Implementation Requirements

This section is intended to make the business aware of the depth and scope of the system implementation. The simulation is delivered through the coordinated work of four agent families (BRD, technical design/coding/unit testing, system-test/automation, and defect root-cause analysis). Human review and approval of agent output is required. Detailed training, migration, and implementation planning requirements are NOT SPECIFIED by the source material.

---

# 10. Issues

## 10.1 Open Issues

Open questions that remain unresolved and require business confirmation are listed in section 8.6. These items must be confirmed before being treated as approved requirements. See also the Open Questions artifact.

## 10.2 New Problems

NOT SPECIFIED. No probable adverse effects are defined by the source material.

## 10.3 Deferred Requirements

None identified in the source material as deferred in the current development scenario.

## 10.4 Ideas for Solutions

NOT SPECIFIED. The source material does not identify solution ideas at the business-requirements stage.

## 10.5 Management Issues

Governance through baselines, versioning, change control, traceability, evidence, risk management, and retrospectives is a stated project success criterion (CHARTER-7). Detailed management-issue resolution steps are NOT SPECIFIED by the source material.

---

## Status

- **Status:** RAW
- **Ready for human review:** READY_FOR_HUMAN_REVIEW
- **Approval status:** NOT_APPROVED
- **Version:** 1.0
