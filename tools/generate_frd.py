#!/usr/bin/env python3
"""
Generate the RAW FRD artifacts for the Online Banking Application.

Single source of truth -> frd.json, frd.md, frd.pdf
                          data_spec.json, data_spec.md, data_spec.pdf
                          error_catalogue.json, error_catalogue.md, error_catalogue.pdf
Uses ReportLab (tools/generate_pdf.py) for PDF generation.
"""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "frd", "raw")
os.makedirs(RAW, exist_ok=True)

GENERATED_AT = "2026-09-07T00:00:00Z"

PROJECT = "Online Banking Application"
PROJECT_CODE = "ONLINE-BANKING"
VERSION = "1.0"
STATUS = "RAW"
APPROVAL_STATUS = "NOT_APPROVED"
READY_FOR_HUMAN_REVIEW = True
GENERATOR_AGENT = "FRD Agent"

SOURCE_BASIS = [
    "brd/raw/brd.json",
    "brd/raw/business_rules.json",
    "brd/raw/open_questions.json",
]

# ---------------------------------------------------------------------------
# Canonical FRD data
# ---------------------------------------------------------------------------

functional_requirements = [
    {
        "id": "FR-001",
        "title": "Customer Completes Onboarding",
        "description": "The system shall allow a customer to complete onboarding.",
        "source_business_requirement": "BR-001",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "A customer exists and has initiated the onboarding journey."
        ],
        "trigger": "The customer initiates onboarding.",
        "functional_behavior": [
            "The system shall make available an onboarding journey to a customer.",
            "The system shall accept the information required for onboarding.",
            "The system shall allow the customer to complete the onboarding journey."
        ],
        "business_rules": [],
        "inputs": [
            "Customer-supplied onboarding information."
        ],
        "outputs": [
            "An onboarding completion state/record for the customer."
        ],
        "validation": [],
        "error_behavior": [
            "If onboarding cannot be completed, the system shall surface a relevant error. Exact error codes and messages are unresolved (see OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-005", "OQ-012", "OQ-013"]
    },
    {
        "id": "FR-002",
        "title": "Customer Provides KYC Information",
        "description": "The system shall allow a customer to provide KYC information.",
        "source_business_requirement": "BR-002",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer is progressing through onboarding."
        ],
        "trigger": "The customer provides KYC information.",
        "functional_behavior": [
            "The system shall accept KYC information from the customer.",
            "KYC information is captured for the simulation; it is not verified against any real authority."
        ],
        "business_rules": [
            "Business rule BR-002 (simulated identity verification; Aadhaar/PAN format-only and mocked).",
            "Constraint CON-003 (format-only, mocked identity verification).",
            "Constraint CON-005 (no external KYC integration)."
        ],
        "inputs": [
            "Customer KYC information."
        ],
        "outputs": [
            "A stored record of the customer's KYC information."
        ],
        "validation": [],
        "error_behavior": [
            "If KYC information cannot be accepted, the system shall surface a relevant error. Exact validation constraints and error text are unresolved (see OQ-012, OQ-013)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-012", "OQ-013"]
    },
    {
        "id": "FR-003",
        "title": "Customer Provides Aadhaar and PAN Information",
        "description": "The system shall allow a customer to provide Aadhaar and PAN information. Verification of Aadhaar/PAN is format-only and mocked.",
        "source_business_requirement": "BR-003",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer is providing KYC information during onboarding."
        ],
        "trigger": "The customer provides Aadhaar and/or PAN information.",
        "functional_behavior": [
            "The system shall accept Aadhaar and PAN information from the customer.",
            "Aadhaar/PAN verification performed by the system, if any, shall be format-only and mocked.",
            "The system shall not perform real identity verification against any external authority."
        ],
        "business_rules": [
            "Business rule BR-002 (Aadhaar/PAN verification is format-only and mocked).",
            "Constraint CON-003 (format-only, mocked identity verification).",
            "Constraint CON-005 (no external KYC integration)."
        ],
        "inputs": [
            "Customer Aadhaar information.",
            "Customer PAN information."
        ],
        "outputs": [
            "A stored record of the customer's Aadhaar/PAN information."
        ],
        "validation": [],
        "error_behavior": [
            "If Aadhaar/PAN information is not in the expected format, the system shall surface a relevant error. Exact format rules and error text are unresolved (see OQ-012, OQ-013)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-012", "OQ-013"]
    },
    {
        "id": "FR-004",
        "title": "Customer Activates an Account",
        "description": "The system shall allow a customer to activate an account.",
        "source_business_requirement": "BR-004",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has an account associated with their profile."
        ],
        "trigger": "The customer, or bank operations on the customer's behalf, initiates account activation.",
        "functional_behavior": [
            "The system shall allow a customer account to be activated.",
            "Account activation shall result in an account state that reflects the activation."
        ],
        "business_rules": [
            "Business rule BR-006 (state changes must be auditable)."
        ],
        "inputs": [
            "Account activation request."
        ],
        "outputs": [
            "An account whose state reflects activation.",
            "An audit record of the state change."
        ],
        "validation": [],
        "error_behavior": [
            "If account activation cannot be performed, the system shall surface a relevant error. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-006", "OQ-012", "OQ-013"]
    },
    {
        "id": "FR-005",
        "title": "Customer Login",
        "description": "The system shall allow a customer to log in.",
        "source_business_requirement": "BR-005",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has a registered identity in the system."
        ],
        "trigger": "The customer initiates login.",
        "functional_behavior": [
            "The system shall allow a customer to log in.",
            "Login shall provide the customer access consistent with role-based access requirements (see FR-019)."
        ],
        "business_rules": [
            "Business rule BR-005 (two distinct roles: Customer and Bank Operations, with role-based access)."
        ],
        "inputs": [
            "Customer login credentials/request."
        ],
        "outputs": [
            "An authenticated customer session."
        ],
        "validation": [],
        "error_behavior": [
            "If login fails, the system shall surface a relevant error. Exact authentication rules and error text are unresolved (see OQ-009, OQ-010, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-009", "OQ-010", "OQ-012"]
    },
    {
        "id": "FR-006",
        "title": "Customer Logout",
        "description": "The system shall allow a customer to log out.",
        "source_business_requirement": "BR-006",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has an active session."
        ],
        "trigger": "The customer initiates logout.",
        "functional_behavior": [
            "The system shall allow a customer to log out.",
            "Logout shall terminate the customer session."
        ],
        "business_rules": [],
        "inputs": [
            "Customer logout request."
        ],
        "outputs": [
            "A terminated customer session."
        ],
        "validation": [],
        "error_behavior": [
            "If logout cannot be completed, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-012"]
    },
    {
        "id": "FR-007",
        "title": "Customer Transfers Simulated Money",
        "description": "The system shall allow a customer to transfer simulated money.",
        "source_business_requirement": "BR-007",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has an active session and an account in a state that permits transfer."
        ],
        "trigger": "The customer initiates a transfer of simulated money.",
        "functional_behavior": [
            "The system shall allow a customer to initiate a transfer of simulated money.",
            "Money movement is simulated using synthetic data; no real money moves."
        ],
        "business_rules": [
            "Business rule BR-001 (money movement is simulated using synthetic data).",
            "Constraint CON-002 (real money movement is not permitted).",
            "Constraint CON-004 (credit decisioning is not permitted).",
            "Constraint CON-005 (no production bank integration or real payment gateways)."
        ],
        "inputs": [
            "Transfer/payment request details."
        ],
        "outputs": [
            "A simulated payment/transfer record and resulting balance change."
        ],
        "validation": [],
        "error_behavior": [
            "If a transfer cannot be completed, the system shall surface a relevant error. Exact transfer/payment rules, limits, and error text are unresolved (see OQ-007, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-007", "OQ-012", "OQ-013"]
    },
    {
        "id": "FR-008",
        "title": "Customer Receives Simulated Money",
        "description": "The system shall allow a customer to receive simulated money.",
        "source_business_requirement": "BR-008",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has an account in a state that permits receipt."
        ],
        "trigger": "Simulated money is received for the customer.",
        "functional_behavior": [
            "The system shall allow a customer to receive simulated money.",
            "Money movement is simulated using synthetic data; no real money moves."
        ],
        "business_rules": [
            "Business rule BR-001 (money movement is simulated using synthetic data).",
            "Constraint CON-002 (real money movement is not permitted).",
            "Constraint CON-005 (no production bank integration or real payment gateways)."
        ],
        "inputs": [
            "Incoming simulated payment/transfer details."
        ],
        "outputs": [
            "A simulated payment/transfer record and resulting balance change."
        ],
        "validation": [],
        "error_behavior": [
            "If receipt cannot be recorded, the system shall surface a relevant error. Exact transfer/payment rules and error text are unresolved (see OQ-007, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-007", "OQ-012"]
    },
    {
        "id": "FR-009",
        "title": "Customer Views Statements",
        "description": "The system shall allow a customer to view statements.",
        "source_business_requirement": "BR-009",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has an active session and an account with statement data."
        ],
        "trigger": "The customer requests to view a statement.",
        "functional_behavior": [
            "The system shall allow a customer to view statements."
        ],
        "business_rules": [
            "Constraint CON-001 (educational simulation, not a production banking system)."
        ],
        "inputs": [
            "Statement-viewing request."
        ],
        "outputs": [
            "A statement presented to the customer."
        ],
        "validation": [],
        "error_behavior": [
            "If a statement cannot be presented, the system shall surface a relevant error. Exact statement content and error text are unresolved (see OQ-008, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-008", "OQ-012"]
    },
    {
        "id": "FR-010",
        "title": "Customer Downloads Statements",
        "description": "The system shall allow a customer to download statements.",
        "source_business_requirement": "BR-010",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The customer has an active session and an account with statement data."
        ],
        "trigger": "The customer requests to download a statement.",
        "functional_behavior": [
            "The system shall allow a customer to download statements."
        ],
        "business_rules": [
            "Constraint CON-001 (educational simulation, not a production banking system)."
        ],
        "inputs": [
            "Statement-download request."
        ],
        "outputs": [
            "A downloadable statement artifact for the customer."
        ],
        "validation": [],
        "error_behavior": [
            "If a statement cannot be downloaded, the system shall surface a relevant error. Exact download behaviour and error text are unresolved (see OQ-008, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-008", "OQ-012"]
    },
    {
        "id": "FR-011",
        "title": "Bank Operations Reviews KYC",
        "description": "The system shall allow bank operations to review KYC information.",
        "source_business_requirement": "BR-011",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session and the required role-based access."
        ],
        "trigger": "Bank operations requests to review a customer's KYC information.",
        "functional_behavior": [
            "The system shall allow bank operations to review KYC information."
        ],
        "business_rules": [
            "Business rule BR-005 (two distinct roles with role-based access)."
        ],
        "inputs": [
            "A KYC review request identifying the customer."
        ],
        "outputs": [
            "KYC information presented to bank operations."
        ],
        "validation": [],
        "error_behavior": [
            "If KYC information cannot be presented, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-009", "OQ-012"]
    },
    {
        "id": "FR-012",
        "title": "Bank Operations Sets KYC Status",
        "description": "The system shall allow bank operations to set KYC status.",
        "source_business_requirement": "BR-012",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session, the required role-based access, and has reviewed the KYC information."
        ],
        "trigger": "Bank operations sets the KYC status for a customer.",
        "functional_behavior": [
            "The system shall allow bank operations to set the KYC status of a customer."
        ],
        "business_rules": [
            "Business rule BR-006 (state changes must be auditable)."
        ],
        "inputs": [
            "A KYC status update for a customer."
        ],
        "outputs": [
            "An updated KYC status for the customer.",
            "An audit record of the state change."
        ],
        "validation": [],
        "error_behavior": [
            "If the KYC status cannot be updated, the system shall surface a relevant error. Exact status values and error text are unresolved (see OQ-012, OQ-013)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-009", "OQ-012", "OQ-013"]
    },
    {
        "id": "FR-013",
        "title": "Bank Operations Activates Customer Accounts",
        "description": "The system shall allow bank operations to activate customer accounts.",
        "source_business_requirement": "BR-013",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session and the required role-based access."
        ],
        "trigger": "Bank operations initiates activation of a customer account.",
        "functional_behavior": [
            "The system shall allow bank operations to activate a customer account."
        ],
        "business_rules": [
            "Business rule BR-006 (state changes must be auditable)."
        ],
        "inputs": [
            "An account-activation request from bank operations."
        ],
        "outputs": [
            "A customer account whose state reflects activation.",
            "An audit record of the state change."
        ],
        "validation": [],
        "error_behavior": [
            "If the account cannot be activated, the system shall surface a relevant error. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-006", "OQ-009", "OQ-012"]
    },
    {
        "id": "FR-014",
        "title": "Bank Operations Freezes Customer Accounts",
        "description": "The system shall allow bank operations to freeze customer accounts.",
        "source_business_requirement": "BR-014",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session and the required role-based access."
        ],
        "trigger": "Bank operations initiates a freeze of a customer account.",
        "functional_behavior": [
            "The system shall allow bank operations to freeze a customer account.",
            "A frozen account shall reflect the frozen state."
        ],
        "business_rules": [
            "Business rule BR-006 (state changes must be auditable)."
        ],
        "inputs": [
            "An account-freeze request from bank operations."
        ],
        "outputs": [
            "A customer account whose state reflects a freeze.",
            "An audit record of the state change."
        ],
        "validation": [],
        "error_behavior": [
            "If the account cannot be frozen, the system shall surface a relevant error. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-006", "OQ-009", "OQ-012"]
    },
    {
        "id": "FR-015",
        "title": "Bank Operations Views Customer Account State",
        "description": "The system shall allow bank operations to view customer account state.",
        "source_business_requirement": "BR-015",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session and the required role-based access."
        ],
        "trigger": "Bank operations requests to view a customer's account state.",
        "functional_behavior": [
            "The system shall allow bank operations to view the state of a customer account."
        ],
        "business_rules": [
            "Business rule BR-005 (two distinct roles with role-based access)."
        ],
        "inputs": [
            "An account-state view request identifying the customer/account."
        ],
        "outputs": [
            "Customer account state presented to bank operations."
        ],
        "validation": [],
        "error_behavior": [
            "If the account state cannot be presented, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-006", "OQ-009", "OQ-012"]
    },
    {
        "id": "FR-016",
        "title": "Bank Operations Accesses the Audit Trail",
        "description": "The system shall allow bank operations to access the audit trail.",
        "source_business_requirement": "BR-016",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session and the required role-based access."
        ],
        "trigger": "Bank operations requests access to the audit trail.",
        "functional_behavior": [
            "The system shall allow bank operations to access the audit trail."
        ],
        "business_rules": [
            "Business rule BR-006 (state changes must be auditable).",
            "Business rule BR-005 (two distinct roles with role-based access)."
        ],
        "inputs": [
            "An audit-trail access request."
        ],
        "outputs": [
            "Audit trail information presented to bank operations."
        ],
        "validation": [],
        "error_behavior": [
            "If the audit trail cannot be accessed, the system shall surface a relevant error. Exact audit events and error text are unresolved (see OQ-011, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-011", "OQ-009", "OQ-012"]
    },
    {
        "id": "FR-017",
        "title": "Bank Operations Login",
        "description": "The system shall allow bank operations to log in.",
        "source_business_requirement": "BR-017",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has a registered identity in the system."
        ],
        "trigger": "Bank operations initiates login.",
        "functional_behavior": [
            "The system shall allow bank operations to log in.",
            "Login shall provide bank operations access consistent with role-based access requirements (see FR-019)."
        ],
        "business_rules": [
            "Business rule BR-005 (two distinct roles: Customer and Bank Operations, with role-based access)."
        ],
        "inputs": [
            "Bank-operations login credentials/request."
        ],
        "outputs": [
            "An authenticated bank-operations session."
        ],
        "validation": [],
        "error_behavior": [
            "If login fails, the system shall surface a relevant error. Exact authentication rules and error text are unresolved (see OQ-009, OQ-010, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-009", "OQ-010", "OQ-012"]
    },
    {
        "id": "FR-018",
        "title": "Bank Operations Logout",
        "description": "The system shall allow bank operations to log out.",
        "source_business_requirement": "BR-018",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "Bank operations has an active session."
        ],
        "trigger": "Bank operations initiates logout.",
        "functional_behavior": [
            "The system shall allow bank operations to log out.",
            "Logout shall terminate the bank-operations session."
        ],
        "business_rules": [],
        "inputs": [
            "Bank-operations logout request."
        ],
        "outputs": [
            "A terminated bank-operations session."
        ],
        "validation": [],
        "error_behavior": [
            "If logout cannot be completed, the system shall surface a relevant error. Exact error text is unresolved (see OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-012"]
    },
    {
        "id": "FR-019",
        "title": "Role-Based Access",
        "description": "The system shall provide role-based access so that customer and bank-operations journeys are kept distinct.",
        "source_business_requirement": "BR-019",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The system has defined roles for Customer and Bank Operations."
        ],
        "trigger": "A user (Customer or Bank Operations) attempts to perform an action in the system.",
        "functional_behavior": [
            "The system shall keep customer and bank-operations journeys distinct through role-based access.",
            "Actions available to a user shall be consistent with the user's role."
        ],
        "business_rules": [
            "Business rule BR-005 (two distinct roles: Customer and Bank Operations, with role-based access)."
        ],
        "inputs": [
            "A user action request carrying role context."
        ],
        "outputs": [
            "Access granted or denied consistent with the user's role."
        ],
        "validation": [],
        "error_behavior": [
            "If a user attempts an action not permitted for their role, the system shall surface a relevant error. Exact role permissions and error text are unresolved (see OQ-009, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-009", "OQ-012"]
    },
    {
        "id": "FR-020",
        "title": "Auditable State Changes",
        "description": "The system shall make state changes auditable.",
        "source_business_requirement": "BR-020",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "A state change occurs in the system."
        ],
        "trigger": "A state change is performed (for example, account activation, account freeze, or KYC status update).",
        "functional_behavior": [
            "The system shall record state changes so that they are auditable."
        ],
        "business_rules": [
            "Business rule BR-006 (state changes in the system must be auditable)."
        ],
        "inputs": [
            "State change event information."
        ],
        "outputs": [
            "An audit record of the state change, accessible via the audit trail (see FR-016)."
        ],
        "validation": [],
        "error_behavior": [
            "If a state change cannot be recorded for audit, the system shall surface a relevant error. Exact audit events and error text are unresolved (see OQ-011, OQ-012)."
        ],
        "acceptance_reference": [],
        "related_open_questions": ["OQ-011", "OQ-012"]
    },
    {
        "id": "FR-021",
        "title": "Synthetic Data Simulation",
        "description": "The system shall use synthetic identities, accounts, balances, beneficiaries, and payments for the simulation.",
        "source_business_requirement": "BR-021",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "The simulation operates with synthetic data."
        ],
        "trigger": "The simulation instantiates identities, accounts, balances, beneficiaries, or payments.",
        "functional_behavior": [
            "The system shall use synthetic identities, accounts, balances, beneficiaries, and payments.",
            "The system shall not use real money, real identity verification, or real banking integration."
        ],
        "business_rules": [
            "Business rule BR-001 (money movement is simulated using synthetic data).",
            "Business rule BR-002 (Aadhaar/PAN verification is format-only and mocked).",
            "Business rule BR-004 (no production bank, real payment gateway, or external KYC integration).",
            "Constraints CON-001 through CON-005."
        ],
        "inputs": [
            "Synthetic simulation data."
        ],
        "outputs": [
            "A coherent simulation populated with synthetic data."
        ],
        "validation": [],
        "error_behavior": [],
        "acceptance_reference": [],
        "related_open_questions": []
    },
    {
        "id": "FR-022",
        "title": "Agent Artifact Quality",
        "description": "Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval.",
        "source_business_requirement": "BR-022",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "An agent produces an artifact."
        ],
        "trigger": "An agent produces or delivers an artifact.",
        "functional_behavior": [
            "Agent-produced artifacts shall be reviewable, reproducible, schema-valid, source-linked, and subject to human approval."
        ],
        "business_rules": [
            "Business rule BR-007 (out-of-scope requirements go through change control).",
            "Business rule BR-008 (each handoff carries version, source IDs, assumptions, open questions, and approval status)."
        ],
        "inputs": [
            "Artifact content and metadata."
        ],
        "outputs": [
            "A reviewable, reproducible, schema-valid, source-linked artifact."
        ],
        "validation": [
            "Artifact is schema-valid.",
            "Artifact is source-linked.",
            "Artifact records version, status, and approval status."
        ],
        "error_behavior": [],
        "acceptance_reference": [],
        "related_open_questions": []
    },
    {
        "id": "FR-023",
        "title": "Requirements Traceability",
        "description": "Approved business rules shall remain traceable through requirements and downstream evidence.",
        "source_business_requirement": "BR-023",
        "priority": "UNSPECIFIED",
        "preconditions": [
            "BRD artifacts record source-to-requirement mappings."
        ],
        "trigger": "Downstream requirements or evidence are produced from business requirements.",
        "functional_behavior": [
            "Approved business rules shall remain traceable through requirements, design, implementation, test, defect decision, and final evidence record."
        ],
        "business_rules": [
            "Business rule BR-008 (every handoff carries version, source IDs, assumptions, open questions, and approval status)."
        ],
        "inputs": [
            "Tracing information linking downstream artifacts to approved business requirements/rules."
        ],
        "outputs": [
            "Traceable downstream artifacts (FRD, UAT, evidence records)."
        ],
        "validation": [
            "Every functional requirement traces to an approved business requirement.",
            "No orphan functional requirements exist.",
            "No unknown business-requirement references exist."
        ],
        "error_behavior": [],
        "acceptance_reference": [],
        "related_open_questions": []
    }
]

