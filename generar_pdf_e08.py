import sys
import subprocess

def install_fpdf():
    try:
        import fpdf
    except ImportError:
        print("Instalando fpdf2...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2"])

install_fpdf()
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, 'INF-8239 Ciencia de Datos II - Ejercicio 08', align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', 'I', 11)
        self.cell(0, 8, 'Expediente de Gobernanza y Simulacro de Incidente (U04.LAB13)', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', align='C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.set_fill_color(220, 235, 255)
        self.cell(0, 8, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def chapter_body(self, text):
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 6, text)
        self.ln(4)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 6, 'Estudiante: Kendy Baez Santos', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, 'Repositorio: https://github.com/kendyb18-dotcom/INF8239_U04_Gobernanza_DSS_Proyecto_Base_uv.git', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.chapter_title('1. Inventario, Minimizacion y Retencion')
pdf.chapter_body(
    "Sistema analizado: Territorial Review DSS - Synthetic.\\n"
    "- Minimizacion de datos: Exclusion estricta de identificadores directos (nombre, documento, telefono, correo) "
    "durante el entrenamiento. Conservacion de variables sensibles unicamente para auditorias de equidad.\\n"
    "- Politica de retencion: Almacenamiento controlado en entorno seguro con trazabilidad de versiones."
)

pdf.chapter_title('2. Datasheet y Model Card Trazables')
pdf.chapter_body(
    "Se documentaron las especificaciones tecnicas y de procedencia del dataset sintetico y del modelo "
    "baseline (Logistic Regression). Se definieron explícitamente los usos prohibidos (intervención automática, "
    "declaración de emergencia y elegibilidad) para evitar la expansión no autorizada de la autoridad del DSS."
)

pdf.chapter_title('3. Matriz RACI y Traspaso de Roles')
pdf.chapter_body(
    "Se estructuro la matriz RACI (student_inputs/raci.csv) asegurando un unico Accountable y multiples "
    "Responsible por fase criticada:\\n"
    "- Data Quality: Data Engineer (R), Product Owner (A).\\n"
    "- Model Validation: Data Scientist (R), Product Owner (A).\\n"
    "- Deployment: ML Engineer (R), Product Owner (A).\\n"
    "- Incident Response: ML Engineer (R), Institutional Owner (A)."
)

pdf.chapter_title('4. Monitoreo, Runbook y Simulacro de Incidente')
pdf.chapter_body(
    "Se ejecuto el simulacro de incidente (INC-2026-001) documentado en reports/lab13/INCIDENT_POSTMORTEM.md:\\n"
    "- Deteccion: Alerta por exceso de brecha de recall.\\n"
    "- Contencion: Activación de revisión humana obligatoria (REVIEW) y uso de baseline seguro.\\n"
    "- Preservacion y Postmortem: Resguardo de logs de prediccion, analisis de deriva (drift) y plan de reentrenamiento."
)

pdf.chapter_title('5. Pruebas, Calidad Documental y Declaracion de IA')
pdf.chapter_body(
    "Pruebas y Versionado: Suite completa de pruebas unitarias superadas en verde (pytest -q) y etiquetado u04-lab13.\\n"
    "Declaracion de Uso de Herramientas de IA:\\n"
    "Se empleo asistencia de Inteligencia Artificial (Google Gemini) para la estructuracion del script fpdf2, "
    "la sintesis de los reportes y la revision de sintaxis en archivos YAML/Python.\\n"
    "Responsabilidad: Todas las decisiones normativas, valores de umbrales, asignaciones RACI y conclusiones eticas "
    "fueron evaluadas, validadas y asumidas enteramente por el estudiante."
)

output_file = 'U04_E08_KendyBaez.pdf'
pdf.output(output_file)
print(f"PDF generado exitosamente: {output_file}")