# Library management system requirements

Requirement documentation following the PEGS method

## Changelog

| Date       | Description |
|------------|-------------|
| 2026-01-19 | Initial draft |
| 2026-01-20 | Add readme description |
| 2026-01-20 | Add requirements markdown base |
| 2026-01-27 | Add Goals, Environment, System & Project section |
| 2026-01-27 | Add CI/CD pipeline |

## Content :

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

## Goals
Goals are "needs of the target organization, which the system will address". While the development team is the principal user of the other books, the Goals book addresses a wider audience: essentially, all stakeholders. It must contain enough information to provide — if read just by itself — a general sketch of the entire project. To this effect, chapter G.3 presents a short overview of the system, and G1 will typically include some key properties of the environment. As it addresses a wide readership, it should be clear and minimize the use of specialized technical terms. Together, G1, G2 and G3 describe the rationale for the project. It is important to state these justifications explicitly. Typically, they are well understood at the start of the project, but management and priorities can change (see [Handbook](https://link.springer.com/book/10.1007/978-3-031-06739-6)).

### G.1 Overall context and goals
**Context:** Many libraries still use outdated systems that slow down daily tasks. This project defines the requirements for a simple, modern Library Management System (LMS) to improve how books and users are managed.The goal is to build a clear, adaptable foundation for future development.

**Goals:**
`G.1.1` Simplify Lending: To streamline the process of checking out and returning books across different library branches, making the workflow efficient for staff and seamless for users.


`G.1.2` Enhance Accessibility: To provide a clear, user-friendly interface that allows patrons to easily search the catalog, place holds, and manage their account status without requiring constant staff intervention.


`G.1.3` Ensure Fair Access: To automatically enforce borrowing rules—such as loan limits, reservation queues, and return deadlines—ensuring that library resources remain available to the widest possible audience.

### G.2 Current situation
`G.2.1` Manual Processes: Librarians often rely on manual record-keeping or disconnected legacy software, leading to inefficiencies in tracking book locations and user status.

`G.2.2` Lack of Autonomy: Users cannot check real-time availability or manage their loans remotely, forcing them to visit the library or contact staff for simple queries.

`G.2.3` Process Definition: The structure and specific feature sets for the digital transformation are currently being defined to replace these obsolete methods.

`G.2.4` Poor Visibility: Members have limited visibility regarding book availability and their own borrowing status.

### G.3 Expected benefits
`G.3.1` Improved accuracy and consistency in tracking books, copies, and loans.

`G.3.2` Clear enforcement of library policies such as loan periods and borrowing limits.

`G.3.3` Reduced manual effort for librarians through automation of routine operations.

`G.3.4` Better user experience for members through transparent access to borrowing information.

`G.3.5` A shared and reliable source of truth about the state of the library inventory.

### G.4 Functionality overview
`G.4.1` Manage the library catalog (books and their physical copies).

`G.4.2` Register and manage library members.

`G.4.3` Handle borrowing, returning, and tracking of loans.

`G.4.4` Enforce lending rules and constraints.

`G.4.5` Provide visibility into availability, loan status, and overdue items.

`G.4.6` Detailed behavior and technical design choices are intentionally deferred to later sections.

### G.5 High-level usage scenarios
`G.5.1` A librarian registers new books and copies into the system.

`G.5.2` A member searches for a book and checks its availability.

`G.5.3` A member borrows an available copy following library rules.

`G.5.4` A member returns a borrowed copy.

`G.5.5` A librarian reviews overdue loans and current inventory status.

### G.6 Limitations and exclusions
The system is not required to address the following aspects:

`G.6.1` Financial management (payments, fines processing, accounting).

`G.6.2` Acquisition workflows with publishers or suppliers.

`G.6.3` Detailed analytics or recommendation engines.
Physical security systems (RFID gates, surveillance).

`G.6.4` Full digital content delivery (e-book readers, DRM platforms).

### G.7 Stakeholders and requirements sources
Primary stakeholders include:

`G.7.1` Library members, who borrow and return books.

`G.7.2` Librarians, responsible for catalog management and daily operations.

`G.7.3` Library administrators, who define policies and oversee operations.

`G.7.4` Development team, responsible for designing and implementing the system.

Requirements are derived from:

`G.7.5` Common library operational practices.

`G.7.6` Domain-driven design principles applied to library systems.

`G.7.7` Educational and reference material on library management system design.

## Environment
This section describes the context in which the Library Management System operates. It focuses on the real-world elements of a library, the rules that govern it, and the assumptions made about how it functions. The goal is to clearly define the domain independently of any technical implementation.

### E.1 Glossary
**Library:** An organization that manages a collection of books and allows registered users to borrow them.

**Book:** A published work identified by information such as title, author, and ISBN.

**Copy:** A physical instance of a book that can be borrowed by a member.

**Member:** A registered user of the library who is allowed to borrow books.

**Librarian:** A staff member responsible for managing the library’s collection and supervising borrowing activities.

**Loan:** The action of lending a book copy to a member for a limited period.

**Availability:** The state of a copy indicating whether it can currently be borrowed.

**Loan policy:** A set of rules defining how long and how many books a member can borrow.

### E.2 Components
`E.2.1`The environment of the system includes several real-world elements:

`E.2.2`A collection of books composed of multiple physical copies.

`E.2.3`People interacting with the library, such as members and librarians.

`E.2.4`Rules defined by the library regarding borrowing and returning books.

`E.2.5`Time-related aspects, including loan durations and due dates.

`E.2.6`These elements exist regardless of the system and are simply represented and managed by it.

### E.3 Constraints
`E.3.1`The Library Management System must respect the following constraints:

`E.3.2`A physical copy can only be loaned to one member at a time.

`E.3.3`Borrowing conditions, such as loan duration and maximum number of loans, are defined by the library.

`E.3.4`Only registered members are allowed to borrow books.

`E.3.5`Librarians are responsible for keeping the catalog accurate and up to date.

`E.3.6`The system must always reflect real library operations consistently.

### E.4 Assumptions
`E.4.1`The following assumptions are made about the environment:

`E.4.2`Each book can be uniquely identified using standard metadata.

`E.4.3`Physical copies are tracked individually.

`E.4.4`Members follow the library’s rules when borrowing and returning books.

`E.4.5`Library policies do not change frequently.

`E.4.6`The system is initially designed for a single library.

### E.5 Effects
`E.5.1`The introduction of the system has several effects on the library environment:

`E.5.2`Manual tracking of loans and inventory is reduced.

`E.5.3`Information about availability and loan status becomes more accessible.

`E.5.4`Lending rules are applied more consistently.

`E.5.5`Communication between members and librarians is improved.

`E.5.6`The system supports existing processes without changing the library’s policies.

### E.6 Invariants
`E.6.1`The following properties must always remain true:

`E.6.2`A copy cannot be available and on loan at the same time.

`E.6.3`Each loan is linked to exactly one member and one copy.

`E.6.4`Once a copy is returned, it becomes available again.

`E.6.5`The catalog only contains books and copies that actually exist.

`E.6.6`The system state must always match the real situation of the library.

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
