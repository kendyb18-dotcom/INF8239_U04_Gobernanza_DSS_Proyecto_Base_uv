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
        self.cell(0, 10, 'INF-8239 Ciencia de Datos II - Ejercicio 07', align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', 'I', 11)
        self.cell(0, 8, 'Evaluacion de Impacto y Auditoria de Equidad (Expediente U04)', align='C', new_x="LMARGIN", new_y="NEXT")
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
pdf.cell(0, 6, 'Estudiante: Kendy Báez Santos', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, 'Repositorio: https://github.com/kendyb18-dotcom/INF8239_U04_Gobernanza_DSS_Proyecto_Base_uv.git', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.chapter_title('1. Finalidad, Interesados y Proporcionalidad (LAB11)')
pdf.chapter_body(
    "Sistema evaluado: Sistema de Apoyo a Decisiones de Riesgo Territorial (DSS-TR).\n"
    "- Proposito: Priorizar la asignacion de recursos preventivos y operativos en zonas vulnerables.\n"
    "- Obligacion legal vs Marco voluntario: El cumplimiento normativo de privacidad contrasta con "
    "los lineamientos voluntarios del NIST AI RMF adoptados para la gestion de riesgos socio-tecnicos."
)

pdf.chapter_title('2. Registro de Riesgos y NIST AI RMF')
pdf.chapter_body(
    "Se documentaron 8 riesgos especificos abarcando las dimensiones GOVERN, MAP, MEASURE y MANAGE. "
    "Se identificaron los riesgos criticos asociados a sesgos historicos de datos y dependencia de operadores, "
    "asignando controles preventivos, responsables directos y evidencias verificables en reports/lab11/."
)

pdf.chapter_title('3. Auditoria de Equidad y Desempeno (LAB12)')
pdf.chapter_body(
    "Se audito el clasificador baseline (Logistic Regression) frente a un arbol de decision usando Fairlearn:\n"
    "- Grupo G1 (101 muestras): Accuracy ~0.703 | Recall ~0.711 | FPR ~0.250\n"
    "- Grupo G2 (59 muestras): Accuracy ~0.746 | Recall ~0.850 | FPR ~0.375\n"
    "Se analizo la disparidad de recall e interseccionalidad, reconociendo que las brechas estadisticas "
    "requieren investigacion contextual y no constituyen prueba automatica de discriminacion causal."
)

pdf.chapter_title('4. Mitigacion, Trade-offs y Decision Final')
pdf.chapter_body(
    "Decision recomendada: GO_WITH_CONTROLS.\n"
    "Se selecciono el modelo logístico por su menor complejidad y alineacion con Green AI (menor uso computacional "
    "y tamano serializado de 3.56 KB). Se establecieron condiciones de retiro estrictas (parada si el sesgo de "
    "falsos negativos supera el 15%) y obligatoriedad de revision humana para evitar sesgos de automatizacion."
)

pdf.chapter_title('5. Declaracion de Uso de Herramientas de IA')
pdf.chapter_body(
    "Se utilizo asistencia de Inteligencia Artificial (Google Gemini) para:\n"
    "1. Estructuracion del script automatizado en fpdf2 para cumplir la rubrica del E07.\n"
)

output_file = 'U04_E07_KendyBaez.pdf'
pdf.output(output_file)
print(f"PDF generado exitosamente: {output_file}")