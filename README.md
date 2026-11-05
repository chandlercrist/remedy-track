

# RemedyTrack

RemedyTrack is a web application designed to help organizations manage cybersecurity findings and track their remediation progress. During security assessments, organizations may identify numerous vulnerabilities or areas that need improvement. Keeping track of these findings, especially when multiple people are responsible for addressing them, can become difficult.

RemedyTrack provides a central location for documenting findings, assigning remediation responsibilities, and tracking the status of identified issues. Users can record findings, categorize them by severity, and update their progress as corrective actions are completed.

The goal is to provide IT staff and security personnel with a simple way to stay organized and ensure that identified security issues are not overlooked or left unresolved.

## Installation

### Prerequisites

- Python 3.12 or newer
- Git
- pip

### Setup

1. Clone the repository:

```bash
git clone https://github.com/chandlercrist/remedy-track.git
cd remedy-track
```

2. Create a virtual environment:

```bash
python3 -m venv .venv
```

3. Activate the virtual environment (macOS/Linux):

```bash
source .venv/bin/activate
```

4. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

5. Set up the database:

```bash
python manage.py migrate
```

6. Create an administrator account:

```bash
python manage.py createsuperuser
```

## Getting Started

Start the Django development server:

```bash
python manage.py runserver
```

Once the server is running, open a browser and navigate to:

http://127.0.0.1:8000/

The application is designed to allow users to:

- View and manage cybersecurity findings.
- Record new findings and assign severity levels.
- Assign responsibility for remediation tasks.
- Update findings as remediation work progresses.
- Review outstanding findings.

To access the Django administrative interface, navigate to:

http://127.0.0.1:8000/admin/

To stop the development server, press `Ctrl+C` in the terminal.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


