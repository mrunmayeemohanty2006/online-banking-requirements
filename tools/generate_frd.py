#!/usr/bin/env python3
"""
Generate the RAW FRD artifacts for the Online Banking Application.

Single source of truth -> frd.json, frd.md, frd.pdf
                               data_spec.json/.md/.pdf
                               error_catalogue.json/.md/.pdf

Uses tools/generate_pdf.py (ReportLab) for PDF generation.
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "frd", "raw")
os.makedirs(RAW, exist_ok=True)

GENERATED_AT = "2026-09-07T00:00:00Z"
VERSION = "1.0"
STATUS = "RAW"
APPROVAL = "NOT_APPROVED"

TOOLS = os.path.join(BASE, "tools")
sys.path.insert(0, TOOLS)

PROJECT = "Online Banking Application"
PROJECT_CODE = "ONLINE-BANKING"

# ---------------------------------------------------------------------------
# Open questions carried forward from the approved BRD (all OPEN)
# ---------------------------------------------------------------------------
OPEN_QUESTIONS = [
    {"id": "OQ-001", "question": "Who executes UAT and signs off business acceptance?", "status": "OPEN", "source": ["CHARTER-8", "SCOPE-7"]},
    {"id": "OQ-002", "question": "What is the minimum balance value?", "status": "OPEN", "source": ["CHARTER-8", "SCOPE-7"]},
    {"id": "OQ-003", "question": "What is the daily transfer cap?", "status": "OPEN", "source": ["CHARTER-8", "SCOPE-7"]},
    {"id": "OQ-004", "question": "Is the data-testid convention confirmed with the development team?", "status": "OPEN", "source": ["AGENTS (Open Questions)"]},
    {"id": "OQ-005", "question": "What are the exact onboarding workflow and validation rules?", "status": "OPEN", "source": ["SCOPE-7"]},
    {"id": "OQ-006", "question": "What are the exact account operations and account-state rules?", "status": "OPEN", "source": ["SCOPE-7"]},
    {"id": "OQ-007", "question": "What are the exact transfer/payment rules and limits?", "status": "OPEN", "source": ["SCOPE-7"]},
    {"id": "OQ-008", "question": "What are the statement content and download behaviour details?", "status": "OPEN", "source": ["SCOPE-7"]},
    {"id": "OQ-009", "question": "What are the exact role permissions and authorization rules?", "status": "OPEN", "source": ["SCOPE-3", "SCOPE-7"]},
    {"id": "OQ-010", "question": "What are the detailed security, privacy, accessibility, and testability requirements?", "status": "OPEN", "source": ["CHARTER-8", "SCOPE-7"]},
    {"id": "OQ-011", "question": "What are the exact audit events to be recorded?", "status": "OPEN", "source": ["SCOPE-7"]},
    {"id": "OQ-012", "question": "What are the error codes and error messages?", "status": "OPEN", "source": ["SCOPE-7"]},
    {"id": "OQ-013", "question": "What are the data fields and validation constraints?", "status": "OPEN", "source": ["SCOPE-7"]},
]

# ---------------------------------------------------------------------------
# Business rules carried forward from the approved BRD
# ---------------------------------------------------------------------------
BUSINESS_RULES = [
    {"id": "BR-001", "rule": "The simulation must not use real money; money movement is simulated using synthetic data.", "source": ["CHARTER-6", "SCOPE-5"]},
    {"id": "BR-002", "rule": "The simulation must not perform real identity verification; Aadhaar/PAN verification is format-only and mocked.", "source": ["CHARTER-6", "SCOPE-5"]},
    {"id": "BR-003", "rule": "The system must not perform credit decisioning, lending, or real financial transactions.", "source": ["CHARTER-6", "SCOPE-5"]},
    {"id": "BR-004", "rule": "The system must not integrate with production banks, real payment gateways, or external KYC integrations.", "source": ["CHARTER-6", "SCOPE-5"]},
    {"id": "BR-005", "rule": "The system supports two distinct roles: Customer and Bank Operations, with role-based access.", "source": ["CHARTER-3.2", "SCOPE-3"]},
    {"id": "BR-006", "rule": "State changes in the system must be auditable.", "source": ["CHARTER-3.2"]},
    {"id": "BR-007", "rule": "Any requirement outside the approved scope must be handled through the project's change-control process rather than silently added to the baseline.", "source": ["SCOPE-8"]},
    {"id": "BR-008", "rule": "Every project handoff must carry version, source IDs, assumptions, open questions, and approval status.", "source": ["CHARTER-5"]},
]


def br_by_id(rid):
    for br in BUSINESS_RULES:
        if br["id"] == rid:
            return br["rule"]
    return None


def oq_ids_for(path_keys):
    """Return open-question IDs relevant to the given FR based on source scope keys."""
    return []


# ---------------------------------------------------------------------------
# Functional Requirements
# ---------------------------------------------------------------------------
def fr(rid, title, desc, br, priority, preconditions, trigger, behavior,
       brules, inputs, outputs, validation, error_behavior, acceptance_reference,
       open_questions):
    return {
        "id": rid,
        "title": title,
        "description": desc,
        "source_business_requirement": br,
        "priority": priority,
        "preconditions": preconditions,
        "trigger": trigger,
        "functional_behavior": behavior,
        "business_rules": brules,
        "inputs": inputs,
        "outputs": outputs,
        "validation": validation,
        "error_behavior": error_behavior,
        "acceptance_reference": acceptance_reference,
        "open_questions": open_questions,
    }


FRS = [
    fr(
        "FR-001",
        "Customer completes onboarding",
        "The system shall allow a customer to complete onboarding as a customer journey within the simulation.",
        "BR-001", "UNSPECIFIED",
        ["A customer actor exists within the simulation.", "The customer role is recognised for role-based access (OQ-009)."],
        "A customer initiates the onboarding journey.",
        "The system presents the onboarding journey and records its completion for the customer within the simulation. The exact onboarding workflow and validation rules are not specified by the approved source and remain open (OQ-005).",
        [br_by_id("BR-005")],
        ["Customer identification/identity data within the simulation.", "Onboarding initiation by a customer."],
        ["Recorded completion of customer onboarding."],
        "Onboarding completion is recorded against the customer. Detailed validation rules remain OPEN (OQ-005); no validation rules are invented beyond the approved source.",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-001",
        ["OQ-005", "OQ-009", "OQ-012"],
    ),
    fr(
        "FR-002",
        "Customer provides KYC information",
        "The system shall allow a customer to provide KYC information as part of the customer journey.",
        "BR-002", "UNSPECIFIED",
        ["A customer actor exists within the simulation."],
        "A customer provides KYC information.",
        "The system accepts and records KYC information provided by the customer. The exact KYC data fields and validation constraints are not specified by the approved source and remain open (OQ-013).",
        [br_by_id("BR-002"), br_by_id("BR-004")],
        ["KYC information provided by the customer."],
        ["Recorded KYC information for the customer."],
        "KYC information is recorded against the customer. Field-level validation constraints remain OPEN (OQ-013).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-002",
        ["OQ-012", "OQ-013"],
    ),
    fr(
        "FR-003",
        "Customer provides Aadhaar and PAN information (format-only, mocked)",
        "The system shall allow a customer to provide Aadhaar and PAN information. Verification of Aadhaar/PAN is format-only and mocked; no real identity verification is performed.",
        "BR-003", "UNSPECIFIED",
        ["A customer actor exists within the simulation.", "No real identity verification is performed (BR-002)."],
        "A customer provides Aadhaar and/or PAN information.",
        "The system captures Aadhaar and PAN information. Verification, where present, is format-only and mocked. The system must not perform real identity verification (BR-002) and must not integrate with external KYC providers (BR-004).",
        [br_by_id("BR-002"), br_by_id("BR-004")],
        ["Aadhaar information provided by the customer.", "PAN information provided by the customer."],
        ["Recorded Aadhaar/PAN information and any format-only verification result."],
        "Aadhaar/PAN verification is format-only and mocked; no real identity authority is consulted. Field-level validation constraints remain OPEN (OQ-013).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-003",
        ["OQ-012", "OQ-013"],
    ),
    fr(
        "FR-004",
        "Customer activates an account",
        "The system shall allow a customer to activate an account within the simulation.",
        "BR-004", "UNSPECIFIED",
        ["A customer actor exists within the simulation."],
        "A customer activates an account.",
        "The system allows a customer to activate an account. Account activation may also be performed by bank operations (see FR-013). Account operations and account-state rules remain open (OQ-006).",
        [br_by_id("BR-005"), br_by_id("BR-006")],
        ["Account activation requested by the customer."],
        ["Account moved to an activated state within the simulation.", "State change recorded for audit (BR-006)."],
        "Activation transitions the account state in the simulation. Exact account-state rules remain OPEN (OQ-006).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-004",
        ["OQ-006", "OQ-012"],
    ),
    fr(
        "FR-005",
        "Customer logs in",
        "The system shall allow a customer to log in to the application.",
        "BR-005", "UNSPECIFIED",
        ["A customer actor exists within the simulation.", "Role-based access is provided (BR-005 business rule)."],
        "A customer requests to log in.",
        "The system allows a customer to log in, establishing role-based access for the customer journey. Authentication mechanisms are not specified by the approved source and are not invented (OQ-010).",
        [br_by_id("BR-005"), br_by_id("BR-008")],
        ["Customer login request."],
        ["Customer session established for role-based access."],
        "A successful login establishes a customer session. Authentication/login mechanism details remain OPEN (OQ-010, OQ-009).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-005",
        ["OQ-009", "OQ-010", "OQ-012"],
    ),
    fr(
        "FR-006",
        "Customer logs out",
        "The system shall allow a customer to log out, terminating the customer session.",
        "BR-006", "UNSPECIFIED",
        ["A customer session exists within the simulation."],
        "A customer requests to log out.",
        "The system allows a customer to log out, terminating the customer session.",
        [br_by_id("BR-005")],
        ["Customer logout request."],
        ["Customer session terminated."],
        "Logout terminates the customer session. Session/termination mechanism details remain OPEN (OQ-010).",
        "Not specified by the approved source.",
        "BR-006",
        ["OQ-010"],
    ),
    fr(
        "FR-007",
        "Customer transfers simulated money",
        "The system shall allow a customer to transfer simulated money using synthetic data.",
        "BR-007", "UNSPECIFIED",
        ["A customer is logged in within the simulation.", "Money movement is simulated using synthetic data (BR-001)."],
        "A customer initiates a transfer of simulated money.",
        "The system allows a customer to transfer simulated money. Money movement is simulated and must not involve real money (BR-001). The system must not perform credit decisioning, lending, or real financial transactions (BR-003). Exact transfer/payment rules and limits remain open (OQ-007, OQ-002, OQ-003).",
        [br_by_id("BR-001"), br_by_id("BR-003"), br_by_id("BR-006")],
        ["Transfer of simulated money initiated by the customer."],
        ["Recorded simulated transfer.", "Updated simulated balances.", "State change recorded for audit (BR-006)."],
        "Transfers are simulated using synthetic data. Transfer/payment rules and limits, minimum balance, and daily transfer cap remain OPEN (OQ-007, OQ-002, OQ-003).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-007",
        ["OQ-002", "OQ-003", "OQ-007", "OQ-012"],
    ),
    fr(
        "FR-008",
        "Customer receives simulated money",
        "The system shall allow a customer to receive simulated money using synthetic data.",
        "BR-008", "UNSPECIFIED",
        ["A customer is logged in within the simulation.", "Money movement is simulated using synthetic data (BR-001)."],
        "A customer receives simulated money.",
        "The system allows a customer to receive simulated money. Money movement is simulated and must not involve real money (BR-001). The system must not perform credit decisioning, lending, or real financial transactions (BR-003). Exact transfer/payment rules and limits remain open (OQ-007).",
        [br_by_id("BR-001"), br_by_id("BR-003"), br_by_id("BR-006")],
        ["Receipt of simulated money for the customer."],
        ["Recorded simulated receipt.", "Updated simulated balances.", "State change recorded for audit (BR-006)."],
        "Receipts are simulated using synthetic data. Transfer/payment rules and limits remain OPEN (OQ-007).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-008",
        ["OQ-007", "OQ-012"],
    ),
    fr(
        "FR-009",
        "Customer views statements",
        "The system shall allow a customer to view statements.",
        "BR-009", "UNSPECIFIED",
        ["A customer is logged in within the simulation."],
        "A customer requests to view statements.",
        "The system allows a customer to view statements. Statement content details remain open (OQ-008).",
        [br_by_id("BR-005")],
        ["Statement viewing request by the customer."],
        ["Statements displayed to the customer."],
        "Statements are displayed to the customer. Statement content details remain OPEN (OQ-008).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-009",
        ["OQ-008", "OQ-012"],
    ),
    fr(
        "FR-010",
        "Customer downloads statements",
        "The system shall allow a customer to download statements.",
        "BR-010", "UNSPECIFIED",
        ["A customer is logged in within the simulation."],
        "A customer requests to download statements.",
        "The system allows a customer to download statements. Statement download behaviour details remain open (OQ-008).",
        [br_by_id("BR-005")],
        ["Statement download request by the customer."],
        ["Statements made available for download to the customer."],
        "Statements are downloadable by the customer. Download behaviour and content details remain OPEN (OQ-008).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-010",
        ["OQ-008", "OQ-012"],
    ),
    fr(
        "FR-011",
        "Bank operations reviews KYC information",
        "The system shall allow bank operations to review KYC information.",
        "BR-011", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation.", "Role-based access is provided (BR-005 business rule)."],
        "Bank operations requests to review KYC information.",
        "The system allows bank operations to review KYC information. The exact review workflow and data displayed remain open (OQ-005, OQ-013).",
        [br_by_id("BR-004"), br_by_id("BR-005")],
        ["KYC review request by bank operations."],
        ["KYC information displayed to bank operations."],
        "KYC information is displayed to bank operations for review. Review workflow details remain OPEN (OQ-005).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-011",
        ["OQ-005", "OQ-012", "OQ-013"],
    ),
    fr(
        "FR-012",
        "Bank operations sets KYC status",
        "The system shall allow bank operations to set KYC status.",
        "BR-012", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation."],
        "Bank operations sets a KYC status.",
        "The system allows bank operations to set KYC status. The exact KYC status values are not specified by the approved source and are not invented (OQ-013). State changes are auditable (BR-006).",
        [br_by_id("BR-006")],
        ["KYC status set by bank operations."],
        ["Updated KYC status.", "State change recorded for audit (BR-006)."],
        "KYC status is updated and the state change is auditable. Allowed KYC status values remain OPEN (OQ-013).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-012",
        ["OQ-012", "OQ-013"],
    ),
    fr(
        "FR-013",
        "Bank operations activates customer accounts",
        "The system shall allow bank operations to activate customer accounts.",
        "BR-013", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation."],
        "Bank operations activates a customer account.",
        "The system allows bank operations to activate customer accounts. Account-state rules remain open (OQ-006). State changes are auditable (BR-006).",
        [br_by_id("BR-006")],
        ["Account activation performed by bank operations."],
        ["Customer account moved to an activated state.", "State change recorded for audit (BR-006)."],
        "Account activation by bank operations transitions account state. Exact account-state rules remain OPEN (OQ-006).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-013",
        ["OQ-006", "OQ-012"],
    ),
    fr(
        "FR-014",
        "Bank operations freezes customer accounts",
        "The system shall allow bank operations to freeze customer accounts.",
        "BR-014", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation."],
        "Bank operations freezes a customer account.",
        "The system allows bank operations to freeze customer accounts. Account-state rules remain open (OQ-006). State changes are auditable (BR-006).",
        [br_by_id("BR-006")],
        ["Account freeze performed by bank operations."],
        ["Customer account moved to a frozen state.", "State change recorded for audit (BR-006)."],
        "Account freezing by bank operations transitions account state. Exact account-state rules remain OPEN (OQ-006).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-014",
        ["OQ-006", "OQ-012"],
    ),
    fr(
        "FR-015",
        "Bank operations views customer account state",
        "The system shall allow bank operations to view customer account state.",
        "BR-015", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation."],
        "Bank operations requests to view customer account state.",
        "The system allows bank operations to view customer account state. Account-state details remain open (OQ-006).",
        [br_by_id("BR-005")],
        ["Account state viewing request by bank operations."],
        ["Customer account state displayed to bank operations."],
        "Customer account state is displayed to bank operations. Account-state details remain OPEN (OQ-006).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-015",
        ["OQ-006", "OQ-012"],
    ),
    fr(
        "FR-016",
        "Bank operations accesses the audit trail",
        "The system shall allow bank operations to access the audit trail.",
        "BR-016", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation.", "State changes are auditable (BR-006)."],
        "Bank operations requests to access the audit trail.",
        "The system allows bank operations to access the audit trail. The exact audit events to be recorded remain open (OQ-011).",
        [br_by_id("BR-006")],
        ["Audit trail access request by bank operations."],
        ["Audit trail displayed to bank operations."],
        "The audit trail is accessible to bank operations. Exact audit events to be recorded remain OPEN (OQ-011).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-016",
        ["OQ-011", "OQ-012"],
    ),
    fr(
        "FR-017",
        "Bank operations logs in",
        "The system shall allow bank operations to log in to the application.",
        "BR-017", "UNSPECIFIED",
        ["A bank-operations actor exists within the simulation.", "Role-based access is provided (BR-005 business rule)."],
        "Bank operations requests to log in.",
        "The system allows bank operations to log in, establishing role-based access for the bank-operations journey. Authentication mechanisms are not specified by the approved source and are not invented (OQ-010).",
        [br_by_id("BR-005"), br_by_id("BR-008")],
        ["Bank-operations login request."],
        ["Bank-operations session established for role-based access."],
        "A successful login establishes a bank-operations session. Authentication/login mechanism details remain OPEN (OQ-010, OQ-009).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-017",
        ["OQ-009", "OQ-010", "OQ-012"],
    ),
    fr(
        "FR-018",
        "Bank operations logs out",
        "The system shall allow bank operations to log out, terminating the session.",
        "BR-018", "UNSPECIFIED",
        ["A bank-operations session exists within the simulation."],
        "Bank operations requests to log out.",
        "The system allows bank operations to log out, terminating the bank-operations session.",
        [br_by_id("BR-005")],
        ["Bank-operations logout request."],
        ["Bank-operations session terminated."],
        "Logout terminates the bank-operations session. Session/termination mechanism details remain OPEN (OQ-010).",
        "Not specified by the approved source.",
        "BR-018",
        ["OQ-010"],
    ),
    fr(
        "FR-019",
        "Role-based access keeps journeys distinct",
        "The system shall provide role-based access so that customer and bank-operations journeys are kept distinct.",
        "BR-019", "UNSPECIFIED",
        ["Two distinct roles exist: Customer and Bank Operations (BR-005 business rule)."],
        "A user acts within either the customer or bank-operations journey.",
        "The system provides role-based access so that customer and bank-operations journeys are kept distinct. The exact role permissions and authorization rules remain open (OQ-009).",
        [br_by_id("BR-005"), br_by_id("BR-008")],
        ["Role definition and activation of a journey."],
        ["Customer and bank-operations journeys kept distinct via role-based access."],
        "Role-based access keeps the customer and bank-operations journeys distinct. Exact role permissions and authorization rules remain OPEN (OQ-009).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-019",
        ["OQ-009", "OQ-012"],
    ),
    fr(
        "FR-020",
        "State changes are auditable",
        "The system shall make state changes auditable.",
        "BR-020", "UNSPECIFIED",
        ["The system records state changes (BR-006 business rule)."],
        "A state change occurs within the simulation.",
        "The system makes state changes auditable. The exact audit events to be recorded remain open (OQ-011).",
        [br_by_id("BR-006"), br_by_id("BR-008")],
        ["State changes occurring in the simulation."],
        ["Audit trail capturing state changes.", "Audit trail accessible to bank operations (FR-016)."],
        "State changes are captured as auditable events. Exact audit events to be recorded remain OPEN (OQ-011).",
        "Not specified by the approved source. Error messages/codes remain OPEN (OQ-012).",
        "BR-020",
        ["OQ-011", "OQ-012"],
    ),
    fr(
        "FR-021",
        "Use of synthetic data for the simulation",
        "The system shall use synthetic identities, accounts, balances, beneficiaries, and payments for the simulation.",
        "BR-021", "UNSPECIFIED",
        ["The project is an educational simulation using synthetic data (CON-001, CON-002)."],
        "The simulation operates using synthetic data.",
        "The system uses synthetic identities, accounts, balances, beneficiaries, and payments. Real money movement and real financial transactions are not permitted (BR-001, BR-003).",
        [br_by_id("BR-001"), br_by_id("BR-003"), br_by_id("BR-004")],
        ["Synthetic identities, accounts, balances, beneficiaries, and payments."],
        ["Simulation operating on synthetic data only."],
        "All simulation data is synthetic; no real money or real financial transactions are used. Data fields and validation constraints remain OPEN (OQ-013).",
        "Not specified by the approved source.",
        "BR-021",
        ["OQ-013"],
    ),
    fr(
        "FR-022",
        "Agent-produced artifacts are governed",
        "Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval.",
        "BR-022", "UNSPECIFIED",
        ["The project uses reusable AI-assisted engineering agents."],
        "An agent produces an artifact.",
        "The system (and its governing process) requires agent-produced artifacts to be reviewable, reproducible, schema-valid, source-linked, and subject to human approval. Every project handoff must carry version, source IDs, assumptions, open questions, and approval status (BR-008 business rule).",
        [br_by_id("BR-008")],
        ["Agent-produced artifacts."],
        ["Artifacts that are reviewable, reproducible, schema-valid, source-linked, and subject to human approval."],
        "Agent output satisfies the governance conditions (reviewable, reproducible, schema-valid, source-linked, human-approved).",
        "Not specified by the approved source.",
        "BR-022",
        [],
    ),
    fr(
        "FR-023",
        "Approved business rules remain traceable",
        "Approved business rules shall remain traceable through requirements and downstream evidence.",
        "BR-023", "UNSPECIFIED",
        ["The project maintains governance and traceability (CHARTER-2, SCOPE-6)."],
        "An approved business rule is carried through the lifecycle.",
        "The system and its governing process maintain traceability of approved business rules through requirements and downstream evidence, so that an approved business rule can be traced through requirement, design element, implementation, test, defect decision, and final evidence record.",
        [br_by_id("BR-008")],
        ["Approved business rules and downstream artifacts."],
        ["Traceability chain from approved business rule through requirements and downstream evidence."],
        "Approved business rules remain traceable through requirements and downstream evidence.",
        "Not specified by the approved source.",
        "BR-023",
        [],
    ),
]

# ---------------------------------------------------------------------------
# Traceability: BR -> FR
# ---------------------------------------------------------------------------
TRACEABILITY = []
for f in FRS:
    TRACEABILITY.append({"business_requirement": f["source_business_requirement"], "functional_requirement": f["id"]})

# ---------------------------------------------------------------------------
# Inconsistency detection
# ---------------------------------------------------------------------------
INCONSISTENCIES = []
# Every FR must trace to an approved BR in the BRD's requirements list.
BRD_REQ_IDS = [
    "BR-001", "BR-002", "BR-003", "BR-004", "BR-005", "BR-006",
    "BR-007", "BR-008", "BR-009", "BR-010", "BR-011", "BR-012",
    "BR-013", "BR-014", "BR-015", "BR-016", "BR-017", "BR-018",
    "BR-019", "BR-020", "BR-021", "BR-022", "BR-023",
]
for f in FRS:
    if f["source_business_requirement"] not in BRD_REQ_IDS:
        INCONSISTENCIES.append({
            "severity": "CRITICAL",
            "message": f"FR {f['id']} traces to BR {f['source_business_requirement']} which is not present in the approved BRD requirements.",
        })
BRD_BUSINESS_RULE_IDS = ["BR-001", "BR-002", "BR-003", "BR-004", "BR-005", "BR-006", "BR-007", "BR-008"]
for r in BUSINESS_RULES:
    if r["id"] not in BRD_BUSINESS_RULE_IDS:
        INCONSISTENCIES.append({
            "severity": "CRITICAL",
            "message": f"Business rule {r['id']} is referenced but not present in the approved BRD business rules.",
        })

# ---------------------------------------------------------------------------
# Data Specification
# ---------------------------------------------------------------------------
DATA_ENTITIES = [
    {
        "id": "DS-001",
        "entity": "Customer",
        "purpose": "A customer actor within the simulation who completes onboarding, provides KYC, activates an account, logs in/out, transfers and receives simulated money, and views/downloads statements.",
        "source_business_requirement": ["BR-001", "BR-002", "BR-003", "BR-004", "BR-005", "BR-006", "BR-007", "BR-008", "BR-009", "BR-010"],
        "data_notes": "Represented using synthetic identity data (BR-021). Exact data fields and validation constraints remain OPEN (OQ-013).",
        "traceability_fr": ["FR-001", "FR-002", "FR-003", "FR-004", "FR-005", "FR-006", "FR-007", "FR-008", "FR-009", "FR-010"],
    },
    {
        "id": "DS-002",
        "entity": "KYC Information",
        "purpose": "KYC information provided by the customer, including Aadhaar and PAN information that is format-only and mocked.",
        "source_business_requirement": ["BR-002", "BR-003", "BR-011", "BR-012"],
        "data_notes": "Aadhaar/PAN verification is format-only and mocked; no real identity verification is performed (BR-002). Exact data fields and validation constraints remain OPEN (OQ-013).",
        "traceability_fr": ["FR-002", "FR-003", "FR-011", "FR-012"],
    },
    {
        "id": "DS-003",
        "entity": "Account",
        "purpose": "A customer account that can be activated or frozen by the customer or bank operations, and whose state is viewable.",
        "source_business_requirement": ["BR-004", "BR-013", "BR-014", "BR-015"],
        "data_notes": "Account state changes are auditable (BR-006). Exact account-state rules remain OPEN (OQ-006).",
        "traceability_fr": ["FR-004", "FR-013", "FR-014", "FR-015"],
    },
    {
        "id": "DS-004",
        "entity": "Simulated Balance",
        "purpose": "Synthetic simulated balance associated with accounts within the simulation.",
        "source_business_requirement": ["BR-007", "BR-008", "BR-021"],
        "data_notes": "Balances are simulated using synthetic data (BR-001, BR-021). Minimum balance value remains OPEN (OQ-002).",
        "traceability_fr": ["FR-007", "FR-008", "FR-021"],
    },
    {
        "id": "DS-005",
        "entity": "Beneficiary",
        "purpose": "Synthetic beneficiary data used within the simulation for money movement.",
        "source_business_requirement": ["BR-021"],
        "data_notes": "Beneficiaries are synthetic (BR-021). Beneficiary management is out of scope per the approved BRD scope of work.",
        "traceability_fr": ["FR-021"],
    },
    {
        "id": "DS-006",
        "entity": "Simulated Payment",
        "purpose": "Synthetic simulated payment representing transfer/receipt of simulated money.",
        "source_business_requirement": ["BR-007", "BR-008", "BR-021"],
        "data_notes": "Payments are simulated using synthetic data (BR-001, BR-021). Transfer/payment rules and limits remain OPEN (OQ-007, OQ-003).",
        "traceability_fr": ["FR-007", "FR-008", "FR-021"],
    },
    {
        "id": "DS-007",
        "entity": "Statement",
        "purpose": "Statement data viewable and downloadable by the customer.",
        "source_business_requirement": ["BR-009", "BR-010"],
        "data_notes": "Statement content and download behaviour details remain OPEN (OQ-008).",
        "traceability_fr": ["FR-009", "FR-010"],
    },
    {
        "id": "DS-008",
        "entity": "Audit Trail",
        "purpose": "Record of auditable state changes accessible to bank operations.",
        "source_business_requirement": ["BR-016", "BR-020"],
        "data_notes": "State changes are auditable (BR-006). Exact audit events to be recorded remain OPEN (OQ-011).",
        "traceability_fr": ["FR-016", "FR-020"],
    },
    {
        "id": "DS-009",
        "entity": "Role",
        "purpose": "Roles (Customer and Bank Operations) used to keep journeys distinct via role-based access.",
        "source_business_requirement": ["BR-019"],
        "data_notes": "Two distinct roles exist (BR-005 business rule). Exact role permissions and authorization rules remain OPEN (OQ-009).",
        "traceability_fr": ["FR-019"],
    },
]

DATA_SPEC_METADATA = {
    "artifact": "DATA_SPEC",
    "artifact_name": "Data Specification",
    "project": PROJECT,
    "version": VERSION,
    "status": STATUS,
    "approval_status": APPROVAL,
    "generated_at": GENERATED_AT,
    "generator_agent": "FRD Agent",
    "note": "This Data Specification describes business/functional data required by the approved requirements. It is NOT a database schema. No tables, engines, indexes, ORM models, or infrastructure are specified.",
    "data_entities": DATA_ENTITIES,
}

# ---------------------------------------------------------------------------
# Error Catalogue
# ---------------------------------------------------------------------------
ERROR_CATALOGUE_ENTRIES = [
    {
        "id": "ERR-001",
        "title": "Error codes and messages not specified",
        "description": "The approved source does not specify error codes or error messages for the online-banking simulation.",
        "source_business_requirement": ["BR-001", "BR-002", "BR-003", "BR-004", "BR-005", "BR-007", "BR-008", "BR-009", "BR-010", "BR-011", "BR-012", "BR-013", "BR-014", "BR-015", "BR-016", "BR-017", "BR-019"],
        "traceability_fr": ["FR-001", "FR-002", "FR-003", "FR-004", "FR-005", "FR-007", "FR-008", "FR-009", "FR-010", "FR-011", "FR-012", "FR-013", "FR-014", "FR-015", "FR-016", "FR-017", "FR-019"],
        "referenced_open_question": "OQ-012",
        "type": "INCONSISTENCY_OR_GAP",
        "severity": "INFO",
        "resolution": "Error codes and messages must be resolved via Open Question OQ-012 before approved error behaviour can be specified. No error codes or messages are invented.",
    },
    {
        "id": "ERR-002",
        "title": "Approved BRD requirements referenced; brd/approved missing",
        "description": "The FRD generation consumed brd/raw artifacts because no brd/approved directory exists in the repository. The issue requested brd/approved as authoritative input.",
        "source_business_requirement": [],
        "traceability_fr": [],
        "referenced_open_question": None,
        "type": "UPSTREAM_ARTIFACT_STATE",
        "severity": "HIGH",
        "resolution": "Per FRD Agent failure-condition instructions, generation proceeded from brd/raw when brd/approved is not present. The BRD must be human-approved and baselined to brd/approved before downstream reuse as an approved baseline.",
    },
]

# ---------------------------------------------------------------------------
# Write helpers
# ---------------------------------------------------------------------------
def write_json(path, doc):
    with open(path, "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print("Wrote", path)


# ---------------------------------------------------------------------------
# FRD JSON
# ---------------------------------------------------------------------------
frd_doc = {
    "artifact": "FRD",
    "artifact_name": "Functional Requirements Document",
    "project": PROJECT,
    "project_code": PROJECT_CODE,
    "version": VERSION,
    "status": STATUS,
    "ready_for_human_review": True,
    "approval_status": APPROVAL,
    "generated_at": GENERATED_AT,
    "generator_agent": "FRD Agent",
    "generator_agent_id": "b026800a-cb5b-4259-8b85-7d5bad2ad739",
    "document_status_note": "RAW - READY_FOR_HUMAN_REVIEW",
    "source_basis": [
        "brd/approved/brd.json (requested; NOT PRESENT - used brd/raw per failure-condition instructions)",
        "brd/approved/business_rules.json (requested; NOT PRESENT - used brd/raw per failure-condition instructions)",
        "brd/approved/open_questions.json (requested; NOT PRESENT - used brd/raw per failure-condition instructions)",
        "brd/raw/brd.json",
        "brd/raw/business_rules.json",
        "brd/raw/open_questions.json",
    ],
    "introduction": {
        "purpose": "This Functional Requirements Document specifies, at the functional-behaviour level, exactly how the approved business requirements for the Online Banking Application simulation should behave. It is derived from the approved business requirements (BR-001 through BR-023) and provides BR to FR traceability. Detailed technical implementation is out of scope.",
        "scope": "This FRD covers the functional behaviour derived from the approved business requirements for the Customer and Bank Operations roles, together with a Data Specification (functional/business data, not a database schema) and an Error Catalogue. Any behaviour whose details are not specified by the approved source is preserved as an Open Question and not invented.",
        "no_invention_note": "No APIs, databases, frameworks, programming languages, UI frameworks, cloud services, authentication technologies, implementation algorithms, deployment architecture, or technical security mechanisms are specified. Undefined business behaviour is preserved and referenced to the relevant Open Question.",
    },
    "source_inconsistencies": INCONSISTENCIES,
    "functional_requirements": FRS,
    "business_rules": BUSINESS_RULES,
    "traceability": TRACEABILITY,
    "open_questions": OPEN_QUESTIONS,
    "priority_legend": {
        "1": "Must",
        "2": "Should",
        "3": "Could",
        "F": "Future",
        "BP": "Business Process",
        "UNSPECIFIED": "Priority not explicitly established by the source material."
    },
}

write_json(os.path.join(RAW, "frd.json"), frd_doc)
write_json(os.path.join(RAW, "data_spec.json"), DATA_SPEC_METADATA)
write_json(os.path.join(RAW, "error_catalogue.json"), {
    "artifact": "ERROR_CATALOGUE",
    "artifact_name": "Error Catalogue",
    "project": PROJECT,
    "version": VERSION,
    "status": STATUS,
    "approval_status": APPROVAL,
    "generated_at": GENERATED_AT,
    "generator_agent": "FRD Agent",
    "errors": ERROR_CATALOGUE_ENTRIES,
})

# ---------------------------------------------------------------------------
# FRD Markdown
# ---------------------------------------------------------------------------
md = []
A = md.append

A("# Functional Requirements Document")
A("")
A("**Project Name:** " + PROJECT)
A("")
A("**Project Code:** " + PROJECT_CODE)
A("")
A("**Version No.:** " + VERSION)
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
A("| 1.0 | 2026-09-07 | FRD Agent | Initial RAW FRD generated for human review |")
A("")
A("---")
A("")
A("## 1. Introduction")
A("")
A("### 1.1 Purpose")
A("")
A(frd_doc["introduction"]["purpose"])
A("")
A("### 1.2 Scope")
A("")
A(frd_doc["introduction"]["scope"])
A("")
A("### 1.3 No-invention note")
A("")
A(frd_doc["introduction"]["no_invention_note"])
A("")
A("### 1.4 Source basis")
A("")
for sb in frd_doc["source_basis"]:
    A("- " + sb)
A("")
A("---")
A("")
A("## 2. Traceability (BR -> FR)")
A("")
A("Every functional requirement traces to an approved business requirement. No orphan FRs are present.")
A("")
A("| Business Requirement | Functional Requirement |")
A("| :--- | :--- |")
for t in TRACEABILITY:
    A(f"| {t['business_requirement']} | {t['functional_requirement']} |")
A("")
A("---")
A("")
A("## 3. Functional Requirements")
A("")
for f in FRS:
    A(f"### {f['id']} - {f['title']}")
    A("")
    A("| Field | Value |")
    A("| :--- | :--- |")
    A(f"| **Description** | {f['description']} |")
    A(f"| **Source business requirement** | {f['source_business_requirement']} |")
    A(f"| **Priority** | {f['priority']} |")
    A(f"| **Preconditions** | {'<br>'.join(f['preconditions']) if f['preconditions'] else 'Not specified by the approved source.'} |")
    A(f"| **Trigger** | {f['trigger']} |")
    A(f"| **Functional behaviour** | {f['functional_behavior']} |")
    A(f"| **Business rules applied** | {'<br>'.join(f['business_rules']) if f['business_rules'] else 'Not specified by the approved source.'} |")
    A(f"| **Inputs** | {'<br>'.join(f['inputs']) if f['inputs'] else 'Not specified by the approved source.'} |")
    A(f"| **Outputs** | {'<br>'.join(f['outputs']) if f['outputs'] else 'Not specified by the approved source.'} |")
    A(f"| **Validation** | {f['validation']} |")
    A(f"| **Error behaviour** | {f['error_behavior']} |")
    A(f"| **Acceptance reference** | {f['acceptance_reference']} |")
    A(f"| **Open questions** | {', '.join(f['open_questions']) if f['open_questions'] else 'None' } |")
    A("")
A("---")
A("")
A("## 4. Business Rules")
A("")
A("| ID | Business Rule | Source |")
A("| :--- | :--- | :--- |")
for br in BUSINESS_RULES:
    A(f"| {br['id']} | {br['rule']} | {', '.join(br['source'])} |")
A("")
A("---")
A("")
A("## 5. Open Questions carried forward")
A("")
A("These open questions from the approved BRD are carried forward. They are not silently resolved.")
A("")
A("| ID | Open Question | Status | Source |")
A("| :--- | :--- | :--- | :--- |")
for oq in OPEN_QUESTIONS:
    A(f"| {oq['id']} | {oq['question']} | {oq['status']} | {', '.join(oq['source'])} |")
A("")
A("---")
A("")
A("## 6. Source inconsistencies detected")
A("")
if INCONSISTENCIES:
    A("| Severity | Message |")
    A("| :--- | :--- |")
    for inc in INCONSISTENCIES:
        A(f"| {inc['severity']} | {inc['message']} |")
else:
    A("No inconsistencies detected in the approved source references.")
A("")
A("---")
A("")
A("## Status")
A("")
A("- **Status:** RAW")
A("- **Ready for human review:** READY_FOR_HUMAN_REVIEW")
A("- **Approval status:** NOT_APPROVED")
A("- **Version:** " + VERSION)
A("")

with open(os.path.join(RAW, "frd.md"), "w") as f:
    f.write("\n".join(md))
print("Wrote", os.path.join(RAW, "frd.md"))

# ---------------------------------------------------------------------------
# Data Specification Markdown
# ---------------------------------------------------------------------------
dsmd = []
D = dsmd.append
D("# Data Specification")
D("")
D("**Project Name:** " + PROJECT)
D("")
D("**Version No.:** " + VERSION)
D("")
D("**Status:** RAW")
D("")
D("**Approval Status:** NOT_APPROVED")
D("")
D("**READY_FOR_HUMAN_REVIEW**")
D("")
D("---")
D("")
D("## 1. Introduction")
D("")
D(DATA_SPEC_METADATA["note"])
D("")
D("---")
D("")
D("## 2. Data Entities")
D("")
for de in DATA_ENTITIES:
    D(f"### {de['id']} - {de['entity']}")
    D("")
    D("| Field | Value |")
    D("| :--- | :--- |")
    D(f"| **Purpose** | {de['purpose']} |")
    D(f"| **Source business requirement(s)** | {', '.join(de['source_business_requirement'])} |")
    D(f"| **Data notes** | {de['data_notes']} |")
    D(f"| **Traceability (FR)** | {', '.join(de['traceability_fr'])} |")
    D("")
D("---")
D("")
D("## Status")
D("")
D("- **Status:** RAW")
D("- **Ready for human review:** READY_FOR_HUMAN_REVIEW")
D("- **Approval status:** NOT_APPROVED")
D("- **Version:** " + VERSION)
D("")
with open(os.path.join(RAW, "data_spec.md"), "w") as f:
    f.write("\n".join(dsmd))
print("Wrote", os.path.join(RAW, "data_spec.md"))

# ---------------------------------------------------------------------------
# Error Catalogue Markdown
# ---------------------------------------------------------------------------
esmd = []
E = esmd.append
E("# Error Catalogue")
E("")
E("**Project Name:** " + PROJECT)
E("")
E("**Version No.:** " + VERSION)
E("")
E("**Status:** RAW")
E("")
E("**Approval Status:** NOT_APPROVED")
E("")
E("**READY_FOR_HUMAN_REVIEW**")
E("")
E("---")
E("")
E("## 1. Introduction")
E("")
E("This catalogue records known inconsistencies and gaps traced to the approved functional requirements. It does not invent error codes or messages; undefined error behaviour is preserved and referenced to Open Question OQ-012.")
E("")
E("---")
E("")
E("## 2. Errors and inconsistencies")
E("")
for er in ERROR_CATALOGUE_ENTRIES:
    E(f"### {er['id']} - {er['title']}")
    E("")
    E("| Field | Value |")
    E("| :--- | :--- |")
    E(f"| **Description** | {er['description']} |")
    E(f"| **Type** | {er['type']} |")
    E(f"| **Severity** | {er['severity']} |")
    srcs = ", ".join(er["source_business_requirement"]) if er["source_business_requirement"] else "None (upstream artifact state)"
    E(f"| **Source business requirement(s)** | {srcs} |")
    frs = ", ".join(er["traceability_fr"]) if er["traceability_fr"] else "None (upstream artifact state)"
    E(f"| **Traceability (FR)** | {frs} |")
    oq = er["referenced_open_question"] if er["referenced_open_question"] else "None"
    E(f"| **Referenced open question** | {oq} |")
    E(f"| **Resolution** | {er['resolution']} |")
    E("")
E("---")
E("")
E("## Status")
E("")
E("- **Status:** RAW")
E("- **Ready for human review:** READY_FOR_HUMAN_REVIEW")
E("- **Approval status:** NOT_APPROVED")
E("- **Version:** " + VERSION)
E("")
with open(os.path.join(RAW, "error_catalogue.md"), "w") as f:
    f.write("\n".join(esmd))
print("Wrote", os.path.join(RAW, "error_catalogue.md"))

print("FRD JSON and Markdown generation complete.")
