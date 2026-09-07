#!/usr/bin/env python3
"""
Generate the RAW BRD artifacts for the Online Banking Application.

Single source of truth -> brd.json, brd.md, brd.pdf
Uses ReportLab for PDF generation.
"""
import json
import os
import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "brd", "raw")
os.makedirs(RAW, exist_ok=True)

GENERATED_AT = "2026-09-07T00:00:00Z"

# ---------------------------------------------------------------------------
# Canonical BRD data
# ---------------------------------------------------------------------------

requirements = [
    {
        "id": "BR-001",
        "category": "Customer - Onboarding",
        "statement": "The system shall allow a customer to complete onboarding.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)", "SCOPE-2"],
        "rationale": "Onboarding is a core customer journey required for the simulation."
    },
    {
        "id": "BR-002",
        "category": "Customer - KYC",
        "statement": "The system shall allow a customer to provide KYC information.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "KYC information is required as part of the customer journey."
    },
    {
        "id": "BR-003",
        "category": "Customer - KYC",
        "statement": "The system shall allow a customer to provide Aadhaar and PAN information. Verification of Aadhaar/PAN is format-only and mocked.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)", "AGENTS (Out of scope)"],
        "rationale": "Aadhaar/PAN details are captured for the simulation but are not verified against any real authority."
    },
    {
        "id": "BR-004",
        "category": "Customer - Account",
        "statement": "The system shall allow a customer to activate an account.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Account activation is a required customer capability."
    },
    {
        "id": "BR-005",
        "category": "Customer - Access",
        "statement": "The system shall allow a customer to log in.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Customer login provides role-based access to the application."
    },
    {
        "id": "BR-006",
        "category": "Customer - Access",
        "statement": "The system shall allow a customer to log out.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Customer logout terminates the customer session."
    },
    {
        "id": "BR-007",
        "category": "Customer - Transactions",
        "statement": "The system shall allow a customer to transfer simulated money.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Money movement is simulated using synthetic data."
    },
    {
        "id": "BR-008",
        "category": "Customer - Transactions",
        "statement": "The system shall allow a customer to receive simulated money.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Money movement is simulated using synthetic data."
    },
    {
        "id": "BR-009",
        "category": "Customer - Statements",
        "statement": "The system shall allow a customer to view statements.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Statement viewing is a required customer capability."
    },
    {
        "id": "BR-010",
        "category": "Customer - Statements",
        "statement": "The system shall allow a customer to download statements.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Customer scope)"],
        "rationale": "Statement download is a required customer capability."
    },
    {
        "id": "BR-011",
        "category": "Bank Operations - KYC",
        "statement": "The system shall allow bank operations to review KYC information.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Bank operations administer KYC within the simulation."
    },
    {
        "id": "BR-012",
        "category": "Bank Operations - KYC",
        "statement": "The system shall allow bank operations to set KYC status.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Bank operations administer KYC status."
    },
    {
        "id": "BR-013",
        "category": "Bank Operations - Account",
        "statement": "The system shall allow bank operations to activate customer accounts.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Account activation is a bank-operations administrative capability."
    },
    {
        "id": "BR-014",
        "category": "Bank Operations - Account",
        "statement": "The system shall allow bank operations to freeze customer accounts.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Account freezing is a bank-operations administrative capability."
    },
    {
        "id": "BR-015",
        "category": "Bank Operations - Account",
        "statement": "The system shall allow bank operations to view customer account state.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Bank operations require visibility into customer account state."
    },
    {
        "id": "BR-016",
        "category": "Bank Operations - Audit",
        "statement": "The system shall allow bank operations to access the audit trail.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)", "CHARTER-3.2"],
        "rationale": "Audit trail access supports auditable state changes."
    },
    {
        "id": "BR-017",
        "category": "Bank Operations - Access",
        "statement": "The system shall allow bank operations to log in.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Bank-operations login provides role-based access."
    },
    {
        "id": "BR-018",
        "category": "Bank Operations - Access",
        "statement": "The system shall allow bank operations to log out.",
        "priority": "UNSPECIFIED",
        "source": ["AGENTS (Bank operations scope)"],
        "rationale": "Bank-operations logout terminates the session."
    },
    {
        "id": "BR-019",
        "category": "Cross-cutting - Access",
        "statement": "The system shall provide role-based access so that customer and bank-operations journeys are kept distinct.",
        "priority": "UNSPECIFIED",
        "source": ["CHARTER-3.2"],
        "rationale": "Role-based access is a stated project objective."
    },
    {
        "id": "BR-020",
        "category": "Cross-cutting - Audit",
        "statement": "The system shall make state changes auditable.",
        "priority": "UNSPECIFIED",
        "source": ["CHARTER-3.2", "CHARTER-7"],
        "rationale": "Auditable state changes are a stated project success criterion."
    },
    {
        "id": "BR-021",
        "category": "Cross-cutting - Simulation",
        "statement": "The system shall use synthetic identities, accounts, balances, beneficiaries, and payments for the simulation.",
        "priority": "UNSPECIFIED",
        "source": ["CHARTER-3.1", "SCOPE-4"],
        "rationale": "The project is an educational simulation using synthetic data."
    },
    {
        "id": "BR-022",
        "category": "Cross-cutting - Governance",
        "statement": "Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval.",
        "priority": "UNSPECIFIED",
        "source": ["CHARTER-3.4", "CHARTER-5"],
        "rationale": "Reviewable and source-linked agent output is a stated project objective."
    },
    {
        "id": "BR-023",
        "category": "Cross-cutting - Traceability",
        "statement": "Approved business rules shall remain traceable through requirements and downstream evidence.",
        "priority": "UNSPECIFIED",
        "source": ["CHARTER-2", "SCOPE-6"],
        "rationale": "Traceability is a stated governance and success requirement."
    }
]

