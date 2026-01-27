# Library management system requirements

Requirement documentation following the PEGS method

Content :

Goals :
- G.1 Overall context and goals
- G.2 Current situation
- G.3 Expected benefits
- G.4 Functionality overview
- G.5 High-level usage scenarios
- G.6 Limitations and exclusions
- G.7 Stakeholders and requirements sources

Environment :
- E.1 Glossary
- E.2 Components
- E.3 Constraints
- E.4 Assumptions
- E.5 Effects
- E.6 Invariants

System :
- S.1 Components
- S.2 Functionality
- S.3 Interfaces
- S.4 Detailed usage scenarios
- S.5 Prioritization
- S.6 Verification and acceptance criteria

Project :
- P.1 Roles
- P.2 Personnel characteristics and constraints
- P.3 Imposed technical choices
- P.4 Tasks and deliverables
- P.5 Schedule and milestones
- P.6 Risks and mitigation analysis
- P.7 Requirements process and report

## System

The System section specifies what the Library Management System must do and how it is structured from a requirements perspective. It describes the system’s responsibilities, its internal decomposition, its interactions with users and external actors, and the criteria used to verify that requirements are met. This section remains independent of any specific technical implementation.

### S.1 Components

The Library Management System is composed of the following logical components:

`S.1.1` Catalog Management Component, responsible for maintaining information about books and their copies.

`S.1.2` Member Management Component, responsible for registering and maintaining member data.

`S.1.3` Loan Management Component, responsible for handling borrowing and returning operations.

`S.1.4` Policy Enforcement Component, responsible for applying lending rules and constraints.

`S.1.5` User Interaction Component, responsible for supporting interactions with members and librarians.

### S.2 Functionality

The system shall provide the following functionalities:

`S.2.1` Register, update, and consult information about books and their physical copies.

`S.2.2` Register and manage library members.

`S.2.3` Allow members to borrow available copies according to library rules.

`S.2.4` Allow members to return borrowed copies.

`S.2.5` Track active loans and their due dates.

`S.2.6` Enforce loan policies such as borrowing limits and loan duration.

`S.2.7` Provide visibility into availability and loan status.

All functionalities must operate in a consistent and controlled manner.

### S.3 Interfaces

The system shall expose interfaces to the following actors:

`S.3.1` Members, who consult the catalog and manage their own loans.

`S.3.2` Librarians, who manage the catalog and supervise borrowing operations.

`S.3.3` Administrators, who define or update library policies.

`S.3.4` These interfaces must provide clear access to system functionality while respecting user roles and permissions.

### S.4 Detailed usage scenarios

Typical system usage scenarios include:

`S.4.1` A librarian registers a new book and its copies in the catalog.

`S.4.2` A member searches for a book and checks copy availability.

`S.4.3` A member borrows an available copy, creating a loan record.

`S.4.4` A member returns a borrowed copy, closing the loan.

`S.4.5` A librarian reviews current loans and identifies overdue items.

Each scenario must result in a consistent update of the system state.

### S.5 Prioritization

System functionalities are prioritized as follows:

`S.5.1` High priority: Loan management, catalog management, member registration.

`S.5.2` Medium priority: Policy enforcement and availability tracking.

`S.5.3` Low priority: Administrative reporting and extended consultation features.

Higher-priority functionalities must be implemented and validated first.

### S.6 Verification and acceptance criteria

The system shall be considered acceptable when:

`S.6.1` All defined functionalities are implemented and operational.

`S.6.2` Lending rules are consistently enforced.

`S.6.3` System state accurately reflects real-world library operations.

`S.6.4` Invariants defined in the Environment section are preserved.

`S.6.5` Usage scenarios can be executed without inconsistency or data loss.

Verification will be performed through scenario-based testing and stakeholder validation.