# ---------------------------------------------------------------------------
# Canonical Data Specification data
# ---------------------------------------------------------------------------

data_spec_entries = [
    {
        "id": "DS-001",
        "title": "Customer Profile",
        "description": "Business/functional identity data for a customer using the simulation.",
        "purpose": "Supports onboarding and identifies the customer across journeys.",
        "related_frs": ["FR-001"],
        "notes": "Exact fields and validation constraints are unresolved (see OQ-013). Identity data is synthetic (see FR-021)."
    },
    {
        "id": "DS-002",
        "title": "KYC Information",
        "description": "KYC information supplied by the customer during onboarding.",
        "purpose": "Supports KYC capture and bank-operations review (see FR-002, FR-011, FR-012).",
        "related_frs": ["FR-002", "FR-011", "FR-012"],
        "notes": "KYC is captured for the simulation and is subject to no real verification (constraint CON-003). Exact fields and validation constraints are unresolved (see OQ-013)."
    },
    {
        "id": "DS-003",
        "title": "Aadhaar/PAN Information",
        "description": "Aadhaar and PAN details provided by the customer, verified format-only and mocked.",
        "purpose": "Supports capture of Aadhaar/PAN details without real identity verification.",
        "related_frs": ["FR-003"],
        "notes": "Verification is format-only and mocked (CON-003, business rule BR-002). Exact fields and format rules are unresolved (see OQ-013)."
    },
    {
        "id": "DS-004",
        "title": "Account Data",
        "description": "Customer account information used in the simulation.",
        "purpose": "Supports account activation, transfers, and statement journeys.",
        "related_frs": ["FR-004", "FR-007", "FR-008", "FR-009", "FR-010", "FR-013", "FR-014", "FR-015"],
        "notes": "Accounts are synthetic (see FR-021). Exact account data fields and account-state rules are unresolved (see OQ-006, OQ-013)."
    },
    {
        "id": "DS-005",
        "title": "Account State",
        "description": "The state of a customer account (for example, active or frozen) as used by bank operations and customers.",
        "purpose": "Supports account activation/freezing, transfers, and state visibility.",
        "related_frs": ["FR-004", "FR-007", "FR-008", "FR-013", "FR-014", "FR-015", "FR-020"],
        "notes": "Exact account-state values and rules are unresolved (see OQ-006). State changes must be auditable (see FR-020)."
    },
    {
        "id": "DS-006",
        "title": "Balance Data",
        "description": "Synthetic balance information associated with a customer account.",
        "purpose": "Supports simulated transfer and receipt of money and balance visibility.",
        "related_frs": ["FR-007", "FR-008"],
        "notes": "Balances are synthetic (see FR-021). Minimum balance and transfer-related limits are unresolved (see OQ-002, OQ-007)."
    },
    {
        "id": "DS-007",
        "title": "Beneficiary Data",
        "description": "Beneficiary information used in the simulation.",
        "purpose": "Supports transfer of simulated money.",
        "related_frs": ["FR-007", "FR-021"],
        "notes": "Beneficiaries are synthetic (see FR-021). Beneficiary management itself is out of scope per the BRD; only the synthetic data used by the simulation is described."
    },
    {
        "id": "DS-008",
        "title": "Payment/Transfer Data",
        "description": "Records of simulated payments/transfers of money.",
        "purpose": "Supports transfer and receipt of simulated money and statement generation.",
        "related_frs": ["FR-007", "FR-008", "FR-009", "FR-010", "FR-021"],
        "notes": "Payments are synthetic (see FR-021); real money movement is not permitted (CON-002). Exact transfer/payment rules and limits are unresolved (see OQ-007, OQ-013)."
    },
    {
        "id": "DS-009",
        "title": "Statement Data",
        "description": "Data needed to present and download customer statements.",
        "purpose": "Supports customer statement viewing and download.",
        "related_frs": ["FR-009", "FR-010"],
        "notes": "Exact statement content and download behaviour are unresolved (see OQ-008)."
    },
    {
        "id": "DS-010",
        "title": "Role and Access Data",
        "description": "Data representing the two roles (Customer and Bank Operations) and the actions permitted per role.",
        "purpose": "Supports role-based access requirements.",
        "related_frs": ["FR-005", "FR-011", "FR-017", "FR-019"],
        "notes": "Exact role permissions and authorization rules are unresolved (see OQ-009)."
    },
    {
        "id": "DS-011",
        "title": "Audit Trail Data",
        "description": "Records of auditable state changes in the simulation.",
        "purpose": "Supports auditable state changes and bank-operations access to the audit trail.",
        "related_frs": ["FR-016", "FR-020"],
        "notes": "Exact audit events to be recorded are unresolved (see OQ-011)."
    },
    {
        "id": "DS-012",
        "title": "Session Data",
        "description": "Data representing an authenticated session for a Customer or Bank Operations user.",
        "purpose": "Supports login, logout, and role-based access.",
        "related_frs": ["FR-005", "FR-006", "FR-017", "FR-018", "FR-019"],
        "notes": "Exact authentication and session rules are unresolved (see OQ-009, OQ-010)."
    }
]

