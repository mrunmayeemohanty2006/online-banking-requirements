# Error Catalogue

**Project Name:** Online Banking Application

**Version No.:** 1.0

**Status:** RAW

**Approval Status:** NOT_APPROVED

**READY_FOR_HUMAN_REVIEW**

---

## 1. Introduction

This catalogue records known inconsistencies and gaps traced to the approved functional requirements. It does not invent error codes or messages; undefined error behaviour is preserved and referenced to Open Question OQ-012.

---

## 2. Errors and inconsistencies

### ERR-001 - Error codes and messages not specified

| Field | Value |
| :--- | :--- |
| **Description** | The approved source does not specify error codes or error messages for the online-banking simulation. |
| **Type** | INCONSISTENCY_OR_GAP |
| **Severity** | INFO |
| **Source business requirement(s)** | BR-001, BR-002, BR-003, BR-004, BR-005, BR-007, BR-008, BR-009, BR-010, BR-011, BR-012, BR-013, BR-014, BR-015, BR-016, BR-017, BR-019 |
| **Traceability (FR)** | FR-001, FR-002, FR-003, FR-004, FR-005, FR-007, FR-008, FR-009, FR-010, FR-011, FR-012, FR-013, FR-014, FR-015, FR-016, FR-017, FR-019 |
| **Referenced open question** | OQ-012 |
| **Resolution** | Error codes and messages must be resolved via Open Question OQ-012 before approved error behaviour can be specified. No error codes or messages are invented. |

### ERR-002 - Approved BRD requirements referenced; brd/approved missing

| Field | Value |
| :--- | :--- |
| **Description** | The FRD generation consumed brd/raw artifacts because no brd/approved directory exists in the repository. The issue requested brd/approved as authoritative input. |
| **Type** | UPSTREAM_ARTIFACT_STATE |
| **Severity** | HIGH |
| **Source business requirement(s)** | None (upstream artifact state) |
| **Traceability (FR)** | None (upstream artifact state) |
| **Referenced open question** | None |
| **Resolution** | Per FRD Agent failure-condition instructions, generation proceeded from brd/raw when brd/approved is not present. The BRD must be human-approved and baselined to brd/approved before downstream reuse as an approved baseline. |

---

## Status

- **Status:** RAW
- **Ready for human review:** READY_FOR_HUMAN_REVIEW
- **Approval status:** NOT_APPROVED
- **Version:** 1.0
