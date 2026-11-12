#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""章节内容 A：课程概览 + 数学地基 + 隐函数"""
from pathlib import Path

CH_A = r"""<!-- ===== 章节：intro ===== -->
<section class="chapter" id="intro" style="display:block">
  <div class="breadcrumb"></div>
  <h2><span class="num">0</span>课程概览：从初中数学到曲线积分</h2>
  <p class="lead">本课程把《数学分析》下册第 18-21 章（隐函数与几何应用、条件极值、含参量积分、欧拉积分、两类曲线积分、二重积分）从初中数学开始逐层推导。每一条公式，你都亲手算得出来。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 怎么学这门课</div>
    这门课只有一个要求：<b>每一步都别跳</b>。所有公式都会从初中知识（斜率、面积、方程组、配方）一步步推出来，每个新符号第一次出现都会用大白话解释。遇到看不懂的地方，展开"推导步骤"逐行看，那里连"两边同时除以 2"这种步骤都不会省略。
  </div>

  <h3>知识树：整门课的地图</h3>
  <p>下面这棵树是整门课的依赖关系。所有东西都长在初中数学的根上。点击节点可跳转到对应章节。</p>
  <div class="knowledge-tree">
    <div class="kt-level"><span class="kt-label root">根系（初中数学）</span>
      <a class="kt-node root" data-goto="math-foundation">函数与方程</a>
      <a class="kt-node root" data-goto="math-foundation">直线斜率</a>
      <a class="kt-node root" data-goto="math-foundation">面积·勾股定理</a>
      <a class="kt-node root" data-goto="math-foundation">解方程组</a>
      <a class="kt-node root" data-goto="math-foundation">配方与最值</a>
      <a class="kt-node root" data-goto="math-foundation">向量与投影</a>
    </div>
    <div class="kt-level"><span class="kt-label base">基础概念（大学一年级前段）</span>
      <a class="kt-node base" data-goto="math-foundation">导数=瞬时斜率</a>
      <a class="kt-node base" data-goto="math-foundation">定积分=分割求和</a>
      <a class="kt-node base" data-goto="math-foundation">偏导数=只动一个变量</a>
      <a class="kt-node base" data-goto="math-foundation">连续=笔不离纸</a>
      <a class="kt-node base" data-goto="math-foundation">梯度=最陡爬坡方向</a>
    </div>
    <div class="kt-level"><span class="kt-label tool">领域工具（本章新学）</span>
      <a class="kt-node tool" data-goto="implicit-func">隐函数定理</a>
      <a class="kt-node tool" data-goto="implicit-system">雅可比行列式</a>
      <a class="kt-node tool" data-goto="conditional-ext">拉格朗日乘数法</a>
      <a class="kt-node tool" data-goto="param-integral">含参量积分</a>
      <a class="kt-node tool" data-goto="improper-param">一致收敛</a>
      <a class="kt-node tool" data-goto="euler-integral">Γ 函数与 B 函数</a>
      <a class="kt-node tool" data-goto="line-integral-2">第二型曲线积分</a>
      <a class="kt-node tool" data-goto="double-integral">二重积分与面积</a>
    </div>
    <div class="kt-level"><span class="kt-label">目标知识主干</span>
      <a class="kt-node main" data-goto="implicit-func">隐函数与隐函数组</a>
      <a class="kt-node main" data-goto="geometry-app">切线·法线·切平面</a>
      <a class="kt-node main" data-goto="conditional-ext">条件极值</a>
      <a class="kt-node main" data-goto="param-integral">含参量积分理论</a>
      <a class="kt-node main" data-goto="euler-integral">欧拉积分</a>
      <a class="kt-node main" data-goto="line-integral">第一型曲线积分</a>
      <a class="kt-node main" data-goto="line-integral-2">第二型曲线积分</a>
      <a class="kt-node main" data-goto="double-integral">二重积分概念</a>
      <a class="kt-node main" data-goto="double-calc">直角坐标下计算</a>
      <a class="kt-node main" data-goto="exercises">习题课与复习</a>
    </div>
  </div>

  <h3>三章内容一句话地图</h3>
  <div class="table-wrap"><table>
    <tr><th style="width:16%">章</th><th style="width:40%">学什么</th><th>一个生活问题</th></tr>
    <tr><td>18 章</td><td>隐函数、隐函数组、几何应用、条件极值</td><td>"由方程 $x^3+y^3=3xy$ 能不能解出 $y$？曲线在一点的切线怎么求？戴条件的最值怎么求？"</td></tr>
    <tr><td>19 章</td><td>含参量积分（正常+反常）、欧拉积分</td><td>"积分的上下限和被积函数里藏着一个参数，积分结果随参数怎么变？"</td></tr>
    <tr><td>20 章</td><td>第一型曲线积分、第二型曲线积分</td><td>"一根弯铁丝质量不均匀，总质量怎么算？变力推着质点沿曲线走，做了多少功？"</td></tr>
    <tr><td>21 章</td><td>二重积分的概念、直角坐标下的计算</td><td>"一片曲面下的体积怎么量？能不能化成两次一元积分？"</td></tr>
  </table></div>

  <h3>学习路径（推荐顺序）</h3>
  <div class="callout callout-key">
    <div class="callout-title">必须按顺序走吗？</div>
    前两章（数学地基、隐函数）是后面所有内容的地基，<b>不要跳过</b>。从"含参量正常积分"开始，与前面关系较独立，但"欧拉积分"依赖"含参量反常积分"，"曲线积分"依赖数学地基里的弧长，仍建议按目录顺序。
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：math-foundation ===== -->
<section class="chapter" id="math-foundation" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">1</span>数学地基：从初中数学开始</h2>
  <p class="lead">这一章是整门课的"地基"。这里只用到初中数学，但每一条都会在后面的章节里反复出现。学完它，你就有了推导后面所有公式的工具。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 为什么从初中开始？</div>
    隐函数要导数，导数要斜率，斜率是初中就学过的"纵坐标差 ÷ 横坐标差"。曲线积分要弧长，弧长要勾股定理，勾股定理也是初中的。拉格朗日乘数法要方程组和极值，还是初中的。所以：<b>只要初中数学够扎实，后面没有一道坎是迈不过去的。</b>
  </div>

  <h3>1.1 函数与方程：两件事，一个视角</h3>
  <p><b>函数</b>：一个"机器"，扔一个数进去，吐一个数出来。记作 $y=f(x)$，读作"$y$ 等于 $f$ 在 $x$ 处的值"。</p>
  <p><b>方程</b>：一个"问号"——$F(x,y)=0$ 问的是"哪些 $(x,y)$ 让这个式子成立"。</p>
  <p>关键视角：<b>一个方程 $F(x,y)=0$ 就是一条曲线</b>。因为把满足方程的所有点 $(x,y)$ 画在平面上，它们连成的图形就是曲线。例如 $x^2+y^2=1$ 是单位圆，$y=x^2$ 是抛物线。</p>
  <div class="formula">$$x^2 + y^2 = 1 \;\Rightarrow\; \text{圆；}\qquad y = x^2 \;\Rightarrow\; \text{抛物线；}\qquad x^3+y^3=3xy \;\Rightarrow\; \text{一条弯弯的曲线}$$</div>
  <p><b>两种表述的桥梁</b>：$y=f(x)$ 也可以写成 $F(x,y)=y-f(x)=0$。也就是说，"显函数"只是"隐式方程"的特例——把 $y$ 单独解出来了而已。</p>

  <h3>1.2 直线的斜率：导数的真正祖先</h3>
  <p><b>斜率</b>：一条直线有多"陡"。初中定义：</p>
  <div class="formula">$$\text{斜率} = \frac{\text{纵坐标变化量}}{\text{横坐标变化量}} = \frac{\Delta y}{\Delta x}$$</div>
  <p>直觉：爬坡。坡越陡，每走 1 米水平距离，上升的高度越多，斜率越大。</p>

  <h4>数值例子：斜率怎么算</h4>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求过 $(1,2)$ 和 $(3,8)$ 两点的直线斜率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>纵坐标变化：$\Delta y = 8 - 2 = 6$</p>
        <p>横坐标变化：$\Delta x = 3 - 1 = 2$</p>
        <p>斜率：$\dfrac{\Delta y}{\Delta x} = \dfrac{6}{2} = 3$</p>
        <p>含义：横坐标每增加 1，纵坐标增加 3。</p>
      </div>
    </div>
  </div>

  <h4>从斜率到导数：把"割线"变成"切线"</h4>
  <p>直线斜率好算。但曲线（比如 $y=x^2$）的"坡度"是处处变的，怎么算某一点的坡度？</p>
  <p><b>初中的老办法</b>：在曲线上取两个点，连一条直线（叫"割线"），算它的斜率，当作这一段的平均坡度。</p>
  <p><b>极限思想</b>：让两个点越来越近，割线越来越像"贴在这一点的线"（切线），斜率就越来越接近"这一点真正的坡度"。</p>
  <div class="formula">$$\text{导数} f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) - f(x)}{\Delta x}$$</div>
  <p>$\lim$ 读作"极限"，就是"无限逼近"的意思。$\Delta x \to 0$ 读作"$\Delta x$ 趋向于 0"。</p>

  <h4>数值例子：用表看清极限</h4>
  <p>算 $f(x)=x^2$ 在 $x=1$ 处的导数。取越来越小的 $\Delta x$：</p>
  <div class="table-wrap"><table>
    <tr><th>$\Delta x$</th><th>$f(1+\Delta x)$</th><th>差商 $\frac{f(1+\Delta x)-f(1)}{\Delta x}$</th></tr>
    <tr><td>0.1</td><td>$1.1^2=1.21$</td><td>$\frac{1.21-1}{0.1}=2.1$</td></tr>
    <tr><td>0.01</td><td>$1.01^2=1.0201$</td><td>$2.01$</td></tr>
    <tr><td>0.001</td><td>$1.001^2=1.002001$</td><td>$2.001$</td></tr>
    <tr><td>→ 0</td><td>→ 1</td><td>→ <b>2</b></td></tr>
  </table></div>
  <div class="callout callout-key">
    <div class="callout-title">结论</div>
    差商越来越接近 2，所以 $(x^2)'$ 在 $x=1$ 处等于 2。一般地，$(x^n)' = nx^{n-1}$（幂函数求导公式，后面常用）。
  </div>

  <h3>1.3 偏导数：只动一个变量</h3>
  <p>函数可以有两个输入，比如 $z = f(x,y) = x^2 + 3y$。问："如果只把 $x$ 动一点点，$z$ 变多少？"——这就是<b>偏导数</b>，记作 $\dfrac{\partial f}{\partial x}$ 或 $f_x$。</p>
  <p>$\partial$ 读作"偏"，和普通 $d$ 长相不同，提醒你"这里只动了一个变量，另一个当常数看"。</p>
  <div class="formula">$$f_x = \frac{\partial f}{\partial x} = \lim_{\Delta x \to 0}\frac{f(x+\Delta x, y) - f(x,y)}{\Delta x} \quad(\text{把 } y \text{ 当常数！})$$</div>
  <div class="callout callout-tip">
    <div class="callout-title"> 生活直觉：时薪与工时的账本</div>
    你的月工资 = 时薪 × 工时，$z = f(x,y) = x \cdot y$（$x$ 时薪、$y$ 工时）。
    问"时薪涨 1 块，工资涨多少？"——工时不变，答案是 $f_x = y$（工时数）。
    问"工时涨 1 小时，工资涨多少？"——时薪不变，答案是 $f_y = x$（时薪数）。
    偏导数就是<b>只改一个条件，看结果变化多少</b>。
  </div>
  <p><b>复合函数求导（链式法则）</b>：如果 $z=f(u)$，而 $u=g(x)$，那么 $\dfrac{dz}{dx} = f'(u)\cdot g'(x)$。直觉：时薪变化（外层导数）× 工时变化（内层导数）= 总工资变化。这一条在第 18 章隐函数求导里是核心工具。</p>

  <h3>1.4 解方程组：从初中的二元一次说起</h3>
  <p>初中解二元一次方程组，比如：</p>
  <div class="formula">$$\begin{cases} x + y = 3 \\ 2x - y = 0 \end{cases}$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">消元法完整过程</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>第一步</b>：两式相加，消去 $y$：$(x+y)+(2x-y)=3+0$，即 $3x=3$。</p>
        <p><b>第二步</b>：两边同时除以 3，$x=1$。</p>
        <p><b>第三步</b>：代回第一式，$1+y=3$，移项得 $y=2$。</p>
        <p>答案：$(x,y)=(1,2)$。</p>
      </div>
    </div>
  </div>
  <p>关键问题：<b>什么时候方程组有唯一解？</b>对两个二元一次方程，可以写成：</p>
  <div class="formula">$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$</div>
  <p>用消元法解，最终分母会出现一个量：$a_1b_2 - a_2b_1$。<b>如果它等于 0，方程组要么无解、要么无穷多解；不等于 0 才有唯一解。</b>这个量就是"二阶行列式"：</p>
  <div class="formula">$$\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1$$</div>
  <div class="callout callout-tip">
    <div class="callout-title"> 行列式的几何直觉：平行四边形的有向面积</div>
    把 $(a_1,a_2)$ 和 $(b_1,b_2)$ 看成平面上的两个箭头，$a_1b_2-a_2b_1$ 的绝对值就是这两个箭头张成的平行四边形的面积。面积为 0 ⟺ 两个箭头在一条直线上（共线）⟺ 两个方程"是同一个方向"，解不出来。第 18 章隐函数组里的"雅可比行列式"就是这个东西的升级版。
  </div>

  <h3>1.5 配方与最值：极值的初中版本</h3>
  <p>二次函数 $y = ax^2 + bx + c$（$a>0$）的图像是开口向上的抛物线，有最低点。最低点的横坐标怎么找？——<b>配方</b>：</p>
  <div class="formula">$$y = a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$$</div>
  <p>因为平方项 $a(x+\frac{b}{2a})^2 \ge 0$，最小值在 $x = -\dfrac{b}{2a}$ 处取到。</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：碗底</div>
    开口向上的抛物线像一只碗，最低点就是碗底。配方的作用就是"把碗平移回原点"看清楚碗底在哪。
  </div>
  <p><b>导数视角的极值</b>：在最低点（或最高点），切线是水平的，即斜率 = 0，即 $f'(x)=0$。反过来，"$f'(x)=0$ 的点"是极值的<b>候选</b>。为什么是候选？因为还有可能是"平的但没拐弯"（比如 $y=x^3$ 在 0 处）。</p>

  <h3>1.6 面积、勾股定理与弧长：定积分的全部家底</h3>
  <p><b>勾股定理</b>：直角三角形的两条直角边 $a,b$ 和斜边 $c$ 满足 $a^2+b^2=c^2$。</p>
  <p><b>微元（微小线段）</b>：平面上一条弯曲线的一小段，放大看几乎是一段直线。这段小直线的长度，用勾股定理算：横坐标走了 $dx$，纵坐标走了 $dy$，则小段长度</p>
  <div class="formula">$$ds = \sqrt{(dx)^2 + (dy)^2} = \sqrt{1 + (dy/dx)^2}\, dx = \sqrt{1 + y'^2}\, dx$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：把弯线放大成斜边</div>
    曲线的一小段，放大看是一个小直角三角形：底边 $dx$、高 $dy$、斜边就是曲线的这一小段。所以弧长微元 = 斜边 = $\sqrt{dx^2+dy^2}$。这就是第 20 章曲线积分里 $ds$ 的来源。
  </div>
  <p><b>定积分</b>：求曲线下方的面积。办法是<b>分割 → 近似求和 → 取极限</b>：把区间切成 $n$ 个小条，每个小条用矩形近似，加起来，然后让 $n\to\infty$（条数无限多、条宽无限细）。</p>
  <div class="formula">$$\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i)\,\Delta x$$</div>
  <p>$\int$ 是拉长的 $S$，来自"求和（Sum）"。$dx$ 提醒你"宽度无限小"。</p>
  <div class="callout callout-key">
    <div class="callout-title">三个基本结论（后面反复用）</div>
    <p><b>①</b> 微积分基本定理：$\int_a^b f(x)dx = F(b)-F(a)$，其中 $F'=f$（$F$ 叫 $f$ 的原函数）。"先算面积再减"变成"找原函数代上下限"。</p>
    <p><b>②</b> 几个原函数：$\int x^n dx = \frac{x^{n+1}}{n+1}+C$；$\int \frac{1}{x}dx = \ln|x|+C$；$\int e^x dx = e^x+C$；$\int \cos x\, dx = \sin x+C$。其中 $\ln$ 读作"自然对数"，是 $e^x$（$e\approx2.71828$）的逆运算：$y=e^x \iff x=\ln y$。直觉：$e$ = 连续复利（利息无限频繁地生利息的极限倍数），$\ln$ = 连续复利下本金翻倍所需时间（翻倍要 $\ln2\approx0.693$ 单位时间）。</p>
    <p><b>③</b> 分部积分：$\int u\,dv = uv - \int v\,du$。直觉：$d(uv) = u\,dv + v\,du$ 两边积分再移项。</p>
  </div>

  <h3>1.7 向量与点积：梯度和法向量的家</h3>
  <p><b>向量</b>：带方向的箭头。$(3,4)$ 表示"往东 3 步、往北 4 步"。</p>
  <p><b>点积（内积）</b>：两个向量对应分量相乘再相加。</p>
  <div class="formula">$$\vec{a}\cdot\vec{b} = a_1b_1 + a_2b_2 \qquad \text{（三维：} a_1b_1+a_2b_2+a_3b_3\text{）}$$</div>
  <div class="callout callout-tip">
    <div class="callout-title"> 点积的直觉：手电筒影子</div>
    点积 = 一个向量在另一个向量方向上的投影长度 × 另一个向量的长度。如果两个向量垂直（影子缩成一点），点积 = 0。反过来，<b>点积 = 0 ⟺ 垂直</b>。这一条在第 18 章"梯度是法向量"里是核心。
  </div>
  <p><b>梯度</b>：把 $f(x,y)$ 的两个偏导数排成一个向量：</p>
  <div class="formula">$$\nabla f = \left(\frac{\partial f}{\partial x},\, \frac{\partial f}{\partial y}\right)$$</div>
  <p>直觉：站在山坡上，梯度指向<b>爬升最陡的方向</b>，它的长度是"最陡有多陡"。</p>

  <h3>1.8 连续：笔不离纸</h3>
  <p><b>连续函数</b>：画图像时笔可以不离开纸。没有"断口"。</p>
  <div class="callout callout-tip">
    <div class="callout-title"> 介值定理（中间值定理）——隐函数定理的根基</div>
    如果函数连续，从下面的值走到上面的值，<b>中间每个值都会经过</b>。直觉：你从一楼坐电梯到三楼，电梯不可能跳过二楼。形式化：$F(a)<0$、$F(b)>0$，则中间必有 $c$ 使 $F(c)=0$。<b>这个"必有一个零点"的结论，正是隐函数存在性的全部秘密。</b>
  </div>

  <h3>1.9 求导法则工具箱（后面章节到处用）</h3>
  <p>第 2 章隐函数要二阶导数，第 6、9 章的证明也要用。这里把三个求导法则配齐，每个都给直觉和例子：</p>
  <div class="formula">
    <p>① <b>乘积法则</b>：$(uv)' = u'v + uv'$</p>
    <p>② <b>商法则</b>：$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$（$v\ne0$）</p>
    <p>③ <b>链式法则</b>：$(f(g(x)))' = f'(g(x))\cdot g'(x)$（已学）</p>
  </div>
  <div class="callout callout-tip">
    <div class="callout-title"> 乘积法则直觉：长大的长方形</div>
    长方形长 $u$、宽 $v$，面积 $uv$。长增加 $u'$、宽增加 $v'$（都微小），面积增加 = 长变多贡献的 $u'v$（长变化 × 原宽）+ 宽变多贡献的 $uv'$（原长 × 宽变化），交叉项（$u'\cdot v'$，两个微小量相乘）小到忽略。所以 $(uv)'=u'v+uv'$。
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">商法则从乘积法则推出</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $w=\frac{u}{v}$，则 $u = wv$。两边用乘积法则：$u' = w'v + wv'$。</p>
        <p>解出 $w'$：$w'v = u' - wv' = u' - \frac{u}{v}v'$，两边除以 $v$：$w' = \frac{u' - \frac{u}{v}v'}{v} = \frac{u'v - uv'}{v^2}$。</p>
        <p>记忆：<b>"上导下不导减下导上不导，除以分母平方"</b>（分子次序：$u'v - uv'$，先上后下）。</p>
      </div>
    </div>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">数值例子：用商法则求 (sin x / x)' 在 x=1 处</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$u=\sin x$，$u'=\cos x$；$v=x$，$v'=1$。</p>
        <p>$$\left(\frac{\sin x}{x}\right)' = \frac{\cos x\cdot x - \sin x\cdot 1}{x^2} = \frac{x\cos x - \sin x}{x^2}$$</p>
        <p>在 $x=1$（弧度制）：$\frac{1\cdot\cos1-\sin1}{1}\approx\frac{0.5403-0.8415}{1}\approx-0.3012$。</p>
        <p><b>弧度制是什么？</b>初中量角用"度"（360° 一圈），高等数学用"弧度"：一圈 = $2\pi$ 弧度，所以 $180°=\pi$，$90°=\frac\pi2$，$1$ 弧度 ≈ $57.3°$。用弧度，$\sin'=\cos$ 这些公式才成立。$x=1$ 意思是 $1$ 弧度（≈57.3°）。</p>
        <p>（若不用商法则，用数值差商验证：$f(1.01)-f(1)\over0.01$ 应接近 -0.3012。）</p>
      </div>
    </div>
  </div>

  <h3>1.10 中值定理：平均速度 = 某时刻瞬时速度</h3>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：开车从 0 加速到 100</div>
    开车从 $t=a$ 到 $t=b$，平均速度是 $\frac{f(b)-f(a)}{b-a}$（比如全程平均 60km/h）。那么途中<b>至少有一个时刻</b>的瞬时速度恰好等于 60km/h——不可能"一直低于平均速"还能追上平均速。
  </div>
  <div class="formula">$$\text{拉格朗日中值定理：}\exists\,\xi\in(a,b)\text{，使 } \frac{f(b)-f(a)}{b-a} = f'(\xi)$$</div>  <p>用途：第 6 章证明"积分号下求导"、第 9 章证明曲线积分公式，都用它把"差值"变成"导数"。</p>

  <h3>1.11 部分分式分解：把"大分式"拆成"小分式"</h3>
  <p>积分时，$\frac{x}{(1+x^2)(1+ax)}$ 这种"两个因式相乘的分母"没法直接积。办法：拆成 $\frac{Ax+B}{1+x^2}+\frac{C}{1+ax}$ 的简单分式之和。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">完整例子：拆 x/[(1+x²)(1+2x)]</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>第一步，假设形状</b>：$\frac{x}{(1+x^2)(1+2x)} = \frac{Ax+B}{1+x^2} + \frac{C}{1+2x}$（一次因式 $1+2x$ 用常数 $C$；二次因式 $1+x^2$ 用 $Ax+B$）。</p>
        <p><b>第二步，通分</b>：$x = (Ax+B)(1+2x) + C(1+x^2)$</p>
        <p><b>第三步，展开</b>：$= Ax+B+2Ax^2+2Bx+C+Cx^2$</p>
        <p><b>第四步，匹配系数</b>：$x^2$ 项：$2A+C=0$；$x$ 项：$A+2B=1$；常数项：$B+C=0$。</p>
        <p><b>第五步，解方程</b>：$C=-2A$，$B=2A$，代到 $x$ 项：$A+4A=1$，$A=\frac15$，$B=\frac25$，$C=-\frac25$。</p>
        <p>结果：$\frac{x}{(1+x^2)(1+2x)} = \frac{\frac15x+\frac25}{1+x^2} - \frac{\frac25}{1+2x}$，每一项都能积了。</p>
      </div>
    </div>
  </div>

  <h3>1.12 反三角函数：知道斜率，求角度</h3>
  <p>$\arctan$ 读作"反正切"：<b>输入一个斜率（正切值），输出角度</b>。</p>
  <div class="formula">$$\arctan(1) = \frac{\pi}{4} \;(45°),\qquad \arctan(0)=0,\qquad \lim_{x\to\infty}\arctan x = \frac{\pi}{2}\;(90°)$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：测坡角</div>
    站在山坡上，用水平仪量出"每走 1 米水平距离上升多少"（斜率），$\arctan$ 告诉你坡的角度。极坐标里 $\theta=\arctan(y/x)$ 就是"知道横纵坐标，求方向角"。
  </div>

  <h3>1.13 叉积（向量积）：同时垂直于两个向量的向量</h3>
  <p>第 1.7 节学了点积（结果是一个数，判断垂直）。叉积的结果是<b>一个向量</b>，它同时垂直于原来的两个向量。</p>
  <div class="formula">$$\vec a \times \vec b = \begin{vmatrix}\vec i & \vec j & \vec k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3\end{vmatrix} = (a_2b_3-a_3b_2,\; a_3b_1-a_1b_3,\; a_1b_2-a_2b_1)$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：两面墙的交线方向</div>
    一面墙的法线是 $\vec n_1$，另一面墙的法线是 $\vec n_2$。两面墙相交出一条棱，棱的方向既垂直于 $\vec n_1$ 又垂直于 $\vec n_2$——就是 $\vec n_1\times\vec n_2$。第 4 章求"两曲面交线的切向量"全靠它。
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">数值例子：(1,0,0)×(0,1,0) = (0,0,1)</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$x$ 轴方向 $(1,0,0)$ 与 $y$ 轴方向 $(0,1,0)$ 的叉积：</p>
        <p>第一个分量 $=0\cdot0-0\cdot1=0$；第二个 $=0\cdot0-1\cdot0=0$；第三个 $=1\cdot1-0\cdot0=1$。</p>
        <p>结果 $(0,0,1)$——$z$ 轴方向。确实同时垂直于 $x$ 轴和 $y$ 轴 ✓。这就是"右手定则"：$x$ 叉 $y$ 得 $z$。</p>
      </div>
    </div>
  </div>

  <h3>1.14 克莱姆法则：用行列式写方程组唯一解</h3>
  <p>第 1.4 节说"行列式 ≠ 0 ⟺ 有唯一解"。现在给出解本身（第 3 章隐函数组推导要用）：</p>
  <div class="formula">$$\begin{cases}a_1x+b_1y=c_1\\a_2x+b_2y=c_2\end{cases}\;\Rightarrow\; x=\frac{\begin{vmatrix}c_1&b_1\\c_2&b_2\end{vmatrix}}{\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}},\quad y=\frac{\begin{vmatrix}a_1&c_1\\a_2&c_2\end{vmatrix}}{\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}}$$</div>
  <div class="callout callout-tip">
    <div class="callout-title"> 记忆：把"要求的变量"那一列换成常数项</div>
    求 $x$：把系数行列式里 $x$ 的系数列（$a_1,a_2$）换成常数项列（$c_1,c_2$），除以原行列式。求 $y$：把 $y$ 的系数列换成常数项列。分母永远是原系数行列式。
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">克莱姆法则证明（消元法两行）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>对 $\begin{cases}a_1x+b_1y=c_1\\a_2x+b_2y=c_2\end{cases}$：</p>
        <p>用消元法：第一式乘 $b_2$，第二式乘 $b_1$，相减消 $y$：$a_1b_2x - a_2b_1x = c_1b_2 - c_2b_1$。</p>
        <p>$$x(a_1b_2-a_2b_1) = c_1b_2-c_2b_1 \;\Rightarrow\; x = \frac{c_1b_2-c_2b_1}{a_1b_2-a_2b_1}$$</p>
        <p>分子正是 $\begin{vmatrix}c_1&b_1\\c_2&b_2\end{vmatrix}=c_1b_2-c_2b_1$，分母是原行列式。$y$ 同理。证毕。</p>
      </div>
    </div>
  </div>

  <h3>1.15 均值不等式：算术平均 ≥ 几何平均</h3>
  <div class="formula">$$a,b>0 \;\Rightarrow\; \frac{a+b}{2} \ge \sqrt{ab}\text{，即 } a+b \ge 2\sqrt{ab}$$</div>
  <p>等号当且仅当 $a=b$。用途：条件极值（第 5 章）、不等式证明。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">配方证明（初中知识够用）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$(\sqrt{a}-\sqrt{b})^2 \ge 0$（平方非负，永远成立）。展开：$a - 2\sqrt{ab} + b \ge 0$。</p>
        <p>移项：$a+b \ge 2\sqrt{ab}$。✓</p>
        <p>等号条件：$(\sqrt{a}-\sqrt{b})^2=0$，即 $a=b$。</p>
        <p>数值检查：$a=4,b=9$：$\frac{13}{2}=6.5 \ge \sqrt{36}=6$ ✓。</p>
      </div>
    </div>
  </div>

  <h3>1.16 求根公式速查（初中内容，温故）</h3>
  <div class="formula">$$ax^2+bx+c=0 \;(a\ne0) \;\Rightarrow\; x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$</div>
  <p>判别式 $b^2-4ac$：$>0$ 两个实根，$=0$ 一个重根，$<0$ 无实根。来源：配方（第 1.5 节）。第 5 章解条件极值方程组时会用到。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">求根公式从配方推出（复习）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$ax^2+bx+c=0$，两边除以 $a$：$x^2+\frac ba x = -\frac ca$。</p>
        <p>配方：$x^2+\frac ba x + (\frac{b}{2a})^2 = -\frac ca + \frac{b^2}{4a^2}$，即 $(x+\frac{b}{2a})^2 = \frac{b^2-4ac}{4a^2}$。</p>
        <p>开平方：$x+\frac{b}{2a} = \pm\frac{\sqrt{b^2-4ac}}{2a}$，移项得 $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$。</p>
      </div>
    </div>
  </div>

  <h3>1.17 微积分基本定理的直觉（面积函数的导数 = 原函数）</h3>
  <p>第 1.6 节给出了 $\int_a^b f(x)dx=F(b)-F(a)$。为什么成立？直觉：</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">为什么 F(b)-F(a) 等于面积</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $A(x)=\int_a^x f(t)dt$（从 $a$ 积到 $x$ 的面积，是 $x$ 的函数）。</p>
        <p>$A(x+\Delta x)-A(x)$ = 从 $x$ 到 $x+\Delta x$ 新增的一小条面积 ≈ 高 $f(x)$ × 宽 $\Delta x$。</p>
        <p>所以 $\frac{A(x+\Delta x)-A(x)}{\Delta x}\approx f(x)$，取极限 $A'(x)=f(x)$——<b>面积函数的导数就是曲线的高度</b>。</p>
        <p>于是 $A(x)$ 是 $f$ 的原函数：$A(x)=F(x)+C$。又 $A(a)=0$，所以 $C=-F(a)$，$A(b)=F(b)-F(a)$。</p>
        <p>结论：面积 = 原函数值之差。这就是"微积分基本定理"。</p>
      </div>
    </div>
  </div>

  <h3>1.18 地基清单：本章你必须带走的东西</h3>
  <div class="table-wrap"><table>
    <tr><th style="width:22%">地基块</th><th style="width:44%">一句话</th><th>后面用在哪</th></tr>
    <tr><td>斜率</td><td>$\Delta y/\Delta x$，陡峭程度</td><td>导数 → 隐函数求导 → 切线</td></tr>
    <tr><td>导数</td><td>瞬时斜率，$(x^n)'=nx^{n-1}$</td><td>整本 18 章</td></tr>
    <tr><td>偏导数</td><td>只动一个变量</td><td>隐函数组、切平面、梯度</td></tr>
    <tr><td>二阶行列式</td><td>$a_1b_2-a_2b_1$，平行四边形面积</td><td>雅可比行列式</td></tr>
    <tr><td>配方/极值</td><td>$f'(x)=0$ 是候选</td><td>条件极值</td></tr>
    <tr><td>勾股定理</td><td>$a^2+b^2=c^2$</td><td>弧长微元 → 曲线积分</td></tr>
    <tr><td>定积分</td><td>分割-近似-取极限；$F(b)-F(a)$</td><td>含参量积分、曲线积分</td></tr>
    <tr><td>点积/梯度</td><td>点积=0 垂直；梯度=最陡方向</td><td>法向量、切平面</td></tr>
    <tr><td>介值定理</td><td>连续函数必经过中间值</td><td>隐函数存在性</td></tr>
  </table></div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：$f(x,y)=x^2y$ 在 $(2,3)$ 处的两个偏导数各是多少？</div>
    <div class="qa-a"><b>答案</b>：把 $y$ 当常数：$f_x = 2xy$，代入 $(2,3)$ 得 $2\cdot2\cdot3=12$。把 $x$ 当常数：$f_y = x^2$，代入得 $4$。验证直觉：$f=4\times3=12$，$x$ 加一点点 $z$ 变 12 倍/单位，$y$ 加一点点 $z$ 变 4 倍/单位。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：$\begin{vmatrix}1 & 2 \\ 3 & 4\end{vmatrix}$ 等于多少？它说明什么？</div>
    <div class="qa-a"><b>答案</b>：$1\times4 - 2\times3 = 4-6 = -2 \ne 0$。不等于 0，说明向量 $(1,3)$ 和 $(2,4)$ 不共线，对应方程组有唯一解。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：曲线 $y=x^2$ 从 $x=0$ 到 $x=2$ 的弧长大约是多少？（提示：$ds=\sqrt{1+(2x)^2}dx$，数值积分或近似即可）</div>
    <div class="qa-a"><b>答案</b>：$\int_0^2\sqrt{1+4x^2}\,dx \approx 4.65$（用数值积分近似）。这条抛物线实际比直线段（长度 2）弯出去不少。</div>
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：implicit-func ===== -->
<section class="chapter" id="implicit-func" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">2</span>隐函数：方程里藏着的函数</h2>
  <p class="lead">前置知识：函数与方程、导数、偏导数、复合函数求导（第 1 章）。后续应用：隐函数组、切线切平面、条件极值、含参量积分。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的三个问题</div>
    <p>① 方程 $F(x,y)=0$ 到底什么时候能"解出 $y$ 作为 $x$ 的函数"？</p>
    <p>② 即使解不出来，$y$ 的导数 $y'$ 能不能直接算？</p>
    <p>③ 算出来的导数长什么样？——答案：$y' = -\dfrac{F_x}{F_y}$，两个偏导数之比取负号。</p>
  </div>

  <h3>2.1 什么是隐函数：x 和 y 地位平等</h3>
  <p><b>显函数</b>：$y = f(x)$，明确告诉你"$y$ 等于什么"。如 $y = \sqrt{1-x^2}$。</p>
  <p><b>隐函数</b>：$F(x,y)=0$，只告诉你"$x$ 和 $y$ 必须满足这个关系"。如 $x^2+y^2=1$。</p>
  <p>关键理解：<b>同一个圆 $x^2+y^2=1$，既可以是 $y=\sqrt{1-x^2}$（上半圆），也可以是 $y=-\sqrt{1-x^2}$（下半圆）</b>。一个方程可能藏着好几个函数——你只取其中"一小段"。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">圆方程解出 y：看清楚"一个点附近"的含义</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$x^2+y^2=1$，把 $y$ 解出来：$y^2 = 1-x^2$，两边开平方：$y = \pm\sqrt{1-x^2}$。</p>
        <p>"$\pm$" 说明一个 $x$ 对应两个 $y$——这不是函数（函数要求一个 $x$ 只对应一个 $y$）。</p>
        <p>但在<b>某一点附近</b>，比如点 $(0,1)$ 附近，曲线只有上半部分，$y = +\sqrt{1-x^2}$ 就是函数。</p>
        <p>所以隐函数是<b>局部</b>的概念：在一个小邻域内，方程确定唯一的 $y=f(x)$。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-warn">
    <div class="callout-title"> 为什么圆不能整体解成一个函数？</div>
    函数的要求：每个 $x$ 恰好对应一个 $y$。圆上 $x=0$ 对应 $y=1$ 和 $y=-1$ 两个点，所以整体不是函数。但局部（上半圆、下半圆分开看）都是函数。这就是"隐函数定理"里"局部存在"的由来。
  </div>

  <h3>2.2 隐函数存在性的直觉：曲面切出来的交线</h3>
  <p>把 $z=F(x,y)$ 想成一个"曲面"（山坡）。$F(x,y)=0$ 是"海拔 0 米的等高线"——即曲面与水平面 $z=0$ 的交线。</p>
  <p>问：这条交线能不能写成 $y=f(x)$（即"每走一步横坐标，交线上有唯一的纵坐标"）？</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：看交线是否"竖直折叠"</div>
    <p>想象交线是一条山路。如果山路在某点"竖直"（切线竖直），那么同一个 $x$ 会对应两个 $y$，无法写成 $y=f(x)$。</p>
    <p>山路切线竖直 ⟺ $\dfrac{dy}{dx}$ 无穷大 ⟺ 隐函数求导公式 $y'=-\dfrac{F_x}{F_y}$ 的分母 $F_y=0$。</p>
    <p>所以：<b>能不能解出 $y$，看的是 $F_y$ 是否等于 0</b>。$F_y \ne 0$ ⟹ 能解；$F_y=0$ 处要小心。</p>
  </div>
  <p>用圆验证：$F=x^2+y^2-1$，$F_y=2y$。在 $(0,1)$ 处 $F_y=2\ne0$，能解出 $y$（上半圆）。在 $(1,0)$ 处 $F_y=0$——这一点切线竖直，不能解出 $y$，但能解出 $x$ 作为 $y$ 的函数。</p>

  <h3>2.3 隐函数定理（定理 18.1）：存在性与连续性的完整证明</h3>
  <p><b>定理（白话版）</b>：设 $F(x,y)$ 满足三条：</p>
  <div class="formula">
    <p>(i) 在 $P_0(x_0,y_0)$ 附近连续；</p>
    <p>(ii) $F(x_0,y_0)=0$（点确实在曲线上）；</p>
    <p>(iii) $F_y$ 在 $P_0$ 附近连续且 $F_y(x_0,y_0)\ne0$。</p>
    <p>则：在 $x_0$ 附近存在唯一的 $y=f(x)$，满足 $F(x,f(x))\equiv 0$ 且 $f(x_0)=y_0$，并且 $f$ 连续。</p>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">定理在说什么？</div>
    一句话："<b>只要曲线在某点不是竖直的（$F_y\ne0$），这点附近就能把 $y$ 写成 $x$ 的函数，而且这个函数是连续的（笔不离纸）。</b>"
  </div>
  <p><b>为什么 $F_y\ne0$ 就保证能解出来？——四步证明</b></p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">第1步</span><span class="derive-step-title">一点正，一片正：F_y 在附近保持符号</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F_y(x_0,y_0) \ne 0$，不妨设 $F_y(x_0,y_0) > 0$。</p>
        <p>因为 $F_y$ 连续，"大于 0"这个性质在小范围内保持：存在一个小方框 $[x_0-\delta,x_0+\delta]\times[y_0-\delta,y_0+\delta]$，里面 $F_y$ 处处 $>0$。</p>
        <p>直觉：体温计测得 36.5℃，那么一小段时间内体温都在 36℃ 以上——连续量不会瞬间跳变。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">第2步</span><span class="derive-step-title">正负上下分：固定 x，F 关于 y 严格上升</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>固定 $x$（在 $x_0$ 附近），把 $F(x,y)$ 看成关于 $y$ 的一元函数。</p>
        <p>由于 $F_y > 0$（斜率处处为正），这个一元函数关于 $y$ <b>严格上升</b>——$y$ 越大 $F$ 越大。</p>
        <p>在 $y_0$ 上方取一点 $y_0+h$，则 $F(x_0, y_0+h) > F(x_0,y_0) = 0$（上升所以更大）。</p>
        <p>在 $y_0$ 下方取一点 $y_0-h$，则 $F(x_0, y_0-h) < F(x_0,y_0) = 0$（上升所以更小）。</p>
        <p>即：固定 $x_0$ 时，函数值从负变正——"下方为负、上方为正"。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">第3步</span><span class="derive-step-title">同号两边伸：把"下方为负、上方为正"推广到 x0 附近</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>因为 $F$ 连续，$(x_0, y_0+h)$ 附近的值和 $F(x_0,y_0+h)>0$ 差不了多少，所以对 $x_0$ 附近的一切 $x$，仍有 $F(x, y_0+h) > 0$。</p>
        <p>同理，对 $x_0$ 附近的一切 $x$，仍有 $F(x, y_0-h) < 0$。</p>
        <p>直观：整条"上边线"都在海平面以上，整条"下边线"都在海平面以下。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">第4步</span><span class="derive-step-title">利用介值性：从负到正必穿零，而且只穿一次</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>固定任意一个 $x$（在 $x_0$ 附近），$F(x,y)$ 关于 $y$ 连续，在 $y_0-h$ 处为负、在 $y_0+h$ 处为正。</p>
        <p>由介值定理（电梯不可能跳过 2 楼），中间必有某个 $y$ 使 $F(x,y)=0$。</p>
        <p>又因为 $F_y>0$（严格上升），这个零点<b>唯一</b>——函数只能穿零一次。</p>
        <p>于是对每个 $x$，有且仅有一个 $y=f(x)$ 满足 $F(x,f(x))=0$。隐函数存在！</p>
        <p>连续性：$x$ 变一点点时，这个零点也只动一点点（由"上/下边线"的连续性可证）——所以 $f$ 连续。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">证明的四个字口诀</div>
    <b>一点正 → 一片正 → 正负上下分 → 同号两边伸 → 介值穿零唯一解</b>。本质：$F_y\ne0$ 保证了"横着切过去必有交点且只交一次"。
  </div>

  <h3>2.4 隐函数的导数：y' = -Fx/Fy 的完整推导</h3>
  <p><b>问题</b>：知道 $F(x,y)=0$，想求 $y'$，但 $y$ 解不出来怎么办？——<b>不需要解出来</b>。</p>
  <p><b>工具</b>：等式两边同时对 $x$ 求导。注意 $y$ 是 $x$ 的函数 $y(x)$，所以出现 $y$ 的地方要用链式法则。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">推导 y' = -Fx/Fy（定理 18.2）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>出发点</b>：$F(x, y(x)) \equiv 0$ 对一切 $x$ 成立。</p>
        <p><b>两边对 $x$ 求导</b>。左边用链式法则（$F$ 先对 $x$、再对 $y$，$y$ 再对 $x$）：</p>
        <p>$$\frac{d}{dx}F(x,y(x)) = F_x \cdot \frac{dx}{dx} + F_y \cdot \frac{dy}{dx} = F_x + F_y\, y'$$</p>
        <p><b>右边</b>：0 的导数是 0。</p>
        <p>所以：$F_x + F_y\, y' = 0$</p>
        <p><b>移项</b>：$F_y\, y' = -F_x$</p>
        <p><b>两边除以 $F_y$</b>（因为 $F_y\ne0$）：</p>
        <p>$$\boxed{y' = -\frac{F_x}{F_y}}$$</p>
        <p>读法："$y$ 的导数等于负的 $F$ 对 $x$ 的偏导除以 $F$ 对 $y$ 的偏导"。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-tip">
    <div class="callout-title"> 为什么有负号？——直觉</div>
    <p>在曲线附近，$F$ 几乎是线性变化的：$F$ 的变化 ≈ $F_x \Delta x + F_y \Delta y$。</p>
    <p>曲线要求 $F$ 不变（恒等于 0），所以 $F_x\Delta x + F_y\Delta y = 0$。</p>
    <p>解得 $\dfrac{\Delta y}{\Delta x} = -\dfrac{F_x}{F_y}$：<b>$x$ 增加让 $F$ 涨了 $F_x$，$y$ 就得"退" $\frac{F_x}{F_y}$ 来抵消，所以带负号。</b></p>
    <p>类比：天平一端加了砝码（$F_x\Delta x>0$），另一端必须减掉同样重量（$F_y\Delta y<0$）才能保持平衡。</p>
  </div>

  <h4>数值例子：圆的隐函数求导</h4>
  <p>对 $x^2+y^2=1$，设 $F=x^2+y^2-1$。则 $F_x=2x$，$F_y=2y$。由公式：</p>
  <div class="formula">$$y' = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y}$$</div>
  <p>在 $(0,1)$：$y'=0$（上半圆顶点切线水平——对）。在 $(\frac{\sqrt2}{2},\frac{\sqrt2}{2})$：$y'=-1$（45° 点切线斜率 -1——对）。在 $(1,0)$：$y'=-\frac{1}{0}$ 无定义（切线竖直——对）。</p>
  <p><b>对同一个例子，再用"先解出再求导"验证</b>：$y=\sqrt{1-x^2}$，$y'=\frac{-x}{\sqrt{1-x^2}}=-\frac{x}{y}$。两种方法答案一致。</p>

  <h4>数值例子：笛卡儿叶形线</h4>
  <p>方程 $x^3+y^3=3xy$（一条著名的弯曲线）。$F=x^3+y^3-3xy$：</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求 y' 并看它在点 (3/2, 3/2) 的值</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F_x = 3x^2 - 3y$（注意 $-3xy$ 对 $x$ 求导是 $-3y$）；$F_y = 3y^2 - 3x$。</p>
        <p>$$y' = -\frac{3x^2-3y}{3y^2-3x} = -\frac{x^2-y}{y^2-x}$$</p>
        <p>在点 $(\frac32,\frac32)$（它在曲线上吗？验证：$\frac{27}{8}+\frac{27}{8}=3\cdot\frac32\cdot\frac32=\frac{27}{4}$，在！）：</p>
        <p>分子 $= \frac94 - \frac32 = \frac34$，分母 $= \frac94-\frac32 = \frac34$，$y' = -1$。</p>
        <p>这条著名的曲线在该点切线斜率 -1（对称位置，合理）。</p>
      </div>
    </div>
  </div>

  <h3>2.5 二阶导数：把一阶导数的结果再求一次</h3>
  <p>有时需要 $y''$。方法：把 $y'=-F_x/F_y$ 当作 $x$ 的函数再求导（$y$ 还是 $x$ 的函数，处处用链式法则）。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">推导二阶导数公式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>记 $y' = -\dfrac{F_x}{F_y}$。两边对 $x$ 求导（商的求导法则：$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$）：</p>
        <p>$$y'' = -\frac{(F_x)' F_y - F_x (F_y)'}{F_y^2}$$</p>
        <p>其中 $(F_x)' = F_{xx} + F_{xy}\,y'$（$F_x$ 里也有 $y$，链式法则），$(F_y)' = F_{yx} + F_{yy}\,y'$。</p>
        <p>代入并利用 $y' = -F_x/F_y$，整理：</p>
        <p>$$y'' = -\frac{F_{xx}F_y^2 - 2F_{xy}F_xF_y + F_{yy}F_x^2}{F_y^3}$$</p>
        <p>（通常写作：$y'' = -\dfrac{F_{xx} + 2F_{xy}y' + F_{yy}y'^2}{F_y}$，两者等价——用 $y'$ 表示更短。）</p>
      </div>
    </div>
  </div>
  <div class="callout callout-warn">
    <div class="callout-title"> 记不住怎么办？</div>
    不需要背公式。你只需要记住<b>方法</b>：$F(x,y)=0$ 两边求导得 $y'$；把 $y'$ 的表达式再求导一次得 $y''$。每一步用"$y$ 是 $x$ 的函数"这个事实。数值例子看下一个折叠框。
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">圆的二阶导数：y² = 1 - x² 求 y''</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>已知 $y' = -\frac{x}{y}$。</p>
        <p>再求导：$y'' = \left(-\frac{x}{y}\right)' = -\frac{1\cdot y - x\cdot y'}{y^2}$（商的法则）</p>
        <p>代入 $y'=-\frac{x}{y}$：$y'' = -\frac{y - x(-\frac{x}{y})}{y^2} = -\frac{y + \frac{x^2}{y}}{y^2} = -\frac{y^2+x^2}{y^3}$</p>
        <p>但 $x^2+y^2=1$，所以 $y'' = -\frac{1}{y^3}$。</p>
        <p>在上半圆 $y>0$：$y''<0$，曲线"开口向下"（拱形）——对的，上半圆是凸向下的。</p>
      </div>
    </div>
  </div>

  <h3>2.6 隐函数求极值：y' = 0 处找候选点</h3>
  <p>第 1 章说过：极值的候选点是 $f'(x)=0$。对隐函数，$y' = -\frac{F_x}{F_y} = 0$ ⟺ $F_x = 0$（分母非零）。</p>
  <p>此时极值点的判断用 $y''$ 的符号：$y''<0$ 极大、$y''>0$ 极小。在 $F_x=0$ 处，二阶导数公式简化为：</p>
  <div class="formula">$$y'' = -\frac{F_{xx}}{F_y}\qquad(\text{当 } F_x=0)$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">极值点的二阶导数简化</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>在 $y'=0$（即 $F_x=0$）的点，把 $y'=0$ 代入二阶公式 $y'' = -\frac{F_{xx}+2F_{xy}y'+F_{yy}y'^2}{F_y}$：</p>
        <p>含 $y'$ 的项全部消失，只剩 $y'' = -\frac{F_{xx}}{F_y}$。</p>
        <p>例子（圆的上半）：$F_x=2x$，$F_x=0$ 得 $x=0$，即 $(0,1)$。$F_{xx}=2$，$F_y=2$，$y'' = -\frac{2}{2} = -1 < 0$，极大值点。上半圆的最高点，对！</p>
      </div>
    </div>
  </div>

  <h3>2.7 多元隐函数：F(x,y,z)=0 时 z 对 x、y 的偏导</h3>
  <p>三维：方程 $F(x,y,z)=0$ 是一个<b>曲面</b>。如果 $F_z\ne0$，局部能解出 $z=f(x,y)$。</p>
  <p>求偏导的方法与二维完全一样：<b>等式两边对 $x$ 求偏导（$y$ 当常数，$z$ 当 $x$ 的函数）</b>。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">推导 z_x = -Fx/Fz 和 z_y = -Fy/Fz</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F(x,y,z(x,y)) \equiv 0$ 对 $x$ 求偏导（$y$ 固定，链式法则过 $z$）：</p>
        <p>$$F_x \cdot 1 + F_z \cdot z_x = 0 \quad\Rightarrow\quad z_x = -\frac{F_x}{F_z}$$</p>
        <p>对 $y$ 求偏导（$x$ 固定）：</p>
        <p>$$F_y \cdot 1 + F_z \cdot z_y = 0 \quad\Rightarrow\quad z_y = -\frac{F_y}{F_z}$$</p>
        <p>规律：<b>要求谁，就把"另一个自变量"放分子，$F_z$ 放分母，前面加负号。</b></p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">记忆口诀</div>
    "<b>分子是要求的那一项，分母是解不出的那个变量，前面永远带负号。</b>"二维 $y'=-F_x/F_y$ 是三维公式的特例（把 $z$ 换回 $y$）。
  </div>

  <h4>数值例子：全微分</h4>
  <p>方程 $xyz + x^3 + y^3 - z^3 = 0$ 在点 $P(0,1,1)$。验证：$0\cdot1\cdot1 + 0 + 1 - 1 = 0$ ✓。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求 P 处的 dz 表达式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>记 $F = xyz + x^3 + y^3 - z^3$。</p>
        <p>$F_x = yz + 3x^2$，在 P：$F_x = 1\cdot1 + 0 = 1$。</p>
        <p>$F_y = xz + 3y^2$，在 P：$F_y = 0 + 3 = 3$。</p>
        <p>$F_z = xy - 3z^2$，在 P：$F_z = 0 - 3 = -3$。</p>
        <p>$$z_x = -\frac{F_x}{F_z} = -\frac{1}{-3} = \frac13, \qquad z_y = -\frac{F_y}{F_z} = -\frac{3}{-3} = 1$$</p>
        <p>全微分 $dz = z_x dx + z_y dy = \frac13 dx + 1\cdot dy$。</p>
      </div>
    </div>
  </div>

  <h3>2.8 反函数：隐函数的一个特例</h3>
  <p>$y=f(x)$ 的反函数 $x=f^{-1}(y)$ 满足 $f(x) - y = 0$，即 $F(x,y)=f(x)-y=0$。$F_x=f'(x)$，$F_y=-1$，代入公式：</p>
  <div class="formula">$$\frac{dx}{dy} = -\frac{F_y}{F_x} = -\frac{-1}{f'(x)} = \frac{1}{f'(x)}$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：反函数的导数互为倒数</div>
    若 $y=2x$，则 $x=\frac12 y$。$y'=2$，$x'=\frac12$，乘积 = 1。斜率互为倒数——因为反函数就是把"横纵轴对调"，陡的程度对调。
  </div>

  <h3>2.9 双纽线例题：一个方程藏着多处"麻烦"</h3>
  <p>双纽线（Bernoulli 双纽线）：$(x^2+y^2)^2 = x^2 - y^2$。这是一条像"∞"号的曲线。</p>
  <p><b>问题</b>：哪些点附近不能解出 $y=f(x)$？</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">析</span><span class="derive-step-title">分析双纽线的隐函数存在性</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $F = (x^2+y^2)^2 - x^2 + y^2$。$F_y = 4y(x^2+y^2) + 2y$。</p>
        <p>能解 $y$ 的条件：$F_y \ne 0$，即 $y[4(x^2+y^2)+2] \ne 0$。</p>
        <p>当 $y=0$ 时 $F_y = 0$ ——危险点。代入原方程：$(x^2)^2 = x^2$，即 $x^4=x^2$，得 $x=0, \pm1$。</p>
        <p>所以曲线上 $y=0$ 的三个点 $(0,0)$、$(\pm1,0)$ 处 $F_y=0$：</p>
        <p>• $(0,0)$：双纽线在这里自交（"∞"的中心），四支曲线交叉，任何一个小邻域内一个 $x$ 对应多个 $y$，不能解出函数。</p>
        <p>• $(\pm1,0)$：切线竖直（$F_y=0$ 但 $F_x\ne0$），能解出 $x$ 作为 $y$ 的函数，但不能解 $y$。</p>
        <p>其余点：$F_y\ne0$，局部都能解出 $y=f(x)$。</p>
      </div>
    </div>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：对 $x^2 + xy + y^2 = 3$，求在点 $(1,1)$ 处的 $y'$。</div>
    <div class="qa-a"><b>答案</b>：$F = x^2+xy+y^2-3$，$F_x=2x+y=3$，$F_y=x+2y=3$，$y' = -\frac{3}{3} = -1$。验证：$1+1+1=3$ 确实在曲线上。曲线在该点的切线斜率 -1。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：$x^2+y^2=25$ 在 $(3,4)$ 处的 $y''$ 是多少？</div>
    <div class="qa-a"><b>答案</b>：$F=25-x^2-y^2$ 或直接用公式：$y'=-\frac{x}{y}$，$y'' = -\frac{y^2+x^2}{y^3} = -\frac{25}{64} \approx -0.39$。负号说明曲线在该处"开口向下"（在圆周上部，正确）。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：方程 $e^y = x + y$（即 $F=e^y-x-y=0$）能确定隐函数吗？求 $y'$。</div>
    <div class="qa-a"><b>答案</b>：$F_y = e^y - 1$。只要 $y\ne0$ 就 $F_y\ne0$，能解。$F_x = -1$，$y' = -\frac{F_x}{F_y} = \frac{1}{e^y-1}$。检验：$y=0$ 时 $F=e^0-0-0=0$，$F_y=0$，该点附近需小心（$y'$ 无穷大，切线竖直）。</div>
  </div>
  <div class="chapter-nav"></div>
</section>
"""

def write(path: Path, content: str) -> None:
    path.write_text(content, encoding='utf-8')

if __name__ == "__main__":
    out = Path(__file__).parent / 'chapters_a.py.txt'
    write(out, CH_A)
    print('chapters_a 内容长度:', len(CH_A))
