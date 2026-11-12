# -*- coding: utf-8 -*-
"""第五批章节：第二型曲线积分、二重积分概念与计算、习题课精讲"""

CH_E = r"""
<section class="chapter" id="line-integral-2" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">10</span>第二型曲线积分：变力沿曲线做的功</h2>
  <p class="lead">前置知识：第一型曲线积分与弧长微元 $ds$（第 9 章）、参数方程、向量点积（第 1 章）、定积分的分割求和。后续应用：格林公式、曲面积分、保守场与势函数。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 第一型曲线积分算"质量"，与走向无关；第二型算"做功"，与走向有关。</p>
    <p>② 同一条曲线、同一个被积表达式，从 $A$ 走到 $B$ 与从 $B$ 走到 $A$，结果差一个负号。</p>
    <p>③ 一个积分是否与路径有关，要看 $P\,dx+Q\,dy$ 是不是某个函数的全微分。</p>
  </div>

  <h3>10.1 为什么还需要第二种曲线积分</h3>
  <p>第 9 章算的是"一根弯铁丝有多重"：把铁丝切段，每段质量＝密度×弧长，加起来。弧长 $\Delta s$ 不分方向，所以那个积分不关心你是从左往右走还是从右往左走。</p>
  <p>现在换个问题：<b>一个力推着质点沿曲线走，做了多少功</b>。力是向量 $\vec F=(P,Q)$，位移也是向量 $d\vec s=(dx,dy)$。做功等于力与位移的点积：</p>
  <div class="formula">$$dW=\vec F\cdot d\vec s=P\,dx+Q\,dy$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：推箱子走盘山路</div>
    <p>力与前进方向夹角越小，做功越多；垂直时不做功；反向时做负功。走反了，$dx$ 和 $dy$ 同时变号，功就变号。</p>
    <p>所以这一类积分的被积对象不是"密度"，而是"力沿着路径方向的分量"，它天生带方向。</p>
  </div>

  <h3>10.2 定义：分割、投影、求和、取极限</h3>
  <p>设 $L$ 是平面上一条<b>有向</b>可求长曲线，起点 $A$、终点 $B$，函数 $P(x,y)$、$Q(x,y)$ 在 $L$ 上有定义。把 $L$ 分成 $n$ 小段，分点 $A=M_0,M_1,\dots,M_n=B$，第 $i$ 段上取一点 $(\xi_i,\eta_i)$。</p>
  <p>关键的一步是取<b>投影</b>而不是弧长：第 $i$ 段在 $x$ 轴上的投影 $\Delta x_i=x_i-x_{i-1}$，在 $y$ 轴上的投影 $\Delta y_i=y_i-y_{i-1}$。作和式：</p>
  <div class="formula">$$\sum_{i=1}^{n}\bigl[P(\xi_i,\eta_i)\Delta x_i+Q(\xi_i,\eta_i)\Delta y_i\bigr]$$</div>
  <p>令细度 $||T||=\max\{\text{第 }i\text{ 段弧长}\}\to0$。若这个和式的极限存在，且与分割方式、取点方式都无关，就称它为 $P,Q$ 沿有向曲线 $L$ 的<b>第二型曲线积分</b>：</p>
  <div class="formula">$$\int_L P(x,y)\,dx+Q(x,y)\,dy \quad\text{或}\quad \int_{AB} P\,dx+Q\,dy$$</div>
  <p>曲线封闭时记作 $\oint_L P\,dx+Q\,dy$。也可以拆成两个积分写：$\int_L P\,dx+\int_L Q\,dy$。</p>
  <div class="callout callout-warn">
    <div class="callout-title">和第一型的区别只有一处</div>
    <p>第一型的和式里是 $\Delta s_i$（永远为正）；第二型的和式里是 $\Delta x_i,\Delta y_i$（<b>可正可负</b>，取决于这段是往右走还是往左走、往上走还是往下走）。</p>
    <p>正因为如此，第二型积分才"认方向"。</p>
  </div>

  <h3>10.3 方向一反过来，积分变号</h3>
  <p>设 $L^-$ 是把 $L$ 的方向反过来（起点终点互换），则：</p>
  <div class="formula">$$\int_{BA}P\,dx+Q\,dy=-\int_{AB}P\,dx+Q\,dy$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">为什么只差一个负号</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>原来第 $i$ 段从 $M_{i-1}$ 到 $M_i$，投影是 $x_i-x_{i-1}$。方向反过来以后，同一小段变成从 $M_i$ 到 $M_{i-1}$，投影是 $x_{i-1}-x_i=-(x_i-x_{i-1})$。</p>
        <p>$\Delta y_i$ 同理变号。取点还是那些点，被积函数的值不变，于是每一项都变成原来的相反数。</p>
        <p>和式整体乘以 $-1$，取极限后积分也乘以 $-1$。证毕。</p>
        <p><b>物理翻译</b>：同一段路，上坡时重力做负功，下坡时重力做正功，大小相等符号相反。</p>
      </div>
    </div>
  </div>

  <h3>10.4 计算公式：化成定积分</h3>
  <p>设曲线由参数方程给出：$x=\varphi(t),\;y=\psi(t)$，$t$ 从 $\alpha$ 变到 $\beta$（起点对应 $\alpha$，终点对应 $\beta$）。若 $\varphi,\psi$ 有连续的一阶导数，则：</p>
  <div class="formula">$$\int_L P\,dx+Q\,dy=\int_\alpha^\beta\Bigl[P\bigl(\varphi(t),\psi(t)\bigr)\varphi'(t)+Q\bigl(\varphi(t),\psi(t)\bigr)\psi'(t)\Bigr]dt$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">公式 (6) 是怎么来的</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>把曲线的参数分割 $t_0=\alpha&lt;t_1&lt;\cdots&lt;t_n=\beta$ 当作曲线分割。由拉格朗日中值定理：</p>
        <p>$$\Delta x_i=\varphi(t_i)-\varphi(t_{i-1})=\varphi'(\tau_i)\Delta t_i,\qquad \Delta y_i=\psi(t_i)-\psi(t_{i-1})=\psi'(\tau_i')\Delta t_i$$</p>
        <p>代入和式：$\sum[P(\xi_i,\eta_i)\varphi'(\tau_i)+Q(\xi_i,\eta_i)\psi'(\tau_i')]\Delta t_i$，其中 $\xi_i=\varphi(\tau_i'')$，$\eta_i=\psi(\tau_i'')$。</p>
        <p>细度趋于 0 时 $\tau_i,\tau_i',\tau_i''$ 挤在同一小段上，由 $\varphi',\psi'$ 的连续性与 $P,Q$ 的连续性，误差趋于 0。</p>
        <p>剩下的极限恰好是 $\int_\alpha^\beta[P\varphi'+Q\psi']dt$ 的定义式。证毕。</p>
        <p>本质：<b>$dx=\varphi'(dt)$，$dy=\psi'(t)dt$，把微分换掉就变成普通定积分</b>。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">三个必须养成的手感</div>
    <p>① 先把 $x,y$ 换成参数式，再分别乘上 $x'(t)$、$y'(t)$，最后对 $t$ 积分。</p>
    <p>② <b>积分限的上下必须与起点终点对应</b>，这里不要求 $\alpha&lt;\beta$。若起点对应较大的参数，积分限就反过来，公式自己会把负号算进去。</p>
    <p>③ 曲线写成 $y=y(x)$ 时，$x$ 当参数：$\int_L P\,dx+Q\,dy=\int_a^b[P(x,y(x))+Q(x,y(x))y'(x)]dx$；写成 $x=x(y)$ 时同理，$dy$ 留在外面。</p>
  </div>

  <h4>例 1：同一个积分，三条路径三个答案</h4>
  <p>计算 $I=\int_L xy\,dx+(y-x)dy$，其中 $L$ 是从 $A(1,1)$ 到 $B(2,3)$ 的：<br>
  (i) 直线段 $AB$；(ii) 抛物线 $y=2(x-1)^2+1$ 上的一段 $ACB$；(iii) 折线 $A\to D(2,1)\to B$ 再回到 $A$（三角形周界）。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">(i) 直线段：$y=2x-1$，$x:1\to2$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$dy=2\,dx$。被积式 $=x(2x-1)dx+(2x-1-x)\cdot2dx=(2x^2-x+2x-2)dx=(2x^2+x-2)dx$。</p>
        <p>$$I=\int_1^2(2x^2+x-2)dx=\left[\frac{2x^3}{3}+\frac{x^2}{2}-2x\right]_1^2=\frac{25}{6}\approx4.167$$</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">(ii) 抛物线：换元 $u=x-1$ 省力</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>令 $u=x-1$，$x=u+1$，$u:0\to1$，$y=2u^2+1$，$dy=4u\,du$。</p>
        <p>$xy\,dx=(u+1)(2u^2+1)du=(2u^3+2u^2+u+1)du$。</p>
        <p>$(y-x)dy=(2u^2+1-u-1)\cdot4u\,du=(8u^3-4u^2)du$。</p>
        <p>$$I=\int_0^1(10u^3-2u^2+u+1)du=\frac{10}{4}-\frac{2}{3}+\frac{1}{2}+1=\frac{10}{3}\approx3.333$$</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">(iii) 折线：分三段，第三段反向</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$AD$：$y=1$，$dy=0$，$x:1\to2$，$\int_1^2 x\,dx=\frac32$。</p>
        <p>$DB$：$x=2$，$dx=0$，$y:1\to3$，$\int_1^3(y-2)dy=\left[\frac{y^2}{2}-2y\right]_1^3=0$。</p>
        <p>$BA$：沿直线 $y=2x-1$ 从 $x=2$ 走到 $x=1$，等于 (i) 的反向：$-\frac{25}{6}$。</p>
        <p>$$I=\frac32+0-\frac{25}{6}=-\frac{8}{3}\approx-2.667$$</p>
      </div>
    </div>
  </div>
  <div class="callout callout-warn">
    <div class="callout-title">这个例子的结论</div>
    <p>同一起点、同一终点、同一被积表达式，三条路给出 $\frac{25}{6}$、$\frac{10}{3}$、$-\frac{8}{3}$ 三个不同的值。所以<b>第二型曲线积分一般与路径有关</b>。</p>
    <p>如果只看到这里，很容易误以为"曲线积分都跟路径有关"。下一节的例子正好相反。</p>
  </div>

  <h4>例 5：换三条路径，答案却是同一个</h4>
  <p>计算 $\int_L 2xy\,dx+x^2dy$，$L$ 从 $O(0,0)$ 到 $B(1,1)$，分别沿：(1) 抛物线 $y=x^2$；(2) 抛物线 $x=y^2$；(3) 折线 $O\to(1,0)\to B$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">三条路径各算一遍</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>(1) $y=x^2$，$dy=2x\,dx$：$\int_0^1(2x\cdot x^2+x^2\cdot 2x)dx=\int_0^1 4x^3dx=1$。</p>
        <p>(2) $x=y^2$，$dx=2y\,dy$：$\int_0^1(2y^2\cdot y\cdot 2y+y^4)dy=\int_0^1 5y^4dy=1$。</p>
        <p>(3) $O\to(1,0)$：$y=0,dy=0$，积分为 0；$(1,0)\to B$：$x=1,dx=0$，$\int_0^1 1\,dy=1$。合计 1。</p>
        <p>三条路径都等于 1。</p>
      </div>
    </div>
  </div>
  <p>为什么这次路径不起作用？注意 $2xy\,dx+x^2dy$ 恰好是 $d(x^2y)$ 的展开：$d(x^2y)=2xy\,dx+x^2dy$。于是</p>
  <div class="formula">$$\int_L 2xy\,dx+x^2dy=\int_L d(x^2y)=x^2y\Big|_{(0,0)}^{(1,1)}=1-0=1$$</div>
  <p>只要被积表达式是某个二元函数 $u(x,y)$ 的全微分，积分就只依赖起点和终点，与走哪条路无关——这就是下一章"格林公式"与"保守场"的入口。判断办法是对照：$P=2xy$，$Q=x^2$，$\dfrac{\partial P}{\partial y}=2x=\dfrac{\partial Q}{\partial x}$。</p>

  <h4>例 4：方向与路径各影响一次</h4>
  <p>计算 $\int_L y^2dx$：(1) $L$ 是半径为 $a$、圆心在原点的上半圆周，按逆时针从 $A(a,0)$ 到 $B(-a,0)$；(2) $L$ 是从 $A$ 沿 $x$ 轴到 $B$ 的直线段。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">半圆与直线段对比</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>(1) $x=a\cos t,\;y=a\sin t$，$t:0\to\pi$，$dx=-a\sin t\,dt$。</p>
        <p>$$\int_0^\pi a^2\sin^2t\cdot(-a\sin t)dt=-a^3\int_0^\pi\sin^3t\,dt=-a^3\cdot\frac43=-\frac{4a^3}{3}$$</p>
        <p>（$\int_0^\pi\sin^3t\,dt=\frac43$：用 $\sin^3t=\sin t(1-\cos^2t)$，换元 $u=\cos t$ 得 $\int_{-1}^{1}(1-u^2)du=\frac43$。）</p>
        <p>(2) $y=0$，$dy=0$，被积函数 $y^2=0$，所以积分为 0。</p>
        <p>结果不同，说明这个积分与路径有关；若把 (1) 的方向反过来（$t:\pi\to0$），结果变成 $+\frac{4a^3}{3}$，说明方向也影响符号。</p>
      </div>
    </div>
  </div>

  <h3>10.5 空间曲线：多写一项 $R\,dz$</h3>
  <p>若 $L$ 是空间有向曲线 $x=x(t),y=y(t),z=z(t)$（$t:\alpha\to\beta$），力 $\vec F=(P,Q,R)$，则：</p>
  <div class="formula">$$\int_L P\,dx+Q\,dy+R\,dz=\int_\alpha^\beta\bigl[P\,x'(t)+Q\,y'(t)+R\,z'(t)\bigr]dt$$</div>
  <h4>例 7：螺旋线上力做的功</h4>
  <p>力 $\vec F=(y,-x,x+y+z)$，质点沿螺旋线 $x=a\cos t,\;y=a\sin t,\;z=bt$ 从 $t=0$ 走到 $t=2\pi$，求功。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">逐项代入并合并</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$dx=-a\sin t\,dt$，$dy=a\cos t\,dt$，$dz=b\,dt$。</p>
        <p>$y\,dx=a\sin t\cdot(-a\sin t)dt=-a^2\sin^2t\,dt$。</p>
        <p>$-x\,dy=-a\cos t\cdot a\cos t\,dt=-a^2\cos^2t\,dt$。</p>
        <p>$(x+y+z)dz=(a\cos t+a\sin t+bt)\cdot b\,dt$。</p>
        <p>前三项里 $-a^2(\sin^2t+\cos^2t)=-a^2$，于是被积式 $=-a^2+ab\cos t+ab\sin t+b^2t$。</p>
        <p>$$\int_0^{2\pi}(-a^2+ab\cos t+ab\sin t+b^2t)dt=-2\pi a^2+0+0+b^2\cdot\frac{(2\pi)^2}{2}=-2\pi a^2+2\pi^2b^2$$</p>
        <p>检查符号：$a^2$ 项做负功（力的水平分量与绕行方向相反），$b^2$ 项做正功（$z$ 方向分量随 $z$ 增大而增大）。</p>
      </div>
    </div>
  </div>

  <h3>10.6 两类曲线积分的联系</h3>
  <p>同一段有向曲线，第一型积的是 $ds$（长度微元），第二型积的是 $dx,dy$（坐标微元）。它们之间差一个"方向余弦"：</p>
  <div class="formula">$$\int_L P\,dx+Q\,dy=\int_L\bigl(P\cos\alpha+Q\cos\beta\bigr)ds$$</div>
  <p>其中 $\cos\alpha=\dfrac{\varphi'(t)}{\sqrt{\varphi'^2+\psi'^2}}$，$\cos\beta=\dfrac{\psi'(t)}{\sqrt{\varphi'^2+\psi'^2}}$ 是切向量 $\vec\tau=(\varphi',\psi')$ 的方向余弦。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">为什么乘上方向余弦就换过去了</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>曲线上的位移微元是向量 $d\vec s=(dx,dy)$。它的长度是 $ds$，方向是切向量方向。把向量写成长度×方向：</p>
        <p>$$(dx,dy)=ds\cdot(\cos\alpha,\cos\beta)$$</p>
        <p>于是 $P\,dx+Q\,dy=P\cos\alpha\,ds+Q\cos\beta\,ds$，逐项对应，两边同时积分即得。</p>
        <p>反过来也常用：已知第二型，想换成第一型，就把 $\cos\alpha,\cos\beta$ 提出来；空间曲线再加 $R\cos\gamma\,dz$ 那一项。</p>
      </div>
    </div>
  </div>

  <h3>10.7 小结</h3>
  <div class="callout callout-key">
    <div class="callout-title">这一章只需要记住四句话</div>
    <p>① 第二型积分算的是"力沿路径的分量"，因此<b>有方向</b>；方向反过来，结果变号。</p>
    <p>② 计算套路固定：参数化 → 求 $x',y'$ → 代入 → 对 $t$ 积分，<b>限与起点终点对应</b>。</p>
    <p>③ 与路径有关还是无关，取决于 $P\,dx+Q\,dy$ 是否为全微分；检验式是 $P_y=Q_x$。</p>
    <p>④ 与第一型的换算只差方向余弦：$(dx,dy)=(\cos\alpha,\cos\beta)ds$。</p>
  </div>

  <div class="qa-item">
    <p><b>思考 1</b>：$\int_L x\,dy$ 与 $\int_L y\,dx$ 在一条封闭曲线上相等吗？</p>
    <p>不一定。但它们之和 $\oint_L x\,dy-y\,dx$ 有意义：它等于该闭曲线围成区域面积的两倍（格林公式的推论），这正是下一章的内容。</p>
  </div>
  <div class="qa-item">
    <p><b>思考 2</b>：为什么例 5 里三条路径结果相同，而例 1 不同？</p>
    <p>因为例 5 的被积式是全微分 $d(x^2y)$，积分只由起点终点决定；例 1 的被积式不是全微分，路径中间的"绕行"会真实地改变累加量。</p>
  </div>
  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="double-integral" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">11</span>二重积分：曲面下的体积怎么量</h2>
  <p class="lead">前置知识：定积分的"分割-近似-求和-取极限"（第 1 章）、平面区域与面积、极限与确界。后续应用：直角坐标下的计算（第 12 章）、极坐标、三重积分、曲面积分。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 定积分量的是"一条线段上的累积"，二重积分量的是"一整块平面区域上的累积"。</p>
    <p>② 区域本身得先"能算面积"，否则积分没有底。</p>
    <p>③ 可积的判据、八条性质，与定积分几乎逐条对应，只是把"长度"换成"面积"。</p>
  </div>

  <h3>11.1 从曲边梯形到曲顶柱体</h3>
  <p>回忆定积分：曲边梯形由 $x=a,\;x=b,\;y=0,\;y=f(x)$ 围成，面积用"切成竖条、每条约当成矩形、求和、取极限"得到。现在把图形从平面推到空间：</p>
  <p>底面是平面区域 $D$，顶上盖着一张曲面 $z=f(x,y)\ge0$，四周是竖直的柱面。这个"曲顶柱体"的体积怎么算？办法完全一样，只是切法从"切成竖条"变成"切成小柱"：</p>
  <div class="formula">$$V=\lim_{||T||\to0}\sum_{i=1}^{n}f(\xi_i,\eta_i)\,\Delta\sigma_i$$</div>
  <p>$\Delta\sigma_i$ 是第 $i$ 个小块的<b>面积</b>（不是长度），$f(\xi_i,\eta_i)$ 是这块上方的高。这就是二重积分的雏形。</p>

  <h3>11.2 先解决一个前提：平面图形"面积"是什么</h3>
  <p>定积分里区间长度天生就有，不用定义。平面区域的面积不那么显然：边界弯弯曲曲，凭什么说它有个确定的数？教材先把这个补上，否则二重积分的地基是空的。</p>
  <p>设 $P$ 是平面有界图形（能被某个矩形 $R$ 罩住）。用一组平行于坐标轴的直线网 $T$ 把它切开，小矩形（网眼）分三类：</p>
  <div class="callout callout-tip">
    <div class="callout-title">三类小矩形</div>
    <p>(i) 整块都在 $P$ 内部（全是内点）；(ii) 整块都在 $P$ 外部（全是外点）；(iii) 跨在边界上（含边界点）。</p>
  </div>
  <p>把所有 (i) 类的面积加起来，记 $s_P(T)$；把 (i) 类加 (iii) 类的面积加起来，记 $S_P(T)$。显然</p>
  <div class="formula">$$s_P(T)\le P\text{ 的面积}\le S_P(T)$$</div>
  <p>对所有直线网取上确界与下确界，得到<b>内面积</b>与<b>外面积</b>：</p>
  <div class="formula">$$\underline I=\sup_T s_P(T),\qquad \overline I=\inf_T S_P(T)$$</div>
  <p>定义 1：若 $\underline I=\overline I$，称 $P$ <b>可求面积</b>，共同值就是 $P$ 的面积。</p>
  <div class="callout callout-key">
    <div class="callout-title">一句话理解</div>
    <b>里外两套逼近必须挤到同一个数，面积才存在。</b>直线网越细，内接近从下面往上顶，外接近从上面往下压；两边能合拢，面积才算"量得出来"。
  </div>
  <p>定理 21.2：平面有界图形 $P$ 可求面积的充要条件是<b>它的边界面积为零</b>。推论：由光滑曲线或分段光滑曲线围成的图形都可求面积。</p>
  <p>反例：$[0,1]\times[0,1]$ 中坐标都是有理数的点集，边界"到处都是"，外面积恒为 1、内面积为 0，不可求面积。这个反例说明"能求面积"不是自动成立的。</p>

  <h3>11.3 定义：分割、取点、求和、取极限</h3>
  <p>设 $f(x,y)$ 定义在可求面积的有界闭域 $D$ 上。用直线网把 $D$ 分成 $n$ 个小区域 $\Delta\sigma_1,\dots,\Delta\sigma_n$，第 $i$ 块的直径记 $\rho_i$，细度 $||T||=\max\rho_i$。每块任取一点 $(\xi_i,\eta_i)$，作和式 $\sum f(\xi_i,\eta_i)\Delta\sigma_i$。</p>
  <p>定义 2：若存在实数 $J$，对任意 $\varepsilon&gt;0$ 存在 $\delta&gt;0$，使得对 $D$ 的<b>任何</b>分割 $T$，只要 $||T||&lt;\delta$，就有</p>
  <div class="formula">$$\left|\sum_{i=1}^{n}f(\xi_i,\eta_i)\Delta\sigma_i-J\right|&lt;\varepsilon$$</div>
  <p>则称 $f$ 在 $D$ 上<b>可积</b>，$J$ 称为 $f$ 在 $D$ 上的<b>二重积分</b>，记</p>
  <div class="formula">$$\iint_D f(x,y)\,d\sigma \quad\text{或}\quad \iint_D f(x,y)\,dx\,dy$$</div>
  <div class="callout callout-warn">
    <div class="callout-title">注意"任何分割"这四个字</div>
    <p>要求对<b>所有</b>分割、<b>所有</b>取点都收敛到同一个 $J$。只要有一种分割方式让和式跑偏，这个 $J$ 就不成立。</p>
    <p>这也解释了为什么后面能"挑最方便的分割"来计算：既然所有分割都给同一个极限，就可以选平行于坐标轴的直线网。</p>
  </div>
  <p>几何意义：$f\ge0$ 时 $\iint_D f\,d\sigma$ 就是曲顶柱体的体积；$f=1$ 时等于 $D$ 的面积；$f$ 有正有负时，正的部分算"体积"，负的部分算"减去的体积"。</p>

  <h3>11.4 可积的判据</h3>
  <p>用定义判断可积要验证所有分割，不现实。教材改用"上和与下和"：</p>
  <p>设 $f$ 在 $D$ 上有界，$M_i$、$m_i$ 分别是 $f$ 在第 $i$ 块上的上确界与下确界，令</p>
  <div class="formula">$$S(T)=\sum M_i\Delta\sigma_i,\qquad s(T)=\sum m_i\Delta\sigma_i$$</div>
  <p>定理 21.4：$f$ 在 $D$ 上可积的充要条件是 $\lim_{||T||\to0}S(T)=\lim_{||T||\to0}s(T)$。</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：上包络与下包络夹逼</div>
    <p>每块都取最高点，得到"偏大的估计"；每块都取最低点，得到"偏小的估计"。随着切得越来越细，两套估计越来越接近；能合拢，才说明积分存在。</p>
    <p>这和定积分里的达布上下和是一回事，只是把区间长度换成了小区域面积。</p>
  </div>
  <p>两条好用的充分条件：</p>
  <div class="formula">
    <p>• <b>定理 21.6</b>：有界闭域 $D$ 上的连续函数必可积。</p>
    <p>• <b>定理 21.7</b>：$f$ 在 $D$ 上有界，且不连续点集是面积为 0 的集合，则 $f$ 可积。</p>
  </div>
  <p>第二条很实用：函数在有限条曲线或有限个点上有间断，不影响可积性——那些地方的"面积贡献"为零，积分不理会。</p>

  <h3>11.5 八条性质（和定积分对照）</h3>
  <div class="table-wrap"><table>
    <colgroup><col style="width:10%"><col style="width:45%"><col style="width:45%"></colgroup>
    <tr><th>序号</th><th>二重积分</th><th>对应的定积分</th></tr>
    <tr><td>1</td><td>$\iint_D kf\,d\sigma=k\iint_D f\,d\sigma$</td><td>$\int_a^b kf\,dx=k\int_a^b f\,dx$</td></tr>
    <tr><td>2</td><td>$\iint_D(f\pm g)= \iint_D f\pm\iint_D g$</td><td>$\int(f\pm g)=\int f\pm\int g$</td></tr>
    <tr><td>3</td><td>$D=D_1\cup D_2$（内部不重叠）时积分相加</td><td>区间分段可加</td></tr>
    <tr><td>4</td><td>$f\le g$ 时 $\iint_D f\le\iint_D g$</td><td>$\int f\le\int g$</td></tr>
    <tr><td>5</td><td>$\left|\iint_D f\right|\le\iint_D|f|$</td><td>$\left|\int f\right|\le\int|f|$</td></tr>
    <tr><td>6</td><td>$mS\le\iint_D f\le MS$（估值）</td><td>$m(b-a)\le\int f\le M(b-a)$</td></tr>
    <tr><td>7</td><td>中值定理：$\iint_D f=f(\xi,\eta)\cdot S$</td><td>$\int_a^b f=f(\xi)(b-a)$</td></tr>
    <tr><td>8</td><td>关于坐标轴对称时奇函数部分为零</td><td>奇函数在对称区间积分为零</td></tr>
  </table></div>
  <p>其中 $S$ 表示 $D$ 的面积。第 7 条要求 $f$ 连续；第 8 条最常用，展开说：</p>
  <div class="callout callout-key">
    <div class="callout-title">对称性：能省一半以上的计算量</div>
    <p>若 $D$ 关于 $x$ 轴对称，$f(x,-y)=-f(x,y)$（关于 $y$ 是奇函数），则 $\iint_D f\,d\sigma=0$；若 $f(x,-y)=f(x,y)$（偶函数），则 $\iint_D f=2\iint_{D_1} f$，$D_1$ 是上半部分。</p>
    <p>关于 $y$ 轴对称同理，只需把"$y$ 的奇偶"换成"$x$ 的奇偶"。直觉：上下（左右）两块形状一样，函数值一正一负，正好抵消。</p>
  </div>

  <h4>例 1：比较两个积分的大小</h4>
  <p>比较 $\iint_D(x+y)^2d\sigma$ 与 $\iint_D(x+y)^3d\sigma$，其中 $D:(x-2)^2+(y-1)^2\le2$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">先判断 $x+y$ 在 $D$ 上的范围</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>圆的边界 $(x-2)^2+(y-1)^2=2$ 与 $x$ 轴交于 $(1,0)$；圆心到直线 $x+y=1$ 的距离：$\dfrac{|2+1-1|}{\sqrt2}=\sqrt2$，正好等于半径，所以圆与直线 $x+y=1$ <b>相切</b>。</p>
        <p>整个 $D$ 在直线 $x+y=1$ 的上方（$x+y\ge1$），等号只在切点成立。</p>
        <p>于是 $x+y\ge1$ 且不全为 1，$x+y$ 的立方不小于它的平方：$(x+y)^2\le(x+y)^3$，且严格不等号在大部分区域成立。</p>
        <p>由性质 4（保序）：$\iint_D(x+y)^2d\sigma\le\iint_D(x+y)^3d\sigma$。</p>
        <p>检验：取圆心 $(2,1)$，$x+y=3&gt;1$；取切点 $(1,0)$，$x+y=1$。范围判断正确。</p>
      </div>
    </div>
  </div>

  <h4>例 2：用中值定理估计积分</h4>
  <p>估计 $I=\iint_D\dfrac{dx\,dy}{100+\cos^2x+\cos^2y}$，$D:|x|+|y|\le10$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">夹住被积函数，再乘面积</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$D$ 是菱形，对角线各长 20，面积 $S=\dfrac{20\cdot20}{2}=200$。</p>
        <p>$\cos^2x+\cos^2y$ 在 $[0,1]$ 内，所以分母在 $[100,102]$ 内，被积函数夹在 $\frac1{102}$ 与 $\frac1{100}$ 之间。</p>
        <p>由估值性质 6：$\dfrac{200}{102}\le I\le\dfrac{200}{100}$，即 $1.96\le I\le2$。</p>
        <p>注意这个估计只用了"函数有界"和"区域面积"，没有真的去积——中值定理与估值性质的价值就在这里。</p>
      </div>
    </div>
  </div>

  <h3>11.6 小结</h3>
  <div class="callout callout-key">
    <div class="callout-title">这一章的主线</div>
    <p>① 先用"内面积/外面积"把"平面图形的面积"定义清楚：两边能合拢才叫可求面积，边界面积为零即可求面积。</p>
    <p>② 再把"分割-取点-求和-取极限"搬到平面区域上，得到 $\iint_D f\,d\sigma$。</p>
    <p>③ 可积的判据是上下和能合拢；连续函数、间断点集面积为 0 的函数都可积。</p>
    <p>④ 八条性质与定积分逐条对应；对称性是最省力的一条。</p>
  </div>

  <div class="qa-item">
    <p><b>思考 1</b>：$\iint_D 1\,d\sigma$ 等于什么？</p>
    <p>等于 $D$ 的面积。所以"面积"这件事在二重积分里退化成了"密度为 1 的总质量"。</p>
  </div>
  <div class="qa-item">
    <p><b>思考 2</b>：为什么"间断点集面积为 0"不影响可积？</p>
    <p>因为上下和的差别只来自那些异常的小块，而这些小块的总面积可以压到任意小；它们对积分的贡献趋于 0。</p>
  </div>
  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="double-calc" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">12</span>直角坐标下算二重积分：切成两次一元积分</h2>
  <p class="lead">前置知识：二重积分的定义与性质（第 11 章）、一元定积分的牛顿-莱布尼茨公式、区域的不等式描述。后续应用：极坐标变换、三重积分、曲面积分。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 二重积分不能直接算，但可以化成<b>两次一元定积分</b>，一次算一层。</p>
    <p>② 化成哪一次先算，取决于区域的形状，也取决于哪个被积函数积得出来。</p>
    <p>③ 次序选错会卡死（比如 $e^{-y^2}$ 没有初等原函数），这时候必须交换次序。</p>
  </div>

  <h3>12.1 核心思想：先切条，再累加</h3>
  <p>把曲顶柱体沿 $x$ 方向切成薄片。固定一个 $x$，这一片是一个"曲边梯形"：底边在 $y$ 方向从 $y_1(x)$ 到 $y_2(x)$，高度是 $f(x,y)$。它的面积是一元积分：</p>
  <div class="formula">$$A(x)=\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy$$</div>
  <p>再把所有薄片的面积沿 $x$ 方向累加，得到体积：</p>
  <div class="formula">$$V=\int_a^b A(x)\,dx=\int_a^b\left[\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy\right]dx$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：切面包</div>
    <p>面包（曲顶柱体）横着切片，每片的面积能算；把所有片的"面积 × 厚度"加起来就是体积。这里"厚度"是 $dx$，"片面积"是里面那层积分。</p>
    <p>所以二重积分等于"先对 $y$ 积、再对 $x$ 积"。反过来先对 $x$ 后对 $y$ 也行，只要区域描述得出来。</p>
  </div>
  <p>注意两层积分的<b>写法顺序</b>：$\displaystyle\int_a^b dx\int_{y_1(x)}^{y_2(x)}f\,dy$ 表示先算后面那个（含 $dy$ 的），再算前面那个。这个写法把"积分限跟着谁走"标得很清楚：外层的限只含常数，内层的限可以含外层变量。</p>

  <h3>12.2 矩形区域：最干净的情形</h3>
  <p>定理 21.8：设 $f$ 在矩形 $D=[a,b]\times[c,d]$ 上可积，且对每个 $x\in[a,b]$，$\int_c^d f(x,y)dy$ 存在，则</p>
  <div class="formula">$$\iint_D f(x,y)\,d\sigma=\int_a^b dx\int_c^d f(x,y)\,dy$$</div>
  <p>定理 21.9（对称版）：若对每个 $y$，$\int_a^b f(x,y)dx$ 存在，则</p>
  <div class="formula">$$\iint_D f(x,y)\,d\sigma=\int_c^d dy\int_a^b f(x,y)\,dx$$</div>
  <p>$f$ 连续时两式都成立，可以随便挑一个方便的。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">定理 21.8 的思路</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>把 $[a,b]$ 分成 $m$ 份、$[c,d]$ 分成 $n$ 份，得到 $mn$ 个小矩形。二重和式可以按行重排：</p>
        <p>$$\sum_{i,j}f(\xi_i,\eta_j)\Delta x_i\Delta y_j=\sum_{i=1}^{m}\left[\sum_{j=1}^{n}f(\xi_i,\eta_j)\Delta y_j\right]\Delta x_i$$</p>
        <p>有限和可以交换顺序，这是关键。内层括号里是"固定 $x=\xi_i$ 时对 $y$ 的一元和式"。</p>
        <p>当 $||T||\to0$，内层趋近 $\int_c^d f(\xi_i,y)dy=A(\xi_i)$；外层再趋近 $\int_a^b A(x)dx$。</p>
        <p>严格证明要用到 $A(x)$ 的可积性与误差估计（教材用 $\omega_i$ 振幅控制），但骨架就是"重排 + 两次取极限"。证毕。</p>
      </div>
    </div>
  </div>

  <h4>例 1：$y\sin(xy)$</h4>
  <p>计算 $\iint_D y\sin(xy)\,d\sigma$，$D=[0,\pi]\times[0,1]$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">先对 $x$ 积，因为 $\sin(xy)$ 对 $x$ 好积</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先对 $x$：$\displaystyle\int_0^\pi y\sin(xy)\,dx=y\left[-\frac{\cos(xy)}{y}\right]_0^\pi=1-\cos(\pi y)$。</p>
        <p>再对 $y$：$\displaystyle\int_0^1(1-\cos\pi y)dy=\left[y-\frac{\sin\pi y}{\pi}\right]_0^1=1-0=1$。</p>
        <p>所以 $\iint_D y\sin(xy)d\sigma=1$。</p>
        <p>若反过来先对 $y$ 积，会得到 $-\frac{\cos x}{x}+\frac{\sin x}{x^2}$ 这类式子，再对 $x$ 积分麻烦得多。次序的选择在这里已经显出价值。</p>
      </div>
    </div>
  </div>

  <h3>12.3 X 型区域与 Y 型区域</h3>
  <p>矩形之外的区域，边界是曲线。按"竖着扫得通还是横着扫得通"分两类：</p>
  <div class="formula">
    <p><b>X 型区域</b>（竖线扫）：$D=\{(x,y)\mid y_1(x)\le y\le y_2(x),\;a\le x\le b\}$</p>
    <p><b>Y 型区域</b>（横线扫）：$D=\{(x,y)\mid x_1(y)\le x\le x_2(y),\;c\le y\le d\}$</p>
  </div>
  <p>定理 21.10：若 $D$ 是 X 型区域，$f$ 在 $D$ 上连续，则</p>
  <div class="formula">$$\iint_D f\,d\sigma=\int_a^b dx\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy$$</div>
  <p>定理 21.11：若 $D$ 是 Y 型区域，则</p>
  <div class="formula">$$\iint_D f\,d\sigma=\int_c^d dy\int_{x_1(y)}^{x_2(y)}f(x,y)\,dx$$</div>
  <div class="callout callout-key">
    <div class="callout-title">判断口诀</div>
    <p>在区域上随便竖着画一条线：如果它<b>进出边界各一次</b>（不多不少），就是 X 型；横着画一条线同样只进出一次，就是 Y 型。两种都行时挑好算的那个；都不行就切开成几块。</p>
  </div>

  <h4>例 2：次序选错就积不出来</h4>
  <p>计算 $I=\iint_D x^2e^{-y^2}d\sigma$，$D$ 由 $x=0$、$y=1$、$y=x$ 围成。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">先试着按原顺序走，发现卡住，于是换序</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>区域是三角形：$0\le x\le1$，$x\le y\le1$。若先对 $y$ 积：$\int x^2e^{-y^2}dy$ 积不出来——$e^{-y^2}$ 没有初等原函数。</p>
        <p>改成先对 $x$ 积。把区域按 $y$ 描述：$0\le y\le1$，$0\le x\le y$。</p>
        <p>$$\int_0^y x^2dx=\frac{y^3}{3}\;\Rightarrow\;I=\int_0^1\frac{y^3}{3}e^{-y^2}dy$$</p>
        <p>换元 $u=y^2$，$du=2y\,dy$，$y^3dy=y^2\cdot y\,dy=u\cdot\frac{du}{2}$：</p>
        <p>$$I=\frac13\int_0^1\frac{u}{2}e^{-u}du=\frac16\int_0^1 ue^{-u}du$$</p>
        <p>$\int ue^{-u}du=-(u+1)e^{-u}$（分部积分），所以 $\int_0^1ue^{-u}du=1-\frac{2}{e}$。</p>
        <p>$$I=\frac16\left(1-\frac2e\right)=\frac16-\frac{1}{3e}\approx0.0441$$</p>
        <p>数值检查：$1/6\approx0.1667$，$1/(3e)\approx0.1226$，差 $0.0441$，与被积函数在三角形上"小 $x$、$y$ 接近 1 时 $e^{-y^2}\approx0.37$"的量级相符。</p>
      </div>
    </div>
  </div>

  <h4>例 3：$\dfrac{\sin x}{x}$ 也只能换序</h4>
  <p>计算 $\iint_D\dfrac{\sin x}{x}d\sigma$，$D$ 由 $y=x$、$y=0$、$x=\pi$ 围成。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">先对 $y$ 积一行，$\dfrac{\sin x}{x}$ 就变成 $\sin x$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>区域：$0\le x\le\pi$，$0\le y\le x$。注意这里<b>先对 $y$ 积</b>反而是对的：</p>
        <p>$$\int_0^x\frac{\sin x}{x}dy=\frac{\sin x}{x}\cdot x=\sin x$$</p>
        <p>再对 $x$：$\displaystyle\int_0^\pi\sin x\,dx=2$。所以 $I=2$。</p>
        <p>若先对 $x$ 积，$\int\frac{\sin x}{x}dx$ 不是初等函数，此题就做不下去了。同一道题，次序决定成败。</p>
      </div>
    </div>
  </div>

  <h3>12.4 交换积分次序：画图、换描述、重写限</h3>
  <p>遇到"给了累次积分但积不出来"或者"区域描述不顺"的情况，就交换次序。做法固定三步：</p>
  <div class="callout callout-key">
    <div class="callout-title">三步走</div>
    <p>① 从原来的积分限把区域的边界画出来；② 换一种扫法重新描述区域（找出新的上下界）；③ 按新描述重写累次积分，注意内层限可以含外层变量，外层限必须是常数。</p>
  </div>
  <p>例 4（教材）：把下列两个累次积分合并成一个先对 $x$ 后对 $y$ 的积分：</p>
  <div class="formula">$$I=\int_0^2dx\int_0^{x^2/2}f\,dy+\int_2^{2\sqrt2}dx\int_0^{\sqrt{8-x^2}}f\,dy$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先还原区域，再横着扫</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>第一段：$0\le x\le2$，$0\le y\le x^2/2$，下边界是 $y=0$，上边界是抛物线 $y=x^2/2$。</p>
        <p>第二段：$2\le x\le2\sqrt2$，$0\le y\le\sqrt{8-x^2}$，上边界是圆 $x^2+y^2=8$ 的上半支。</p>
        <p>两段在 $x=2$ 处接上：抛物线 $y=x^2/2$ 在 $x=2$ 时为 $2$，圆在 $x=2$ 时为 $\sqrt{8-4}=2$，正好交于 $(2,2)$。</p>
        <p>所以整个区域由 $y=x^2/2$（下边界）与 $x^2+y^2=8$（上边界）围成，右端点 $x=2\sqrt2$ 是圆与 $x$ 轴的交点。</p>
        <p>改成横着扫：$y$ 从 $0$ 到 $2$。固定 $y$，左边界由抛物线给出：$x=\sqrt{2y}$；右边界由圆给出：$x=\sqrt{8-y^2}$。</p>
        <p>$$I=\int_0^2dy\int_{\sqrt{2y}}^{\sqrt{8-y^2}}f(x,y)\,dx$$</p>
        <p>验证端点：$y=0$ 时左边界 $0$、右边界 $2\sqrt2$，与横轴一致；$y=2$ 时左右都是 $2$，退化为一点 ✓。</p>
      </div>
    </div>
  </div>

  <h3>12.5 一般区域：切开再拼</h3>
  <p>既不是 X 型也不是 Y 型的区域，用平行于坐标轴的直线切成有限块，每块单独算，再用性质 3（区域可加）加起来。</p>
  <h4>例 5：两圆之间的月牙</h4>
  <p>设 $D=\{(x,y)\mid 2x\le x^2+y^2\le4x\}$，把 $\iint_D f\,d\sigma$ 化成两种次序的累次积分。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先认区域：两个圆，相切于原点</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>配方：$x^2+y^2=2x\Rightarrow(x-1)^2+y^2=1$；$x^2+y^2=4x\Rightarrow(x-2)^2+y^2=4$。两个圆都过原点，内圆半径 1、圆心 $(1,0)$，外圆半径 2、圆心 $(2,0)$。</p>
        <p>$D$ 是"外圆之内、内圆之外"的月牙，左右对称于 $x$ 轴。</p>
        <p><b>先对 $y$ 后对 $x$（X 型）</b>：$x$ 从 $0$ 到 $4$。当 $0\le x\le2$，内圆还在，要分上下两支：</p>
        <p>$$\int_0^2dx\int_{\sqrt{2x-x^2}}^{\sqrt{4x-x^2}}f\,dy+\int_0^2dx\int_{-\sqrt{4x-x^2}}^{-\sqrt{2x-x^2}}f\,dy+\int_2^4dx\int_{-\sqrt{4x-x^2}}^{\sqrt{4x-x^2}}f\,dy$$</p>
        <p><b>先对 $x$ 后对 $y$（Y 型）</b>：$y$ 从 $0$ 到 $2$（外圆最高点在 $y=2$）。$0\le y\le1$ 时内圆存在，左右各一支：</p>
        <p>$$\int_0^1dy\int_{2-\sqrt{4-y^2}}^{1-\sqrt{1-y^2}}f\,dx+\int_0^1dy\int_{1+\sqrt{1-y^2}}^{2+\sqrt{4-y^2}}f\,dx+\int_1^2dy\int_{2-\sqrt{4-y^2}}^{2+\sqrt{4-y^2}}f\,dx$$</p>
        <p>两种写法都得拆成三块——区域本身的形状决定了这一点，而不是计算者的偏好。判断是否拆对：每块的上下（左右）边界都是单值函数，且拼起来恰好覆盖整个 $D$、不重不漏。</p>
      </div>
    </div>
  </div>

  <h4>例 6：带绝对值的分块</h4>
  <p>计算 $\iint_D\left|xy-\dfrac14\right|dx\,dy$，$D=[0,1]\times[0,1]$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用对称性把绝对值拆开，只算一半</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先算不带绝对值的积分：$\iint_D\left(xy-\frac14\right)=\left(\int_0^1x\,dx\right)\left(\int_0^1y\,dy\right)-\frac14\cdot1=\frac14-\frac14=0$。</p>
        <p>所以 $xy-\frac14$ 在 $D$ 上的"正部分"与"负部分"面积相等。于是</p>
        <p>$$\iint_D\left|xy-\frac14\right|=2\iint_{D_1}\left(xy-\frac14\right),\quad D_1=\left\{xy\ge\frac14\right\}$$</p>
        <p>$D_1$：$x$ 从 $\frac14$ 到 $1$，$y$ 从 $\frac{1}{4x}$ 到 $1$（双曲线 $y=\frac{1}{4x}$ 上方）。</p>
        <p>$$\iint_{D_1}xy=\int_{1/4}^1x\,dx\int_{1/(4x)}^1y\,dy=\int_{1/4}^1x\left(\frac12-\frac{1}{32x^2}\right)dx=\frac{15}{64}-\frac{\ln2}{16}$$</p>
        <p>$D_1$ 的面积 $=\displaystyle\int_{1/4}^1\left(1-\frac{1}{4x}\right)dx=\frac34-\frac{\ln2}{2}$，所以 $\iint_{D_1}\frac14=\frac{3}{16}-\frac{\ln2}{8}$。</p>
        <p>$$\iint_{D_1}\left(xy-\frac14\right)=\left(\frac{15}{64}-\frac{\ln2}{16}\right)-\left(\frac{3}{16}-\frac{\ln2}{8}\right)=\frac{3}{64}+\frac{\ln2}{16}$$</p>
        <p>乘 2：$$\iint_D\left|xy-\frac14\right|=\frac{3}{32}+\frac{\ln2}{8}\approx0.180$$</p>
        <p>数值复核：对 $[0,1]^2$ 做 $4000\times4000$ 网格求平均，得 $0.1804$，与解析值一致。</p>
      </div>
    </div>
  </div>

  <h3>12.6 应用：两个圆柱相交的体积</h3>
  <p>例 4：两个底面半径都是 $a$ 的圆柱，轴互相垂直相交，求围成的立体体积。</p>
  <p>设两圆柱为 $x^2+y^2=a^2$ 与 $x^2+z^2=a^2$。立体关于三个坐标平面都对称，只算第一卦限再乘 8。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">第一卦限里，顶是 $z=\sqrt{a^2-x^2}$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>第一卦限中，底 $D$ 是四分之一圆 $x^2+y^2\le a^2$（$x,y\ge0$）；顶由第二个圆柱给出 $z=\sqrt{a^2-x^2}$。</p>
        <p>$$V=8\iint_D\sqrt{a^2-x^2}\,d\sigma=8\int_0^adx\int_0^{\sqrt{a^2-x^2}}\sqrt{a^2-x^2}\,dy$$</p>
        <p>内层对 $y$ 积时被积函数不含 $y$，等于"高 × 底边长"：$\sqrt{a^2-x^2}\cdot\sqrt{a^2-x^2}=a^2-x^2$。</p>
        <p>$$V=8\int_0^a(a^2-x^2)dx=8\left(a^3-\frac{a^3}{3}\right)=\frac{16a^3}{3}$$</p>
        <p>检查：$a=1$ 时体积约 $5.33$，小于外接立方体 $2\times2\times2=8$，合理。</p>
      </div>
    </div>
  </div>

  <h3>12.7 小结</h3>
  <div class="callout callout-key">
    <div class="callout-title">计算流程可以固定成五步</div>
    <p>① 画区域，判断是 X 型、Y 型，还是得切块；② 看被积函数，哪个变量先积得出来；③ 写出两层积分，外层限必须常数；④ 内层算完代入外层；⑤ 用对称性、面积、量级做一次合理性检查。</p>
  </div>

  <div class="qa-item">
    <p><b>思考 1</b>：为什么外层积分限必须是常数，内层可以是变量？</p>
    <p>因为外层积的是"薄片的编号"（比如 $x$），它从区域的一端走到另一端，范围与内层无关；内层的范围则取决于当前这一片在哪里，所以含外层变量。</p>
  </div>
  <div class="qa-item">
    <p><b>思考 2</b>：例 2 里若硬要先对 $y$ 积，能不能做？</p>
    <p>用级数展开可以，但那就不是初等解法了。二重积分的题目里，"换序"本身就是标准技巧，不必死磕。</p>
  </div>
  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="exercises" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">13</span>习题课与复习课：把方法固化成动作</h2>
  <p class="lead">前置知识：第 18–21 章全部内容。这一章不讲新定理，只把习题课、复习课里反复出现的题型和判据整理成可执行的动作，并给出易错点清单。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 这一章的用法</div>
    <p>考前过一遍：每道题先判"属于哪一类"，再套对应的动作。动作记熟了，题目只是换数字。</p>
  </div>

  <h3>13.1 隐函数存在性：四个条件逐个核对</h3>
  <p>题目：方程 $\cos x+\sin y=e^{xy}$ 能否在原点的某邻域确定隐函数 $y=f(x)$？能否确定 $x=g(y)$？</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">设 $F=\cos x+\sin y-e^{xy}$，逐条检查</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>① $F$ 在原点邻域连续（初等函数复合，处处连续）。</p>
        <p>② $F(0,0)=\cos0+\sin0-e^0=1+0-1=0$，原点在曲线上。</p>
        <p>③ $F_x=-\sin x-ye^{xy}$，$F_y=\cos y-xe^{xy}$，都在邻域内连续。</p>
        <p>④ $F_y(0,0)=\cos0-0=1\ne0$；$F_x(0,0)=-\sin0-0=0$。</p>
        <p>结论：$F_y(0,0)\ne0$，可以确定 $y=f(x)$；$F_x(0,0)=0$，条件不满足，<b>不能</b>断定能确定 $x=g(y)$（事实上在这个点附近 $x$ 不是 $y$ 的单值函数）。</p>
        <p>顺带能写出导数值：$f'(0)=-\dfrac{F_x(0,0)}{F_y(0,0)}=0$。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-warn">
    <div class="callout-title">易错点：条件缺一不可，但只有偏导非零那条决定"解谁"</div>
    <p>连续性、$F=0$、偏导连续这三条是"资格线"；$F_y\ne0$ 或 $F_x\ne0$ 决定"谁是自变量、谁是函数"。两条偏导都为零时，定理失效，需要另想办法（比如直接观察方程结构）。</p>
  </div>

  <h3>13.2 含参量积分：极限什么时候能搬进积分号</h3>
  <p>题目：求 $\displaystyle\lim_{\alpha\to0}\int_0^2x^2\cos\alpha x\,dx$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">先看能否直接用连续性定理</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>被积函数 $f(x,\alpha)=x^2\cos\alpha x$ 在矩形 $[0,2]\times[-1,1]$ 上连续。由含参量积分的连续性，$I(\alpha)=\int_0^2f(x,\alpha)dx$ 在 $\alpha=0$ 处连续。</p>
        <p>于是极限可以搬进去：$$\lim_{\alpha\to0}I(\alpha)=I(0)=\int_0^2x^2dx=\frac83$$</p>
        <p>若硬算：$\int_0^2x^2\cos\alpha x\,dx$ 要分部积分两次，得到含 $\alpha$ 的表达式再取极限，结果同样是 $\frac83$，但多写一页。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-warn">
    <div class="callout-title">易错点：连续性定理有前提</div>
    <p>要求 $f(x,\alpha)$ 在<b>闭矩形</b>上连续（对 $x$ 连续、对 $\alpha$ 一致有界那一类条件）。若积分区间是无穷的（反常积分），必须换成"一致收敛"的判别法，直接搬极限会出错。</p>
  </div>

  <h3>13.3 曲线积分：先看是 $ds$ 还是 $dx,dy$</h3>
  <p>题目：计算 $\displaystyle\int_L(x^2+y^2)^{1/2}ds$，$L$ 是以原点为中心、$R$ 为半径的右半圆周。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">认出第一型，直接上弧长公式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>被积式里是 $ds$，没有方向，属于第一型曲线积分。</p>
        <p>参数化右半圆：$x=R\cos\theta$，$y=R\sin\theta$，$\theta\in\left[-\frac\pi2,\frac\pi2\right]$。</p>
        <p>$\sqrt{x'^2+y'^2}=R$，所以 $ds=R\,d\theta$；被积函数 $(x^2+y^2)^{1/2}=R$。</p>
        <p>$$\int_L(x^2+y^2)^{1/2}ds=\int_{-\pi/2}^{\pi/2}R\cdot R\,d\theta=R^2\cdot\pi=\pi R^2$$</p>
        <p>合理性：均匀"密度"为 $R$，弧长为 $\pi R$，乘积正是 $\pi R^2$。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">两个判断动作</div>
    <p>① 看微分：$ds$ → 第一型（无方向，用弧长公式）；$dx,dy,dz$ → 第二型（有方向，用 $x',y',z'$ 代入）。</p>
    <p>② 看对称性：区域或曲线关于坐标轴对称时，先判被积函数的奇偶性，能直接判零的不要硬算。</p>
  </div>

  <h3>13.4 复习课串讲：18 章的方法链</h3>
  <p>18 章的主线是"方程 → 函数 → 几何 → 极值"，四步各有固定动作。</p>
  <div class="table-wrap"><table>
    <colgroup><col style="width:22%"><col style="width:38%"><col style="width:40%"></colgroup>
    <tr><th>环节</th><th>动作</th><th>检查点</th></tr>
    <tr><td>隐函数存在</td><td>设 $F$，验证连续、$F=0$、偏导连续、某偏导非零</td><td>解 $y$ 看 $F_y$，解 $x$ 看 $F_x$</td></tr>
    <tr><td>隐函数求导</td><td>$y'=-\dfrac{F_x}{F_y}$；方程组用雅可比行列式</td><td>分母不为零</td></tr>
    <tr><td>几何应用</td><td>切线方向 $(1,y')$；切平面法向量 $(F_x,F_y,F_z)$</td><td>法向量非零</td></tr>
    <tr><td>条件极值</td><td>作 $L=f+\lambda\varphi$，解 $L_x=L_y=L_\lambda=0$，再判极值</td><td>稳定点要在约束曲线上</td></tr>
  </table></div>
  <p>拉格朗日乘数法的三步在 18 复习课的总结页上写得很清楚：作辅助函数、求偏导为零的方程组、考察稳定点。第三步最容易被跳过——解出 $\lambda$ 只是找到"候选点"，是不是极值还要看。</p>

  <h3>13.5 复习课串讲：19 章的定理链</h3>
  <p>19 章一条线走下来是"连续性 → 可微性 → 可积性 → 一致收敛 → 判别法 → 欧拉积分"。</p>
  <div class="callout callout-tip">
    <div class="callout-title">八条主定理的记忆线索</div>
    <p>连续性与可微性回答"能不能在积分号下取极限、求导"；可积性回答"能不能交换两个积分的次序"；一致收敛是这些操作的<b>许可证</b>；柯西准则、$M$ 判别法、狄利克雷、阿贝尔判别法是领许可证的四把钥匙；$\Gamma$ 与 $B$ 函数是这套工具最著名的两个产物。</p>
  </div>
  <p>做题时的顺序：先问"要不要交换极限与积分"，再问"一致收敛成不成立"，最后才动笔算。顺序反了，容易写出没有依据的等式。</p>

  <h3>13.6 易错点清单</h3>
  <div class="table-wrap"><table>
    <colgroup><col style="width:6%"><col style="width:34%"><col style="width:60%"></colgroup>
    <tr><th>#</th><th>错误</th><th>正确做法</th></tr>
    <tr><td>1</td><td>第二型曲线积分把方向写反</td><td>积分限与起点终点一一对应；反向后整体加负号</td></tr>
    <tr><td>2</td><td>把 $\int_L P\,dx$ 里的 $dx$ 当成弧长</td><td>$dx$ 是坐标增量，可为负；弧长是 $ds\ge0$</td></tr>
    <tr><td>3</td><td>二重积分外层限写成变量</td><td>外层限必须是常数，内层才可含外层变量</td></tr>
    <tr><td>4</td><td>换序后忘改积分限</td><td>三步走：画图、换描述、重写限，最后验端点</td></tr>
    <tr><td>5</td><td>先对 $e^{-y^2}$、$\frac{\sin x}{x}$ 这类无初等原函数的变量积分</td><td>先判"谁积得出来"，再定次序</td></tr>
    <tr><td>6</td><td>区域不拆就硬写一个累次积分</td><td>不是 X/Y 型就切块，每块单独写</td></tr>
    <tr><td>7</td><td>用对称性时不检查被积函数的奇偶性</td><td>区域对称 + 函数奇 → 0；函数偶 → 2 倍半区</td></tr>
    <tr><td>8</td><td>条件极值只解出稳定点就交卷</td><td>补一步：用二阶条件或问题背景判断极大极小</td></tr>
    <tr><td>9</td><td>含参量积分直接搬极限</td><td>先确认一致收敛或连续性前提</td></tr>
    <tr><td>10</td><td>绝对值、$\max$、$\min$ 不分块直接积</td><td>找出符号变化的分界线，分区计算后相加</td></tr>
  </table></div>

  <h3>13.7 综合自测</h3>
  <div class="qa-item">
    <p><b>1</b>：设 $F(x,y)=x^2+y^2-1$，在 $(0,1)$ 处能确定 $y=f(x)$ 吗？$f'(0)=?$</p>
    <p>$F_y=2y$，在 $(0,1)$ 处为 2，非零，可以。$f'(0)=-\dfrac{F_x}{F_y}=-\dfrac{0}{2}=0$。几何上单位圆在最高点切线水平 ✓</p>
  </div>
  <div class="qa-item">
    <p><b>2</b>：$\displaystyle\int_L y\,dx+x\,dy$ 沿从 $(0,0)$ 到 $(1,1)$ 的直线段等于多少？沿抛物线 $y=x^2$ 呢？</p>
    <p>被积式 $=d(xy)$，两者都等于 $xy\big|_{(0,0)}^{(1,1)}=1$。这是全微分型，路径无关。</p>
  </div>
  <div class="qa-item">
    <p><b>3</b>：$\displaystyle\iint_D(x^2+y^2)d\sigma$，$D:x^2+y^2\le a^2$，用直角坐标能算吗？</p>
    <p>能，但要拆上下半圆并做三角换元，很麻烦。这类圆对称区域应留到极坐标（下一册内容），直角坐标不是万能工具。</p>
  </div>
  <div class="qa-item">
    <p><b>4</b>：判断 $\displaystyle\int_0^1dx\int_x^1 e^{-y^2}dy$ 该怎么处理。</p>
    <p>先对 $y$ 积不出来，换序：区域 $0\le y\le1,\;0\le x\le y$，得 $\int_0^1dy\int_0^ye^{-y^2}dx=\int_0^1ye^{-y^2}dy=\frac12(1-e^{-1})$。</p>
  </div>
  <div class="qa-item">
    <p><b>5</b>：为什么 $\iint_D f\,d\sigma$ 里的 $d\sigma$ 在直角坐标下写成 $dx\,dy$？</p>
    <p>因为用平行于坐标轴的直线网分割时，小矩形的面积就是 $\Delta x\Delta y$；换成极坐标后小面积元变成 $r\,dr\,d\theta$，那时不能直接写 $dr\,d\theta$。</p>
  </div>
  <div class="chapter-nav"></div>
</section>
"""