# ---------------------------------------------------------------------------
# Canonical Error Catalogue data
# ---------------------------------------------------------------------------

error_catalogue_entries = [
    {
        "id": "ERR-001",
        "title": "Onboarding cannot be completed",
        "description": "A customer is unable to complete the onboarding journey.",
        "related_fr": "FR-001",
        "source_business_requirement": "BR-001",
        "severity": "UNSPECIFIED",
        "condition": "Onboarding cannot be completed or accepted by the system.",
        "expected_behavior": "The system shall surface a relevant error to the customer.",
        "notes": "Exact error codes/messages are unresolved (see OQ-012); exact onboarding workflow and validation rules are unresolved (see OQ-005)."
    },
    {
        "id": "ERR-002",
        "title": "KYC information cannot be accepted",
        "description": "KYC information provided by a customer cannot be accepted.",
        "related_fr": "FR-002",
        "source_business_requirement": "BR-002",
        "severity": "UNSPECIFIED",
        "condition": "KYC information cannot be accepted or recorded.",
        "expected_behavior": "The system shall surface a relevant error to the customer.",
        "notes": "Exact validation constraints and error text are unresolved (see OQ-012, OQ-013)."
    },
    {
        "id": "ERR-003",
        "title": "Aadhaar/PAN information fails format validation",
        "description": "Aadhaar/PAN information provided by a customer does not conform to the expected format.",
        "related_fr": "FR-003",
        "source_business_requirement": "BR-003",
        "severity": "UNSPECIFIED",
        "condition": "Aadhaar/PAN information fails format-only, mocked validation.",
        "expected_behavior": "The system shall surface a relevant error to the customer.",
        "notes": "Format is format-only and mocked (CON-003). Exact format rules and error text are unresolved (see OQ-012, OQ-013)."
    },
    {
        "id": "ERR-004",
        "title": "Account activation cannot be performed",
        "description": "A customer account cannot be activated.",
        "related_fr": "FR-004",
        "source_business_requirement": "BR-004",
        "severity": "UNSPECIFIED",
        "condition": "Account activation fails or is not permitted.",
        "expected_behavior": "The system shall surface a relevant error to the requesting user.",
        "notes": "Exact account-state rules and error text are unresolved (see OQ-006, OQ-012)."
    },
    {
        "id": "ERR-005",
        "title": "Customer login fails",
        "description": "A customer cannot log in.",
        "related_fr": "FR-005",
        "source_business_requirement": "BR-005",
        "severity": "UNSPECIFIED",
        "condition": "Customer login fails, including invalid credentials or unauthorized access.",
        "expected_behavior": "The system shall surface a relevant error to the customer.",
        "notes": "Exact authentication and authorization rules and error text are unresolved (see OQ-009, OQ-010, OQ-012)."
    },
    {
        "id": "ERR-006",
        "title": "Transfer of simulated money cannot be completed",
        "description": "A customer cannot complete a transfer of simulated money.",
        "related_fr": "FR-007",
        "source_business_requirement": "BR-007",
        "severity": "UNSPECIFIED",
        "condition": "A simulated transfer cannot be completed (for example, blocked by account state or unresolved limits).",
        "expected_behavior": "The system shall surface a relevant error to the customer.",
        "notes": "Exact transfer/payment rules and limits are unresolved (see OQ-007, OQ-012). Minimum balance and daily caps are open (see OQ-002, OQ-003)."
    },
    {
        "id": "ERR-007",
        "title": "Receipt of simulated money cannot be recorded",
        "description": "Incoming simulated money cannot be recorded for a customer.",
        "related_fr": "FR-008",
        "source_business_requirement": "BR-008",
        "severity": "UNSPECIFIED",
        "condition": "A simulated receipt cannot be recorded.",
        "expected_behavior": "The system shall surface a relevant error.",
        "notes": "Exact transfer/payment rules and error text are unresolved (see OQ-007, OQ-012)."
    },
    {
        "id": "ERR-008",
        "title": "Statement cannot be presented or downloaded",
        "description": "A customer cannot view or download a statement.",
        "related_fr": "FR-009",
        "source_business_requirement": "BR-009",
        "severity": "UNSPECIFIED",
        "condition": "A statement cannot be presented or downloaded.",
        "expected_behavior": "The system shall surface a relevant error to the customer.",
        "notes": "Statement content/download behaviour is unresolved (see OQ-008); error text is unresolved (see OQ-012). Relates to FR-010 for download behaviour."
    },
    {
        "id": "ERR-009",
        "title": "KYC review or status update fails",
        "description": "Bank operations cannot review KYC or set KYC status.",
        "related_fr": "FR-012",
        "source_business_requirement": "BR-012",
        "severity": "UNSPECIFIED",
        "condition": "KYC review fails or a KYC status update cannot be recorded.",
        "expected_behavior": "The system shall surface a relevant error to bank operations.",
        "notes": "See also FR-011 for KYC review. Exact status values and error text are unresolved (see OQ-012, OQ-013)."
    },
    {
        "id": "ERR-010",
        "title": "Account activation or freeze fails",
        "description": "Bank operations cannot activate or freeze a customer account.",
        "related_fr": "FR-013",
        "source_business_requirement": "BR-013",
        "severity": "UNSPECIFIED",
        "condition": "An account activation or freeze cannot be performed.",
        "expected_behavior": "The system shall surface a relevant error to bank operations.",
        "notes": "See also FR-014 for account freeze. Exact account-state rules and error text are unresolved (see OQ-006, OQ-012)."
    },
    {
        "id": "ERR-011",
        "title": "Customer account state cannot be viewed",
        "description": "Bank operations cannot view a customer account's state.",
        "related_fr": "FR-015",
        "source_business_requirement": "BR-015",
        "severity": "UNSPECIFIED",
        "condition": "Account state cannot be presented to bank operations.",
        "expected_behavior": "The system shall surface a relevant error to bank operations.",
        "notes": "Exact error text is unresolved (see OQ-012)."
    },
    {
        "id": "ERR-012",
        "title": "Audit trail access fails",
        "description": "Bank operations cannot access the audit trail.",
        "related_fr": "FR-016",
        "source_business_requirement": "BR-016",
        "severity": "UNSPECIFIED",
        "condition": "The audit trail cannot be accessed or returned.",
        "expected_behavior": "The system shall surface a relevant error to bank operations.",
        "notes": "Exact audit events are unresolved (see OQ-011); error text is unresolved (see OQ-012)."
    },
    {
        "id": "ERR-013",
        "title": "Bank-operations login fails",
        "description": "Bank operations cannot log in.",
        "related_fr": "FR-017",
        "source_business_requirement": "BR-017",
        "severity": "UNSPECIFIED",
        "condition": "Bank-operations login fails, including invalid credentials or unauthorized access.",
        "expected_behavior": "The system shall surface a relevant error to bank operations.",
        "notes": "Exact authentication and authorization rules and error text are unresolved (see OQ-009, OQ-010, OQ-012)."
    },
    {
        "id": "ERR-014",
        "title": "Action not permitted by role",
        "description": "A user attempts an action that is not permitted for their role.",
        "related_fr": "FR-019",
        "source_business_requirement": "BR-019",
        "severity": "UNSPECIFIED",
        "condition": "A user requests an action inconsistent with their role's permissions.",
        "expected_behavior": "The system shall deny the action and surface a relevant error.",
        "notes": "Exact role permissions and authorization rules are unresolved (see OQ-009); error text is unresolved (see OQ-012)."
    },
    {
        "id": "ERR-015",
        "title": "State change cannot be recorded for audit",
        "description": "A state change cannot be recorded as an auditable event.",
        "related_fr": "FR-020",
        "source_business_requirement": "BR-020",
        "severity": "UNSPECIFIED",
        "condition": "An auditable state change cannot be recorded.",
        "expected_behavior": "The system shall surface a relevant error and preserve auditable state-change behaviour.",
        "notes": "Exact audit events are unresolved (see OQ-011); error text is unresolved (see OQ-012)."
    },
    {
        "id": "ERR-016",
        "title": "Logout cannot be completed",
        "description": "A customer or bank-operations user cannot log out.",
        "related_fr": "FR-006",
        "source_business_requirement": "BR-006",
        "severity": "UNSPECIFIED",
        "condition": "Session termination cannot be completed for a customer or bank-operations user.",
        "expected_behavior": "The system shall surface a relevant error.",
        "notes": "Applies to FR-006 (customer) and FR-018 (bank operations). Exact error text is unresolved (see OQ-012)."
    }
]

