#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""章节内容 D：欧拉积分 + 第一型曲线积分 + 总结自测"""

CH_D = r"""<!-- ===== 章节：euler-integral ===== -->
<section class="chapter" id="euler-integral" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">8</span>欧拉积分：Γ 函数与 B 函数</h2>
  <p class="lead">前置知识：反常积分、一致收敛与换序（第 7 章）、分部积分（第 1.6 节）、含参量积分的求导（第 6 章）。后续应用：概率论（Γ分布）、统计、数学物理。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 用含参量反常积分"造"两个新函数：Γ 函数 $\Gamma(s)$ 和 B 函数 $B(p,q)$。</p>
    <p>② 它们有什么性质？（递推、对称、连续、任意阶可导）</p>
    <p>③ 两个函数什么关系？——$B(p,q)=\frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$。</p>
  </div>

  <h3>8.1 Γ 函数：阶乘的"连续化"</h3>
  <div class="formula">$$\Gamma(s) = \int_0^\infty x^{s-1}e^{-x}dx, \qquad s > 0$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：阶乘的"成人版"</div>
    <p>初中就认识 $n!$（$3!=6$）。但它只对整数有意义。Γ 函数把阶乘"插值"成连续函数：$\Gamma(n+1)=n!$。</p>
    <p>以后遇到"$\frac12$ 的阶乘"这种怪问题，就用 $\Gamma(\frac12)=\sqrt\pi$。Γ 函数是数学里最著名的"新函数"之一。</p>
  </div>
  <p><b>为什么定义域是 $s>0$？</b>因为 $s-1<0$ 时 $x=0$ 是瑕点（$x^{s-1}$ 在 0 附近爆炸），需要收敛；$x\to\infty$ 时 $e^{-x}$ 把所有多项式压下去，远处没事。两个方向的病都得治，合起来 $s>0$。</p>

  <h4>推导：递推公式 Γ(s+1) = sΓ(s)（核心性质）</h4>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">用分部积分推出递推公式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Gamma(s+1) = \int_0^\infty x^{s}e^{-x}dx$</p>
        <p>分部积分：$u=x^s,\; dv=e^{-x}dx$，则 $du=sx^{s-1}dx,\; v=-e^{-x}$。</p>
        <p>$$\Gamma(s+1) = \left[-x^s e^{-x}\right]_0^\infty + s\int_0^\infty x^{s-1}e^{-x}dx$$</p>
        <p>边界项：$x=0$ 处 $0^s\cdot 1=0$；$x\to\infty$ 处 $e^{-x}$ 压过 $x^s$（指数比多项式跑得快），也是 0。所以边界项消失：</p>
        <p>$$\Gamma(s+1) = s\int_0^\infty x^{s-1}e^{-x}dx = s\,\Gamma(s)$$</p>
        <p>递推公式 $\boxed{\Gamma(s+1)=s\Gamma(s)}$ 得证。</p>
      </div>
    </div>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">从递推公式推出 Γ(n+1)=n!</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>连用递推公式：$\Gamma(n+1) = n\Gamma(n) = n(n-1)\Gamma(n-1) = \cdots = n!\cdot\Gamma(1)$。</p>
        <p>而 $\Gamma(1)=\int_0^\infty e^{-x}dx = 1$（基本积分，$e^{-x}$ 从 0 到 $\infty$ 总面积 1）。</p>
        <p>所以 $\Gamma(n+1)=n!$。✓ 阶乘的连续版。</p>
      </div>
    </div>
  </div>
  <p><b>其他性质</b>（教材逐个证明，思路都来自第 6、7 章的换序定理）：</p>
  <div class="formula">
    <p>• $\Gamma(s)$ 在 $s>0$ 上连续，且任意阶可导（利用 $f$ 与 $f_s$ 在闭区间上一致收敛 + 定理 19.11）。</p>
    <p>• 递推公式还能<b>延拓</b>：$\Gamma(s)=\frac{\Gamma(s+1)}{s}$ 把定义域扩到负半轴（除 $s=0,-1,-2,\dots$）。</p>
    <p>• $\Gamma(\frac12) = \sqrt\pi$（高斯积分）。</p>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">算 Γ(1/2) = √π</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Gamma(\frac12)=\int_0^\infty x^{-1/2}e^{-x}dx$。换元 $x=t^2$：$dx=2t\,dt$，$x^{-1/2}=1/t$：</p>
        <p>$$\Gamma(\tfrac12) = \int_0^\infty \frac{1}{t}e^{-t^2}\cdot 2t\,dt = 2\int_0^\infty e^{-t^2}dt = 2\cdot\frac{\sqrt\pi}{2} = \sqrt\pi$$</p>
        <p>（$\int_0^\infty e^{-t^2}dt=\frac{\sqrt\pi}{2}$ 是著名的高斯积分。为什么？见下一个折叠框的思路——需要二重积分知识，可先记住结论。）</p>
        <p>于是 $\Gamma(\frac32)=\frac12\Gamma(\frac12)=\frac{\sqrt\pi}{2}$，$\Gamma(\frac52)=\frac32\cdot\frac12\sqrt\pi=\frac{3\sqrt\pi}{4}$，等等。</p>
      </div>
    </div>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">思路</span><span class="derive-step-title">高斯积分 ∫e^(-t²)dt = √π/2 为什么成立（极坐标技巧）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $I = \int_0^\infty e^{-t^2}dt$。技巧：<b>把 $I$ 和自己相乘</b>，变成二重积分，再用极坐标。</p>
        <p>$I^2 = \int_0^\infty e^{-x^2}dx\cdot\int_0^\infty e^{-y^2}dy = \int_0^\infty\int_0^\infty e^{-(x^2+y^2)}dx\,dy$（两个独立积分相乘 = 二重积分）。</p>
        <p>换极坐标 $x=r\cos\theta,\;y=r\sin\theta$，$dx\,dy = r\,dr\,d\theta$（这是第 3 章雅可比 $=r$ 的直接应用！），区域是第一象限（$r\ge0,\;0\le\theta\le\frac\pi2$）：</p>
        <p>$I^2 = \int_0^{\pi/2}\int_0^\infty e^{-r^2}r\,dr\,d\theta = \int_0^{\pi/2}d\theta\int_0^\infty re^{-r^2}dr = \frac\pi2\cdot\frac12 = \frac\pi4$</p>
        <p>（$\int_0^\infty re^{-r^2}dr=\frac12$：换元 $u=r^2$，$du=2rdr$，$\frac12\int_0^\infty e^{-u}du=\frac12$。）</p>
        <p>所以 $I = \sqrt{\frac\pi4} = \frac{\sqrt\pi}{2}$。✓ 顺便看到：第 3 章的雅可比行列式在这里立了大功。</p>
      </div>
    </div>
  </div>

  <h3>8.2 B 函数：两个参数的积分</h3>
  <div class="formula">$$B(p,q) = \int_0^1 x^{p-1}(1-x)^{q-1}dx, \qquad p>0,\; q>0$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：分蛋糕的比例</div>
    $x$ 从 0 到 1（一整块蛋糕），$x^{p-1}(1-x)^{q-1}$ 度量"把蛋糕切成 $x$ 和 $1-x$ 两部分的权重"。$p,q$ 控制权重偏向哪头。$p=q=1$ 时被积函数 = 1，$B(1,1)=1$（整块蛋糕）。
  </div>
  <p><b>对称性</b>：$B(p,q)=B(q,p)$。证明：换元 $x=1-y$，被积函数里的 $x$ 和 $1-x$ 互换，$p,q$ 也跟着换。</p>
  <p><b>递推公式</b>：</p>
  <div class="formula">$$B(p,q)=\frac{q-1}{p+q-1}B(p,q-1),\qquad B(p,q)=\frac{p-1}{p+q-1}B(p-1,q)$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">推递推公式（用分部积分）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$B(p,q)=\int_0^1 x^{p-1}(1-x)^{q-1}dx$，分部积分：$u=(1-x)^{q-1},\; dv=x^{p-1}dx$，则 $du=-(q-1)(1-x)^{q-2}dx,\; v=\frac{x^p}{p}$。</p>
        <p>$$B(p,q) = \left[\frac{x^p}{p}(1-x)^{q-1}\right]_0^1 + \frac{q-1}{p}\int_0^1 x^p(1-x)^{q-2}dx$$</p>
        <p>边界项：两端都是 0（$x=0$ 处 $x^p$；$x=1$ 处 $(1-x)^{q-1}$，$q>1$ 时）。</p>
        <p>把 $x^p = x^{p-1}\cdot x$ 拆分：$\int_0^1 x^p(1-x)^{q-2}dx = \int_0^1 x^{p-1}(1-x)^{q-2}\cdot x\,dx$。而 $x = 1-(1-x)$，所以</p>
        <p>$= \int_0^1 x^{p-1}(1-x)^{q-2}dx - \int_0^1 x^{p-1}(1-x)^{q-1}dx = B(p,q-1) - B(p,q)$</p>
        <p>代入：$B(p,q) = \frac{q-1}{p}[B(p,q-1)-B(p,q)]$</p>
        <p>移项：$B(p,q)+\frac{q-1}{p}B(p,q) = \frac{q-1}{p}B(p,q-1)$，即 $\frac{p+q-1}{p}B(p,q)=\frac{q-1}{p}B(p,q-1)$。</p>
        <p>$$B(p,q) = \frac{q-1}{p+q-1}B(p,q-1)$$</p>
        <p>✓ 得证。另一个递推由对称性立刻得到。</p>
      </div>
    </div>
  </div>
  <p><b>其他形式</b>（教材列出的变形，做题常用）：换元 $x=\cos^2\theta$：</p>
  <div class="formula">$$B(p,q) = 2\int_0^{\pi/2}\sin^{2q-1}\theta\cos^{2p-1}\theta\,d\theta$$</div>
  <p>换元 $x=\frac{y}{1+y}$：</p>
  <div class="formula">$$B(p,q) = \int_0^\infty \frac{y^{p-1}}{(1+y)^{p+q}}dy$$</div>

  <h3>8.3 Γ 与 B 的关系：B = ΓΓ/Γ</h3>
  <div class="formula">$$B(p,q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$$</div>
  <p>（教材里这个关系的证明放到第二十一章，但整数情形可先自己验证。）</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">验</span><span class="derive-step-title">整数情形：B(m,n) 手算验证</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>用递推公式反复降阶：$B(m,n)=\frac{n-1}{m+n-1}\cdot\frac{n-2}{m+n-2}\cdots\frac{1}{m+1}B(m,1)$。</p>
        <p>而 $B(m,1)=\int_0^1 x^{m-1}dx=\frac{1}{m}$。</p>
        <p>所以 $B(m,n)=\frac{(n-1)!}{(m+1)(m+2)\cdots(m+n-1)}\cdot\frac1m = \frac{(n-1)!(m-1)!}{(m+n-1)!}$。</p>
        <p>而 $\frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)} = \frac{(m-1)!(n-1)!}{(m+n-1)!}$（用 $\Gamma(k+1)=k!$）。两边相等 ✓。</p>
        <p>数值验证：$B(2,3)=\int_0^1 x(1-x)^2dx=\frac1{12}$；公式 $\frac{1!2!}{4!}=\frac{2}{24}=\frac1{12}$ ✓。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：算 ∫₀^{π/2} sin²ⁿθ dθ</h4>
  <p>这是数学分析最经典的积分之一（Wallis 积分），用 B 函数秒杀。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用 B 函数算 sin 的偶次幂积分</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$I_{2n}=\int_0^{\pi/2}\sin^{2n}\theta d\theta$。要写成 $B$ 的形式：$\sin^{2q-1}\theta$ 匹配 $2q-1=2n$ 得 $q=n+\frac12$；$\cos^{2p-1}$ 匹配常数项 $2p-1=0$ 得 $p=\frac12$。</p>
        <p>由 $B$ 的三角函数形式：$2\int_0^{\pi/2}\sin^{2q-1}\cos^{2p-1}d\theta = B(p,q)$，所以</p>
        <p>$$I_{2n} = \frac12 B\left(\frac12, n+\frac12\right) = \frac12\cdot\frac{\Gamma(\frac12)\Gamma(n+\frac12)}{\Gamma(n+1)}$$</p>
        <p>用 $\Gamma(\frac12)=\sqrt\pi$，$\Gamma(n+\frac12)=\frac{(2n)!}{4^n n!}\sqrt\pi$（可自己用递推推出来），$\Gamma(n+1)=n!$：</p>
        <p>$$I_{2n} = \frac12\cdot\frac{\sqrt\pi\cdot\frac{(2n)!}{4^n n!}\sqrt\pi}{n!} = \frac{(2n)!}{2^{2n}(n!)^2}\cdot\frac{\pi}{2}$$</p>
        <p>验证 $n=1$：$\int_0^{\pi/2}\sin^2\theta d\theta=\frac{\pi}{4}$；公式 $\frac{2!}{4\cdot1}\cdot\frac\pi2=\frac\pi4$ ✓。</p>
        <p>$n=2$：$\int_0^{\pi/2}\sin^4\theta d\theta=\frac{3\pi}{16}$；公式 $\frac{24}{16\cdot4}\cdot\frac\pi2=\frac{3\pi}{16}$ ✓。</p>
        <p><b>Γ(n+½) 公式从哪来？</b>（递推验证）：$\Gamma(n+\frac12) = (n-\frac12)(n-\frac32)\cdots\frac12\cdot\Gamma(\frac12)$。把这些分数乘起来：$(n-\frac12)(n-\frac32)\cdots\frac12 = \frac{(2n-1)(2n-3)\cdots1}{2^n}$（分子是奇数连乘 $1\cdot3\cdots(2n-1)$）。而 $(2n)! = 1\cdot2\cdot3\cdots(2n) = (1\cdot3\cdots(2n-1))(2\cdot4\cdots2n) = (2n-1)!!\cdot2^n n!$，所以 $(2n-1)!! = \frac{(2n)!}{2^n n!}$。代入得 $\Gamma(n+\frac12)=\frac{(2n)!}{2^n n!}\cdot\frac{1}{2^n}\sqrt\pi=\frac{(2n)!}{4^n n!}\sqrt\pi$。✓</p>
      </div>
    </div>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：$\Gamma(\frac72)$ 等于多少？</div>
    <div class="qa-a"><b>答案</b>：$\Gamma(\frac72)=\frac52\cdot\frac32\cdot\frac12\cdot\sqrt\pi=\frac{15\sqrt\pi}{8}$。递推三次。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：$B(\frac12,\frac12)$ 是多少？（用公式）</div>
    <div class="qa-a"><b>答案</b>：$B(\frac12,\frac12)=\frac{\Gamma(\frac12)\Gamma(\frac12)}{\Gamma(1)}=\frac{\sqrt\pi\cdot\sqrt\pi}{1}=\pi$。直接积分验证：$\int_0^1\frac{dx}{\sqrt{x(1-x)}}=\pi$（换元 $x=\sin^2\theta$ 得 $\int_0^{\pi/2}2d\theta=\pi$）✓。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：为什么说 Γ 函数"任意阶可导"值得专门证明？</div>
    <div class="qa-a"><b>答案</b>：因为 $\Gamma(s)$ 是积分定义的函数，它的导数不是"显然"的——必须验证积分号下求导的合法性（被积函数和偏导一致收敛）。这是第 7 章换序定理的实践，也是"用积分造的新函数也需要证明性质"的典型例子。</div>
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：line-integral ===== -->
<section class="chapter" id="line-integral" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">9</span>第一型曲线积分：弯铁丝的质量</h2>
  <p class="lead">前置知识：定积分与"分割-近似-取极限"（第 1.6 节）、弧长微元 $ds$（第 1.6 节）、参数方程（初中就学过的 $x=\cos t, y=\sin t$）。后续应用：第二型曲线积分、曲面积分（后续章节）。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 定积分积的是直线段上的函数；曲线积分积的是<b>弯曲线</b>上的函数。</p>
    <p>② 典型背景：一根<b>弯铁丝</b>，各处密度不同，总质量怎么算？</p>
    <p>③ 计算公式：把"弧长微元 $ds$"换掉，就变成普通的定积分。</p>
  </div>

  <h3>9.1 从"直线杆"到"弯铁丝"</h3>
  <p>先回忆定积分：一段<b>直杆</b>，密度 $\rho(x)$ 随位置变化，总质量 $=\int_a^b\rho(x)dx$（分割-近似-取极限）。</p>
  <p>现在杆是<b>弯的</b>（比如一根弯曲的铁丝 $L$），密度 $\rho(x,y)$ 随位置变化。总质量怎么算？——还是"分割-近似-取极限"，只是把"小区间长度 $\Delta x$"换成"小段弧长 $\Delta s$"：</p>
  <div class="formula">$$\text{质量} = \lim_{||T||\to0}\sum_{i=1}^{n}\rho(P_i)\,\Delta s_i = \int_L \rho(x,y)\,ds$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：把弯铁丝剪成小段</div>
    <p>把铁丝剪成 $n$ 小段，每小段近似看成直线，质量 ≈ 密度 × 段长，加起来。剪得越细越准，取极限就是精确值。</p>
    <p>这和定积分一模一样，唯一的区别：<b>每段的"长度"是弧长 $\Delta s$ 而不是 $\Delta x$</b>。所以记号是 $\int_L \rho\,ds$ 而不是 $\int\rho\,dx$。</p>
  </div>
  <p><b>严格定义</b>：设 $L$ 是平面上可求长度的曲线段，$f(x,y)$ 定义在 $L$ 上。对 $L$ 做分割 $T$ 成 $n$ 段 $L_i$（弧长 $\Delta s_i$，细度 $||T||=\max\Delta s_i$），每段任取点 $(\xi_i,\eta_i)$，若极限 $\lim_{||T||\to0}\sum f(\xi_i,\eta_i)\Delta s_i$ 存在且与分割和取点无关，则称它为 $f$ 在 $L$ 上的<b>第一型曲线积分</b>，记 $\int_L f(x,y)ds$。</p>
  <p>空间曲线同理：$\int_L f(x,y,z)ds$。</p>

  <h3>9.2 弧长微元：弯度怎么折算</h3>
  <p>第 1.6 节已经埋好伏笔：曲线上极小一段，放大看是直角三角形，斜边就是这段弧长。</p>
  <p>若曲线参数方程 $x=x(t),\; y=y(t)$（$t$ 从 $\alpha$ 到 $\beta$）：</p>
  <div class="formula">$$dx = x'(t)dt,\qquad dy = y'(t)dt \;\Rightarrow\; ds = \sqrt{(dx)^2+(dy)^2} = \sqrt{x'(t)^2+y'(t)^2}\,dt$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：速度 × 时间 = 路程</div>
    <p>参数 $t$ 像时间，$(x'(t),y'(t))$ 是速度向量。$|v|=\sqrt{x'^2+y'^2}$ 是速率（速度大小），速率 × 时间微元 $dt$ = 路程微元 $ds$。</p>
    <p>就像汽车：仪表盘显示时速 60km，0.5 小时走 30km。$ds=|v|dt$ 就是"仪表盘 × 时间"。</p>
  </div>
  <p>特别地，曲线以 $y=\psi(x)$ 给出时（$x$ 当参数，$x'=1,\;y'=\psi'(x)$）：</p>
  <div class="formula">$$ds = \sqrt{1+\psi'(x)^2}dx$$</div>

  <h3>9.3 计算公式：把 ds 换掉（定理 20.1）</h3>
  <p>光滑曲线 $L: x=\varphi(t),\; y=\psi(t)$（$\alpha\le t\le\beta$），$f$ 在 $L$ 上连续，则：</p>
  <div class="formula">$$\int_L f(x,y)\,ds = \int_\alpha^\beta f(\varphi(t),\psi(t))\sqrt{\varphi'(t)^2+\psi'(t)^2}\,dt$$</div>
  <div class="callout callout-key">
    <div class="callout-title">一句话记忆</div>
    <b>把 $x,y$ 换成参数式，把 $ds$ 换成 $\sqrt{x'^2+y'^2}\,dt$，曲线积分就变成了普通定积分。</b>空间曲线加一项：$\sqrt{x'^2+y'^2+z'^2}dt$。
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">定理 20.1 的证明（把曲线积分翻译成定积分）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>分割 $L$ 对应参数分割 $t_0=\alpha&lt;t_1&lt;\cdots&lt;t_n=\beta$。每小段弧长（积分中值定理）：</p>
        <p>$$\Delta s_i = \int_{t_{i-1}}^{t_i}\sqrt{x'(t)^2+y'(t)^2}dt = \sqrt{x'(\tau_i')^2+y'(\tau_i')^2}\,\Delta t_i$$</p>
        <p>（积分中值定理：$\int_a^b g\,dt = g(\xi)(b-a)$。）</p>
        <p>和式：$\sum f(\xi_i,\eta_i)\Delta s_i = \sum f(x(\tau_i''),y(\tau_i''))\sqrt{x'(\tau_i')^2+y'(\tau_i')^2}\Delta t_i$。</p>
        <p>当 $\tau_i'\approx\tau_i''$（细度趋于 0），用 $\sqrt{x'^2+y'^2}$ 的连续性与 $f$ 的有界性可证误差 $\to0$（教材的 $\sigma\to0$ 部分）。</p>
        <p>极限就是 $\int_\alpha^\beta f(x(t),y(t))\sqrt{x'(t)^2+y'(t)^2}dt$——正是定积分的定义。证毕。</p>
        <p>本质：<b>曲线积分的"和式"和定积分的"和式"是同一个和式的两个写法</b>，换元只是换了个名字。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：半圆周</h4>
  <p>$L$：$x=a\cos t,\; y=a\sin t$（$0\le t\le\pi$，上半圆）。算 $\int_L(x^2+y^2)ds$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">代入公式完整算</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$x'=-a\sin t,\; y'=a\cos t$，所以 $\sqrt{x'^2+y'^2}=\sqrt{a^2\sin^2t+a^2\cos^2t}=a$（速率恒为 $a$，圆周运动）。</p>
        <p>$x^2+y^2=a^2\cos^2t+a^2\sin^2t=a^2$。</p>
        <p>$$\int_L(x^2+y^2)ds = \int_0^\pi a^2\cdot a\,dt = a^3\pi$$</p>
        <p>直觉检查：被积函数恒为 $a^2$（密度均匀），积分 = 密度 × 弧长 = $a^2\cdot\pi a=a^3\pi$ ✓（半圆周长 $\pi a$）。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：抛物线</h4>
  <p>$L: y^2=4x$ 从 $O(0,0)$ 到 $A(1,2)$，算 $\int_L y\,ds$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">以 y 为参数（避开开方）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>把 $x$ 解成 $y$ 的函数：$x=\frac{y^2}{4}$，$y\in[0,2]$。</p>
        <p>用 $ds=\sqrt{1+(dx/dy)^2}dy$：$\frac{dx}{dy}=\frac{y}{2}$，$ds=\sqrt{1+\frac{y^2}{4}}dy$。</p>
        <p>$$\int_L y\,ds = \int_0^2 y\sqrt{1+\frac{y^2}{4}}dy = \frac12\int_0^2 y\sqrt{4+y^2}dy$$</p>
        <p>换元 $u=4+y^2$，$du=2y\,dy$，$y\,dy=\frac12du$：$=\frac12\cdot\frac12\int_4^8\sqrt{u}\,du=\frac14\cdot\frac23u^{3/2}\Big|_4^8=\frac16(8\sqrt8-4\sqrt4)=\frac16(16\sqrt2-8)=\frac{8}{3}(2\sqrt2-1)$。</p>
        <p>≈ $4.21$。选择"对谁积分方便"（这里 $y$ 比 $x$ 方便）是技巧。</p>
      </div>
    </div>
  </div>

  <h3>9.4 对称性：偷懒的合法途径</h3>
  <p>曲线积分的对称性跟定积分很像：</p>
  <div class="formula">
    <p>• <b>奇偶对称</b>：若 $L$ 关于 $y$ 轴对称且 $f$ 关于 $x$ 是奇函数（$f(-x,y)=-f(x,y)$），则 $\int_L f\,ds=0$；偶函数则取一半乘 2。</p>
    <p>• <b>轮换对称</b>：若 $L$ 在变量置换下不变（如球面上的圆），则 $\int_L x^2ds=\int_L y^2ds=\int_L z^2ds$。</p>
  </div>
  <h4>数值例子：对称性活用</h4>
  <p>$\int_L x^2ds$，其中 $L$ 是球面 $x^2+y^2+z^2=a^2$ 被平面 $x+y+z=0$ 截出的圆。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用轮换对称性三秒解决</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>这个圆在球面上，变量 $x,y,z$ 地位完全对称，所以 $\int_L x^2ds=\int_L y^2ds=\int_L z^2ds$。</p>
        <p>三式相加：$3\int_L x^2ds = \int_L(x^2+y^2+z^2)ds = \int_L a^2 ds = a^2\cdot$（圆周长）。</p>
        <p>圆的半径：球面 $x^2+y^2+z^2=a^2$ 与平面 $x+y+z=0$（过球心！）交线是大圆，半径 $a$，周长 $2\pi a$。</p>
        <p>$$\int_L x^2ds = \frac{a^2\cdot 2\pi a}{3} = \frac{2\pi a^3}{3}$$</p>
        <p>硬算几乎不可能（要找圆的参数方程），对称性让它在三行内完成。</p>
      </div>
    </div>
  </div>

  <h3>9.5 应用：转动惯量</h3>
  <p>线密度 $\rho(x,y)$ 的曲线状物体对 $y$ 轴的转动惯量：$I_y = \int_L x^2\rho\,ds$（对 $x$ 轴：$I_x=\int_L y^2\rho\,ds$）。</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：转动惯量 = "难转程度"</div>
    质量离转轴越远，越难转起来（就像推门推门把手比推门轴省力）。$x^2$ 就是"到 $y$ 轴距离的平方"，距离越远权重越大。
  </div>
  <h4>数值例子：教材例 4</h4>
  <p>线密度 $\rho(x,y)=\frac{y}{1+x^2}$，曲线 $L: y=\ln x$（$1\le x\le2$），求对 $y$ 轴的转动惯量。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">代入公式并分部积分</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$I_y=\int_L x^2\rho\,ds=\int_L x^2\frac{y}{1+x^2}ds$。曲线 $y=\ln x$，$ds=\sqrt{1+(1/x)^2}dx$。</p>
        <p>$$\int_1^2 x^2\cdot\frac{\ln x}{1+x^2}\cdot\sqrt{1+\frac1{x^2}}dx = \int_1^2 x^2\frac{\ln x}{1+x^2}\cdot\frac{\sqrt{1+x^2}}{x}dx = \int_1^2\frac{x\ln x}{\sqrt{1+x^2}}dx$$</p>
        <p>分部积分（$u=\ln x$，$dv=\frac{x}{\sqrt{1+x^2}}dx$，$v=\sqrt{1+x^2}$，因为 $(\sqrt{1+x^2})'=\frac{x}{\sqrt{1+x^2}}$）：</p>
        <p>$=\left[\sqrt{1+x^2}\ln x\right]_1^2 - \int_1^2\sqrt{1+x^2}\cdot\frac1x dx = \sqrt5\ln2 - \int_1^2\frac{\sqrt{1+x^2}}{x}dx$</p>
        <p>剩下的积分换元 $t=\sqrt{1+x^2}$：$t^2=1+x^2$，$2t\,dt=2x\,dx$，$\frac{dx}{x}=\frac{t\,dt}{t^2-1}$，所以 $\frac{\sqrt{1+x^2}}{x}dx=\frac{t^2}{t^2-1}dt=dt+\frac{dt}{t^2-1}$，而 $\int\frac{dt}{t^2-1}=\frac12\ln\left|\frac{t-1}{t+1}\right|$。换限：$x=1\to t=\sqrt2$，$x=2\to t=\sqrt5$：</p>
        <p>$$\int_1^2\frac{\sqrt{1+x^2}}{x}dx = \left[t+\frac12\ln\frac{t-1}{t+1}\right]_{\sqrt2}^{\sqrt5} = \sqrt5-\sqrt2+\frac12\ln\frac{(\sqrt5-1)(\sqrt2+1)}{(\sqrt5+1)(\sqrt2-1)}$$</p>
        <p>所以 $I_y=\sqrt5\ln2-\sqrt5+\sqrt2-\frac12\ln\frac{(\sqrt5-1)(\sqrt2+1)}{(\sqrt5+1)(\sqrt2-1)}\approx0.33$。</p>
        <p>要点：<b>把 $ds$ 换掉 → 普通定积分 → 分部积分 + 换元</b>，每一步都是第 1 章的工具。</p>
      </div>
    </div>
  </div>

  <h3>9.6 第一型曲线积分的性质（与定积分一致）</h3>
  <div class="formula">
    <p>• 线性：$\int_L(c_1f+c_2g)ds = c_1\int_L f\,ds+c_2\int_L g\,ds$</p>
    <p>• 可加：曲线分段 $L=L_1\cup L_2$ 时，$\int_L=\int_{L_1}+\int_{L_2}$</p>
    <p>• 保序：$f\le g$ 时 $\int_L f\le\int_L g$；$|\int_L f|\le\int_L|f|$</p>
    <p>• 中值：$\int_L f\,ds = c\cdot s$（$c$ 在 $f$ 的上下确界之间，$s$ 是弧长）</p>
    <p>• <b>与方向无关</b>：$\int_{\overrightarrow{AB}}f\,ds = \int_{\overleftarrow{BA}}f\,ds$（只积"长度"，不积"方向"——这点和第二型曲线积分不同，下章会讲）</p>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：$\int_L 1\,ds$ 等于什么？（$L$ 任意曲线）</div>
    <div class="qa-a"><b>答案</b>：等于 $L$ 的弧长。因为 $f\equiv1$，积分 = $\int_L ds$ = 总长度。这也是"弧长 = 曲线积分特例"的体现。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：为什么第一型曲线积分与方向无关，而 $\int_a^b f(x)dx$ 反向会变号？</div>
    <div class="qa-a"><b>答案</b>：第一型积分积的是"弧长微元 $ds$"（总是正的），不关心走哪个方向。而 $\int$ 的 $dx$ 在反向时是负的。$ds=|v|dt$ 里的绝对值让方向失效。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：半径为 $R$、线密度 $\rho$ 均匀的完整圆周，对直径轴的转动惯量？（用对称性）</div>
    <div class="qa-a"><b>答案</b>：$I=\int_L x^2\rho ds$（直径取 $y$ 轴）。$I_y+I_x=\int_L(x^2+y^2)\rho ds=\int_L R^2\rho ds=R^2\rho\cdot2\pi R=2\pi\rho R^3$。由对称 $I_x=I_y$，所以 $I=\pi\rho R^3$。</div>
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：summary ===== -->
<section class="chapter" id="summary" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">14</span>知识图谱与自测</h2>
  <p class="lead">学完这门课，你应当能"从头推导"这里的每一条公式。这一章把所有知识串成一张网，并给出自测题检验是否达到"专家理解"。</p>

  <h3>14.1 全课程知识图谱</h3>
  <div class="knowledge-tree">
    <div class="kt-level"><span class="kt-label root">根系（初中）</span>
      <span class="kt-label root">斜率 Δy/Δx</span>
      <span class="kt-label root">勾股定理</span>
      <span class="kt-label root">解方程组</span>
      <span class="kt-label root">配方/最值</span>
      <span class="kt-label root">函数与方程</span>
    </div>
    <div class="kt-level"><span class="kt-label base">基础（大一）</span>
      <span class="kt-label base">导数/偏导</span>
      <span class="kt-label base">定积分</span>
      <span class="kt-label base">连续/介值</span>
      <span class="kt-label base">向量/点积/梯度</span>
    </div>
    <div class="kt-level"><span class="kt-label tool">第18章</span>
      <span class="kt-label tool">隐函数定理</span>
      <span class="kt-label tool">雅可比行列式</span>
      <span class="kt-label tool">切线/切平面</span>
      <span class="kt-label tool">拉格朗日乘数法</span>
    </div>
    <div class="kt-level"><span class="kt-label tool">第19章</span>
      <span class="kt-label tool">含参量积分</span>
      <span class="kt-label tool">一致收敛</span>
      <span class="kt-label tool">Γ/B 函数</span>
    </div>
    <div class="kt-level"><span class="kt-label tool">第20章</span>
      <span class="kt-label tool">弧长微元 ds</span>
      <span class="kt-label tool">第一型曲线积分</span>
    </div>
    <div class="kt-level"><span class="kt-label">综合能力</span>
      <span class="kt-label">换序三件套（极限/导数/积分 × 积分）</span>
      <span class="kt-label">"造参数—求导—解方程"套路</span>
      <span class="kt-label">"分割-近似-取极限"思想</span>
      <span class="kt-label">几何直觉（梯度/法向量/相切）</span>
    </div>
  </div>

  <h3>14.2 三条贯穿全书的主线</h3>
  <div class="callout callout-key">
    <div class="callout-title">主线一：换序（交换运算次序）</div>
    第 6 章：连续 ⟹ 极限入积分号；可微 ⟹ 导数入积分号。第 7 章：一致收敛 ⟹ 无穷区间也能换。第 8 章：Γ、B 的性质全靠换序。第 3 章雅可比、第 5 章拉格朗日其实也是"换视角"（消元 ↔ 罚函数）。<b>数学里"换序"是最高频的思维武器。</b>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">主线二：造参数（含参量方法）</div>
    第 6 章例 3：$I(\alpha)$ 求导后解方程得 $I=\frac{\pi\ln2}{8}$。第 7 章例 6：塞 $e^{-px}$ 算 $\frac{\sin ax}{x}$。第 8 章：整个 Γ、B 函数就是"积分造新函数"。<b>把未知积分放进一个含参函数族里，求导、解方程、取极限——这是分析学最优雅的套路。</b>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">主线三：局部线性化（微分思想）</div>
    隐函数：$F_x\Delta x+F_y\Delta y=0$ 得 $y'=-F_x/F_y$。雅可比：线性方程组决定局部可解性。切平面：$\Delta z=f_x\Delta x+f_y\Delta y$。拉格朗日：梯度平行。曲线积分：$ds=|v|dt$。<b>一切都源于"放大看，弯的是直的"。</b>
  </div>

  <h3>14.3 自测：你能从零推导吗？</h3>
  <div class="qa-item">
    <div class="qa-q">S1（隐函数）：由 $x^2y+xy^2=6$ 求 $y'$ 在 $(1,2)$ 处的值，并说明 $F_y$ 的作用。</div>
    <div class="qa-a"><b>答案</b>：$F=x^2y+xy^2-6$，$F_x=2xy+y^2$，$F_y=x^2+2xy$。$(1,2)$：$F_x=4+4=8$，$F_y=1+4=5\ne0$。$y'=-\frac85$。$F_y\ne0$ 保证能局部解出 $y=f(x)$（隐函数定理条件）。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">S2（雅可比）：写出 $\frac{\partial(u,v)}{\partial(x,y)}$ 的定义，并解释为什么 $\ne0$ 意味着"可逆"。</div>
    <div class="qa-a"><b>答案</b>：$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}u_x&u_y\\v_x&v_y\end{vmatrix}=u_xv_y-u_yv_x$。$\ne0$ 意味着局部线性化方程组 $\begin{cases}\Delta u=u_x\Delta x+u_y\Delta y\\\Delta v=v_x\Delta x+v_y\Delta y\end{cases}$ 可由 $\Delta u,\Delta v$ 唯一解出 $\Delta x,\Delta y$（克莱姆法则），所以变换局部可逆，反函数组的雅可比 = 原雅可比的倒数。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">S3（切平面）：曲面 $x^2+y^2-z^2=1$ 在 $(1,0,0)$ 的切平面是什么？它和锥面有什么关系？</div>
    <div class="qa-a"><b>答案</b>：$F=x^2+y^2-z^2-1$，$\nabla F=(2x,2y,-2z)=(2,0,0)\parallel(1,0,0)$。切平面：$1(x-1)=0$，即 $x=1$。曲面是单叶双曲面，$x=1$ 处切线竖直方向为 $y,z$ 自由——即双曲面在腰部最"平"。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">S4（拉格朗日）：约束 $x^2+y^2=1$ 下求 $f=x+2y$ 的最大值。为什么最大值是 $\sqrt5$？</div>
    <div class="qa-a"><b>答案</b>：$L=x+2y+\lambda(x^2+y^2-1)$。$L_x=1+2\lambda x=0$，$L_y=2+2\lambda y=0$ ⇒ $x=-\frac{1}{2\lambda}$，$y=-\frac{1}{\lambda}$，故 $y=2x$。代入约束 $x^2+4x^2=1$，$x=\pm\frac1{\sqrt5}$，$y=\pm\frac2{\sqrt5}$。$f=x+2y=\frac1{\sqrt5}+\frac4{\sqrt5}=\sqrt5$（最大值）。几何：$\sqrt5$ 是 $(1,2)$ 的长度，因为 $f=(1,2)\cdot(x,y)$，在单位圆上点积最大 = 向量长度 × 投影最大 = $\sqrt5\times1$。这就是柯西不等式的几何版！</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">S5（换序）：$\int_0^\infty e^{-px}\frac{\sin x}{x}dx$ 中 $p$ 的作用是什么？为什么 $p>0$ 才有好性质？</div>
    <div class="qa-a"><b>答案</b>：$p$ 是"阻尼因子"（镇静剂）。$p>0$ 时 $e^{-px}$ 让积分绝对收敛（M 判别法），可以在积分号下求导。$p=0$ 时只是条件收敛，需用阿贝尔判别法另证。$p$ 的引入把"病态积分"放进"健康家族"，算完再取极限 $p\to0^+$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">S6（欧拉积分）：证明 $\Gamma(s+1)=s\Gamma(s)$ 并计算 $\Gamma(\frac72)$。</div>
    <div class="qa-a"><b>答案</b>：分部积分（$u=x^s$，$dv=e^{-x}dx$），边界项消失（$x=0$ 处 $x^s\to0$；$x\to\infty$ 处 $e^{-x}$ 主导）。$\Gamma(\frac72)=\frac52\cdot\frac32\cdot\frac12\sqrt\pi=\frac{15\sqrt\pi}{8}$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">S7（曲线积分）：$L$ 是单位圆 $x^2+y^2=1$（整圈），算 $\int_L y^2ds$。</div>
    <div class="qa-a"><b>答案</b>：参数 $x=\cos t,y=\sin t$（$0\le t\le2\pi$），$ds=\sqrt{\sin^2t+\cos^2t}dt=dt$。$\int_0^{2\pi}\sin^2t\,dt=\pi$。或对称性：$\int x^2ds=\int y^2ds$，两者和 $=\int_0^{2\pi}dt=2\pi$，所以各 $\pi$。</div>
  </div>

  <h3>14.4 达到"专家"的三个标志</h3>
  <div class="callout callout-tip">
    <div class="callout-title"> 自检清单</div>
    <p>① <b>能推导</b>：不看课本，能从"等式两边求导"推出 $y'=-F_x/F_y$；能从分部积分推出 $\Gamma$ 递推；能从"分割-取极限"推出曲线积分公式。</p>
    <p>② <b>能解释为什么</b>：为什么 $F_y\ne0$？（曲线不竖直）；为什么雅可比？（线性方程组唯一解）；为什么 $\lambda$？（梯度平行）；为什么一致收敛？（全班统一截止日期）；为什么 $ds=|v|dt$？（速率×时间）。</p>
    <p>③ <b>能迁移</b>：看到新问题能认出"这是换序问题""这是造参数问题""这是分割取极限问题"。</p>
  </div>

  <h3>14.5 下一步学什么</h3>
  <div class="table-wrap"><table>
    <tr><th style="width:30%">后续主题</th><th>与本课程的联系</th></tr>
    <tr><td>第二型曲线积分</td><td>积"方向"而非"长度"，$dx,dy$ 会变号——第一型积分的姊妹版</td></tr>
    <tr><td>重积分（二重/三重）</td><td>把"曲线"升级成"平面/空间"，分割-取极限思想直接迁移</td></tr>
    <tr><td>曲面积分</td><td>曲线积分的三维升级，$ds$ 变 $dS$</td></tr>
    <tr><td>傅里叶变换</td><td>含参量积分的巅峰应用（$\int e^{-x^2}\cos(rx)dx$ 只是热身）</td></tr>
    <tr><td>概率论</td><td>Γ分布、B分布直接就是 Γ、B 函数</td></tr>
  </table></div>

  <div class="callout callout-key">
    <div class="callout-title">恭喜完成</div>
    你现在拥有了"从初中数学推到曲线积分"的完整推导链。遇到任何不懂的步骤，回翻对应章节的折叠推导；遇到新公式，问自己三句话：<b>它从哪来（前置）？它为什么这样设计（直觉）？它用在哪（后续）？</b>
  </div>
  <div class="chapter-nav"></div>
</section>
"""

def write(path) -> None:
    path.write_text(CH_D, encoding='utf-8')

if __name__ == "__main__":
    from pathlib import Path
    out = Path(__file__).parent / 'chapters_d.py.txt'
    write(out)
    print('chapters_d 内容长度:', len(CH_D))
