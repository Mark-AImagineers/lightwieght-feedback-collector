# CHANGELOG.md

Offline Feedback Collector
This document logs all meaningful code changes, grouped by semantic version and date.

---

## [v0.1.0] 2025-07-31



## [v0.1.1] 2025-07-31
### Fixed
- Corrected custom user model save method so superuser creation persists.


## 🧭 Build RoadMap

This section maps the full project journey — all core components we plan to build or refine, written as sequential goals.

- Set up a clean public Django project with versioning and changelog rules
- Integrate a downloaded Bootstrap 5 theme into Django templates
- Create models for Business, Branch, and Feedback
- Build public feedback form (mobile-first, QR-linked)
- Implement QR code generation logic and store QR per branch
- Add Django admin customization for business owners and branch managers
- Implement login/logout and permission-based dashboard views
- Build dashboard UI for viewing feedback entries
- Add basic stats summary (e.g., satisfaction average, counts)
- Implement CSV export for feedback entries
- Style dashboard using Bootstrap components
- Create a simple printable flyer view with QR and instructions
- Finalize clean UX for feedback form and thank-you screen
- Add project metadata via version.json
- Document versioning, agent behavior, and changelog rules
- Containerize the app with Docker (planned)
- Add a read-only `/version/` endpoint (planned)
- Add JWT token handling (Hybrid, keep it stateful)
- Add Password Reset
- Switch to GUNICORN / UVICORN
- admin panel to monitor registered users and payment
- social media signin/signup

This list will expand or shift as the project evolves.