# source -> BR traceability map
traceability = []
for req in requirements:
    for src in req["source"]:
        traceability.append({"source": src, "requirement": req["id"]})

business_rules = [
    {
        "id": "BR-001",
        "rule": "The simulation must not use real money; money movement is simulated using synthetic data.",
        "source": ["CHARTER-6", "SCOPE-5"]
    },
    {
        "id": "BR-002",
        "rule": "The simulation must not perform real identity verification; Aadhaar/PAN verification is format-only and mocked.",
        "source": ["CHARTER-6", "SCOPE-5"]
    },
    {
        "id": "BR-003",
        "rule": "The system must not perform credit decisioning, lending, or real financial transactions.",
        "source": ["CHARTER-6", "SCOPE-5"]
    },
    {
        "id": "BR-004",
        "rule": "The system must not integrate with production banks, real payment gateways, or external KYC integrations.",
        "source": ["CHARTER-6", "SCOPE-5"]
    },
    {
        "id": "BR-005",
        "rule": "The system supports two distinct roles: Customer and Bank Operations, with role-based access.",
        "source": ["CHARTER-3.2", "SCOPE-3"]
    },
    {
        "id": "BR-006",
        "rule": "State changes in the system must be auditable.",
        "source": ["CHARTER-3.2"]
    },
    {
        "id": "BR-007",
        "rule": "Any requirement outside the approved scope must be handled through the project's change-control process rather than silently added to the baseline.",
        "source": ["SCOPE-8"]
    },
    {
        "id": "BR-008",
        "rule": "Every project handoff must carry version, source IDs, assumptions, open questions, and approval status.",
        "source": ["CHARTER-5"]
    }
]

