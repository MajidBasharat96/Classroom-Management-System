
from reportlab.pdfgen import canvas

def generate_report(student, marks):
    file = f"{student}_report.pdf"
    c = canvas.Canvas(file)
    c.drawString(100,750,"Student Report Card")
    c.drawString(100,720,student)
    for m in marks:
        c.drawString(100,700,f"{m.subject} {m.obtained_marks}")
    c.save()
