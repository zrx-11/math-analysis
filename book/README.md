# 数学分析（第五版）上下册 · 知枢学习系统

华东师大《数学分析》第五版上下册的点化学习库，总入口 `index.html`。

## 目录结构

| 路径 | 说明 |
|---|---|
| `index.html` | 总学习手册（单文件，统一入口，470 KB） |
| `index.md` | Markdown 导航页 |
| `00-跨书总览/` | 学习路线、跨书概念映射、综合检验建议 |
| `01-数学分析上册/` | 11 章正文、6 个概念页、manifest、学习伴侣 HTML、速查表、模式库 |
| `02-数学分析下册/` | 12 章正文、6 个概念页、manifest、学习伴侣 HTML、速查表、模式库 |
| `_scan/` | 原书目录页渲染图与 OCR 文本（仅用于核对章节结构） |

## 怎么用

1. 双击 `index.html`，或用 GitHub Pages 打开。
2. 左侧目录切换书籍与章节；「学习路径」按依赖顺序推进。
3. 每章末有自测题，答错会沿前置链给出根因链接。
4. 「诊断测试」随机抽题；「抽认卡」翻转记忆；「术语表」「速查表」查定义与公式。
5. 进度保存在浏览器 localStorage，可导出/导入 JSON。

## 重新构建

```bash
# 单书伴侣
cd 01-数学分析上册
python3 <zhishu>/scripts/build_companion.py --manifest manifest.json --out 数学分析上册学习伴侣.html

# 总入口
python3 <zhishu>/scripts/build_handbook.py --root .
```

## 验证

```bash
python3 <zhishu>/scripts/verify_handbook.py --index index.html --chromium /usr/local/bin/chromium
```

本次结果：39/39 通过，控制台无错误。

## 已知边界

- 公式渲染依赖 CDN（npmmirror → jsdelivr → unpkg 三源回退），完全离线时公式显示源码，文字与导航不受影响。
- 原书为扫描件，正文按教材结构重写，例题与数值均自行验算；不与原书页码逐字对应。
- 章节页码标注为原书大致位置，用于溯源，不保证精确到行。
