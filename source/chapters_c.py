#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""章节内容 C：含参量正常积分 + 含参量反常积分"""

CH_C = r"""<!-- ===== 章节：param-integral ===== -->
<section class="chapter" id="param-integral" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">6</span>含参量正常积分</h2>
  <p class="lead">前置知识：定积分（第 1.6 节）、偏导数（第 1.3 节）、连续（第 1.8 节）。后续应用：含参量反常积分（第 7 章）、欧拉积分（第 8 章）。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 积分号里有参数，结果是什么？——一个关于参数的<b>新函数</b>。</p>
    <p>② 这个新函数连续吗？可导吗？可积吗？</p>
    <p>③ 核心工具：<b>连续 ⟹ 极限可换序；可微 ⟹ 导数可换序（积分号下求导）</b>。</p>
  </div>

  <h3>6.1 定义：把 x 冻住，对 y 积分</h3>
  <p>设 $f(x,y)$ 是二元函数。把 $x$ 固定（当成常数），$f(x,y)$ 就变成关于 $y$ 的一元函数，可以积分：</p>
  <div class="formula">$$I(x) = \int_c^d f(x,y)\,dy$$</div>
  <p>不同的 $x$ 给出不同的积分值，所以 $I(x)$ 是 $x$ 的<b>新函数</b>——这叫"含参量积分"（$x$ 是参量）。更一般地，上下限也可以依赖 $x$：</p>
  <div class="formula">$$I(x) = \int_{c(x)}^{d(x)} f(x,y)\,dy$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：一个"积分机器"</div>
    想象一台机器：输入一个 $x$，机器先"冻住 $x$"，把 $f(x,y)$ 关于 $y$ 从 $c(x)$ 积到 $d(x)$，吐出数字 $I(x)$。这台机器定义了一个新函数。
    <p>为什么这有用？很多"奇怪"的函数（比如误差函数、Γ函数）都是这样出生的：<b>用积分造新函数</b>。</p>
  </div>

  <h3>6.2 连续性：极限可以钻进积分号</h3>
  <p><b>定理 19.1</b>：若 $f(x,y)$ 在矩形 $R=[a,b]\times[c,d]$ 上连续，则 $I(x)=\int_c^d f(x,y)dy$ 在 $[a,b]$ 上连续。</p>
  <p>连续 = $\lim_{x\to x_0} I(x) = I(x_0)$。展开写：</p>
  <div class="formula">$$\lim_{x\to x_0}\int_c^d f(x,y)\,dy = \int_c^d \lim_{x\to x_0}f(x,y)\,dy = \int_c^d f(x_0,y)\,dy$$</div>
  <p>也就是<b>极限和积分可以交换顺序</b>。为什么能换？因为 $f$ 连续（在闭区域上还"一致连续"），$x$ 动一点点，$f(x,y)$ 到处都只动一点点，积分值也只动一点点。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">定理 19.1 的完整证明（epsilon-delta）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>要证：对任意 $\varepsilon>0$，存在 $\delta>0$，使 $|x-x_0|<\delta$ 时 $|I(x)-I(x_0)|<\varepsilon$。</p>
        <p>差值：$I(x)-I(x_0) = \int_c^d [f(x,y)-f(x_0,y)]dy$。</p>
        <p>关键：$f$ 在闭矩形上连续 ⇒ 一致连续：对 $\varepsilon'=\frac{\varepsilon}{d-c}$，存在 $\delta>0$，只要 $|x-x_0|<\delta$，对<b>所有</b> $y\in[c,d]$ 都有 $|f(x,y)-f(x_0,y)|<\frac{\varepsilon}{d-c}$。</p>
        <p>于是（绝对值进积分：$|\int g|\le\int|g|$）：</p>
        <p>$$|I(x)-I(x_0)| \le \int_c^d \frac{\varepsilon}{d-c}\,dy = \frac{\varepsilon}{d-c}(d-c) = \varepsilon$$</p>
        <p>连续得证。"一致连续"保证 $\delta$ 不依赖 $y$——这是换序合法的关键。</p>
      </div>
    </div>
  </div>
  <p><b>定理 19.2</b>（上下限也动）：若 $f(x,y)$ 连续、$c(x),d(x)$ 连续，则 $I(x)=\int_{c(x)}^{d(x)}f(x,y)dy$ 连续。做法：换元 $y=c(x)+t(d(x)-c(x))$ 把它变成固定区间 $[0,1]$ 的积分，再用定理 19.1。</p>

  <h4>数值例子：极限钻进积分号</h4>
  <p>求 $\lim_{a\to0}\int_a^{1+a}\frac{dx}{1+x^2+a^2}$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用连续性定理求极限</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>被积函数 $\frac{1}{1+x^2+a^2}$ 关于 $(a,x)$ 连续，上下限 $a$ 和 $1+a$ 关于 $a$ 连续。由定理 19.2，$I(a)$ 在 $a=0$ 连续。</p>
        <p>所以 $\lim_{a\to0}I(a) = I(0) = \int_0^1 \frac{dx}{1+x^2} = \arctan x\Big|_0^1 = \frac{\pi}{4}$。</p>
        <p>（用到 $\int\frac{dx}{1+x^2}=\arctan x$，这是第 1 章原函数表的延伸。）</p>
      </div>
    </div>
  </div>

  <h3>6.3 可微性：导数钻进积分号（积分号下求导）</h3>
  <p><b>定理 19.3</b>：若 $f(x,y)$ 和 $f_x(x,y)$ 在矩形 $R$ 上连续，则 $I(x)=\int_c^d f(x,y)dy$ 可微，且</p>
  <div class="formula">$$I'(x) = \frac{d}{dx}\int_c^d f(x,y)\,dy = \int_c^d f_x(x,y)\,dy$$</div>
  <p>即<b>先积分再求导 = 先求导再积分</b>。条件：被积函数和它的偏导都要连续。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">定理 19.3 的完整证明</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>差商：$\frac{I(x+\Delta x)-I(x)}{\Delta x} = \int_c^d \frac{f(x+\Delta x,y)-f(x,y)}{\Delta x}dy$。</p>
        <p>对括号里的差商用<b>拉格朗日中值定理</b>（第 1 章导数章节的定理：$f(b)-f(a)=f'(\xi)(b-a)$）：存在 $\theta\in(0,1)$ 使</p>
        <p>$$\frac{f(x+\Delta x,y)-f(x,y)}{\Delta x} = f_x(x+\theta\Delta x, y)$$</p>
        <p>由于 $f_x$ 一致连续，$\Delta x\to0$ 时 $f_x(x+\theta\Delta x,y)$ 一致地逼近 $f_x(x,y)$（对 $y$ 一致）。于是</p>
        <p>$$\frac{I(x+\Delta x)-I(x)}{\Delta x} \to \int_c^d f_x(x,y)\,dy$$</p>
        <p>这正是导数定义。证毕。核心还是<b>一致连续让"取极限"和"积分"换序合法</b>。</p>
      </div>
    </div>
  </div>
  <p><b>定理 19.4</b>（上下限也动）：若 $f, f_x$ 连续，$c(x),d(x)$ 可微，则</p>
  <div class="formula">$$I'(x) = \int_{c(x)}^{d(x)} f_x(x,y)\,dy + f(x,d(x))\,d'(x) - f(x,c(x))\,c'(x)$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：三个来源的增量</div>
    <p>$I(x)$ 变化来自三处：① 被积函数整体随 $x$ 变（积分号内求导）；② 上限 $d(x)$ 动（多了 $f(x,d)\cdot d'$，即"新长出来的一小条"）；③ 下限 $c(x)$ 动（少了 $f(x,c)\cdot c'$，减号）。</p>
    <p>类比：队伍变长了——既因为每个人变"胖"（被积函数变），又因为进队和出队的人（上下限变）。</p>
  </div>

  <h4>数值例子：补例（教材补例）</h4>
  <p>$\varphi(x) = \int_x^{x^2}\frac{\sin xy}{y}\,dy$，求 $\varphi'(x)$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用定理 19.4 完整计算</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>对 $x$ 求偏导（被积函数里 $y$ 是哑变量，$x$ 在 $\sin xy$ 里）：$f_x = \frac{y\cos(xy)}{y} = \cos(xy)$。</p>
        <p>上限 $d(x)=x^2$，$d'=2x$；下限 $c(x)=x$，$c'=1$。</p>
        <p>$$\varphi'(x) = \int_x^{x^2}\cos(xy)\,dy + f(x,x^2)\cdot 2x - f(x,x)\cdot 1$$</p>
        <p>$f(x,x^2)=\frac{\sin(x\cdot x^2)}{x^2}=\frac{\sin x^3}{x^2}$；$f(x,x)=\frac{\sin(x\cdot x)}{x}=\frac{\sin x^2}{x}$。</p>
        <p>$$\varphi'(x) = \int_x^{x^2}\cos(xy)\,dy + \frac{2x\sin x^3}{x^2} - \frac{\sin x^2}{x} = \frac{\sin x^3 - \sin x^2}{x} + \frac{2\sin x^3}{x} - \frac{\sin x^2}{x}$$</p>
        <p>$$= \frac{3\sin x^3 - 2\sin x^2}{x}$$</p>
        <p>（第一步：$\int_x^{x^2}\cos(xy)dy = \frac{\sin(xy)}{x}\Big|_y^{x^2} = \frac{\sin x^3-\sin x^2}{x}$。）与教材答案一致。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：经典积分 ln(1+x)/(1+x²)</h4>
  <p>计算 $I = \int_0^1 \frac{\ln(1+x)}{1+x^2}dx$。这是"参数法"的经典示范：先造一个带参数的积分，求导，再对参数积分。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">参数法求 I（教材例 3 解法一）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>造参数</b>：$I(\alpha) = \int_0^1\frac{\ln(1+\alpha x)}{1+x^2}dx$，则 $I(0)=0$，$I(1)=I$。</p>
        <p><b>积分号下求导</b>（$\frac{\partial}{\partial\alpha}\ln(1+\alpha x)=\frac{x}{1+\alpha x}$）：</p>
        <p>$$I'(\alpha) = \int_0^1 \frac{x}{(1+x^2)(1+\alpha x)}dx$$</p>
        <p><b>部分分式</b>（把 $\frac{x}{(1+x^2)(1+\alpha x)}$ 拆成简单分式之和）。设 $\frac{x}{(1+x^2)(1+\alpha x)} = \frac{Ax+B}{1+x^2}+\frac{C}{1+\alpha x}$：</p>
        <p>通分比较分子：$x = (Ax+B)(1+\alpha x)+C(1+x^2)$</p>
        <p>展开：$= A x + B + A\alpha x^2 + B\alpha x + C + C x^2$</p>
        <p>匹配系数：$x^2$: $A\alpha+C=0$；$x^1$: $A+B\alpha=1$；$x^0$: $B+C=0$。</p>
        <p>解得：$C=-A\alpha$，$B=-C=A\alpha$，$A+B\alpha = A + A\alpha^2 = 1$，$A=\frac{1}{1+\alpha^2}$，$B=\frac{\alpha}{1+\alpha^2}$，$C=-\frac{\alpha}{1+\alpha^2}$。</p>
        <p>代入：$I'(\alpha) = \int_0^1\left[\frac{\frac{x}{1+\alpha^2}+\frac{\alpha}{1+\alpha^2}}{1+x^2} - \frac{\frac{\alpha}{1+\alpha^2}}{1+\alpha x}\right]dx$</p>
        <p>$= \frac{1}{1+\alpha^2}\int_0^1\frac{x+\alpha}{1+x^2}dx - \frac{\alpha}{1+\alpha^2}\int_0^1\frac{dx}{1+\alpha x}$</p>
        <p>$= \frac{1}{1+\alpha^2}\left[\frac12\ln(1+x^2)+\alpha\arctan x\right]_0^1 - \frac{\alpha}{1+\alpha^2}\cdot\frac{\ln(1+\alpha x)}{\alpha}\Big|_0^1$</p>
        <p>$= \frac{1}{1+\alpha^2}\left(\frac12\ln2 + \alpha\frac{\pi}{4}\right) - \frac{\ln(1+\alpha)}{1+\alpha^2}$</p>
        <p><b>再对 α 积分</b>（$I(1)-I(0)=\int_0^1 I'(\alpha)d\alpha$）：</p>
        <p>$I = \frac{\ln2}{2}\int_0^1\frac{d\alpha}{1+\alpha^2} + \frac{\pi}{4}\int_0^1\frac{\alpha\,d\alpha}{1+\alpha^2} - \int_0^1\frac{\ln(1+\alpha)}{1+\alpha^2}d\alpha$</p>
        <p>第一个积分 $=\frac{\ln2}{2}\cdot\frac{\pi}{4}=\frac{\pi\ln2}{8}$；第二个 $=\frac{\pi}{4}\cdot\frac12\ln2=\frac{\pi\ln2}{8}$；第三个正好是 $I$（就是原积分）！</p>
        <p>所以 $I = \frac{\pi\ln2}{8}+\frac{\pi\ln2}{8}-I$，移项 $2I=\frac{\pi\ln2}{4}$，$I=\frac{\pi\ln2}{8}$。</p>
        <p>妙处：解方程解出了自己！这就是"积分号下求导"的威力。</p>
      </div>
    </div>
  </div>

  <h3>6.4 可积性：累次积分可换序（富比尼定理初阶版）</h3>
  <p><b>定理 19.6</b>：若 $f(x,y)$ 在矩形 $R=[a,b]\times[c,d]$ 上连续，则</p>
  <div class="formula">$$\int_a^b dx\int_c^d f(x,y)\,dy = \int_c^d dy\int_a^b f(x,y)\,dx$$</div>
  <p>即<b>先对 y 积再对 x 积 = 先对 x 积再对 y 积</b>，与顺序无关。这种"先积一个变量再积另一个"的写法叫<b>累次积分</b>。</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：数豆子的两种方式</div>
    <p>一块地里种了豆子（密度 $f$）。算总产量：可以"按行收"（先对 $y$ 积分 = 每行的产量，再对 $x$ 加总），也可以"按列收"。结果当然一样——只要豆子密度连续（没有诡异的分布）。</p>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">定理 19.6 的证明思路</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>记 $I_1(u)=\int_a^u dx\int_c^d f\,dy$，$I_2(u)=\int_c^d dy\int_a^u f\,dx$。</p>
        <p>$I_1'(u) = \int_c^d f(u,y)dy$（外层积分的导数，微积分基本定理）。</p>
        <p>$I_2'(u) = \int_c^d f(u,y)dy$（定理 19.3 积分号下求导）。</p>
        <p>两者导数相同 ⇒ $I_1(u)=I_2(u)+$ 常数。$u=a$ 时都为 0 ⇒ 常数 0。取 $u=b$ 得等式。</p>
        <p>漂亮：用"导数相同则函数相差常数"把换序问题转化为求导问题。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：换序算积分</h4>
  <p>$I=\int_0^1\frac{x^b-x^a}{\ln x}dx$（$b>a>0$）。直接积分不会（$\ln x$ 在分母）。换序：</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用"积分表示分子"再换序</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>关键恒等式：$\int_a^b x^y dy = \frac{x^b - x^a}{\ln x}$（因为 $\int x^y dy = \frac{x^y}{\ln x}$）。</p>
        <p>所以 $I = \int_0^1 dx\int_a^b x^y dy$。$x^y$ 在 $[0,1]\times[a,b]$ 连续（$a>0$），由定理 19.6 换序：</p>
        <p>$$I = \int_a^b dy\int_0^1 x^y dx = \int_a^b \frac{1}{y+1}dy = \ln(y+1)\Big|_a^b = \ln\frac{1+b}{1+a}$$</p>
        <p>（用到 $\int_0^1 x^y dx = \frac{1}{y+1}$，因为 $x^{y+1}/(y+1)\Big|_0^1$。）</p>
        <p>妙：换序让"没法积的积分"变成"会积的积分"。</p>
      </div>
    </div>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：$I(x)=\int_0^1 e^{xy}dy$，求 $I'(x)$ 和 $I(x)$ 本身。</div>
    <div class="qa-a"><b>答案</b>：$I'(x)=\int_0^1 ye^{xy}dy$（积分号下求导）。直接算：$I(x)=\frac{e^{xy}}{x}\Big|_0^1=\frac{e^x-1}{x}$，再验证导数：$I'(x)=\frac{xe^x-(e^x-1)}{x^2}$。两种方法一致。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：为什么"一致连续"这么重要？（第 6 章的核心）</div>
    <div class="qa-a"><b>答案</b>：一致连续保证"一个 $\delta$ 对全场 $y$ 都有效"，这样才能把 $\lim$ 从积分号外搬进积分号内（换序）。普通连续只在单点附近成立，不够用。这是第 19 章所有换序定理的公共基础。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：$\int_0^1 dx\int_0^1 (x+y)dy$ 等于多少？（验算换序）</div>
    <div class="qa-a"><b>答案</b>：先对 $y$：$\int_0^1(x+y)dy = x+\frac12$，再对 $x$：$\int_0^1(x+\frac12)dx=\frac12+\frac12=1$。换序：先对 $x$：$\int_0^1(x+y)dx=\frac12+y$，再对 $y$：$\int_0^1(\frac12+y)dy=\frac12+\frac12=1$。一致 ✓。</div>
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：improper-param ===== -->
<section class="chapter" id="improper-param" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">7</span>含参量反常积分：一致收敛</h2>
  <p class="lead">前置知识：反常积分（无穷限、瑕积分）、级数收敛、含参量正常积分（第 6 章）。后续应用：欧拉积分（第 8 章）。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 积分上限变成无穷大时，第 6 章的换序还成立吗？——不一定！必须加一个条件：<b>一致收敛</b>。</p>
    <p>② 什么叫一致收敛？——"尾巴"（从 $A$ 到 $\infty$ 的部分）对<b>所有 $x$ 同时</b>变得任意小。</p>
    <p>③ 怎么判断一致收敛？——M 判别法（找一个统一的"大块头"压住）、狄利克雷/阿贝尔判别法。</p>
  </div>

  <h3>7.1 为什么换序会失败：一个反例</h3>
  <p>先看危险在哪。考虑 $\int_0^\infty f(x,y)dy$，$f$ 连续。想换序 $\lim\int = \int\lim$。若 $f$ 在"远方"（$y$ 很大处）随 $x$ 变化不一致，不同 $x$ 的"尾巴"消失速度不同，换序就崩。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">反例</span><span class="derive-step-title">一个换序失败的例子（感受一下）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>想象 $f(x,y)$ 对每个 $x$ 都是一座"小土包"，但土包的位置随着 $x$ 不断向右（向无穷远）移动。</p>
        <p>对每个固定的 $x$，土包在有限处，积分有确定值（比如总质量 1）。</p>
        <p>但 $x$ 趋于某值时，土包跑到无穷远——"尾巴"始终没收干净。</p>
        <p>结果：$I(x)$ 的极限 ≠ 极限处的积分。这就是"不一致收敛"的灾难。</p>
        <p>形式化反例：$f(x,y)=xy e^{-x^2y^2}$ 之类的函数可以精确构造这种失败。结论：<b>无穷区间上换序必须检查"一致收敛"</b>。</p>
      </div>
    </div>
  </div>

  <h3>7.2 一致收敛的定义：把"每个 x"升级成"所有 x 一起"</h3>
  <p><b>普通收敛</b>（对每个固定的 $x$）：$\int_A^\infty f(x,y)dy \to 0$（$A\to\infty$）。即对每个 $x$，尾巴都能变任意小。</p>
  <p><b>一致收敛</b>（对 $x\in J$ 全体）：同一个 $A$ 够大时，<b>所有 $x$</b> 的尾巴同时小于 $\varepsilon$。即</p>
  <div class="formula">$$\forall \varepsilon>0,\; \exists N>c,\; \forall A>N,\; \forall x\in J:\; \left|\int_A^\infty f(x,y)dy\right| < \varepsilon$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：全班统一交作业</div>
    <p>普通收敛：每个同学（每个 $x$）自己保证"再给我足够多的时间，我能把尾巴收完"——但每个人需要的时间不同。</p>
    <p>一致收敛：<b>全班有一个共同的截止日期</b>（同一个 $N$），到期后所有同学（所有 $x$）的尾巴都收完了。</p>
    <p>差别就在"同一个 $N$"：一致 = 统一标准，不依赖 $x$。</p>
  </div>
  <p><b>判别工具 1：柯西准则（定理 19.7）</b>：$I(x)$ 在 $[a,b]$ 上一致收敛 ⟺ 对任意 $\varepsilon>0$，存在 $N$，当 $A_1,A_2>N$ 时对所有 $x$ 有 $\left|\int_{A_1}^{A_2}f(x,y)dy\right|<\varepsilon$。即"中段"也能同时收小。</p>

  <h3>7.3 判别法一：M 判别法（魏尔斯特拉斯）</h3>
  <p><b>定理 19.8（M 判别法）</b>：若存在"大块头"函数 $g(y)\ge0$，使对一切 $x\in J$、$y\ge c$ 有 $|f(x,y)|\le g(y)$，且 $\int_c^\infty g(y)dy$ 收敛，则 $\int_c^\infty f(x,y)dy$ 在 $J$ 上一致收敛。</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：用统一的雨伞遮住所有人</div>
    <p>给所有 $x$ 的 $f$ 找一把共同的"伞" $g$：谁的绝对值都不超过伞的边界。伞的总面积（积分）有限，那所有人（所有 $x$）的尾巴同时被伞压住，一起收敛。</p>
    <p>为什么需要 $g$ 不依赖 $x$？因为这样才拿到"同一个 $N$"（一致）。</p>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">M 判别法证明（三行）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>对任意 $x$ 和 $A_1&lt;A_2$：</p>
        <p>$$\left|\int_{A_1}^{A_2}f(x,y)dy\right| \le \int_{A_1}^{A_2}|f(x,y)|dy \le \int_{A_1}^{A_2}g(y)dy$$</p>
        <p>因为 $\int_c^\infty g\,dy$ 收敛，由柯西准则，$\int_{A_1}^{A_2}g\,dy$ 对大的 $A_1,A_2$ 任意小（<em>不依赖 $x$！</em>）。</p>
        <p>所以 $f$ 的积分也任意小（同样不依赖 $x$），由柯西准则得一致收敛。证毕。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：M 判别法</h4>
  <p>证明 $\int_0^\infty\frac{\cos xy}{1+x^2}dx$ 在 $y\in(-\infty,\infty)$ 上一致收敛。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">找伞 g(x)=1/(1+x²)</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>对任何实数 $y$：$|\cos xy|\le1$，所以 $\left|\frac{\cos xy}{1+x^2}\right| \le \frac{1}{1+x^2}$。</p>
        <p>而 $\int_0^\infty\frac{dx}{1+x^2}=\frac{\pi}{2}$ 收敛。</p>
        <p>M 判别法生效：一致收敛。</p>
        <p>（注意这里参量是 $y$，积分变量是 $x$——谁当参量、谁当积分变量不重要，方法一样。）</p>
      </div>
    </div>
  </div>

  <h3>7.4 判别法二、三：狄利克雷与阿贝尔</h3>
  <p>M 判别法要求"伞"存在。但 $\int_0^\infty\frac{\sin x}{x}dx$ 这类积分没有"伞"（$\frac{|\sin x|}{x}$ 的积分发散），却依然收敛——靠震荡。这类要用狄利克雷/阿贝尔判别法。</p>
  <p><b>狄利克雷判别法</b>：若 ① $\int_c^N f(x,y)dy$ 对 $N$ 一致有界；② $g(x,y)$ 关于 $y$ 单调且一致趋于 0（$y\to\infty$），则 $\int_c^\infty f(x,y)g(x,y)dy$ 一致收敛。</p>
  <p><b>阿贝尔判别法</b>：若 ① $\int_c^\infty f(x,y)dy$ 一致收敛；② $g(x,y)$ 关于 $y$ 单调且一致有界，则 $\int_c^\infty fg\,dy$ 一致收敛。</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：震荡乘以单调</div>
    <p>狄利克雷：$f$ 是"来回震荡的钟摆"（积分一致有界，钟摆不跑飞），$g$ 是"逐渐停下来的阻尼"（单调趋于 0）——钟摆×阻尼，自然慢慢停住，而且所有 $x$ 一起停（一致）。</p>
    <p>阿贝尔：$f$ 本身已经"好好收敛"，$g$ 只是"有礼貌地乘上去"（单调有界），不会捣乱。</p>
    <p>类比：狄利克雷像"摇摆的秋千慢慢停下"，阿贝尔像"给已经停稳的钟再轻轻盖上布"。</p>
  </div>

  <h4>数值例子：狄利克雷型</h4>
  <p>证明 $\int_0^\infty e^{-xy}\frac{\sin x}{x}dx$ 在 $y\in[0,d]$ 上一致收敛。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">判</span><span class="derive-step-title">用阿贝尔判别法</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>拆成 $f(x,y)=\frac{\sin x}{x}$ 和 $g(x,y)=e^{-xy}$。</p>
        <p>① $\int_0^\infty\frac{\sin x}{x}dx$ 收敛（经典狄利克雷积分 $=\frac{\pi}{2}$，不含参量所以"一致"地收敛）。</p>
        <p>② $g(x,y)=e^{-xy}$ 对每个 $y\in[0,d]$ 关于 $x$ 单调递减（$e$ 的负指数次方），且 $0\le e^{-xy}\le1$ 一致有界。</p>
        <p>由阿贝尔判别法：一致收敛。✓</p>
        <p>这个积分在 $y=0$ 处等于 $\frac{\pi}{2}$，是后面算 $\int_0^\infty\frac{\sin ax}{x}dx$ 的跳板。</p>
      </div>
    </div>
  </div>

  <h3>7.5 一致收敛下的三大性质：连续、可微、可积</h3>
  <p>第 6 章的换序定理，在"一致收敛"条件下对无穷区间照样成立：</p>
  <div class="formula">
    <p><b>定理 19.10（连续性）</b>：$f$ 连续 + 积分一致收敛 ⇒ $I(x)$ 连续，且 $\lim_{x\to x_0}\int_c^\infty f\,dy = \int_c^\infty \lim_{x\to x_0} f\,dy$（极限入积分号）。</p>
    <p><b>定理 19.11（可微性）</b>：$f, f_x$ 连续 + $I(x)$ 收敛 + $\int_c^\infty f_x\,dy$ 一致收敛 ⇒ $I'(x)=\int_c^\infty f_x\,dy$（导数入积分号）。</p>
    <p><b>定理 19.12（可积性）</b>：$f$ 连续 + $I(x)$ 在 $[a,b]$ 上一致收敛 ⇒ $\int_a^b I(x)dx = \int_c^\infty dy\int_a^b f\,dx$（换序）。</p>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">口诀</div>
    <b>有限区间：连续就够换序。无穷区间：连续 + 一致收敛才能换序。</b>多出来的是"一致收敛"，因为尾巴必须对所有 $x$ 同时收干净。
  </div>

  <h4>数值例子：算狄利克雷积分</h4>
  <p>算 $\int_0^\infty\frac{\sin ax}{x}dx$（$a$ 任意实数）。这是含参量反常积分的王牌例题。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">五步走：造参数、求导、解微分方程、取极限</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>第 1 步，造参数</b>：$F(p)=\int_0^\infty e^{-px}\frac{\sin ax}{x}dx$（$p\ge0$）。我们想求 $F(0)$。</p>
        <p><b>第 2 步，积分号下求导</b>：$\frac{\partial}{\partial p}\left(e^{-px}\frac{\sin ax}{x}\right)=-e^{-px}\sin ax$。</p>
        <p>先验证一致收敛：$|-e^{-px}\sin ax|\le e^{-px}$，$\int_0^\infty e^{-px}dx=\frac1p$ 收敛，M 判别法 ⇒ 一致收敛。定理 19.11 可用：</p>
        <p>$$F'(p) = -\int_0^\infty e^{-px}\sin ax\,dx = -\frac{a}{p^2+a^2}$$</p>
        <p>（这个"基本积分"怎么来的？——见下方推导框。不跳步原则：任何一步都要能自己算出来。）</p>
        <div class="derive-step">
          <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">∫e^(-px)sin(ax)dx 的完整推导（两次分部积分 + 解方程）</span><span class="derive-step-arrow">▶</span></div>
          <div class="derive-step-body">
            <p>记 $K=\int_0^\infty e^{-px}\sin(ax)dx$（$p>0$）。</p>
            <p><b>第一次分部积分</b>：$u=\sin(ax)$，$dv=e^{-px}dx$，$du=a\cos(ax)dx$，$v=-\frac1p e^{-px}$：</p>
            <p>$K = \left[-\frac1p e^{-px}\sin(ax)\right]_0^\infty + \frac{a}{p}\int_0^\infty e^{-px}\cos(ax)dx$</p>
            <p>边界项：$x=0$ 处 $-\frac1p\cdot1\cdot0=0$；$x\to\infty$ 处 $e^{-px}\to0$。所以 $K=\frac{a}{p}L$，其中 $L=\int_0^\infty e^{-px}\cos(ax)dx$。</p>
            <p><b>第二次分部积分</b>（对 $L$）：$u=\cos(ax)$，$dv=e^{-px}dx$，$du=-a\sin(ax)dx$，$v=-\frac1p e^{-px}$：</p>
            <p>$L = \left[-\frac1p e^{-px}\cos(ax)\right]_0^\infty - \frac{a}{p}\int_0^\infty e^{-px}\sin(ax)dx = \frac1p - \frac{a}{p}K$</p>
            <p>（边界项：$x=0$ 处 $-\frac1p\cdot1\cdot1=-\frac1p$，$x\to\infty$ 处为 0，所以 $0-(-\frac1p)=\frac1p$。）</p>
            <p><b>联立解方程</b>：$K=\frac{a}{p}L$ 且 $L=\frac1p-\frac{a}{p}K$。代入：$K=\frac{a}{p}(\frac1p-\frac{a}{p}K)=\frac{a}{p^2}-\frac{a^2}{p^2}K$。</p>
            <p>移项：$K(1+\frac{a^2}{p^2})=\frac{a}{p^2}$，即 $K\cdot\frac{p^2+a^2}{p^2}=\frac{a}{p^2}$，所以 $K=\frac{a}{p^2+a^2}$。✓</p>
            <p>套路：<b>分部积分两次后，要求的积分出现在方程两边，解方程得到它</b>——和第 6 章例 3（$\frac{\pi\ln2}{8}$）同一个灵魂。</p>
          </div>
        </div>
        <p><b>第 3 步，对 p 积分</b>：$F(p)=\int -\frac{a}{p^2+a^2}dp = -\arctan\frac{p}{a}+C$。</p>
        <p><b>第 4 步，定常数</b>：$F(p)\to 0$（$p\to\infty$，因为 $e^{-px}$ 压扁一切），所以 $C=\arctan(\infty)=\frac{\pi}{2}$（$a>0$）。$F(p)=\frac{\pi}{2}-\arctan\frac{p}{a}$。</p>
        <p><b>第 5 步，取极限</b>：$p\to0^+$ 时积分在 $p\ge0$ 上一致收敛（前面阿贝尔判别法已证），$F$ 连续，所以</p>
        <p>$$\int_0^\infty\frac{\sin ax}{x}dx = F(0) = \lim_{p\to0^+}\left(\frac{\pi}{2}-\arctan\frac pa\right) = \frac{\pi}{2}\quad(a>0)$$</p>
        <p>$a<0$ 时是 $-\frac{\pi}{2}$（奇函数），$a=0$ 时是 0。合写：$\frac{\pi}{2}\operatorname{sgn}(a)$。</p>
        <p><b>sgn 是什么？</b>读作"符号函数"，就是"看正负"：正数返回 1，负数返回 -1，0 返回 0。$\operatorname{sgn}(a)=\begin{cases}1&a>0\\0&a=0\\-1&a<0\end{cases}$。合写省去分情况讨论。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">这题的套路（必考）</div>
    <p>含参量反常积分的标准流程：<b>① 塞一个收敛因子（如 $e^{-px}$）把"病态"积分变成好积分 → ② 积分号下求导 → ③ 解出 $F(p)$ → ④ 让 $p\to$ 边界值。</b>塞进去的因子像"给病人打镇静剂"，算完再撤掉。</p>
  </div>

  <h4>数值例子：高斯型的 e^{-x²}cos(rx)</h4>
  <p>$\varphi(r)=\int_0^\infty e^{-x^2}\cos(rx)dx$（在概率论/傅里叶分析里极重要）。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求导得微分方程，解出 φ(r)</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>① 求导（一致收敛用 M 判别法，$|-x e^{-x^2}\sin rx|\le x e^{-x^2}$ 可积）：</p>
        <p>$$\varphi'(r) = -\int_0^\infty x e^{-x^2}\sin(rx)dx$$</p>
        <p>② 分部积分（$u=\sin rx,\; dv = -xe^{-x^2}dx$，$v=\frac12e^{-x^2}$）：</p>
        <p>$\int_0^\infty x e^{-x^2}\sin(rx)dx = \left[\frac12e^{-x^2}\sin rx\right]_0^\infty - \frac r2\int_0^\infty e^{-x^2}\cos(rx)dx = -\frac r2\varphi(r)$</p>
        <p>所以 $\varphi'(r) = \frac r2\varphi(r)$，即 $\varphi'=\frac{r}{2}\varphi$——一个简单的微分方程！</p>
        <p>③ 解：$\frac{d\varphi}{\varphi}=\frac r2 dr$，两边积分 $\ln\varphi=\frac{r^2}{4}+C$，$\varphi(r)=Ce^{r^2/4}$。</p>
        <p>④ 定常数：$\varphi(0)=\int_0^\infty e^{-x^2}dx=\frac{\sqrt\pi}{2}$（高斯积分，已知结论），所以 $C=\frac{\sqrt\pi}{2}$。</p>
        <p>$$\varphi(r) = \frac{\sqrt\pi}{2}e^{-r^2/4}$$</p>
        <p>看：一个看似复杂的积分，用"求导建微分方程"就解出来了。</p>
      </div>
    </div>
  </div>

  <h3>7.6 含参量无界函数反常积分（瑕积分版）</h3>
  <p>如果"病"在区间内部或端点的奇点（如 $\int_c^d\frac{dy}{(y-c)^\alpha}$ 在 $y=c$ 处发散），处理完全平行：定义"瑕点处一致收敛"，判别法照搬（M 判别法、狄利克雷等），性质照搬。方法一致，只是"尾巴"换成"靠近瑕点的部分"。</p>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：$\int_0^\infty e^{-px}\frac{\sin ax}{x}dx$ 在 $p>0$ 上为什么一致收敛？（不用判别法名字，用直觉说）</div>
    <div class="qa-a"><b>答案</b>：$e^{-px}$ 是"统一的压缩弹簧"——无论 $a,x$ 取什么，尾巴都被 $e^{-px}$ 压住，而 $\int_0^\infty e^{-px}dx$ 有限。压住所有人的力量不依赖 $a$，所以一致。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：M 判别法和"每个 x 单独收敛"的区别是什么？为什么必须区分？</div>
    <div class="qa-a"><b>答案</b>：区别在"同一个 $N$"。每个 $x$ 单独收敛允许每个 $x$ 用不同的 $N$；一致收敛要求一个共同的 $N$ 管住所有 $x$。必须区分是因为换序定理（极限入积分号）需要"尾巴同时消失"，否则极限过程会与积分过程打架。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：$F(p)=\int_0^\infty e^{-px}\frac{\sin x}{x}dx$ 在 $p=0$ 处能直接代入吗？</div>
    <div class="qa-a"><b>答案</b>：不能直接代入 $p=0$（此时积分 $\int_0^\infty\frac{\sin x}{x}dx$ 只是条件收敛，不是一致收敛的极限可直接换）。但 $F(p)$ 在 $p\ge0$ 连续（阿贝尔判别法保证），所以可以用连续性 $\lim_{p\to0^+}F(p)$ 来取——极限进入积分号是合法的。这正是上例第 5 步的精细之处。</div>
  </div>
  <div class="chapter-nav"></div>
</section>
"""

def write(path) -> None:
    path.write_text(CH_C, encoding='utf-8')

if __name__ == "__main__":
    from pathlib import Path
    out = Path(__file__).parent / 'chapters_c.py.txt'
    write(out)
    print('chapters_c 内容长度:', len(CH_C))
