import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A3, A4
import AweSomeTk as tk
from collections import namedtuple
import pypdftk

text_to_insert = namedtuple('InsertText', ['point', 'text', 'font', 'height', 'width_factor', 'look_factor'])


def get_fonts():
    for i in os.listdir('Fonts'):
        if 'ttf' in i:
            i_font_name = i.split('.')[0]
            pdfmetrics.registerFont(TTFont(i_font_name, i))


def general_drawing(drawing: tk.AweSomeTk, number: text_to_insert, title, page, total_page):
    """
    常规图框，插入图号、图名、页码、总页码
    :param drawing: AwesomeTk 对象
    :param number: 图号
    :param title: 图名
    :param page: 页码
    :param total_page: 总页码
    :return:
    """
    for txt in number, title, page, total_page:
        drawing.insert_text(
            txt.point,
            txt.text,
            txt.font,
            txt.height,
            txt.width_factor,
            txt.look_factor
        )
    drawing.canvas.showPage()
    drawing.canvas.save()


def stamp_pdf(old_pdf, tk_pdf, watermark_pdf, new_pdf):
    pypdftk.stamp(tk_pdf, watermark_pdf, r'pdf\WaterTk.pdf')
    pypdftk.stamp(old_pdf, r'pdf\WaterTk.pdf', new_pdf)


if __name__ == '__main__':

    # 所需输入参数
    pypdftk.PDFTK_PATH = r'C:\Program Files (x86)\PDFtk Server\bin\pdftk.exe'

    watermark_pdf = r'pdf\watermark.pdf'
    old_pdf = r'pdf\IN\old.pdf'
    tk_pdf = r'pdf\tk.pdf'

    draw_number = text_to_insert((365, 15), 'C-1-23', '仿宋_GB2312', 4, 0.75, 0)
    draw_title = text_to_insert((204, 15), '方案一 施工流程图', '仿宋_GB2312', 4, 0.75, 0)
    draw_page = text_to_insert((380, 282), '1', '仿宋_GB2312', 4, 0.75, 0)
    draw_total_page = text_to_insert((400, 282), '3', '仿宋_GB2312', 4, 0.75, 0)

    new_pdf = f'pdf\\OUT\\{draw_number.text}_{draw_title.text}_{draw_page.text}OF{draw_total_page.text}.pdf'

    # GO
    get_fonts()
    test_tk = tk.AweSomeTk(A3, watermark_pdf)
    general_drawing(test_tk, draw_number, draw_title, draw_page, draw_total_page)
    stamp_pdf(old_pdf, tk_pdf, watermark_pdf, new_pdf)


    # # 最基本应用
    # get_fonts()
    # test_tk = tk.AweSomeTk(A3)
    # test_tk.insert_text(
    #     (150, 97.5),
    #     'Good Question',
    #     'Arial',
    #     3,
    #     0.75
    # )
    # test_tk.insert_text(
    #     (150, 92.5),
    #     '图名图号',
    #     '仿宋',
    #     3,
    #     0.75
    # )
    # test_tk.canvas.showPage()
    # test_tk.canvas.save()