# ---------------------------------------------------------------------------
# Consistency notes / detected issues
# ---------------------------------------------------------------------------

consistency_notes = [
    "The BRD business-rule artifact and the BRD document both use the ID prefix BR- for business rules (BR-001..BR-008), which is distinct from but identical-in-prefix to the business-requirement IDs (BR-001..BR-023). The convention is preserved verbatim from the approved source; no rewrite was made.",
    "All open questions OQ-001 through OQ-013 are carried forward from the BRD; none were silently resolved.",
    "ERR-016 intentionally traces to FR-006 (source BR-006, customer logout), which is noted because it also covers FR-018 (bank-operations logout). This is an explicit consistency note, not an invented requirement.",
    "No missing FR references were detected in the approved source material."
]

# ---------------------------------------------------------------------------
# Metadata block
# ---------------------------------------------------------------------------

def metadata(artifact_name):
    return {
        "project": PROJECT,
        "project_code": PROJECT_CODE,
        "artifact": artifact_name,
        "version": VERSION,
        "status": STATUS,
        "ready_for_human_review": READY_FOR_HUMAN_REVIEW,
        "approval_status": APPROVAL_STATUS,
        "generated_at": GENERATED_AT,
        "generator_agent": GENERATOR_AGENT,
        "source_basis": SOURCE_BASIS
    }


