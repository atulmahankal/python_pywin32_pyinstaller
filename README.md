# Sample Windows Service App

This is a sample Python project demonstrating how to create a Windows service as well as a command-line application.

## Installation

1. Clone the repository:
	```bash
	git clone https://github.com/atulmahankal/python_pywin32_pyinstaller
	```

2. Create a virtual environment:
	```bash
	python -m venv .venv
	```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Linux/MacOS: `source .venv/bin/activate`

4. Install required packages: 
	```bash
	pip install -r requirements.txt
	```
	
5. Update version information (optional):
	```bash
	python versionfile.py
	```

## Building and Installation

1. Build the project:
	```bash
	python build.py
	```

2. Install the service:
	```bash
	disk/service.exe install
	```

## Service Management

- Start the service:
```bash
disk/service.exe start
```

- Restart the service:
```bash
disk/service.exe restart
```

- Stop the service:
```bash
disk/service.exe stop
```

- Uninstall the service:
```bash
disk/service.exe stop
disk/service.exe remove
```
