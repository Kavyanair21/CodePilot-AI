from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report, score, filename="CodePilot_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>CodePilot AI Review Report</b>", styles["Title"])
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(f"<b>Overall Score:</b> {score}/100", styles["Heading2"])
    )

    elements.append(Spacer(1, 20))

    for section, content in report.items():

        elements.append(
            Paragraph(section, styles["Heading2"])
        )

        elements.append(
            Paragraph(str(content), styles["BodyText"])
        )

        elements.append(
            Spacer(1, 15)
        )

    doc.build(elements)

    return filename