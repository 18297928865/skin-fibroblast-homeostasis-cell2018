import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECTIONS_DIR = os.path.join(BASE_DIR, "sections")

SECTION_FILES = [
    "sec1_front_intro.html",
    "sec2_results_1_3.html",
    "sec3_results_4_8.html",
    "sec4_discussion.html",
    "sec5_methods.html",
    "sec6_supp_figs.html",
    "sec7_summary_bg.html",
]

body_parts = []
for fname in SECTION_FILES:
    with open(os.path.join(SECTIONS_DIR, fname), "r", encoding="utf-8") as f:
        body_parts.append(f.read())

content_html = "\n\n".join(body_parts)

HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>位置稳定性与膜占据定义体内皮肤成纤维细胞稳态 · Cell (2018) 全文精译与文献汇报</title>
  <style>
    :root {{
      --bg: #f8fafc;
      --surface: #ffffff;
      --surface-alt: #f1f5f9;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --accent: #0f766e;
      --accent-soft: #ccfbf1;
      --accent-dark: #115e59;
      --highlight-bg: #f0fdfa;
      --code-bg: #f1f5f9;
      --shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
      --sidebar-w: 290px;
    }}
    [data-theme="dark"] {{
      --bg: #0f172a;
      --surface: #1e293b;
      --surface-alt: #263349;
      --text: #e2e8f0;
      --text-muted: #94a3b8;
      --border: #334155;
      --accent: #2dd4bf;
      --accent-soft: #134e4a;
      --accent-dark: #5eead4;
      --highlight-bg: #132a2e;
      --code-bg: #0f172a;
      --shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }}

    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.85;
      font-size: 16px;
      transition: background 0.2s, color 0.2s;
    }}

    /* Reading progress bar */
    #progress-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: linear-gradient(90deg, var(--accent), #38bdf8);
      z-index: 1000;
      transition: width 0.1s linear;
    }}

    /* Layout */
    .layout {{
      display: flex;
      min-height: 100vh;
    }}

    /* Sidebar TOC */
    .sidebar {{
      position: fixed;
      top: 0;
      left: 0;
      width: var(--sidebar-w);
      height: 100vh;
      background: var(--surface);
      border-right: 1px solid var(--border);
      padding: 20px 16px 32px;
      overflow-y: auto;
      z-index: 900;
      transition: transform 0.25s ease;
    }}
    .sidebar-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}
    .sidebar-brand {{
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--accent);
      letter-spacing: 0.02em;
    }}
    .theme-btn {{
      background: var(--surface-alt);
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.8rem;
      cursor: pointer;
    }}
    .theme-btn:hover {{ border-color: var(--accent); }}

    .toc-group {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin: 14px 0 6px 8px;
      font-weight: 700;
    }}
    .toc-list {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .toc-list a {{
      display: block;
      padding: 5px 10px;
      border-radius: 6px;
      color: var(--text);
      text-decoration: none;
      font-size: 0.84rem;
      line-height: 1.4;
      transition: background 0.15s, color 0.15s;
    }}
    .toc-list a:hover {{
      background: var(--surface-alt);
      color: var(--accent);
    }}
    .toc-list a.active {{
      background: var(--accent-soft);
      color: var(--accent-dark);
      font-weight: 600;
    }}
    .toc-sub {{
      padding-left: 14px;
    }}
    .toc-sub a {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    /* Mobile menu button */
    .mobile-toggle {{
      display: none;
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 950;
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: 999px;
      padding: 10px 16px;
      font-size: 0.9rem;
      font-weight: 600;
      box-shadow: 0 6px 18px rgba(0,0,0,0.22);
      cursor: pointer;
    }}

    /* Main Content */
    .main-content {{
      margin-left: var(--sidebar-w);
      flex: 1;
      padding: 36px 40px 80px;
      max-width: calc(980px + var(--sidebar-w));
    }}

    .paper-section {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 34px 40px;
      margin-bottom: 28px;
      box-shadow: var(--shadow);
    }}

    .journal-badge {{
      display: inline-block;
      background: var(--accent-soft);
      color: var(--accent-dark);
      font-weight: 600;
      font-size: 0.82rem;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 14px;
    }}

    .paper-title {{
      font-size: 1.95rem;
      line-height: 1.3;
      margin: 0 0 8px;
      color: var(--text);
    }}
    .paper-title-en {{
      font-size: 1.12rem;
      color: var(--text-muted);
      font-style: italic;
      margin: 0 0 18px;
    }}

    .authors-block {{
      background: var(--surface-alt);
      border-radius: 10px;
      padding: 14px 18px;
      font-size: 0.9rem;
      margin-bottom: 24px;
    }}
    .authors-block p {{ margin: 4px 0; }}
    .affiliations {{ color: var(--text-muted); font-size: 0.84rem; }}

    .front-grid {{
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 20px;
      align-items: start;
    }}
    .front-card {{
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 16px;
    }}
    .front-card h3 {{
      margin-top: 0;
      font-size: 1rem;
      color: var(--accent);
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }}
    .highlights-card ul {{
      margin: 8px 0 0;
      padding-left: 18px;
    }}
    .highlights-card li {{
      margin-bottom: 8px;
      font-size: 0.93rem;
    }}
    .inbrief-card {{
      background: var(--highlight-bg);
      border-color: var(--accent);
    }}

    h2 {{
      font-size: 1.45rem;
      margin: 0 0 18px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--accent);
      color: var(--text);
    }}
    h3 {{
      font-size: 1.16rem;
      margin: 28px 0 12px;
      color: var(--accent-dark);
    }}
    h4 {{
      font-size: 1.02rem;
      margin: 20px 0 8px;
      color: var(--text);
    }}

    p {{
      margin: 0 0 15px;
      text-align: justify;
    }}

    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.88em;
      background: var(--code-bg);
      padding: 1px 6px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }}

    a {{ color: var(--accent); }}

    .fig-ref {{
      display: inline-block;
      background: var(--accent-soft);
      color: var(--accent-dark);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.88em;
      padding: 0 6px;
      border-radius: 4px;
      transition: transform 0.12s, background 0.12s;
    }}
    .fig-ref:hover {{
      background: var(--accent);
      color: #fff;
    }}

    /* Figures */
    .paper-figure {{
      margin: 26px 0;
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
    }}
    .paper-figure img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      background: #fff;
      box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      cursor: zoom-in;
      transition: transform 0.15s ease;
    }}
    .paper-figure img:hover {{
      transform: scale(1.008);
    }}
    .paper-figure figcaption {{
      margin-top: 14px;
      text-align: left;
      font-size: 0.89rem;
      line-height: 1.7;
      color: var(--text);
      padding: 10px 14px;
      background: var(--surface);
      border-radius: 8px;
      border-left: 3px solid var(--accent);
    }}

    .info-note {{
      margin-top: 24px;
      padding: 14px 18px;
      background: var(--surface-alt);
      border-left: 4px solid var(--accent);
      border-radius: 8px;
      font-size: 0.9rem;
      color: var(--text-muted);
    }}

    /* Tables */
    .table-wrap {{
      overflow-x: auto;
      margin: 16px 0 24px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 9px 12px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: var(--surface-alt);
      font-weight: 700;
    }}
    .table-group td {{
      background: var(--accent-soft);
      color: var(--accent-dark);
      font-weight: 700;
    }}

    /* Analysis / Journal Club Section */
    .analysis-section {{
      border-top: 5px solid var(--accent);
    }}
    .analysis-banner {{
      background: linear-gradient(135deg, var(--highlight-bg), var(--surface-alt));
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 26px;
    }}
    .analysis-banner h2 {{
      border: none;
      margin: 8px 0 6px;
      padding: 0;
    }}
    .analysis-banner p {{ margin: 0; color: var(--text-muted); }}
    .analysis-tag {{
      display: inline-block;
      background: var(--accent);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}

    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 16px 0 24px;
    }}
    .insight-card {{
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px 20px;
      position: relative;
    }}
    .card-num {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--accent);
      opacity: 0.35;
      position: absolute;
      top: 10px;
      right: 16px;
    }}
    .insight-card h4 {{
      margin: 0 0 10px;
      padding-right: 34px;
      color: var(--accent-dark);
    }}
    .insight-card p {{
      font-size: 0.91rem;
      margin: 0;
    }}

    .styled-list {{
      padding-left: 20px;
    }}
    .styled-list li {{
      margin-bottom: 10px;
    }}

    .bg-item {{
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 14px;
    }}
    .bg-item h4 {{
      margin: 0 0 8px;
      color: var(--accent-dark);
    }}
    .bg-item p:last-child, .bg-item ul:last-child {{ margin-bottom: 0; }}

    .jc-box {{
      background: var(--highlight-bg);
      border: 1px solid var(--accent);
      border-radius: 12px;
      padding: 20px 24px;
    }}
    .jc-box h4 {{
      margin-top: 6px;
      color: var(--accent-dark);
    }}
    .jc-box li {{ margin-bottom: 10px; }}

    /* Lightbox Modal */
    .lightbox {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.9);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 24px;
      cursor: zoom-out;
    }}
    .lightbox.open {{ display: flex; }}
    .lightbox img {{
      max-width: 95vw;
      max-height: 92vh;
      border-radius: 8px;
      background: #fff;
      box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }}
    .lightbox-hint {{
      position: fixed;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%);
      color: #e2e8f0;
      font-size: 0.85rem;
      background: rgba(0,0,0,0.55);
      padding: 6px 14px;
      border-radius: 999px;
    }}

    @media (max-width: 980px) {{
      .sidebar {{
        transform: translateX(-100%);
      }}
      .sidebar.open {{
        transform: translateX(0);
        box-shadow: 4px 0 24px rgba(0,0,0,0.25);
      }}
      .mobile-toggle {{ display: block; }}
      .main-content {{
        margin-left: 0;
        padding: 20px 16px 80px;
      }}
      .paper-section {{ padding: 22px 18px; }}
      .front-grid {{ grid-template-columns: 1fr; }}
    }}

    @media print {{
      .sidebar, .mobile-toggle, #progress-bar, .lightbox {{ display: none !important; }}
      .main-content {{ margin-left: 0; padding: 0; max-width: 100%; }}
      .paper-section {{ box-shadow: none; border: none; padding: 10px 0; }}
    }}
  </style>
