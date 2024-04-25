import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="version.txt",
    version="1.0.0",
    company_name="Atul Mahankal",
    file_description="Test Windows Service",
    internal_name="service_application",
    legal_copyright="© Atul Mahankal. All rights reserved.",
    original_filename="service_application.exe",
    product_name="Test Windows Service",
    translations=[0, 1200]
)