def build_frd_document():
    doc = metadata("FRD")
    doc["artifact_name"] = "Functional Requirements Document"
    doc["document_status_note"] = "RAW - READY_FOR_HUMAN_REVIEW"
    doc["introduction"] = {
        "purpose": "This Functional Requirements Document (FRD) translates the approved business requirements of the Online Banking Application into precise, testable functional requirements. It is derived exclusively from the RAW BRD artifacts and maintains BR-to-FR traceability.",
        "scope": "This FRD covers the functional behaviour required by BR-001 through BR-023. It does not prescribe technical implementation: it names no APIs, databases, authentication mechanisms, or infrastructure.",
        "audience": [
            "Architecture and Development teams",
            "Quality Assurance and Testing teams",
            "UAT teams",
            "Defect Root Cause Analysis teams",
            "Human reviewers and approvers of functional requirements"
        ]
    }
    doc["requirements"] = functional_requirements
    doc["traceability"] = [
        {"business_requirement": fr["source_business_requirement"], "functional_requirement": fr["id"]}
        for fr in functional_requirements
    ]
    doc["traceability_matrix"] = {
        "BR-001": ["FR-001"],
        "BR-002": ["FR-002"],
        "BR-003": ["FR-003"],
        "BR-004": ["FR-004"],
        "BR-005": ["FR-005"],
        "BR-006": ["FR-006"],
        "BR-007": ["FR-007"],
        "BR-008": ["FR-008"],
        "BR-009": ["FR-009"],
        "BR-010": ["FR-010"],
        "BR-011": ["FR-011"],
        "BR-012": ["FR-012"],
        "BR-013": ["FR-013"],
        "BR-014": ["FR-014"],
        "BR-015": ["FR-015"],
        "BR-016": ["FR-016"],
        "BR-017": ["FR-017"],
        "BR-018": ["FR-018"],
        "BR-019": ["FR-019"],
        "BR-020": ["FR-020"],
        "BR-021": ["FR-021"],
        "BR-022": ["FR-022"],
        "BR-023": ["FR-023"]
    }
    doc["carried_forward_open_questions"] = [
        {
            "id": oq["id"],
            "question": oq["question"],
            "status": oq["status"],
            "source": oq["source"]
        }
        for oq in open_questions_list
    ]
    doc["consistency_notes"] = consistency_notes
    doc["status"] = STATUS
    doc["approval_status"] = APPROVAL_STATUS
    doc["version"] = VERSION
    return doc