</head>
<body>
  <div id="progress-bar"></div>
  <button class="mobile-toggle" id="mobile-toggle">目录导航</button>

  <div class="layout">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <span class="sidebar-brand">Cell (2018) 文献精译</span>
        <button class="theme-btn" id="theme-btn">深色模式</button>
      </div>

      <div class="toc-group">论文正文（逐字翻译）</div>
      <ul class="toc-list">
        <li><a href="#sec-header">标题 · 图文摘要 · 亮点</a></li>
        <li><a href="#sec-summary">摘要（Summary）</a></li>
        <li><a href="#sec-introduction">引言（Introduction）</a></li>
        <li><a href="#sec-results">结果（Results）</a>
          <ul class="toc-list toc-sub">
            <li><a href="#res-1">1. 无毛皮肤中成纤维细胞稳定</a></li>
            <li><a href="#res-2">2. 邻近细胞丢失后稳定性维持</a></li>
            <li><a href="#fig-1">↳ Figure 1</a></li>
            <li><a href="#res-3">3. 成纤维细胞膜维持高占据率</a></li>
            <li><a href="#fig-2">↳ Figure 2</a></li>
            <li><a href="#res-4">4. 动态膜活动代偿邻居丢失</a></li>
            <li><a href="#fig-3">↳ Figure 3</a></li>
            <li><a href="#res-5">5. 较大损伤后的膜延伸与修复</a></li>
            <li><a href="#fig-4">↳ Figure 4</a></li>
            <li><a href="#res-6">6. 非重塑有毛皮肤的稳定性</a></li>
            <li><a href="#res-7">7. 生理性真皮重塑期稳定性丧失</a></li>
            <li><a href="#fig-5">↳ Figure 5</a></li>
            <li><a href="#res-8">8. 衰老中的局部成簇丢失与代偿</a></li>
            <li><a href="#fig-6">↳ Figure 6</a></li>
          </ul>
        </li>
        <li><a href="#sec-discussion">讨论（Discussion）</a></li>
      </ul>

      <div class="toc-group">方法与补充材料</div>
      <ul class="toc-list">
        <li><a href="#sec-methods">STAR★Methods 逐字翻译</a>
          <ul class="toc-list toc-sub">
            <li><a href="#meth-krt">关键资源表</a></li>
            <li><a href="#meth-models">实验模型（小鼠）</a></li>
            <li><a href="#meth-details">方法详情（成像/消融/分析）</a></li>
            <li><a href="#meth-stats">统计分析与代码</a></li>
          </ul>
        </li>
        <li><a href="#sec-supp-figs">补充图表（Figures S1–S6）</a>
          <ul class="toc-list toc-sub">
            <li><a href="#fig-S1">Figure S1 · 解剖与 SHG</a></li>
            <li><a href="#fig-S2">Figure S2 · mTmG 与 Rac1</a></li>
            <li><a href="#fig-S3">Figure S3 · 消融后膜追踪</a></li>
            <li><a href="#fig-S4">Figure S4 · 垂直膜延伸</a></li>
            <li><a href="#fig-S5">Figure S5 · 跨组织密度对比</a></li>
            <li><a href="#fig-S6">Figure S6 · 衰老有毛皮肤空隙</a></li>
          </ul>
        </li>
      </ul>

      <div class="toc-group">文献汇报深度总结</div>
      <ul class="toc-list">
        <li><a href="#ana-novelty">一、核心新颖点（Novelty）</a></li>
        <li><a href="#ana-significance">二、重要性与科学意义</a></li>
        <li><a href="#ana-bg">三、背景知识补充</a></li>
        <li><a href="#ana-glossary">四、专业词汇表</a></li>
        <li><a href="#ana-jc">五、汇报主线与 Q&amp;A 预演</a></li>
      </ul>
    </aside>

    <main class="main-content">
      {content_html}
    </main>
  </div>

  <div class="lightbox" id="lightbox">
    <img id="lightbox-img" src="" alt="放大预览">
    <div class="lightbox-hint">点击任意处或按 ESC 键关闭放大视图</div>
  </div>

  <script>
    // Dark mode toggle
    const themeBtn = document.getElementById('theme-btn');
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {{
      document.documentElement.setAttribute('data-theme', 'dark');
      themeBtn.textContent = '浅色模式';
    }}
    themeBtn.addEventListener('click', () => {{
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {{
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        themeBtn.textContent = '深色模式';
      }} else {{
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeBtn.textContent = '浅色模式';
      }}
    }});

    // Mobile sidebar toggle
    const mobileToggle = document.getElementById('mobile-toggle');
    const sidebar = document.getElementById('sidebar');
    mobileToggle.addEventListener('click', () => {{
      sidebar.classList.toggle('open');
    }});
    sidebar.querySelectorAll('a').forEach(a => {{
      a.addEventListener('click', () => sidebar.classList.remove('open'));
    }});

    // Lightbox for zoomable figures
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    document.querySelectorAll('img.zoomable').forEach(img => {{
      img.addEventListener('click', () => {{
        lightboxImg.src = img.src;
        lightbox.classList.add('open');
      }});
    }});
    lightbox.addEventListener('click', () => lightbox.classList.remove('open'));
    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') lightbox.classList.remove('open');
    }});

    // Reading progress bar & active TOC highlight
    const progressBar = document.getElementById('progress-bar');
    const tocLinks = Array.from(document.querySelectorAll('.toc-list a'));
    const targets = tocLinks
      .map(link => document.querySelector(link.getAttribute('href')))
      .filter(Boolean);

    window.addEventListener('scroll', () => {{
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = pct + '%';

      let currentId = '';
      for (const el of targets) {{
        if (el.getBoundingClientRect().top <= 140) {{
          currentId = el.id;
        }}
      }}
      tocLinks.forEach(link => {{
        link.classList.toggle('active', link.getAttribute('href') === '#' + currentId);
      }});
    }}, {{ passive: true }});
  </script>
</body>
</html>
"""

out_path = os.path.join(BASE_DIR, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)
print(f"Successfully generated {out_path} ({os.path.getsize(out_path):,} bytes)")
