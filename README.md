# Prerequisites
- Python 3.10+ installed
- pip (comes with Python)

# 1. Clone or Download the Project
- `git clone https://github.com/tanenunu/Epi_Challenge.git`
- `cd Epi_Challenge`

# 2. Create a Virtual Envrionment
- `python3 -m venv .venv`
### If venv creation fails due to keyboard interrupt:
- `rm -rf .venv`
- `python3 -m venv .venv`

# 3. Activate the Virtual Envrionment
### macOS/Linux
 - `source .venv/bin/activate`
### Windows (PowerShell)
- `.venv\Scripts\Activate.ps1`

# 4. Install Dependencies
- `python -m pip install --upgrade pip`
- `python -m pip install -r requirements.txt`

# 5. Run the Application
- `python3 main.py`