def build_data_spec_document():
    doc = metadata("DATA_SPEC")
    doc["artifact_name"] = "Data Specification"
    doc["document_status_note"] = "RAW - READY_FOR_HUMAN_REVIEW"
    doc["introduction"] = {
        "purpose": "This Data Specification describes the business/functional data used by the Online Banking Application as required by the FRD.",
        "scope": "This specification is not a database schema. It describes functional/business data and names no tables, columns, indexes, databases, or implementation architecture.",
        "audience": [
            "Architecture and Development teams",
            "Quality Assurance and Testing teams",
            "Human reviewers and approvers of functional requirements"
        ]
    }
    doc["data_entries"] = data_spec_entries
    doc["related_fr_coverage"] = {}
    for entry in data_spec_entries:
        for fr in entry["related_frs"]:
            doc["related_fr_coverage"].setdefault(fr, []).append(entry["id"])
    doc["status"] = STATUS
    doc["approval_status"] = APPROVAL_STATUS
    doc["version"] = VERSION
    return doc


def build_error_catalogue_document():
    doc = metadata("ERROR_CATALOGUE")
    doc["artifact_name"] = "Error Catalogue"
    doc["document_status_note"] = "RAW - READY_FOR_HUMAN_REVIEW"
    doc["introduction"] = {
        "purpose": "This Error Catalogue documents validation and business errors derived from the FRD and the underlying BRD.",
        "scope": "Each error traces to a functional requirement and, through it, to a business requirement. Exact error codes and messages are treated as unresolved because the source material leaves them open (OQ-012).",
        "audience": [
            "Architecture and Development teams",
            "Quality Assurance and Testing teams",
            "Defect Root Cause Analysis teams",
            "Human reviewers and approvers of functional requirements"
        ]
    }
    doc["errors"] = error_catalogue_entries
    doc["traceability"] = [
        {
            "error": e["id"],
            "functional_requirement": e["related_fr"],
            "business_requirement": e["source_business_requirement"]
        }
        for e in error_catalogue_entries
    ]
    doc["consistency_notes"] = consistency_notes
    doc["status"] = STATUS
    doc["approval_status"] = APPROVAL_STATUS
    doc["version"] = VERSION
    return doc


