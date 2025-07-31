# AGENTS.md

This document defines the role, boundaries, and behavior of this Django web app: the Offline Feedback Collector.

It serves as a systems-level specification for how the app should behave, what it owns, and what design principles guide development.

---

## Role of the App

This web application acts as a lightweight, mobile-first system for collecting customer feedback in offline business environments via QR codes. It is **not** a chatbot, assistant, or interactive AI agent. It is a form-based collector with opinionated behavior.

The app shall:

- Serve publicly accessible feedback forms, one per business branch
- Accept, store, and summarize customer responses
- Restrict dashboard access to logged-in business owners only
- Generate QR codes to enable customer entry without requiring authentication
- Expose feedback data in a structured and exportable format (CSV, JSON if needed)

---

## What This App Does Not Do

- It does not perform AI analysis, sentiment scoring, or NLP
- It does not expose public APIs or offer integrations (in MVP)
- It does not track users or require customer login
- It does not store personal information unless explicitly extended

---

## Guiding Principles

- **Single-responsibility design** – Keep each view, model, and function purpose-driven
- **Mobile-first experience** – The public-facing form must load and function well on low-end phones and slow connections
- **Separation of concerns** – Logic belongs in service layers or forms, not views or templates
- **Security-first** – Validate all input, sanitize output, avoid exposing internal logic
- **Minimal dependencies** – Stick to core Django and Bootstrap; add libraries only if justified

## Instructions for the AI Agent
- Use Bootstrap 5 classes that work with the current custom theme
- We used a Bootstrap 5 theme called Yuri by pixelstrap for the front end.
- Generated code must be ready to explain - include comments only where intent is unclear
- All public functions must include a meaningful docstring
- This project uses **semantic versioning** and maintains two files to track progress:
    - `version.json` – for programmatic access and CI/CD/debugging
    - `CHANGELOG.md` – for human-readable summaries of all code changes

- Use the format:  
`MAJOR.MINOR.PATCH`
    - Increase **MAJOR** for breaking changes or major rewrites
    - Increase **MINOR** for added features (non-breaking)
    - Increase **PATCH** for bugfixes, adjustments, or internal refactors

- Always update `version.json` when:
    - You bump the version  
    - You change environments (e.g. local → staging)  
    - You want to describe a release in brief

Example structure:

