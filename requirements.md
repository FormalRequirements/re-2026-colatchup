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