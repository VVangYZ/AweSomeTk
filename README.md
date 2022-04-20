# AweSomeTk
为解决图纸图框变更问题，诸如图号命名规则改变、日期改变、图纸排序改变等情况。
可将原始图纸与图框拆分，原始图纸对应一个【唯一识别号】，该识别号恒定不变，通过识别号对应图纸信息，对应规则可更改。

## 基本实现思路
1. 一些需添加图框的【待处理图纸】，一个原始【图框文件】
2. 根据图纸文件名称所含编码与规定图名、图号、页码等进行对应（此处变量后续应可自定义）
3. 根据【图框文件】和生成【图名、图号等】组合成图框水印，依次叠加到【待处理图纸】上
4. 【处理后图纸】可根据图号、页码进行重命名

## 依赖项
1. `reportlab` 包，用来生成水印文件a
2. `pypdftk`及`pdftk`命令行工具，后者用来叠水印（效率较高），前者用来控制后者

## 示例
```Python
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
```
