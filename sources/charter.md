

# Project Charter — Online Banking Student Development Project

## Document Status
- Status: DRAFT — for human review
- Source basis: Project2_Online_Banking_Student_Development_Project.docx
- Business Analysis group: Ritu & Team (Group 2)

## 1. Project Overview
The project is an **Online Banking Application** developed as an educational simulation. The overall initiative covers business analysis, architecture, development, testing, and defect root-cause analysis, together with reusable AI-assisted engineering agents.

## 2. Problem Statement
Customers expect secure digital access to onboarding, accounts, beneficiaries, transfers, statements, notifications, and service requests. A simplified online-banking solution still requires coordinated business analysis, architecture, engineering, testing, evidence management, and defect triage.

Student projects can treat these activities as isolated work, which can result in ambiguous requirements, untestable designs, weak handoffs, and disagreement over whether a failure is a defect or a new request.

The project therefore requires an online-banking simulation and specialized agents that support a traceable SDLC. Success is not limited to a working interface; the team must demonstrate that an approved business rule can be traced through requirement, design element, implementation, test, defect decision, and final evidence record.

## 3. Project Objectives
The project objectives stated in the source are to:

1. Deliver a coherent banking simulation using synthetic identities, accounts, balances, beneficiaries, and payments.
2. Demonstrate customer and bank-operations' journeys with role-based access and auditable state changes.
3. Build four agent families:
   - BRD
   - Technical design/coding/unit testing
   - System-test/automation
   - Defect root-cause analysis
4. Make agent output reviewable, reproducible, schema-valid, source-linked, and subject to human approval.
5. Use security, privacy, accessibility, reliability, and testability as acceptance conditions rather than optional polish.
6. Practice governance including baselines, versioning, change control, traceability, evidence, risk management, and retrospectives.

## 4. Group / Persona Responsibilities
The source defines the following personas:

- **Business Analysis:** Ritu & Team
- **Architecture & Build and Unit Test [Development]:** Mohit & Team
- **Quality Assurance & Testing:** Mandeep & Team
- **Defect Root Cause Analysis:** Adiba & Team

For Group 2, the stated responsibility is to turn approved needs into a BRD.

## 5. Governance and Handoffs
Every handoff must carry:
- version
- source IDs
- assumptions
- open questions
- approval status

Agent-produced artifacts are intended to be reviewable, reproducible, schema-valid, source-linked, and subject to human approval.

## 6. Project Boundaries
The project premise explicitly states that this is an educational simulation.

The following are **not permitted**:
- real money
- real identity verification
- credit decisioning
- production bank integration

## 7. Success Criteria
Project success includes:
- a coherent banking simulation
- role-based customer and bank-operations journeys
- auditable state changes
- traceable requirements and downstream evidence
- reusable AI-assisted engineering agents
- human review and approval of agent output
- application of security, privacy, accessibility, reliability, and testability as acceptance conditions
- governance through baselines, versioning, change control, traceability, evidence, risk management, and retrospectives

## 8. Open Questions
The source material does not specify detailed business rules, numeric limits, detailed user permissions, detailed onboarding/KYC rules, transfer rules, statement rules, notification behaviour, service-request behaviour, data fields, error catalogue, or approval owners.

These details must be confirmed before being treated as approved requirements.
