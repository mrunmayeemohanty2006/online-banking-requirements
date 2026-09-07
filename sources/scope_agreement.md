# Scope Agreement — Online Banking Student Development Project

## Document Status
- Status: DRAFT — for human review
- Source basis: Project2_Online_Banking_Student_Development_Project.docx
- Business Analysis group: Ritu & Team (Group 2)

## 1. Purpose
This scope agreement establishes the business-analysis scope for the Online Banking Application educational simulation and defines the boundaries that downstream BRD, FRD, and UAT work must respect.

## 2. In-Scope Business Areas
The source states that customers expect secure digital access to the following areas:

1. Onboarding
2. Accounts
3. Beneficiaries
4. Transfers
5. Statements
6. Notifications
7. Service requests

These areas are treated as candidate in-scope business capabilities for requirements analysis, subject to detailed requirement confirmation and human approval.

## 3. Users / Personas
The source explicitly identifies:
- Customers
- Bank-operations journeys

Detailed role permissions and authorization rules are not specified in the source and must not be invented.

## 4. Simulation Data and Behaviour
The simulation is expected to use synthetic:
- identities
- accounts
- balances
- beneficiaries
- payments

The project is an educational simulation and is not a production banking system.

## 5. Explicitly Out of Scope / Prohibited
The project premise explicitly prohibits:
- real money
- real identity verification
- credit decisioning
- production bank integration

No downstream requirement, design, test case, or implementation should introduce these capabilities.

## 6. Traceability and Governance Scope
Business analysis must preserve:
- source IDs
- assumptions
- open questions
- approval status
- version information

Approved business rules must remain traceable through requirements and downstream evidence.

## 7. Scope Interpretation Rules
The following must be treated as unresolved until confirmed:
- exact onboarding workflow and validation rules
- exact account operations and account-state rules
- beneficiary management rules
- transfer/payment rules and limits
- statement content and download behaviour
- notification triggers and channels
- service-request types and workflows
- exact role permissions
- detailed security/privacy/accessibility requirements
- exact audit events
- error codes and error messages
- data fields and validation constraints
- acceptance/sign-off ownership

Any missing or ambiguous detail must become an open question rather than being inferred.

## 8. Change Control
Any requirement outside the approved scope must be handled through the project's change-control process rather than being silently added to the baseline.
