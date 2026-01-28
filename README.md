# Library management system

Libraries today are about more than just shelves of books—they are community and digital hubs. However, the software they use is often outdated. This project uses the PEGS methodology to design a better solution: a Library Management System that covers all the essentials while being flexible enough to handle the demands of the modern era.

Each branch describes a different aspect of the system requirements, following the PEGS method.
And additionally, a specific feature branch for CI/CD.

## Requirements Documentation Strategy

We document the LMS requirements in Markdown, following the PEGS methodology structure (Goals, Environment, System, Project). The main requirements document in this repository is [requirements.md](https://github.com/FormalRequirements/re-2026-colatchup/blob/main/requirements.md). The final version is published in both HTML and PDF for easy reading, sharing, and evaluation: [HTML version](https://formalrequirements.github.io/re-2026-colatchup) and [PDF version](https://formalrequirements.github.io/re-2026-colatchup/requirements.pdf).

## CI/CD

To support a CI/CD-friendly workflow, we set up a GitHub Actions pipeline that automatically builds and publishes our requirements documentation. On every push to main, the workflow converts [requirements.md](https://github.com/FormalRequirements/re-2026-colatchup/blob/main/requirements.md) into a styled HTML page (using docs-style.css) and a PDF (via Pandoc + LaTeX), then deploys the generated artifacts to GitHub Pages. This ensures the published documentation stays in sync with the repository. For details, see the workflow definition in [docs.yml](https://github.com/FormalRequirements/re-2026-colatchup/blob/main/.github/workflows/docs.yml).

Moreover, we have implemented automated tests in [verify_structure.py](https://github.com/FormalRequirements/re-2026-colatchup/blob/main/tests/verify_structure.py) to validate :
- The presence of all main sections (Goals, Environment, System, Project).
- The presence of content in each section.
- A lint of the markdown structure to make sure it is a valid markdown file.
- Automated spelling checks to catch common typos and errors.

## Contributors

- [Colin Delrieu](https://github.com/ColinD31).
- [Kawtar Houmid Bennani](https://github.com/kawtar-bennani).