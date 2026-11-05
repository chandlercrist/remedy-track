
# RemedyTrack Documentation

## User Stories

### User Story 1 - User Login

As an **authorized user**, I want to **log in to RemedyTrack** so I can **access and manage cybersecurity findings**.

Acceptance Criteria:
- Users can log in with a valid username and password.
- Invalid login credentials are rejected.
- Users must be logged in before accessing findings.

### User Story 2 - Create Findings

As a **security analyst**, I want to **record new cybersecurity findings** so I can **document issues identified during a security assessment**.

Acceptance Criteria:
- A user can create a finding with a title, description, and severity level.
- Required fields must be completed before a finding can be saved.
- Saved findings appear in the findings list.

### User Story 3 - Assign Findings

As a **security analyst**, I want to **assign findings to IT staff members** so I can **identify who is responsible for addressing each issue**.

Acceptance Criteria:
- A finding can be assigned to an existing user.
- The assigned user is displayed when viewing a finding.
- A security analyst can change the assignment when necessary.

### User Story 4 - Update Remediation Status

As an **IT staff member**, I want to **update the status of findings assigned to me** so I can **show the progress being made toward resolving them**.

Acceptance Criteria:
- Assigned users can change a finding's status to Open, In Progress, or Resolved.
- Status changes are saved and displayed when the finding is viewed again.
- Users cannot modify findings assigned to someone else unless they have administrative permission.

### User Story 5 - View and Filter Findings

As a **security analyst**, I want to **filter findings by severity and status** so I can **focus on issues that require attention**.

Acceptance Criteria:
- Findings can be filtered by severity level.
- Findings can be filtered by remediation status.
- Users can clear filters to view all findings.

### User Story 6 - View Dashboard

As a **security analyst**, I want to **view a dashboard showing the status of findings** so I can **quickly identify outstanding security issues**.

Acceptance Criteria:
- The dashboard displays the number of Open, In Progress, and Resolved findings.
- The displayed counts reflect the findings stored in the application.
- Users can navigate from the dashboard to the findings list.
