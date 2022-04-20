from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os


class AweSomeTk:
    def __init__(self, drawingsize, pdf_name):
        self.canvas = canvas.Canvas(pdf_name, pagesize=drawingsize[::-1])
        self.add_text_time = 0

    def insert_text(self, text_point, text, font='Arial', text_height=3, text_width_factor=0.75, look_factor=0):
        """
        插入文本， 指定插入点（正中间）、字体、字高、宽度因子
        :param text_point: 插入点
        :param text: 插入内容
        :param font: 字体
        :param text_height: 字高
        :param text_width_factor: 宽度因子
        :param look_factor: 文字高度的经验值，有Arial、仿宋、仿宋_GB2312的默认值，若未赋值则其余默认 4
        """

        # 如果插入过则恢复尺寸
        if self.add_text_time == 0:
            self.canvas.saveState()
        else:
            self.canvas.restoreState()      # 恢复常规图像比例
            self.canvas.saveState()
        self.add_text_time += 1

        # 字号、坐标等调节
        if look_factor == 0:
            if font == 'Arial':
                font_factor = 197.97 / 50      # 经过测试得出的经验数值
            elif font == '仿宋':
                font_factor = 12.44 / 3
            elif font == '仿宋_GB2312':
                font_factor = 11.77 / 3
            else:
                font_factor = 4
        else:
            font_factor = look_factor

        font_size = text_height * font_factor    # 计算字号
        in_x = text_point[0] * mm / text_width_factor       # 计算插入x坐标
        in_y = text_point[1] * mm       # 计算插入y坐标

        # 插入文字
        self.canvas.scale(text_width_factor, 1)     # 按照宽度因子缩放图像
        self.canvas.setFont(font, font_size)        # 指定字体
        self.canvas.drawCentredString(              # 插入文字
            in_x,
            in_y - text_height * mm / 2,            # y 数值不用经验而是字号直接转化（不知为何）
            text
        )

        # 直接调整 horizontal 失败
        # text_width = self.canvas.stringWidth(text, font, font_size) * text_width_factor     # 计算文本宽度
        # in_text = self.canvas.beginText(in_x - text_width / 2, in_y)    # 建立文字对象
        # in_text.setFont(font, font_size)        # 设置文字特征
        # in_text.setHorizScale(text_width_factor * 100)
        # in_text.textOut(text)
        # self.canvas.drawText(in_text)









