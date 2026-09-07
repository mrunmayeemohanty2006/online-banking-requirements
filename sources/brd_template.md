
C
Document Conversion Overview
The document has been converted into a structured Markdown file preserving:

Full Document Header & Confidentiality Notes: Retains document versioning metadata, contributors list, ownership details, and advisory notes.  
DOC

Complete Section Hierarchy & Table of Contents: All numbered sections from Section 1 (Introduction) through Section 10 (Issues & Management Issues) are formatted with matching hierarchy and anchors.  
DOC

Instructional & Guidance Annotations: All author instructions (< ... > and [Mandatory: ...]) are preserved as Markdown blockquotes and italicized guidance notes.  
DOC

All Structured Tables:

Document Revision History & Glossary  
DOC

Stakeholder Profile matrices  
DOC

Scope inclusion/exclusion boundaries  
DOC

Functional & Non-Functional Requirements tables across all 12 categories (Audit, Security, Privacy, Usability, Ergonomics, Internationalisation, Integration, Performance, Availability, Supportability, Volumes, etc.)  
DOC

Issues, Management, and Delivery tracking tables  
DOC

Full Embedded Annexures:

Annexure 1 (Requirements Shell): Reconstructed in detail from the embedded Excel workbook (Requirements Shell.xls / QSE/RE/TPL/03), including full column definitions, scoring scales (Customer Satisfaction 1–5, Dissatisfaction 1–5), and the comprehensive requirement classification taxonomy.  
DOC

Annexure 2 (Use Case Template): Complete tabular template structure including flow of events, pre/post-conditions, risk assessment matrix, data requirements table, and revision log.  
DOC

Annexure 3 (Activity Diagram): Process overview and complete reference of UML activity diagram notation elements extracted from the embedded Visio diagram (swimlanes, action states, forks/joins, control flows, decision nodes, and application/non-application data objects).  
DOC




Gemini is AI and can make mistakes.

# Business Requirements Document

**Version No.:**  
**Date:**  
**Project Name:**  
**Project Code:**  

---

### NOTES
> *< This box should be deleted after reading >*  
> **TO BE A FONTERRA DOCUMENT AND NEEDING STANDARD FONTERRA CONFIDENTIALITY AND DOCUMENT STANDARDS.**  
>  
> Main change was removal of Project Management type sections.  
>  
> **Document Owner/Contributors to be:**  
> - **Owner:** Fonterra Business Analyst *(may use HCL BA to do)*  
> - **Contributor:** Business Analyst, Project Manager, Solution Architect?  
>  
> **ALTERNATIVELY & RECOMMENDED:**  
> Utilise the current Fonterra Business Requirements document as includes all the Requirement content of this document, but with more detail, so is less change than incorporating those items into this document. Then add in the additional items like the appendices, which look useful.

---

## Revision History

| Version No | Date | Prepared by / Modified by | Significant Changes |
| :--- | :--- | :--- | :--- |
| | | | |

---

## Glossary

### Abbreviation Description
| Abbreviation | Description |
| :--- | :--- |
| | |

---

