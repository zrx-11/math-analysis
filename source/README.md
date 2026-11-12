# 构建脚本

把本目录（含 `fonts/`、`katex.min.css`、`katex.min.js`、`auto-render.min.js`）当作工作目录，运行：

```bash
python3 insert_chapters.py
```

会生成 `数学分析18-21章从零推导.html`（KaTeX 与字体 base64 内联，单文件离线可用）。

- `build_skeleton.py`：骨架（样式、导航、交互、KaTeX 内联），末尾留 `<!-- REST_CHAPTERS -->` 锚点
- `chapters_a.py` ~ `chapters_e.py`：五批章节内容
- `insert_chapters.py`：替换锚点，输出最终 HTML（幂等）
- `pdf_text/`：源 PDF 的 PyMuPDF 文本提取，仅用于核对结构