open_questions = [
    {
        "id": "OQ-001",
        "question": "Who executes UAT and signs off business acceptance?",
        "status": "OPEN",
        "source": ["CHARTER-8", "SCOPE-7"]
    },
    {
        "id": "OQ-002",
        "question": "What is the minimum balance value?",
        "status": "OPEN",
        "source": ["CHARTER-8", "SCOPE-7"]
    },
    {
        "id": "OQ-003",
        "question": "What is the daily transfer cap?",
        "status": "OPEN",
        "source": ["CHARTER-8", "SCOPE-7"]
    },
    {
        "id": "OQ-004",
        "question": "Is the data-testid convention confirmed with the development team?",
        "status": "OPEN",
        "source": ["AGENTS (Open Questions)"]
    },
    {
        "id": "OQ-005",
        "question": "What are the exact onboarding workflow and validation rules?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    },
    {
        "id": "OQ-006",
        "question": "What are the exact account operations and account-state rules?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    },
    {
        "id": "OQ-007",
        "question": "What are the exact transfer/payment rules and limits?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    },
    {
        "id": "OQ-008",
        "question": "What are the statement content and download behaviour details?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    },
    {
        "id": "OQ-009",
        "question": "What are the exact role permissions and authorization rules?",
        "status": "OPEN",
        "source": ["SCOPE-3", "SCOPE-7"]
    },
    {
        "id": "OQ-010",
        "question": "What are the detailed security, privacy, accessibility, and testability requirements?",
        "status": "OPEN",
        "source": ["CHARTER-8", "SCOPE-7"]
    },
    {
        "id": "OQ-011",
        "question": "What are the exact audit events to be recorded?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    },
    {
        "id": "OQ-012",
        "question": "What are the error codes and error messages?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    },
    {
        "id": "OQ-013",
        "question": "What are the data fields and validation constraints?",
        "status": "OPEN",
        "source": ["SCOPE-7"]
    }
]

# ---------------------------------------------------------------------------
# Assemble the full canonical document
# ---------------------------------------------------------------------------

document = {
    "artifact": "BRD",
    "artifact_name": "Business Requirements Document",
    "project": "Online Banking Application",
    "project_code": "ONLINE-BANKING",
    "version": "1.0",
    "status": "RAW",
    "ready_for_human_review": True,
    "approval_status": "NOT_APPROVED",
    "generated_at": GENERATED_AT,
    "generator_agent": "BRD Agent",
    "generator_agent_id": "84cb1640-5369-48c8-904e-c3f2189231c5",
    "source_basis": [
        "sources/charter.md",
        "sources/scope_agreement.md",
        "sources/brd_template.md"
    ],
    "document_status_note": "RAW - READY_FOR_HUMAN_REVIEW",
    "introduction": {
        "purpose": "The Online Banking Application is an educational simulation developed to demonstrate a coherent, traceable software development lifecycle. This Business Requirements Document specifies, in user/business language, what the business wants the system to do. It is the primary deliverable of the business-analysis stage and forms the basis for the Functional Requirements Document (FRD) and User Acceptance Testing (UAT).",
        "scope": "This BRD covers the business requirements for the Online Banking Application educational simulation as bounded by the project charter and the scope agreement. It defines the business capabilities, business rules, constraints, assumptions, and open questions. It does not specify technical implementation.",
        "audience": [
            "Business Analysts",
            "Requirements Analysts",
            "Architecture and Development teams",
            "Quality Assurance and Testing teams",
            "Defect Root Cause Analysis teams",
            "Human reviewers and approvers of business requirements"
        ],
        "references": [
            "Project2_Online_Banking_Student_Development_Project.docx (source basis)",
            "sources/charter.md",
            "sources/scope_agreement.md",
            "sources/brd_template.md"
        ]
    },
    "project_drivers": {
        "purpose_of_application": "Customers expect secure digital access to banking capabilities, including accounts, transfers, and statements. The project delivers a coherent online-banking simulation using synthetic data, coordinated across business analysis, architecture, development, testing, and defect root-cause analysis, supported by reusable AI-assisted engineering agents. Success requires demonstrating that an approved business rule can be traced through requirement, design element, implementation, test, defect decision, and final evidence record.",
        "stakeholders": [
            {"group": "Business Analysis", "team": "Ritu & Team (Group 2)", "role": "Turn approved needs into a Business Requirements Document."},
            {"group": "Architecture, Build and Unit Test (Development)", "team": "Mohit & Team", "role": "Technical design, build, and unit testing."},
            {"group": "Quality Assurance and Testing", "team": "Mandeep & Team", "role": "System testing and automation."},
            {"group": "Defect Root Cause Analysis", "team": "Adiba & Team", "role": "Defect root-cause analysis."}
        ],
        "users_of_application": [
            {"role": "Customer", "description": "Completes onboarding, provides KYC and Aadhaar/PAN information, activates an account, logs in/out, transfers and receives simulated money, and views/downloads statements."},
            {"role": "Bank Operations", "description": "Reviews KYC, sets KYC status, activates/freezes accounts, views customer account state, accesses the audit trail, and logs in/out."}
        ],
        "key_success_factors": [
            "A coherent banking simulation using synthetic identities, accounts, balances, beneficiaries, and payments.",
            "Role-based customer and bank-operations journeys with auditable state changes.",
            "Agent output that is reviewable, reproducible, schema-valid, source-linked, and subject to human approval.",
            "Traceability of approved business rules through requirement, design, implementation, test, and evidence.",
            "Application of security, privacy, accessibility, reliability, and testability as acceptance conditions.",
            "Governance through baselines, versioning, change control, traceability, evidence, risk management, and retrospectives."
        ]
    },
    "constraints": [
        {"id": "CON-001", "description": "The system is an educational simulation, not a production banking system.", "source": "CHARTER-6"},
        {"id": "CON-002", "description": "Real money movement is not permitted; money movement is simulated using synthetic data.", "source": "CHARTER-6, SCOPE-5"},
        {"id": "CON-003", "description": "Real identity verification is not permitted; Aadhaar/PAN verification is format-only and mocked.", "source": "CHARTER-6, SCOPE-5"},
        {"id": "CON-004", "description": "Credit decisioning is not permitted.", "source": "CHARTER-6, SCOPE-5"},
        {"id": "CON-005", "description": "Production bank integration is not permitted, including real payment gateways and external KYC integrations.", "source": "CHARTER-6, SCOPE-5"},
        {"id": "CON-006", "description": "Business requirements must not invent business decisions not present in the source material.", "source": "AGENTS (BRD Rules)"}
    ],
    "assumptions_and_dependencies": [
        {"id": "ASM-001", "description": "The project uses synthetic identities, accounts, balances, beneficiaries, and payments throughout the simulation.", "source": "CHARTER-3.1, SCOPE-4"},
        {"id": "ASM-002", "description": "The system supports two user roles: Customer and Bank Operations.", "source": "CHARTER-3.2, SCOPE-3"},
        {"id": "ASM-003", "description": "All agent-produced artifacts are reviewable, reproducible, schema-valid, source-linked, and subject to human approval.", "source": "CHARTER-5"},
        {"id": "ASM-004", "description": "Candidate in-scope business areas are subject to detailed requirement confirmation and human approval before being treated as approved requirements.", "source": "SCOPE-2"},
        {"id": "ASM-005", "description": "Aadhaar/PAN verification is format-only and mocked; no real identity verification is performed.", "source": "AGENTS (Business Scope)"}
    ],
    "current_state": {
        "stakeholder_problem": "Customers expect secure digital access to onboarding, accounts, transfers, statements, and related banking functions. Student projects can treat business analysis, architecture, engineering, testing, evidence management, and defect triage as isolated activities, which can result in ambiguous requirements, untestable designs, weak handoffs, and disagreement over whether a failure is a defect or a new request.",
        "existing_business_environment": "No detailed description of an existing business environment is provided in the source material. The project is a new educational simulation and is not based on an existing production banking system.",
        "existing_application_environment": "No existing application environment is described in the source material. The application is greenfield for the purposes of this simulation."
    },
    "stakeholder_profiles": [
        {
            "id": "STK-001",
            "name": "Customer",
            "description": "An end user of the online banking simulation who manages their own onboarding, KYC, account activation, transactions, and statements.",
            "success_criteria": [
                "Can complete onboarding and provide KYC and Aadhaar/PAN information.",
                "Can activate an account and log in/out.",
                "Can transfer and receive simulated money.",
                "Can view and download statements."
            ],
            "deliverables": [
                "Completion of onboarding.",
                "Provision of KYC and Aadhaar/PAN information.",
                "Activation of an account."
            ]
        },
        {
            "id": "STK-002",
            "name": "Bank Operations",
            "description": "A bank-operations user who administers customer accounts and KYC within the simulation.",
            "success_criteria": [
                "Can review KYC and set KYC status.",
                "Can activate and freeze customer accounts.",
                "Can view customer account state.",
                "Can access the audit trail.",
                "Can log in/out."
            ],
            "deliverables": [
                "Review and update of KYC status.",
                "Activation and freezing of customer accounts.",
                "Access to the audit trail."
            ]
        }
    ],
    "scope_of_work": {
        "included": [
            "Customer onboarding",
            "KYC information capture (format-only, mocked for Aadhaar/PAN)",
            "Account activation",
            "Customer login/logout",
            "Transfer of simulated money",
            "Receipt of simulated money",
            "Viewing and downloading of statements",
            "Bank operations: review KYC, set KYC status, activate/freeze accounts, view customer account state, access audit trail, login/logout",
            "Role-based access for customer and bank-operations journeys",
            "Auditable state changes",
            "Traceable requirements and evidence",
            "Reusable AI-assisted engineering agents"
        ],
        "not_included": [
            "Beneficiary management",
            "Notifications",
            "Service requests",
            "Real Aadhaar verification",
            "Real PAN verification",
            "Real banking integrations",
            "Real payment gateways",
            "Real money movement",
            "Credit decisioning",
            "Lending",
            "Real financial transactions",
            "External KYC integrations"
        ]
    },
    "requirements": requirements,
    "traceability": traceability,
    "business_rules": business_rules,
    "open_questions": open_questions,
    "priority_legend": {
        "1": "Must",
        "2": "Should",
        "3": "Could",
        "F": "Future",
        "BP": "Business Process",
        "UNSPECIFIED": "Priority not explicitly established by the source material."
    }
}

# ---------------------------------------------------------------------------
# Write JSON
# ---------------------------------------------------------------------------

brd_json_path = os.path.join(RAW, "brd.json")
with open(brd_json_path, "w") as f:
    json.dump(document, f, indent=2, ensure_ascii=False)
print("Wrote", brd_json_path)

# ---------------------------------------------------------------------------
# Build Markdown
# ---------------------------------------------------------------------------

md = []
A = md.append

A("# Business Requirements Document")
A("")
A("**Project Name:** Online Banking Application")
A("")
A("**Project Code:** ONLINE-BANKING")
A("")
A("**Version No.:** 1.0")
A("")
A("**Date:** 2026-09-07")
A("")
A("**Status:** RAW")
A("")
A("**Approval Status:** NOT_APPROVED")
A("")
A("**READY_FOR_HUMAN_REVIEW**")
A("")
A("---")
A("")
A("## Revision History")
A("")
A("| Version No | Date | Prepared by / Modified by | Significant Changes |")
A("| :--- | :--- | :--- | :--- |")
A("| 1.0 | 2026-09-07 | BRD Agent | Initial RAW BRD generated for human review |")
A("")
A("---")
A("")
A("## Glossary")
A("")
A("### Abbreviation Description")
A("")
A("| Abbreviation | Description |")
A("| :--- | :--- |")
A("| BRD | Business Requirements Document |")
A("| FRD | Functional Requirements Document |")
A("| UAT | User Acceptance Testing |")
A("| KYC | Know Your Customer |")
A("| SDLC | Software Development Life Cycle |")
A("| AI | Artificial Intelligence |")
A("")
A("---")
A("")
A("## Table Of Contents")
A("")
A("- [1. Introduction](#1-introduction)")
A("  - [1.1 Purpose](#11-purpose)")
A("  - [1.2 Scope](#12-scope)")
A("  - [1.3 Audience](#13-audience)")
A("  - [1.4 References](#14-references)")
A("- [2. Project Drivers](#2-project-drivers)")
A("- [3. Constraints](#3-constraints)")
A("- [4. Assumptions and Dependencies](#4-assumptions-and-dependencies)")
A("- [5. Current State](#5-current-state)")
A("- [6. Stakeholder Profiles](#6-stakeholder-profiles)")
A("- [7. Scope of Work](#7-scope-of-work)")
A("- [8. Functional and Data Requirements](#8-functional-and-data-requirements)")
A("  - [8.1 Requirements summary](#81-requirements-summary)")
A("  - [8.2 Requirement priorities](#82-requirement-priorities)")
A("  - [8.3 Functional Requirements](#83-functional-requirements)")
A("  - [8.4 Business Rules](#84-business-rules)")
A("  - [8.5 Traceability](#85-traceability)")
A("  - [8.6 Open Questions](#86-open-questions)")
A("- [9. Business Implementation Requirements](#9-business-implementation-requirements)")
A("- [10. Issues](#10-issues)")
A("")
A("---")
A("")
A("# 1. Introduction")
A("")
A("## 1.1 Purpose")
A("")
A(document["introduction"]["purpose"])
A("")
A("## 1.2 Scope")
A("")
A(document["introduction"]["scope"])
A("")
A("## 1.3 Audience")
A("")
for aud in document["introduction"]["audience"]:
    A("- " + aud)
A("")
A("## 1.4 References")
A("")
for ref in document["introduction"]["references"]:
    A("- " + ref)
A("")
A("---")
A("")
A("# 2. Project Drivers")
A("")
A("## 2.1 The purpose of the application")
A("")
A(document["project_drivers"]["purpose_of_application"])
A("")
A("## 2.2 Client, Customer and other Stakeholders")
A("")
for st in document["project_drivers"]["stakeholders"]:
    A(f"- **{st['group']}** ({st['team']}): {st['role']}")
A("")
A("## 2.3 Users of the Application")
A("")
for u in document["project_drivers"]["users_of_application"]:
    A(f"- **{u['role']}**: {u['description']}")
A("")
A("## 2.4 Key success factors")
A("")
for ksf in document["project_drivers"]["key_success_factors"]:
    A("- " + ksf)
A("")
A("---")
A("")
A("# 3. Constraints")
A("")
A("## 3.1 Constraints")
A("")
A("| ID | Constraint | Source |")
A("| :--- | :--- | :--- |")
for c in document["constraints"]:
    A(f"| {c['id']} | {c['description']} | {c['source']} |")
A("")
A("---")
A("")
A("# 4. Assumptions and Dependencies")
A("")
for a in document["assumptions_and_dependencies"]:
    A(f"- **{a['id']}**: {a['description']} (Source: {a['source']})")
A("")
A("---")
A("")
A("# 5. Current State")
A("")
A("## 5.1 Stakeholder Problem and Desired State Capture")
A("")
A(document["current_state"]["stakeholder_problem"])
A("")
A("## 5.2 Overview of current business environment")
A("")
A("### 5.2.1 Existing business environment")
A("")
A(document["current_state"]["existing_business_environment"])
A("")
A("### 5.2.2 Existing application environment")
A("")
A(document["current_state"]["existing_application_environment"])
A("")
A("---")
A("")
A("# 6. Stakeholder Profiles")
A("")
for idx, sp in enumerate(document["stakeholder_profiles"], start=1):
    A(f"## 6.{idx} {sp['name']} ({sp['id']})")
    A("")
    A("| Attribute | Details |")
    A("| :--- | :--- |")
    A(f"| **Description** | {sp['description']} |")
    A(f"| **Success Criteria** | {'<br>'.join(sp['success_criteria'])} |")
    A(f"| **Deliverables** | {'<br>'.join(sp['deliverables'])} |")
    A("")
A("---")
A("")
A("# 7. Scope of Work")
A("")
A("## 7.1 Scope of the Application")
A("")
A("| Is included | Is not included |")
A("| :--- | :--- |")
inc = "<br>".join("- " + x for x in document["scope_of_work"]["included"])
excl = "<br>".join("- " + x for x in document["scope_of_work"]["not_included"])
A(f"| {inc} | {excl} |")
A("")
A("---")
A("")
A("# 8. Functional and Data Requirements")
A("")
A("## 8.1 Requirements summary")
A("")
A("This section lists the business requirements for the Online Banking Application simulation, grouped by business function for the Customer and Bank Operations roles. Formal technical implementation is out of scope for this document and belongs to the FRD stage. Each requirement is identified by a unique ID (BR-###) and carries source traceability.")
A("")
A("## 8.2 Requirement priorities")
A("")
A("The priority for delivering each requirement is listed to the right of the requirement statement using the following codes:")
A("")
A("| Code | Priority |")
A("| :--- | :--- |")
A("| 1 | Must |")
A("| 2 | Should |")
A("| 3 | Could |")
A("| F | Future |")
A("| BP | Business Process |")
A("")
A("Where the source material does not explicitly establish a priority, the priority is recorded as **UNSPECIFIED**. No priority is invented.")
A("")
A("## 8.3 Functional Requirements")
A("")
# Group requirements by category
from collections import OrderedDict
groups = OrderedDict()
for req in requirements:
    groups.setdefault(req["category"], []).append(req)

for cat, reqs in groups.items():
    A(f"### {cat}")
    A("")
    A("| Detailed requirement | Priority | Source |")
    A("| :--- | :--- | :--- |")
    for r in reqs:
        A(f"| **{r['id']}** — {r['statement']} | {r['priority']} | {', '.join(r['source'])} |")
    A("")

A("## 8.4 Business Rules")
A("")
A("| ID | Business Rule | Source |")
A("| :--- | :--- | :--- |")
for br in business_rules:
    A(f"| {br['id']} | {br['rule']} | {', '.join(br['source'])} |")
A("")
A("## 8.5 Traceability")
A("")
A("The following SOURCE → BUSINESS REQUIREMENT chain is maintained:")
A("")
A("| Source | Business Requirement |")
A("| :--- | :--- |")
for t in traceability:
    A(f"| {t['source']} | {t['requirement']} |")
A("")
A("## 8.6 Open Questions")
A("")
A("| ID | Open Question | Status | Source |")
A("| :--- | :--- | :--- | :--- |")
for oq in open_questions:
    A(f"| {oq['id']} | {oq['question']} | {oq['status']} | {', '.join(oq['source'])} |")
A("")
A("---")
A("")
A("# 9. Business Implementation Requirements")
A("")
A("This section is intended to make the business aware of the depth and scope of the system implementation. The simulation is delivered through the coordinated work of four agent families (BRD, technical design/coding/unit testing, system-test/automation, and defect root-cause analysis). Human review and approval of agent output is required. Detailed training, migration, and implementation planning requirements are NOT SPECIFIED by the source material.")
A("")
A("---")
A("")
A("# 10. Issues")
A("")
A("## 10.1 Open Issues")
A("")
A("Open questions that remain unresolved and require business confirmation are listed in section 8.6. These items must be confirmed before being treated as approved requirements. See also the Open Questions artifact.")
A("")
A("## 10.2 New Problems")
A("")
A("NOT SPECIFIED. No probable adverse effects are defined by the source material.")
A("")
A("## 10.3 Deferred Requirements")
A("")
A("None identified in the source material as deferred in the current development scenario.")
A("")
A("## 10.4 Ideas for Solutions")
A("")
A("NOT SPECIFIED. The source material does not identify solution ideas at the business-requirements stage.")
A("")
A("## 10.5 Management Issues")
A("")
A("Governance through baselines, versioning, change control, traceability, evidence, risk management, and retrospectives is a stated project success criterion (CHARTER-7). Detailed management-issue resolution steps are NOT SPECIFIED by the source material.")
A("")
A("---")
A("")
A("## Status")
A("")
A("- **Status:** RAW")
A("- **Ready for human review:** READY_FOR_HUMAN_REVIEW")
A("- **Approval status:** NOT_APPROVED")
A("- **Version:** 1.0")
A("")

brd_md_path = os.path.join(RAW, "brd.md")
with open(brd_md_path, "w") as f:
    f.write("\n".join(md))
print("Wrote", brd_md_path)

# ---------------------------------------------------------------------------
# Business Rules artifacts
# ---------------------------------------------------------------------------

br_doc = {
    "artifact": "BUSINESS_RULES",
    "artifact_name": "Business Rules",
    "project": "Online Banking Application",
    "version": "1.0",
    "status": "RAW",
    "ready_for_human_review": True,
    "approval_status": "NOT_APPROVED",
    "generated_at": GENERATED_AT,
    "generator_agent": "BRD Agent",
    "source_basis": ["sources/charter.md", "sources/scope_agreement.md"],
    "rules": business_rules
}

with open(os.path.join(RAW, "business_rules.json"), "w") as f:
    json.dump(br_doc, f, indent=2, ensure_ascii=False)

brmd = []
brmd.append("# Business Rules")
brmd.append("")
brmd.append("**Project Name:** Online Banking Application")
brmd.append("")
brmd.append("**Version No.:** 1.0")
brmd.append("")
brmd.append("**Status:** RAW")
brmd.append("")
brmd.append("**Approval Status:** NOT_APPROVED")
brmd.append("")
brmd.append("**READY_FOR_HUMAN_REVIEW**")
brmd.append("")
brmd.append("## Business Rules")
brmd.append("")
brmd.append("| ID | Business Rule | Source |")
brmd.append("| :--- | :--- | :--- |")
for br in business_rules:
    brmd.append(f"| {br['id']} | {br['rule']} | {', '.join(br['source'])} |")
brmd.append("")
brmd.append("## Status")
brmd.append("")
brmd.append("- **Status:** RAW")
brmd.append("- **Ready for human review:** READY_FOR_HUMAN_REVIEW")
brmd.append("- **Approval status:** NOT_APPROVED")
brmd.append("- **Version:** 1.0")
brmd.append("")
with open(os.path.join(RAW, "business_rules.md"), "w") as f:
    f.write("\n".join(brmd))

# ---------------------------------------------------------------------------
# Open Questions artifacts
# ---------------------------------------------------------------------------

oq_doc = {
    "artifact": "OPEN_QUESTIONS",
    "artifact_name": "Open Questions",
    "project": "Online Banking Application",
    "version": "1.0",
    "status": "RAW",
    "ready_for_human_review": True,
    "approval_status": "NOT_APPROVED",
    "generated_at": GENERATED_AT,
    "generator_agent": "BRD Agent",
    "source_basis": ["sources/charter.md", "sources/scope_agreement.md"],
    "questions": open_questions
}

with open(os.path.join(RAW, "open_questions.json"), "w") as f:
    json.dump(oq_doc, f, indent=2, ensure_ascii=False)

oqmd = []
oqmd.append("# Open Questions")
oqmd.append("")
oqmd.append("**Project Name:** Online Banking Application")
oqmd.append("")
oqmd.append("**Version No.:** 1.0")
oqmd.append("")
oqmd.append("**Status:** RAW")
oqmd.append("")
oqmd.append("**Approval Status:** NOT_APPROVED")
oqmd.append("")
oqmd.append("**READY_FOR_HUMAN_REVIEW**")
oqmd.append("")
oqmd.append("## Open Questions")
oqmd.append("")
oqmd.append("| ID | Open Question | Status | Source |")
oqmd.append("| :--- | :--- | :--- | :--- |")
for oq in open_questions:
    oqmd.append(f"| {oq['id']} | {oq['question']} | {oq['status']} | {', '.join(oq['source'])} |")
oqmd.append("")
oqmd.append("## Status")
oqmd.append("")
oqmd.append("- **Status:** RAW")
oqmd.append("- **Ready for human review:** READY_FOR_HUMAN_REVIEW")
oqmd.append("- **Approval status:** NOT_APPROVED")
oqmd.append("- **Version:** 1.0")
oqmd.append("")
with open(os.path.join(RAW, "open_questions.md"), "w") as f:
    f.write("\n".join(oqmd))

print("Wrote JSON and Markdown artifacts.")