# Open questions carried from BRD
open_questions_list = [
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
    {"id": "OQ-013", "question": "What are the data fields and validation constraints?", "status": "OPEN", "source": ["SCOPE-7"]}
]


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def md_frd():
    lines = []
    m = build_frd_document()
    lines.append("# Functional Requirements Document")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- **Project:** {m['project']}")
    lines.append(f"- **Project Code:** {m['project_code']}")
    lines.append(f"- **Artifact:** {m['artifact_name']}")
    lines.append(f"- **Version:** {m['version']}")
    lines.append(f"- **Status:** {m['status']}")
    lines.append(f"- **Approval Status:** {m['approval_status']}")
    lines.append(f"- **Generated At:** {m['generated_at']}")
    lines.append(f"- **Generator Agent:** {m['generator_agent']}")
    lines.append(f"- **Document Status:** RAW - READY_FOR_HUMAN_REVIEW")
    lines.append(f"- **Source Basis:** {', '.join(m['source_basis'])}")
    lines.append("")
    lines.append("## Introduction")
    lines.append("")
    lines.append(m["introduction"]["purpose"])
    lines.append("")
    lines.append(m["introduction"]["scope"])
    lines.append("")
    lines.append("**Audience:** " + ", ".join(m["introduction"]["audience"]))
    lines.append("")
    lines.append("## Functional Requirements")
    lines.append("")
    for fr in m["requirements"]:
        lines.append(f"### {fr['id']} — {fr['title']}")
        lines.append("")
        lines.append(f"**Description:** {fr['description']}")
        lines.append("")
        lines.append(f"**Source Business Requirement:** {fr['source_business_requirement']}")
        lines.append("")
        lines.append(f"**Priority:** {fr['priority']}")
        lines.append("")
        if fr["preconditions"]:
            lines.append("**Preconditions:**")
            for p in fr["preconditions"]:
                lines.append(f"- {p}")
            lines.append("")
        if fr["trigger"]:
            lines.append(f"**Trigger:** {fr['trigger']}")
            lines.append("")
        if fr["functional_behavior"]:
            lines.append("**Functional Behavior:**")
            for b in fr["functional_behavior"]:
                lines.append(f"- {b}")
            lines.append("")
        if fr["business_rules"]:
            lines.append("**Business Rules / Constraints:**")
            for b in fr["business_rules"]:
                lines.append(f"- {b}")
            lines.append("")
        if fr["inputs"]:
            lines.append("**Inputs:**")
            for i in fr["inputs"]:
                lines.append(f"- {i}")
            lines.append("")
        if fr["outputs"]:
            lines.append("**Outputs:**")
            for o in fr["outputs"]:
                lines.append(f"- {o}")
            lines.append("")
        if fr["validation"]:
            lines.append("**Validation:**")
            for v in fr["validation"]:
                lines.append(f"- {v}")
            lines.append("")
        if fr["error_behavior"]:
            lines.append("**Error Behavior:**")
            for e in fr["error_behavior"]:
                lines.append(f"- {e}")
            lines.append("")
        if fr.get("related_open_questions"):
            lines.append("**Related Open Questions:** " + ", ".join(fr["related_open_questions"]))
            lines.append("")
    lines.append("## BR -> FR Traceability")
    lines.append("")
    lines.append("| Business Requirement | Functional Requirement |")
    lines.append("|---|---|")
    for t in m["traceability"]:
        lines.append(f"| {t['business_requirement']} | {t['functional_requirement']} |")
    lines.append("")
    lines.append("## Carried-Forward Open Questions")
    lines.append("")
    lines.append("| ID | Question | Status | Source |")
    lines.append("|---|---|---|---|")
    for oq in m["carried_forward_open_questions"]:
        src = ", ".join(oq["source"])
        lines.append(f"| {oq['id']} | {oq['question']} | {oq['status']} | {src} |")
    lines.append("")
    lines.append("## Consistency Notes")
    lines.append("")
    for note in m["consistency_notes"]:
        lines.append(f"- {note}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**Version:** 1.0 | **Status:** RAW | **Approval Status:** NOT_APPROVED | **READY_FOR_HUMAN_REVIEW**")
    lines.append("")
    return "\n".join(lines)