```json
{
  "name": "offline-feedback",
  "version": "0.3.0",
  "environment": "local",
  "release_notes": "Added CSV export and form validation fixes"
}
---

## Documentation Update Rules (README, CHANGELOG, version.json)

Every PR must include a quick check for documentation relevance.  
Only update if the change justifies it — but **never skip the check**.

### When to Update `README.md`

Update the README if:
- A new feature or flow changes how the app behaves
- Setup steps or commands change
- A dependency or tool is added that affects how someone uses the project
- A previously undocumented concept becomes part of the system design

Do not update README for internal refactors, cosmetic changes, or tiny patches.

---

### When to Update `CHANGELOG.md`

Always check if the PR includes **new behavior, bug fixes, or removed logic**.  
If yes, record the change under today’s date using semantic version grouping.

- Use grouped entries per actual date of work (not PR creation)
- Only document meaningful logic changes, not typo fixes or whitespace tweaks

If nothing relevant changed, no update is needed.

---

### When to Update `version.json`

Update `version.json` if:
- You bump the version number (major, minor, or patch)
- The deployment environment changes (e.g. `local` → `staging`)
- You added release-worthy features or fixes

Never leave `version.json` behind if you’ve already updated the changelog version.

---

### Summary Checklist (for every PR)

Before submitting a PR:

- [ ] README checked — updated if project behavior/setup changed  
- [ ] CHANGELOG reviewed — added new entries if code behavior changed  
- [ ] version.json bumped — if version has changed  

If none of the files are relevant, state clearly in the PR:  
> “Docs unchanged – no impact to README, CHANGELOG, or version.json”


## Project Behavior Summary

| Layer           | Responsibility                                                                |
|-----------------|-------------------------------------------------------------------------------|
| Public Frontend | Show QR-based, branded feedback forms. No login required.                     |
| Auth Layer      | Restrict dashboard access using Django’s built-in authentication              |
| Admin Layer     | Provide full CRUD control for business owners and branch managers             |
| Storage         | Persist responses in relational DB. No analytics or session tracking          |
| Exports         | Enable easy download of responses in clean CSV format                         |

---

## UX Expectations

- The survey flow should be clear, tappable, and fast.
- Forms must submit without friction and confirm with a lightweight thank-you page.
- Admins should quickly see meaningful summaries (e.g., satisfaction averages).
- The experience must feel stable, fast, and unintrusive.

---

## Development Intent

This app is part of a solo learning project meant to:
- Demonstrate real-world Django patterns
- Show how to integrate a custom Bootstrap 5 theme
- Build an actual, useful business tool from scratch
- Be clean, auditable, and suitable for public display (e.g. in job applications)

---

## Versioning & Metadata

- This app uses semantic versioning.
- A `version.json` file at the root of the repo tracks environment, version, and release notes.
- Future improvements may expose a `/version/` endpoint.

---

This document is not boilerplate. Any collaborator must understand this file before writing or editing core logic.

---

## Theme Integration: Yuri (HTML Bootstrap 5)

This project uses the **Yuri HTML theme** from ThemeForest as its visual framework. Only the necessary assets and templates have been extracted — the original app and sample views have been discarded.

### Theme Usage Rules

- Do **not** modify original layout templates unless needed. Extend them instead.
- All base layouts (e.g. `base.html`, `layouts/sidebar.html`) live in `templates/layouts/`.
- All custom pages should **extend `base.html`** unless otherwise specified.

### Static Assets

- This is the folder structure for Static Assets
- Static is located at root /static

static
└── assets
    ├── ajax
    │   ├── api.txt
    │   ├── arrays.txt
    │   ├── object.txt
    │   ├── object_nested.txt
    │   ├── orthogonal.txt
    │   ├── post.php
    │   └── server-processing.php
    ├── audio
    │   └── horse.ogg
    ├── css
    │   ├── color-1.css
    │   ├── color-1.css.map
    │   ├── color-2.css
    │   ├── color-2.css.map
    │   ├── color-3.css
    │   ├── color-3.css.map
    │   ├── color-4.css
    │   ├── color-4.css.map
    │   ├── color-5.css
    │   ├── color-5.css.map
    │   ├── color-6.css
    │   ├── color-6.css.map
    │   ├── font-awesome.css
    │   ├── pages
    │   │   ├── general_widget.css
    │   │   ├── general_widget.css.map
    │   │   ├── invoice.css
    │   │   └── invoice.css.map
    │   ├── responsive.css
    │   ├── responsive.css.map
    │   ├── style.css
    │   ├── style.css.map
    │   └── vendors
    │       ├── animate.css
    │       ├── animate.css.map
    │       ├── aos.css
    │       ├── aos.css.map
    │       ├── autoComplete.min.css
    │       ├── bootstrap.css
    │       ├── bootstrap.rtl.min.css
    │       ├── calendar.css
    │       ├── calendar.css.map
    │       ├── chartist.css
    │       ├── chartist.css.map
    │       ├── datatable-css
    │       │   └── style.css
    │       ├── datatable-extension.css
    │       ├── datatable-extension.css.map
    │       ├── datatables.css
    │       ├── datatables.css.map
    │       ├── date-picker.css
    │       ├── date-picker.css.map
    │       ├── date-time-picker.css
    │       ├── daterange-picker.css
    │       ├── daterange-picker.css.map
    │       ├── dropzone.css
    │       ├── dropzone.css.map
    │       ├── echart.css
    │       └── echart.css.map


### Templates

- Templates is located at root /templates

templates
├── base.html
├── boxed.html
├── footer-dark.html
├── footer-fixed.html
├── footer-light.html
├── general
│   └── index.html
├── hide-on-scroll.html
├── layout
│   ├── breadcrumb.html
│   ├── footer.html
│   ├── header.html
│   └── sidebar.html
├── layout-dark.html
└── layout-rtl.html

Avoid duplicating layout code in your own pages.

### Ownership Boundaries

- The Yuri theme defines look and layout  
- Our Django app defines all business logic, views, and data  
- Treat Yuri as a UI layer, not an app layer

Any updates to Yuri (e.g. new version, layout change) must be reviewed carefully before merging into live views.