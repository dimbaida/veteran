import io
from pathlib import Path
import pdfrw
from django.conf import settings
from reportlab.lib.pagesizes import A5, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


class Cell:
    def __init__(self, text, x, y, font='regular', size=9, align="center"):
        self.text = text
        self.x = x
        self.y = y
        self.font = 'RobotoMono-Regular'
        self.size = size
        self.align = align

        if font == 'bold':
            self.font = 'RobotoMono-Bold'
        if font == 'text':
            self.font = 'Aptos'


class Paycheck:
    def __init__(self,
                 consumer: str,
                 agreement: str,
                 month: str,
                 value_day_prev: int,
                 value_day_curr: int,
                 value_night_prev: int,
                 value_night_curr: int,
                 purpose: str
                 ):
        self.consumer: str = consumer
        self.agreement: str = agreement
        self.month: str = month
        self.value_day_curr: int = value_day_curr
        self.value_day_prev: int = value_day_prev
        self.value_night_prev: int = value_night_prev
        self.value_night_curr: int = value_night_curr
        self.purpose: str = purpose

    def render(self):
        print('PAYCHECK:RENDER')
        PRICE_DAY = 4.32
        PRICE_NIGHT = 2.16

        content = []

        # header
        content.append(Cell(self.consumer, 437, 364, font='text', size=11, align="left"))
        content.append(Cell(self.agreement, 437, 335, font='text', size=11, align="left"))

        # row 1
        value_day_diff = self.value_day_curr - self.value_day_prev
        sum_day = (self.value_day_curr - self.value_day_prev) * 4.32

        content.append(Cell(self.month, 184, 175))
        content.append(Cell(str(self.value_day_prev), 249, 175))
        content.append(Cell(str(self.value_day_curr), 315, 175))
        content.append(Cell(str(value_day_diff), 379, 175))
        content.append(Cell(str(PRICE_DAY), 449, 175))
        content.append(Cell(f"{sum_day:.2f}", 521, 175))

        # row 2
        value_day_tech = (self.value_day_curr - self.value_day_prev) * 0.25
        sum_day_tech = value_day_tech * PRICE_DAY

        content.append(Cell(self.month, 184, 157))
        content.append(Cell(str(value_day_tech), 379, 157))
        content.append(Cell(str(PRICE_DAY), 449, 157))
        content.append(Cell(f"{sum_day_tech:.2f}", 521, 157))

        # row 3
        value_night_diff = self.value_night_curr - self.value_night_prev
        sum_night = value_night_diff * 0.25 * PRICE_NIGHT

        content.append(Cell(self.month, 184, 138.5))
        content.append(Cell(str(self.value_night_prev), 249, 138.5))
        content.append(Cell(str(self.value_night_curr), 315, 138.5))
        content.append(Cell(str(value_night_diff), 379, 138.5))
        content.append(Cell(str(PRICE_NIGHT), 449, 138.5))
        content.append(Cell(f"{sum_night:.2f}", 521, 138.5))

        # row 4
        value_night_tech = (self.value_night_curr - self.value_night_prev) * 0.25
        sum_night_tech = value_night_tech * 0.25 * PRICE_NIGHT

        content.append(Cell(self.month, 184, 121))
        content.append(Cell(str(value_night_tech), 379, 121))
        content.append(Cell(str(PRICE_NIGHT), 449, 121))
        content.append(Cell(f"{sum_night_tech:.2f}", 521, 121))

        total = sum_day + sum_day_tech + sum_night + sum_night_tech
        content.append(Cell(f"{total:.2f}", 521, 100, 'bold', 10))

        purpose_line_01, purpose_line_02 = self.purpose.split('\n')
        content.append(Cell(purpose_line_01, 171, 70, font="text", align="left", size=11))
        content.append(Cell(purpose_line_02, 171, 56, font="text", align="left", size=11))

        canvas_data = self.get_overlay_canvas(content)

        template_path = settings.BASE_DIR / 'electricity/static/pdf/blank.pdf'

        form = self.merge(canvas_data, template_path=template_path)
        return form

    @staticmethod
    def get_overlay_canvas(cells) -> io.BytesIO:
        data = io.BytesIO()
        pdf = canvas.Canvas(data, pagesize=landscape(A5))

        fonts_folder = template_path = settings.BASE_DIR / 'electricity/static/fonts'

        pdfmetrics.registerFont(TTFont('RobotoMono-Regular', fonts_folder / 'RobotoMono-Regular.ttf'))
        pdfmetrics.registerFont(TTFont('RobotoMono-Bold', fonts_folder / 'RobotoMono-Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Aptos', fonts_folder / 'aptos.ttf'))

        for cell in cells:
            pdf.setFont(cell.font, cell.size)
            if cell.align == "left":
                pdf.drawString(x=cell.x, y=cell.y, text=cell.text)
            else:
                pdf.drawCentredString(x=cell.x, y=cell.y, text=cell.text)

        pdf.save()
        data.seek(0)
        return data

    @staticmethod
    def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
        template_pdf = pdfrw.PdfReader(template_path)
        overlay_pdf = pdfrw.PdfReader(overlay_canvas)
        for page, data in zip(template_pdf.pages, overlay_pdf.pages):
            overlay = pdfrw.PageMerge().add(data)[0]
            pdfrw.PageMerge(page).add(overlay).render()
        form = io.BytesIO()
        pdfrw.PdfWriter().write(form, template_pdf)
        form.seek(0)
        return form