def md_data_spec():
    lines = []
    m = build_data_spec_document()
    lines.append("# Data Specification")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- **Project:** {m['project']}")
    lines.append(f"- **Project Code:** {m['project_code']}")
    lines.append(f"- **Artifact:** {m['artifact_name']}")
    lines.append(f"- **Version:** {m['version']}")
    lines.append(f"- **Status:** {m['status']}")
    lines.append(f"- **Approval Status:** {m['approval_status']}")
    lines.append(f"- **Generated At:** {m['generated_at']}")
    lines.append(f"- **Generator Agent:** {m['generator_agent']}")
    lines.append(f"- **Document Status:** RAW - READY_FOR_HUMAN_REVIEW")
    lines.append(f"- **Source Basis:** {', '.join(m['source_basis'])}")
    lines.append("")
    lines.append("## Introduction")
    lines.append("")
    lines.append(m["introduction"]["purpose"])
    lines.append("")
    lines.append(m["introduction"]["scope"])
    lines.append("")
    lines.append("**Audience:** " + ", ".join(m["introduction"]["audience"]))
    lines.append("")
    lines.append("## Data Entries")
    lines.append("")
    for d in m["data_entries"]:
        lines.append(f"### {d['id']} — {d['title']}")
        lines.append("")
        lines.append(f"**Description:** {d['description']}")
        lines.append("")
        lines.append(f"**Purpose:** {d['purpose']}")
        lines.append("")
        lines.append("**Related Functional Requirements:** " + ", ".join(d["related_frs"]))
        lines.append("")
        lines.append(f"**Notes:** {d['notes']}")
        lines.append("")
    lines.append("## Related FR Coverage")
    lines.append("")
    lines.append("| Functional Requirement | Data Entries |")
    lines.append("|---|---|")
    for fr in sorted(m["related_fr_coverage"].keys()):
        lines.append(f"| {fr} | {', '.join(m['related_fr_coverage'][fr])} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**Version:** 1.0 | **Status:** RAW | **Approval Status:** NOT_APPROVED | **READY_FOR_HUMAN_REVIEW**")
    lines.append("")
    return "\n".join(lines)


def md_error_catalogue():
    lines = []
    m = build_error_catalogue_document()
    lines.append("# Error Catalogue")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- **Project:** {m['project']}")
    lines.append(f"- **Project Code:** {m['project_code']}")
    lines.append(f"- **Artifact:** {m['artifact_name']}")
    lines.append(f"- **Version:** {m['version']}")
    lines.append(f"- **Status:** {m['status']}")
    lines.append(f"- **Approval Status:** {m['approval_status']}")
    lines.append(f"- **Generated At:** {m['generated_at']}")
    lines.append(f"- **Generator Agent:** {m['generator_agent']}")
    lines.append(f"- **Document Status:** RAW - READY_FOR_HUMAN_REVIEW")
    lines.append(f"- **Source Basis:** {', '.join(m['source_basis'])}")
    lines.append("")
    lines.append("## Introduction")
    lines.append("")
    lines.append(m["introduction"]["purpose"])
    lines.append("")
    lines.append(m["introduction"]["scope"])
    lines.append("")
    lines.append("**Audience:** " + ", ".join(m["introduction"]["audience"]))
    lines.append("")
    lines.append("## Errors")
    lines.append("")
    for e in m["errors"]:
        lines.append(f"### {e['id']} — {e['title']}")
        lines.append("")
        lines.append(f"**Description:** {e['description']}")
        lines.append("")
        lines.append(f"**Related Functional Requirement:** {e['related_fr']}")
        lines.append("")
        lines.append(f"**Source Business Requirement:** {e['source_business_requirement']}")
        lines.append("")
        lines.append(f"**Severity:** {e['severity']}")
        lines.append("")
        lines.append(f"**Condition:** {e['condition']}")
        lines.append("")
        lines.append(f"**Expected Behavior:** {e['expected_behavior']}")
        lines.append("")
        lines.append(f"**Notes:** {e['notes']}")
        lines.append("")
    lines.append("## Error Traceability")
    lines.append("")
    lines.append("| Error | Functional Requirement | Business Requirement |")
    lines.append("|---|---|---|")
    for t in m["traceability"]:
        lines.append(f"| {t['error']} | {t['functional_requirement']} | {t['business_requirement']} |")
    lines.append("")
    lines.append("## Consistency Notes")
    lines.append("")
    for note in m["consistency_notes"]:
        lines.append(f"- {note}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**Version:** 1.0 | **Status:** RAW | **Approval Status:** NOT_APPROVED | **READY_FOR_HUMAN_REVIEW**")
    lines.append("")
    return "\n".join(lines)


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"Wrote {path}")


def generate_pdfs():
    pdf_helper = os.path.join(BASE, "tools", "generate_pdf.py")
    jobs = [
        ("frd", "Functional Requirements Document"),
        ("data_spec", "Data Specification"),
        ("error_catalogue", "Error Catalogue"),
    ]
    for stem, title in jobs:
        md_path = os.path.join(RAW, f"{stem}.md")
        pdf_path = os.path.join(RAW, f"{stem}.pdf")
        subprocess.run(
            [sys.executable, pdf_helper, md_path, pdf_path, f"ONLINE BANKING APPLICATION — {title}", VERSION, STATUS],
            check=True,
        )


def main():
    frd_doc = build_frd_document()
    data_spec_doc = build_data_spec_document()
    err_cat_doc = build_error_catalogue_document()

    write_file(os.path.join(RAW, "frd.json"), json.dumps(frd_doc, indent=2, ensure_ascii=False) + "\n")
    write_file(os.path.join(RAW, "data_spec.json"), json.dumps(data_spec_doc, indent=2, ensure_ascii=False) + "\n")
    write_file(os.path.join(RAW, "error_catalogue.json"), json.dumps(err_cat_doc, indent=2, ensure_ascii=False) + "\n")

    write_file(os.path.join(RAW, "frd.md"), md_frd())
    write_file(os.path.join(RAW, "data_spec.md"), md_data_spec())
    write_file(os.path.join(RAW, "error_catalogue.md"), md_error_catalogue())

    generate_pdfs()


if __name__ == "__main__":
    main()