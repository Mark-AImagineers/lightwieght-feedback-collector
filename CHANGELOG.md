# CHANGELOG.md

Offline Feedback Collector
This document logs all meaningful code changes, grouped by semantic version and date.

---
## [v0.2.3] 2025-08-7
### Added
- Added forms for business registration
- set default login_url for @login_required decorator

### Changed
-Updated business_view to handle post form submissions and assign request.user as owner
-Show a list of current user's business
-Use @login_required decorator on business view

---

## [v0.2.2] 2025-08-1
### Added
- Added login template


### Changed
- linked `/register` and `/login` to all auth pages

### Fixed
- cleaned sidebar, footer and header pages 

---

## [v0.2.1] 2025-07-31
### Added
- Added static file support /static and custom template directory /templates
- Created a custom user model `EmailUser` inheriting from `AbstractBaseUser`
- Registered `EmailUser` in `AUTH_USER_MODEL`
- Added semantic string representation admin `EmailUser`
- Created `RegistrationForm` extending `UserCreationForm`
- Built `RegisterView` and `UserLoginView`~using class-based views
- Wired up /register, /login, /dashboard with clean Bootstrap form layout (no templates yet)

### Changed
- Replaced unused ```{% sass_src %}``` with proper compiled `style.css` link

### Fixed
- Corrected custom user model save method so superuser creation persists.
- Fixed a `save()` bug (create user not saving)
- Fixed `createsuperuser` not prompting for first and last name

### Notes
- Verified project runs correctly via ```docker compose up```
- Connected index.html and confirmed static assets loading
- Verified `is_superuser` and `is_staff` flags set correctly

---

## [v0.1.0] 2025-07-31
- Scaffolded Basic Django + Boostrap (Yuri) + Postgres + Docker Files
- Added Readme, CHANGELOG, LICENSE

---

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
- image database setup
- image for buisness and profile pages

This list will expand or shift as the project evolves.