## Table Of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Audience](#13-audience)
  - [1.4 References](#14-references)
  - [1.5 Acronyms, Terms and Definitions](#15-acronyms-terms-and-definitions)
    - [1.5.1 Acronyms](#151-acronyms)
    - [1.5.2 Terms and Definitions](#152-terms-and-definitions)
- [2. Project Drivers](#2-project-drivers)
  - [2.1 The purpose of the application](#21-the-purpose-of-the-application)
  - [2.2 Client, Customer and other Stakeholders](#22-client-customer-and-other-stakeholders)
  - [2.3 Users of the Application](#23-users-of-the-application)
  - [2.4 Key success factors](#24-key-success-factors)
- [3. Constraints](#3-constraints)
  - [3.1 Constraints](#31-constraints)
- [4. Assumptions and Dependencies](#4-assumptions-and-dependencies)
- [5. Current state – where are we now?](#5-current-state--where-are-we-now)
  - [5.1 Stakeholder Problem and Desired State Capture](#51-stakeholder-problem-and-desired-state-capture)
  - [5.2 Overview of current business environment](#52-overview-of-current-business-environment)
    - [5.2.1 Existing business environment](#521-existing-business-environment)
    - [5.2.2 Existing application environment](#522-existing-application-environment)
- [6. Stakeholder Profiles](#6-stakeholder-profiles)
  - [6.1 [Stakeholder / Stakeholder group name]](#61-stakeholder--stakeholder-group-name)
  - [6.2 [Stakeholder / Stakeholder group name]](#62-stakeholder--stakeholder-group-name)
- [7. Scope of work](#7-scope-of-work)
  - [7.1 Scope of the Application](#71-scope-of-the-application)
- [8. Functional and Data Requirements](#8-functional-and-data-requirements)
  - [8.1 Requirements summary](#81-requirements-summary)
  - [8.2 How these requirements are organised](#82-how-these-requirements-are-organised)
    - [8.2.1 Requirement priorities](#821-requirement-priorities)
  - [8.3 Functional Requirements](#83-functional-requirements)
    - [8.3.1 Core function name #1](#831-core-function-name-1)
    - [8.3.2 Core function name #2](#832-core-function-name-2)
  - [8.4 Non-functional requirements](#84-non-functional-requirements)
    - [8.4.1 Audit](#841-audit)
    - [8.4.2 Security](#842-security)
    - [8.4.3 Privacy and confidentiality](#843-privacy-and-confidentiality)
    - [8.4.4 User access](#844-user-access)
    - [8.4.5 Useability](#845-useability)
    - [8.4.6 Health and safety, ergonomics](#846-health-and-safety-ergonomics)
    - [8.4.7 Internationalisation](#847-internationalisation)
    - [8.4.8 Integration](#848-integration)
    - [8.4.9 Performance](#849-performance)
    - [8.4.10 Availability, reliability, backup and recovery](#8410-availability-reliability-backup-and-recovery)
    - [8.4.11 Supportability](#8411-supportability)
    - [8.4.12 Volumes](#8412-volumes)
- [9. Business Implementation Requirements](#9-business-implementation-requirements)
- [10. Issues](#10-issues)
  - [10.1 Open Issues](#101-open-issues)
  - [10.2 New Problems](#102-new-problems)
  - [10.3 Deferred Requirements](#103-deferred-requirements)
  - [10.4 Ideas for Solutions](#104-ideas-for-solutions)
  - [10.5 Management Issues](#105-management-issues)
    - [10.5.1 Impact on existing units](#1051-impact-on-existing-units)
    - [10.5.2 Data ownership](#1052-data-ownership)
    - [10.5.3 User Training](#1053-user-training)
    - [10.5.4 Requirement priorities](#1054-requirement-priorities)
    - [10.5.5 Data conversion](#1055-data-conversion)
    - [10.5.6 Delivery issues](#1056-delivery-issues)
    - [10.5.7 Migration and cutover](#1057-migration-and-cutover)
- [Annexures](#annexures)
  - [Annexure 1: Requirements Shell for Reference](#annexure-1-requirements-shell-for-reference)
  - [Annexure 2: Use Case Template](#annexure-2-use-case-template)
  - [Annexure 3: Activity Diagram](#annexure-3-activity-diagram)

---

# 1. Introduction

## 1.1 Purpose
This document describes all elements that need to be considered while documenting a functional specification given by the Business user. The functional specification is the primary deliverable of the project which details the requirements in User specified Language.

## 1.2 Scope
This is applicable for the application development projects in HCL.

## 1.3 Audience
Requirements Analyst

## 1.4 References
- Software Requirement Specification Process
- SRS Guidelines

## 1.5 Acronyms, Terms and Definitions
> *< List and describe all the terms, definitions and acronyms used in the Project. Develop a dictionary built on the standards, which are agreed to by all the stakeholders. Consider use of the existing Dictionary and References. >*

### 1.5.1 Acronyms
| Acronym | Description |
| :--- | :--- |
| | |

### 1.5.2 Terms and Definitions
| Term | Definition |
| :--- | :--- |
| | |

---

# 2. Project Drivers

## 2.1 The purpose of the application
> *< Give a focused description of the vision and need that triggered the whole necessity of the application development. Describe the work that the user wants to accomplish with the application and mention the tangible benefits. Describe in brief the goals and the roadmap and establish ownership for achieving the same. >*

## 2.2 Client, Customer and other Stakeholders
> *< Identify the client and other critical stakeholders for the application. Describe briefly the commitment and focus required from each one of them for the successful development of the application. Identify the critical needs of the customer/client and other people who are affected by it. The application development must satisfy the requirements of the stakeholders and failure to identify the stakeholders could lead to missing requirements. >*

## 2.3 Users of the Application
> *< Identify and prioritize the Users for the application. Categorize the user on their roles and expertise. Consider the possibility of a wide range of users and give precedence and importance based on the priority assigned to the users. Ensure User Participation and describe the contribution and time/effort required by the category of User. >*

## 2.4 Key success factors
> *< Identify the key success factors for the application >.*

---

# 3. Constraints

## 3.1 Constraints
> *< Identify the boundaries within which the application is going to be developed/ enhanced. Consider various parameters like critical deadline limitations and impact of not meeting that, external dependencies and impact, budgeted expense for the development of the application and impact of overshooting, technological and physical environment in which the application will be installed, constraints on methodology of problem solving. >*

---

# 4. Assumptions and Dependencies
> *< List and briefly describe the assumptions and dependencies while preparing the functional requirements specifications. The impact of these assumptions and dependencies on the work products or applications are communicated to all stakeholders. >*

---

# 5. Current state – where are we now?

## 5.1 Stakeholder Problem and Desired State Capture
> *[Mandatory. Provide a summary of the problem statement analysis, to provide the reader with an overview before proceeding to the detailed analysis. Diagram is optional, but is easy to get an overview.]*

`[EMBED Visio.Drawing.11: Current State Problem & Desired State Capture / Context Flow Diagram]`

## 5.2 Overview of current business environment
The objective of this section is to briefly describe the current business environment, in terms of:
- Business functions
- Technology
- Existing systems

> *[Include a context diagram of the existing business environment if appropriate]*

### 5.2.1 Existing business environment
> *[Mandatory. Text]*

### 5.2.2 Existing application environment
> *[Mandatory. Text]*

---

# 6. Stakeholder Profiles

> *[Mandatory. Complete the following section for each stakeholder and ensure the stakeholders are named. If someone’s name is in print they are more likely to take the time to read the document and to ensure they understand and provide feedback if it’s incorrect. Consider carefully who the stakeholders are; for example:*
> - *Internal groups, such as ESG Solution Design Team, if design work may be required to integrate this with other systems. Involve them early (i.e. during the development of this Problem Statement) – they are likely to be able to assist, in particular with the identification of alternative solutions.*
> - *Business owner of any system with which this will need to integrate*
> - *SLA owner, if this will impact on business SLAs with EDS*
> - *EDS, if EDS will be required to maintain the system once in production – contact EDS through the Alliance Team in Strategy & Architecture.*
>
> *Link the “success criteria” back to the point made in the “successful solution” section of the problem statement. Provide a reference to any other documents with detailed stakeholder analysis.]*

### 6.1 [Stakeholder / Stakeholder group name]

| Attribute | Details |
| :--- | :--- |
| **Representative** | Stakeholder’s name |
| **Description** | Stakeholder’s title |
| **Involvement** | State why they are involved/impacted:<br>• Reason 1<br>• Reason 2 |
| **Success Criteria** | State what would need to be achieved for this stakeholder to register a success:<br>• Criterion 1<br>• Criterion 2 |
| **Deliverables** | What they will contribute to the project, e.g. member of Steering Group, sign-off, attendance at meetings, provide resources, etc.:<br>• Contribution 1<br>• Contribution 2 |
| **Comments and Issues** | Provide any details provided by the stakeholder that may influence the solution. For example, identify any success criteria that are not negotiable. |

### 6.2 [Stakeholder / Stakeholder group name]
> *[Repeat the table above for each affected stakeholder or group, as necessary]*

| Attribute | Details |
| :--- | :--- |
| **Representative** | Stakeholder’s name |
| **Description** | Stakeholder’s title |
| **Involvement** | State why they are involved/impacted:<br>• Reason 1<br>• Reason 2 |
| **Success Criteria** | State what would need to be achieved for this stakeholder to register a success:<br>• Criterion 1<br>• Criterion 2 |
| **Deliverables** | What they will contribute to the project, e.g. member of Steering Group, sign-off, attendance at meetings, provide resources, etc.:<br>• Contribution 1<br>• Contribution 2 |
| **Comments and Issues** | Provide any details provided by the stakeholder that may influence the solution. For example, identify any success criteria that are not negotiable. |

---

# 7. Functional Requirements: Scope of Work

## 7.1 Scope of work
> *< Describe the context and events involved that need to be examined in order to build the application. This description should cover a broader spectrum of the intended usage of the work application. The intention should be to understand completely with a shared Vision the business functioning of the Application in the intended environment. Describe the boundaries for the Requirement study, business events and interfaces that will go into the development of the Application. This will be an initial reference to the Design and Analysis. >*
>  
> *[Mandatory. (Complete this last - with the Executive Summary). Which application(s)/ sub-system would this requirements document cover? State the high-level scope in terms of upper and lower parameters (not likely to be bigger than this or smaller than that). Lay this out in a table to clarify scope – what will the project not deliver that people might otherwise assume be covered? Scope may change later in this process, but explicitly stating the project boundaries at this stage is a useful baseline.]*

The following table shows the scope of the **[Project]** project:

| Is included | Is not included |
| :--- | :--- |
| | |

## 7.2 Scope of the Application
> *< Represent the boundaries between the User and the Application by way of Use Cases diagrams. A Use case diagram and description will relate to an individual Requirement end to end, and best-fit criteria for the same. >*

---

# 8. Functional and Data Requirements

> *< The intention is also to identify relation between the individual parts and develop a data model, which would typically be supported by the Name of the Business Object, Statement of Purpose, Description of relationship and Attributes of the Object. Describe the complete functional details of a particular requirement. Each of the functional requirements should have a fit criterion, which again is dependent on the action involved. Give clarity to the Functional Requirement by identifying it with a unique ID and maintain traceability. >*

## 8.1 Requirements summary
This overview gives a broad outline of the systems that may be used to support the business environment, before the user reads the detailed analysis.

> *[Mandatory. Summarise the contents of the Functional requirements section, and the intended operational environment of the new system. List the business strategies upon which the proposed system will be designed, and give an overview of what it will do and how it can be used. Include a high level use case diagram or data flow diagram to represent the context of the requirements.]*

`[EMBED Visio.Drawing.11: High-level Use Case Diagram / Top Process / External Interactor Data Flow]`  
*(or)*  
`[EMBED Visio.Drawing.11: Data Flow Diagram / Context Model]`

## 8.2 How these requirements are organised
> *[Mandatory. Each requirement is a single statement with a unique number to enable traceability throughout the project from this initial analysis through to User Acceptance Test Development.]*

The detailed requirements are grouped by business function. Each function is briefly described and its requirements are presented as a numbered list of acceptance criteria prefixed with a code representing the function.

These requirements will form the basis of system acceptance. Each item is a single statement that can be tested to give a PASS/FAIL result. Detailed information is provided in the appendices to this document.

### 8.2.1 Requirement priorities
The priority for delivering each requirement is listed to the right of the requirements statement:
- **Must haves:** Fundamental to the project's success.
- **Should haves:** Important, but the project's success does not rely on these.
- **Could haves:** Can easily be left out without impacting on the project.
- **Future:** This requirement will not be met in the short term.
- **Business Process:** Requirement will be met with a business process rather than a system process.

---

## 8.3 Functional Requirements

### 8.3.1 Core function name #1
> *[Brief function description. Rationale: a justification for the requirements.]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.3.2 Core function name #2
> *[Brief function description. Rationale: a justification for the requirements.]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

*[etc.]*

---

## 8.4 Non-functional requirements
Non-functional requirements define how well, or to what level, a facility should be provided. They cover issues such as system interfaces, security, performance, availability, audit, monitoring and control.

> *[Mandatory, in that there should be some non-functional requirements. In this section, detail all the system requirements that do not relate specifically to the functionality of the system. As for functional requirements, present all of these requirements as numbered lists of acceptance criteria.*  
>  
> *Create a separate section for each non-functional requirement that you identify:*  
> *The following list is a guideline only - add more if you need to. These are in no particular order - re-arrange them as seems appropriate to your system. For example: You may wish to move all the sections where there are no requirements to the end, or into a separate section titled 'Not required' or just delete them.]*

### 8.4.1 Audit
> *[E.g. logging who by and when changes are made]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.2 Security
> *[E.g. Access Control Lists for parts of the system]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.3 Privacy and confidentiality
> *[E.g. encryption, personal information and the privacy act]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.4 User access
> *[E.g. via a portal, intranet, remote access, existing / new menu]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.5 Useability
> *[E.g. keyboard shortcuts, disabled users, fast data entry, consistent with other systems]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.6 Health and safety, ergonomics
> *[E.g. for data entry operators, font size / readability]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.7 Internationalisation
> *[E.g. multi lingual, time differences]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.8 Integration
> *[List all data items required from other systems and what the purpose is, e.g. data / user verification]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.9 Performance
> *[For a web or client / server application state the expected maximum and usual numbers of users, and what an acceptable response time would be. For batch processing state an acceptable run time in terms of its dependencies]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.10 Availability, reliability, backup and recovery
> *[E.g. peak periods, criticality of the data or process, statefulness in event of failure]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.11 Supportability
> *[E.g. technical documentation, utilities, vendor agreements, user guides]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

### 8.4.12 Volumes
> *[E.g. numbers of users, transactions, frequency of processes]*

| Detailed requirement | Priority |
| :--- | :--- |
| | |

---

# 9. Business Implementation Requirements

> *[Mandatory, in that there should be some business implementation requirements. This section is intended to advise Fonterra of the scope and depth of the [system] implementation project. It focuses primarily on the user involvement in training, testing and migration of existing documents or data.]*

This section is intended to make the business aware of the depth and scope of the system implementation, by describing some of the key implications and impacts of the new system. It outlines the approximate effort necessary to implement the system, with particular attention to the involvement required by users and the hidden aspects of implementing a system in the current business environment. It addresses three key areas:

---

# 10. Issues

## 10.1 Open Issues
> *< Describe issues that have not had a conclusive answer and identify them as risks that could hamper the development of the Application. >*

## 10.2 New Problems
> *< List the probable adverse effects of the Application for the User. Describe the possible pitfalls that could be encountered during the implementation stage. >*

## 10.3 Deferred Requirements
> *< Requirements that are gathered but are not agreed upon and are not part of the current development scenario are logged here. Requirements in the repository shall be the inputs for future versions of the Application. >*

## 10.4 Ideas for Solutions
> *< List all those good ideas that creative thinkers generate during Requirements Gathering and ensure that they are not lost and help separate between requirements and solutions. The aim is to capture with minimum effort an idea that you can come back to later. >*

## 10.5 Management Issues

### 10.5.1 Impact on existing units
Describe the expected effects of the proposed system on the relevant business units, the business as a whole and any other existing automated systems, in terms of management issues such as staffing, workflow boundaries, measurements, corporate culture and policies.

### 10.5.2 Data ownership
Define the ownership issues for data in the automated system; in terms of data management, archiving and the access rights of other groups.

### 10.5.3 User Training
> *[Specify the user and support staff training needs, how they are expected to be met, who is responsible, and when training should be done. The training approach may include courses, involvement in user testing and provision of user manuals.*  
>  
> *Do not give costings! If you are working towards providing a cost for the project, specify either that:*  
> - *Only the courses specified here are included in the costings*  
> - *Any training is not included in the costings provided and shall be organised and costed separately.]*

### 10.5.4 Requirement priorities
If there are multiple components in the proposed system, list them in implementation priority.

### 10.5.5 Data conversion
Specify any data conversion procedures to be followed and the implementation strategy to be carried out once testing has been completed.

### 10.5.6 Delivery issues
Detail any delivery issues such as retention of source code, escrow arrangement, cost-free warranty periods.

### 10.5.7 Migration and cutover
Identify any critical requirements around data or system migration, requirements for parallel systems during cutover, etc.

---

# Annexures

## Annexure 1: Requirements Shell for Reference
Requirements can be defined using the requirement shell as given in `Requirements Shell.xls`.

### Requirements Shell Metadata & Change History (from `Requirements Shell.xls`)
- **Document Title:** Requirements Shell
- **Template / ID:** `QSE/RE/TPL/03`
- **Version No.:** `6.00`
- **Release Date:** `05-Apr-2006`
- **Authors / Contributors:** Amit Gupta, Srinivas.mv
- **Organization / Confidentiality:** HCL Technologies Limited / HCL Confidential

#### Change History
| Sl No | Version | Date | Changed by | Change |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

#### Requirements Shell Attribute Structure & Definitions

| Field / Column Header | Definition / Instruction | Scale / Allowed Values |
| :--- | :--- | :--- |
| **Requirement #** | A Unique number for the requirement | Unique identifier (e.g. REQ-001) |
| **Requirement Type** | The type of the requirement | Selected from standard types list (see below) |
| **Event / Use Case Ref** | List of events / use cases that need this requirement | Reference ID |
| **Description** | A one sentence statement of intention of this requirement | Statement of requirement |
| **Source** | Which stakeholder / actor raised this requirement | Stakeholder / Actor name |
| **Rationale** | A justification of the requirement | Business justification |
| **Fit criterion** | A measurement of the requirement such that it is possible to test if the solution matches the original requirement. If it is not possible to mention this then the requirement is ambiguous. | Testable PASS/FAIL measurement criterion |
| **Customer Satisfaction** | Degree of stakeholder happiness if this requirement is successfully implemented. | Scale: <br>1 = Uninterested<br>2 = Indifferent<br>3 = Satisfied<br>4 = Pleased<br>5 = Extremely pleased |
| **Customer Dissatisfaction** | Measure of stakeholder unhappiness if this requirement is not implemented. | Scale: <br>1 = Hardly matters<br>2 = May be displeased<br>3 = Mostly displeased<br>4 = Displeased<br>5 = Extremely displeased |
| **Dependencies** | A list of other requirements that have some dependency on this one | Requirement reference IDs |
| **Conflicts** | Other requirements that cannot be implemented if this one is implemented | Requirement reference IDs |
| **Supporting material** | Pointer to the documents that illustrate and explain this requirement | File / Document links or names |
| **History** | Creation, changes, deletions, etc. | Change / version logs |

#### Standard Requirement Types Taxonomy (from Requirements Shell)
The template classifies requirements into the following categories:
1. **Functional Requirements**
   - Functional
   - User interface
   - Customization
2. **Technical & Architecture Requirements**
   - Application Servers
   - Web server
   - Database Server
   - Database Management System
   - Database Connectivity
   - Hardware & OS
   - Communication Protocols
   - Software components
3. **Quality & Non-Functional Requirements**
   - Audit Trail
   - Security
   - Reliability
   - Scalability
   - Availability
   - Performance
   - Interoperability
   - Multilanguage Support
   - Supportability
   - Data migration
   - Data Retention
   - Transaction Volume and Data Volume
   - Backup and Recovery
   - Installation and distribution
4. **Planning & Design Requirements**
   - Design Requirements
   - Planning Reqmnt - Design
   - Planning Reqmnt - Architecture and Application Design
   - Planning Reqmnt - Development
   - Planning Reqmnt - Coding Standards & Conventions
   - Planning Reqmnt - Data Migration Dependencies
5. **Project Processes & Quality Requirements**
   - Project Processes
   - Standards & Guidelines
   - Analysis
   - Program Documentation
   - Unit Testing
   - Integration & System Tests
6. **Implementation, Deployment & Governance**
   - Implementation Requirements
   - Deployment Requirements
   - Delivery requirements
   - Time Line
   - User Manuals & Help
   - Training
   - Legal / Regulatory
   - Client Access

---

## Annexure 2: Use Case Template
Requirements can be defined using a Use Case as specified in the below tabular representation:

| Field | Description / Instruction |
| :--- | :--- |
| **Title** | `<Use-case name – indicate the goal of the use-case>` |
| **Actors** | `<Name of actors invoking use-case, you can mention whether they are the initiating or participating actors>` |
| **Status** | `<Open, Closed, On-hold, Suspended, Canceled>` |
| **Description** | `<Textual description of the use-case (Keep it as precise as possible)>` |
| **Flow of Events** | `<Steps of the use-case (Primary flow of events). Describe them as a bulleted/ numbered list>` |
| **Sub-flow / Alternate Flows / Scenarios** | `<Alternative paths to the primary flow of events above>` |
| **Special Requirements** | `<Performance requirements, Any user interface related specifics, implementation concerns, testing concerns>` |
| **Assumptions** | |
| **Pre-conditions** | `<What are the requirements for this use-case to run, list of conditions that should exist before the use case can be executed>` |
| **Post-conditions** | `<What state the system is in after use-case runs>` |
| **User interface** | `<Reference to UI prototype or specific screen and UI related notes>` |
| **Business Rules** | `<Any domain specific knowledge or algorithms or validation rules (relevant to this use-case)>` |
| **Entities / Business Concepts** | `<This is optional. You can list obvious entities/business concepts picked from this use-case. E.g. Order, customer, item>` |
| **Related Use Cases** | `<This is optional. List all Use Cases include, extend or specialize this use case>` |
| **Issues** | `<Clarifications required from user – Any questions related to use-case>` |
| **Reference** | **Requirement #:** <br>**Documents:** <br>**Persons:** |
| **Use-case Authors:** | |

### Risk Assessment
| Risk factor | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| | | | |

### Data Requirements
| Entity | Information Element | Source of Information | Retention Requirement | Audit / Tracking Requirements |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

### Revision log
| Modified by | Date | Version | Description |
| :--- | :--- | :--- | :--- |
| Initial Write | | | |

---

## Annexure 3: Activity Diagram

Business processes and workflow can be described using activity diagrams, expressed in the Unified Modeling Language (UML). Activity diagrams encourage noticing and documenting parallel and concurrent activities. This makes the diagrams excellent tools for modeling workflow, analyzing use cases, and dealing with complex application development.

An example of an activity diagram with an explanation of all the elements of notation is demonstrated below:

`[EMBED Visio.Drawing.4: Activity Diagram Notation and Workflow Model]`

### Summary of Notation Elements (from Embedded Activity Diagram Guide)
- **Swimlane:** Represents a functional area or business role that performs activities (e.g. functional department, user role).
- **Initial State / Start State:** Solid black circle representing the beginning of a business process or workflow.
- **Action State / Activity:** Represents a single business processing step or task performed by an actor or system.
- **Control Flow / Transition:** Direct line with arrow indicating sequence from one action state to another.
- **Decision / Merge:** Diamond symbol used to show alternate conditional branches based on guard conditions (e.g. `[Condition 1]`, `[Condition 2]`).
- **Fork / Synchronization Bar (Join):** Horizontal solid black bar indicating where parallel concurrent activities split (fork) or synchronize/wait to converge (join).
- **Sub-process / Summary Activity:** Activity with an embedded sub-icon indicating that it is further detailed in a separate diagram.
- **Constraint / Note:** Callout note providing additional information, business rules, or pre/post-conditions between states (e.g. data flow, events that must not occur).
- **Object / Data Store (Application vs. Non-Application):** Distinguishes manual vs automated activities, external databases, interfaces, and documents detailing use cases.
- **End State / Final State:** Bullseye circle (encircled solid dot) indicating completion of the workflow or process flow.

---

### Document Classification & Standards
- **Template Identifier:** `FONT_BRD 1.0` / `FONT-BRD v 1.0 Document Template_V1.dot`
- **Classification:** `Fonterra - HCL Confidential` / `Standards Quality`
Business_Requirement_Document_Template_FONT_BRD_v1.0.md
Displaying Business_Requirement_Document_Template_FONT_BRD_v1.0.md.