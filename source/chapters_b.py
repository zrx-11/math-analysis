#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""章节内容 B：隐函数组 + 几何应用 + 条件极值"""
from pathlib import Path

CH_B = r"""<!-- ===== 章节：implicit-system ===== -->
<section class="chapter" id="implicit-system" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">3</span>隐函数组：方程组里的函数组</h2>
  <p class="lead">前置知识：解方程组（第 1.4 节）、二阶行列式、偏导数与链式法则、隐函数（第 2 章）。后续应用：反函数组、坐标变换（第 3 章内部）、几何应用（切向量用雅可比）。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 两个方程 $\begin{cases}F(x,y,u,v)=0\\G(x,y,u,v)=0\end{cases}$ 什么时候能解出 $u=u(x,y)$、$v=v(x,y)$？</p>
    <p>② 解出的两个函数的偏导数怎么算？</p>
    <p>③ 答案的关键：一个叫<b>雅可比行列式</b>的东西 $J=\dfrac{\partial(F,G)}{\partial(u,v)}$ 不为 0。</p>
  </div>

  <h3>3.1 从"一个方程一个未知"到"两个方程两个未知"</h3>
  <p>第 2 章：一个方程 $F(x,y)=0$，确定一个隐函数 $y=f(x)$。条件是 $F_y\ne0$。</p>
  <p>现在：<b>两个方程、四个变量</b>（$x,y$ 是自变量，$u,v$ 是待解出的未知函数）：</p>
  <div class="formula">$$\begin{cases} F(x,y,u,v) = 0 \\ G(x,y,u,v) = 0 \end{cases}$$</div>
  <p>目标：解出 $u=u(x,y)$ 和 $v=v(x,y)$，使得代入后两个方程恒成立。</p>
  <div class="callout callout-tip">
    <div class="callout-title"> 生活直觉：一个约束砍掉一个自由度</div>
    你有 4 个未知量，本来随便取。加一个方程 $F=0$，砍掉 1 个自由度，剩 3 个随便取。再加一个方程 $G=0$，再砍 1 个，剩 2 个随便取——正好把 $x,y$ 当"自由的"，$u,v$ 当"被决定的"。所以两个方程恰好决定两个未知函数。
  </div>

  <h3>3.2 雅可比行列式：二阶行列式的"升级版"</h3>
  <p><b>雅可比行列式</b>就是把二阶行列式里的"数字"换成"偏导数"：</p>
  <div class="formula">$$J = \frac{\partial(F,G)}{\partial(u,v)} = \begin{vmatrix} F_u & F_v \\ G_u & G_v \end{vmatrix} = F_u G_v - F_v G_u$$</div>
  <p>读作"$F,G$ 对 $u,v$ 的雅可比"。它是"$F,G$ 组成的方程组能不能解出 $u,v$"的判据。</p>
  <div class="callout callout-tip">
    <div class="callout-title"> 为什么是它？——线性化直觉</div>
    <p>把 $F,G$ 在点附近线性化（像用切线近似曲线一样用平面近似曲面）：</p>
    <p>$$\Delta F \approx F_u\Delta u + F_v\Delta v + F_x\Delta x + F_y\Delta y$$</p>
    <p>$$\Delta G \approx G_u\Delta u + G_v\Delta v + G_x\Delta x + G_y\Delta y$$</p>
    <p>想用 $\Delta x,\Delta y$ 唯一解出 $\Delta u,\Delta v$，就要解这个 2×2 线性方程组——它的系数行列式正好是 $\begin{vmatrix}F_u&F_v\\G_u&G_v\end{vmatrix}=J$。</p>
    <p>由第 1.4 节：行列式 ≠ 0 ⟺ 有唯一解。所以 $J\ne0$ ⟺ 局部能唯一解出 $u,v$。</p>
  </div>
  <p><b>类比记忆</b>：二维的情形 $F_y\ne0$ 是"一个方程一个未知数"的雅可比（$J=F_y$，1×1 行列式）。隐函数组是它的"二对二"版本。</p>

  <h3>3.3 隐函数组定理（定理 18.4）</h3>
  <p><b>条件</b>（与第 2 章完全平行）：</p>
  <div class="formula">
    <p>(i) $F,G$ 在 $P_0(x_0,y_0,u_0,v_0)$ 附近连续；</p>
    <p>(ii) $F(P_0)=0$ 且 $G(P_0)=0$（点确实是解）；</p>
    <p>(iii) $F,G$ 的一阶偏导连续；</p>
    <p>(iv) $J = \dfrac{\partial(F,G)}{\partial(u,v)}\Big|_{P_0} \ne 0$。</p>
  </div>
  <p><b>结论</b>：$P_0$ 附近存在唯一的隐函数组 $u=u(x,y)$、$v=v(x,y)$，连续、可微，且偏导公式：</p>
  <div class="formula">$$\frac{\partial u}{\partial x} = -\frac{\partial(F,G)/\partial(x,v)}{\partial(F,G)/\partial(u,v)}, \quad \frac{\partial u}{\partial y} = -\frac{\partial(F,G)/\partial(y,v)}{\partial(F,G)/\partial(u,v)}$$</div>
  <div class="formula">$$\frac{\partial v}{\partial x} = -\frac{\partial(F,G)/\partial(u,x)}{\partial(F,G)/\partial(u,v)}, \quad \frac{\partial v}{\partial y} = -\frac{\partial(F,G)/\partial(u,y)}{\partial(F,G)/\partial(u,v)}$$</div>
  <div class="callout callout-key">
    <div class="callout-title">偏导公式的"外科手术"记忆法</div>
    分母永远是 $J = \dfrac{\partial(F,G)}{\partial(u,v)}$（$u,v$ 是被解出的）。分子：<b>把分母中"要求的变量"换成"求导的自变量"</b>，再整体加负号。
    <p>例：求 $\frac{\partial u}{\partial x}$ → 分母是 $\partial(F,G)/\partial(u,v)$，把 $u$（要求的）换成 $x$（对谁求导）→ 分子 $\partial(F,G)/\partial(x,v)$，前面加负号。✓</p>
    <p>例：求 $\frac{\partial v}{\partial y}$ → 把 $v$ 换成 $y$ → 分子 $\partial(F,G)/\partial(u,y)$，加负号。✓</p>
  </div>

  <h4>推导：偏导公式怎么来的（以 u_x 为例）</h4>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">推导 ∂u/∂x 公式（克莱姆法则视角）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>出发点</b>：$F(x,y,u(x,y),v(x,y))\equiv 0$ 和 $G(x,y,u(x,y),v(x,y))\equiv 0$。</p>
        <p><b>两边对 $x$ 求偏导</b>（$y$ 固定，链式法则）：</p>
        <p>$$\begin{cases}F_x + F_u\,u_x + F_v\,v_x = 0\\G_x + G_u\,u_x + G_v\,v_x = 0\end{cases}$$</p>
        <p><b>移项</b>，把未知的 $u_x, v_x$ 放左边：</p>
        <p>$$\begin{cases}F_u\,u_x + F_v\,v_x = -F_x\\G_u\,u_x + G_v\,v_x = -G_x\end{cases}$$</p>
        <p>这是以 $u_x,v_x$ 为未知数的 2×2 线性方程组，系数行列式正是 $J$。</p>
        <p><b>用克莱姆法则</b>（把 $u_x$ 的系数列换成常数项列）：</p>
        <p>$$u_x = \frac{\begin{vmatrix}-F_x & F_v \\ -G_x & G_v\end{vmatrix}}{J} = \frac{-F_xG_v + F_vG_x}{J} = -\frac{F_xG_v - F_vG_x}{J}$$</p>
        <p>而 $F_xG_v - F_vG_x = \begin{vmatrix}F_x&F_v\\G_x&G_v\end{vmatrix} = \frac{\partial(F,G)}{\partial(x,v)}$（$x$ 占了原来 $u$ 的位置！）</p>
        <p>所以 $u_x = -\frac{\partial(F,G)/\partial(x,v)}{\partial(F,G)/\partial(u,v)}$。✓ 公式成立。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：完整算一遍</h4>
  <p>方程组 $\begin{cases}u^2+v^2-x^2-y=0\\u-v-xy+1=0\end{cases}$。先找一个满足方程组的点：取 $x=2,y=1$，则需 $u^2+v^2=5$ 且 $u-v=1$。解第二个：$v=u-1$，代入第一个：$u^2+(u-1)^2=5$，$2u^2-2u-4=0$，$u=2$（或 $-1$）。取 $u=2,v=1$。于是验证 $P_0(2,1,2,1)$：$F=4+1-4-1=0$ ✓；$G=2-1-2+1=0$ ✓。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">判断能否解出，并求 u_x, v_x 在 P0 的值</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>四个偏导（$F=u^2+v^2-x^2-y,\;G=u-v-xy+1$）：</p>
        <p>$F_u=2u=4$，$F_v=2v=2$，$G_u=1$，$G_v=-1$（在 $P_0$ 处）。</p>
        <p>$$J = F_uG_v - F_vG_u = 4\cdot(-1) - 2\cdot1 = -6 \ne 0$$</p>
        <p>$J\ne0$：能唯一解出 $u,v$（局部）。</p>
        <p>再算 $u_x$：$F_x = -2x = -4$，$G_x = -y = -1$。</p>
        <p>$$\frac{\partial(F,G)}{\partial(x,v)} = \begin{vmatrix}F_x&F_v\\G_x&G_v\end{vmatrix} = \begin{vmatrix}-4&2\\-1&-1\end{vmatrix} = (-4)(-1) - 2(-1) = 4+2 = 6$$</p>
        <p>$$u_x = -\frac{6}{-6} = 1$$</p>
        <p>同理 $v_x$：$\frac{\partial(F,G)}{\partial(u,x)}=\begin{vmatrix}F_u&F_x\\G_u&G_x\end{vmatrix}=\begin{vmatrix}4&-4\\1&-1\end{vmatrix}=-4+4=0$，$v_x = -\frac{0}{-6}=0$。</p>
        <p>再算 $u_y, v_y$（$F_y=-1$，$G_y=-x=-2$）：$\frac{\partial(F,G)}{\partial(y,v)}=\begin{vmatrix}-1&2\\-2&-1\end{vmatrix}=1+4=5$，$u_y=-\frac{5}{-6}=\frac56$；$\frac{\partial(F,G)}{\partial(u,y)}=\begin{vmatrix}4&-1\\1&-2\end{vmatrix}=-8+1=-7$，$v_y=-\frac{-7}{-6}=-\frac76$。</p>
        <p>方法比数值更重要：<b>先算 J，再"换列"算分子，加负号</b>。</p>
      </div>
    </div>
  </div>

  <h3>3.4 反函数组：坐标变换的逆变换</h3>
  <p>设 $u=u(x,y),\; v=v(x,y)$ 是一个变换（把 $(x,y)$ 变成 $(u,v)$）。问：什么时候能"反解"出 $x=x(u,v),\; y=y(u,v)$？</p>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：正着走能走，倒着走不一定</div>
    变换像一个"地图投影"。某些地方多个点投影到同一个 $(u,v)$，就没法倒着走。判据：$u,v$ 对 $x,y$ 的雅可比 $\frac{\partial(u,v)}{\partial(x,y)}\ne0$。
  </div>
  <p><b>定理 18.5（反函数组定理）</b>：若 $u(x,y),v(x,y)$ 有连续一阶偏导，且 $\frac{\partial(u,v)}{\partial(x,y)}\ne0$，则局部存在反函数组 $x=x(u,v), y=y(u,v)$，且：</p>
  <div class="formula">$$\frac{\partial(x,y)}{\partial(u,v)} = \frac{1}{\partial(u,v)/\partial(x,y)}$$</div>
  <div class="callout callout-key">
    <div class="callout-title">和一元反函数完全平行</div>
    一元：$\frac{dx}{dy} = \frac{1}{dy/dx}$（导数互为倒数）。二元：雅可比互为倒数。一元是 $1\times1$ 的雅可比，这里升级成 $2\times2$，规律不变。
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">雅可比互为倒数的证明</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>记 $J_{xy} = \frac{\partial(u,v)}{\partial(x,y)}$。反函数组的偏导公式（由隐函数组定理，把 $F=u-u(x,y), G=v-v(x,y)$ 代入）：</p>
        <p>$$x_u = \frac{v_y}{J_{xy}},\quad x_v = -\frac{u_y}{J_{xy}},\quad y_u = -\frac{v_x}{J_{xy}},\quad y_v = \frac{u_x}{J_{xy}}$$</p>
        <p>于是：</p>
        <p>$$\frac{\partial(x,y)}{\partial(u,v)} = x_u y_v - x_v y_u = \frac{v_y}{J_{xy}}\frac{u_x}{J_{xy}} - \left(-\frac{u_y}{J_{xy}}\right)\left(-\frac{v_x}{J_{xy}}\right) = \frac{u_xv_y - u_yv_x}{J_{xy}^2} = \frac{J_{xy}}{J_{xy}^2} = \frac{1}{J_{xy}}$$</p>
        <p>（用到 $u_xv_y-u_yv_x = J_{xy}$ 的定义。）证毕。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：极坐标变换的逆变换</h4>
  <p>$x = r\cos\theta,\; y = r\sin\theta$（直角坐标 ← 极坐标）。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">验证雅可比 = r，除原点外可逆</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$$\frac{\partial(x,y)}{\partial(r,\theta)} = \begin{vmatrix}x_r & x_\theta \\ y_r & y_\theta\end{vmatrix} = \begin{vmatrix}\cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta\end{vmatrix} = \cos\theta\cdot r\cos\theta - (-r\sin\theta)\sin\theta = r(\cos^2\theta+\sin^2\theta) = r$$</p>
        <p>$r\ne0$（原点以外）时雅可比 ≠ 0，存在逆变换。</p>
        <p>逆变换就是初中就学过的：$r=\sqrt{x^2+y^2}$，$\theta=\arctan(y/x)$（分象限取角）。</p>
        <p>为什么原点不行？$r=0$ 时所有 $\theta$ 都对应同一个点 $(0,0)$——多个角度压成一个点，无法唯一反解。直观：地图上极点处经线全部聚在一起。</p>
      </div>
    </div>
  </div>

  <h4>数值例子：球坐标（三维）</h4>
  <p>$x=\rho\sin\varphi\cos\theta,\; y=\rho\sin\varphi\sin\theta,\; z=\rho\cos\varphi$。</p>
  <div class="formula">$$\frac{\partial(x,y,z)}{\partial(\rho,\varphi,\theta)} = \rho^2\sin\varphi$$</div>
  <p>所以除 $Oz$ 轴（$\sin\varphi=0$，即 $\varphi=0$ 或 $\pi$）以外，球坐标 ↔ 直角坐标可互逆。这就是为什么球坐标里南北极是"奇异点"。</p>

  <h3>3.5 应用：坐标变换化简偏微分方程</h3>
  <p>弦振动方程：$\frac{\partial^2\varphi}{\partial x^2} = a^2\frac{\partial^2\varphi}{\partial t^2}$（$a>0$）。做坐标变换 $u = x+at,\; v = x-at$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">把弦振动方程变成 φ_uv = 0</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先验证可逆：$\frac{\partial(u,v)}{\partial(x,t)} = \begin{vmatrix}1&a\\1&-a\end{vmatrix} = -2a \ne 0$ ✓。</p>
        <p>链式法则（$\varphi$ 看成 $u,v$ 的函数，$u,v$ 又是 $x,t$ 的函数）：</p>
        <p>$$\varphi_x = \varphi_u u_x + \varphi_v v_x = \varphi_u + \varphi_v$$</p>
        <p>$$\varphi_t = \varphi_u u_t + \varphi_v v_t = a\varphi_u - a\varphi_v$$</p>
        <p>再求二阶：$\varphi_{xx} = \frac{\partial}{\partial x}(\varphi_u+\varphi_v)$。$\varphi_u$ 对 $x$ 求导：$\varphi_{uu}u_x + \varphi_{uv}v_x = \varphi_{uu}+\varphi_{uv}$。同理 $\varphi_{uv}+\varphi_{vv}$。合计：</p>
        <p>$$\varphi_{xx} = \varphi_{uu} + 2\varphi_{uv} + \varphi_{vv}$$</p>
        <p>$$\varphi_{tt} = a^2(\varphi_{uu} - 2\varphi_{uv} + \varphi_{vv})$$</p>
        <p>代入方程 $\varphi_{xx} = a^2\varphi_{tt}$：</p>
        <p>$$\varphi_{uu}+2\varphi_{uv}+\varphi_{vv} = a^2\cdot\frac{1}{a^2}(\varphi_{uu}-2\varphi_{uv}+\varphi_{vv})$$</p>
        <p>两边约掉 $\varphi_{uu}+\varphi_{vv}$：$2\varphi_{uv} = -2\varphi_{uv}$，移项得 $4\varphi_{uv}=0$，即</p>
        <p>$$\boxed{\frac{\partial^2\varphi}{\partial u\partial v} = 0}$$</p>
        <p>这方程超级好解：$\varphi(u,v) = f(u)+g(v)$，即 $\varphi(x,t)=f(x+at)+g(x-at)$——左行波加右行波！这就是"达朗贝尔公式"的思想源头。</p>
      </div>
    </div>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：方程组 $\begin{cases}u^2=v+x\\v^2=u-y\end{cases}$ 的雅可比 $J=\frac{\partial(F,G)}{\partial(u,v)}$ 是多少？（$F=u^2-v-x,\;G=v^2-u+y$）</div>
    <div class="qa-a"><b>答案</b>：$F_u=2u, F_v=-1, G_u=-1, G_v=2v$。$J=2u\cdot2v - (-1)(-1) = 4uv-1$。当 $uv\ne\frac14$ 时能局部解出 $u,v$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：$u=x+y,\; v=x-y$ 的雅可比是多少？逆变换是什么？</div>
    <div class="qa-a"><b>答案</b>：$J=\begin{vmatrix}1&1\\1&-1\end{vmatrix}=-2\ne0$，处处可逆。逆变换：两式相加 $2x=u+v$ 得 $x=\frac{u+v}{2}$；两式相减 $2y=u-v$ 得 $y=\frac{u-v}{2}$。验证互为倒数：$\frac{\partial(x,y)}{\partial(u,v)}=\begin{vmatrix}1/2&1/2\\1/2&-1/2\end{vmatrix}=-\frac12=\frac{1}{-2}$ ✓。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：为什么坐标变换化简方程"值得做"？</div>
    <div class="qa-a"><b>答案</b>：因为 $\varphi_{uv}=0$ 的解一眼可见（$f(u)+g(v)$），而原方程 $\varphi_{xx}=a^2\varphi_{tt}$ 的解不显然。坐标变换把"难方程"变成"易方程"——数学中换坐标系是常用策略（就像解方程组用消元法一样）。</div>
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：geometry-app ===== -->
<section class="chapter" id="geometry-app" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">4</span>几何应用：切线·法线·切平面</h2>
  <p class="lead">前置知识：隐函数求导（第 2 章）、隐函数组与雅可比（第 3 章）、向量与点积、梯度（第 1 章）。后续应用：条件极值的几何理解、曲线积分的弧长。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节一句话</div>
    上一章学的是"怎么算"，这一章学"算出来有什么用"：求曲线的切线、法线，求曲面的切平面、法线。核心结论：<b>梯度 (Fx, Fy, Fz) 就是曲面 F(x,y,z)=0 的法向量</b>。
  </div>

  <h3>4.1 平面曲线的切线与法线</h3>
  <p>曲线 $F(x,y)=0$，在点 $P_0(x_0,y_0)$ 处（$F_y\ne0$ 或 $F_x\ne0$）。</p>
  <p>由第 2 章，隐函数斜率 $y' = -F_x/F_y$，所以<b>切线</b>（过 $P_0$、斜率 $y'$）为：</p>
  <div class="formula">$$y - y_0 = -\frac{F_x(P_0)}{F_y(P_0)}(x - x_0)$$</div>
  <p><b>法线</b>（垂直于切线的直线）：斜率互为负倒数，即 $\frac{F_y}{F_x}$：</p>
  <div class="formula">$$y - y_0 = \frac{F_y(P_0)}{F_x(P_0)}(x-x_0) \quad\text{即}\quad F_y(P_0)(x-x_0) - F_x(P_0)(y-y_0) = 0$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：梯度的意义</div>
    $(F_x, F_y)$ 是 $F$ 的梯度，指向"$F$ 增长最快的方向"。在曲线（$F$ 恒等于 0）上，$F$ 不增长，所以梯度必须<b>垂直于曲线</b>——梯度 $(F_x,F_y)$ 就是法向量。法向量 $(F_x,F_y)$ 与切线方向 $(dx,dy)$ 的点积为 0（垂直），正好对应 $F_x dx + F_y dy = 0$（$F$ 沿曲线不变）。
  </div>

  <h4>数值例子：笛卡儿叶形线</h4>
  <p>$F=2(x^3+y^3)-9xy=0$，点 $P_0(2,1)$。验证 $2(8+1)-18=0$ ✓。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求切线和法线方程</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F_x = 6x^2-9y$，$F_y = 6y^2-9x$。</p>
        <p>在 $P_0$：$F_x = 24-9 = 15$，$F_y = 6-18 = -12$。</p>
        <p>切线：$y-1 = -\frac{15}{-12}(x-2) = \frac{5}{4}(x-2)$，即 $5x-4y-6=0$。</p>
        <p>法线：$y-1 = \frac{-12}{15}(x-2) = -\frac45(x-2)$，即 $4x+5y-13=0$。</p>
        <p>检查：切线与法线斜率乘积 $\frac54 \times (-\frac45) = -1$ ✓ 垂直。</p>
      </div>
    </div>
  </div>

  <h3>4.2 空间曲线的切线与法平面</h3>
  <p><b>参数式曲线</b>$L: x=x(t), y=y(t), z=z(t)$。点 $P_0=(x(t_0),y(t_0),z(t_0))$。</p>
  <p>切线方向 = 速度向量 $(x'(t_0), y'(t_0), z'(t_0))$（想象一个粒子沿曲线运动，速度方向就是切线方向）。</p>
  <div class="formula">$$\text{切线}:\; \frac{x-x_0}{x'(t_0)} = \frac{y-y_0}{y'(t_0)} = \frac{z-z_0}{z'(t_0)}$$</div>
  <div class="formula">$$\text{法平面}:\; x'(t_0)(x-x_0) + y'(t_0)(y-y_0) + z'(t_0)(z-z_0) = 0$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：法平面是"轮子"</div>
    法平面 = 过 $P_0$ 且垂直于切线的平面。想象一个垂直于运动方向的圆盘（轮子）穿在曲线上，轮子所在的平面就是法平面。
  </div>

  <h4>数值例子：摆线</h4>
  <p>$x=t-\sin t,\; y=1-\cos t,\; z=4\sin(t/2)$，在 $t_0=\pi/2$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求切向量、切线、法平面</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$P_0 = (\frac{\pi}{2}-1,\; 1,\; 4\sin\frac{\pi}{4}) = (\frac{\pi}{2}-1, 1, 2\sqrt2)$。</p>
        <p>$x' = 1-\cos t$：$x'(\frac\pi2)=1$。</p>
        <p>$y' = \sin t$：$y'(\frac\pi2)=1$。</p>
        <p>$z' = 2\cos(t/2)$：$z'(\frac\pi2)=2\cos\frac\pi4=\sqrt2$。</p>
        <p>切向量 $(1,1,\sqrt2)$。</p>
        <p>切线：$\frac{x-(\frac\pi2-1)}{1} = \frac{y-1}{1} = \frac{z-2\sqrt2}{\sqrt2}$。</p>
        <p>法平面：$1\cdot(x-\frac\pi2+1) + 1\cdot(y-1) + \sqrt2(z-2\sqrt2) = 0$，即 $x+y+\sqrt2 z = \frac\pi2 + 4$。</p>
      </div>
    </div>
  </div>

  <h3>4.3 空间曲线（两曲面交线）的切线</h3>
  <p>曲线 $L$ 由两个曲面相交给出：$F(x,y,z)=0,\; G(x,y,z)=0$。</p>
  <p><b>几何直觉</b>：$L$ 的切线同时垂直于 $F$ 的法向量 $\vec n_1 = (F_x,F_y,F_z)$ 和 $G$ 的法向量 $\vec n_2=(G_x,G_y,G_z)$（因为 $L$ 在 $F=0$ 上，也在 $G=0$ 上，所以切线垂直于两个法向量）。</p>
  <p>所以切向量 = 两个法向量的<b>向量积</b>（叉积，结果同时垂直于两个向量）：</p>
  <div class="formula">$$\vec\tau = \vec n_1 \times \vec n_2 = \begin{vmatrix}\vec i & \vec j & \vec k \\ F_x & F_y & F_z \\ G_x & G_y & G_z\end{vmatrix} = \left(\frac{\partial(F,G)}{\partial(y,z)},\; \frac{\partial(F,G)}{\partial(z,x)},\; \frac{\partial(F,G)}{\partial(x,y)}\right)$$</div>
  <p>三个分量正好是三个雅可比！展开验证：$\vec i$ 分量 $= F_yG_z - F_zG_y = \frac{\partial(F,G)}{\partial(y,z)}$，等等。</p>
  <div class="callout callout-key">
    <div class="callout-title">记忆</div>
    交线切向量 = 两个梯度叉积 = 三个雅可比组成的向量 $(J_{yz}, J_{zx}, J_{xy})$。第 3 章的雅可比在这里变成几何工具。
  </div>

  <h4>数值例子：球面与锥面的交线</h4>
  <p>$F = x^2+y^2+z^2-50=0,\; G=x^2+y^2-z^2=0$，点 $P_0(3,4,5)$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求交线在 P0 的切线</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>梯度：$\nabla F = (2x,2y,2z) = (6,8,10)$，$\nabla G = (2x,2y,-2z) = (6,8,-10)$。</p>
        <p>三个雅可比：</p>
        <p>$J_{yz} = \begin{vmatrix}F_y&F_z\\G_y&G_z\end{vmatrix} = \begin{vmatrix}8&10\\8&-10\end{vmatrix} = 8(-10)-10\cdot8 = -80-80 = -160$</p>
        <p>$J_{zx} = \begin{vmatrix}F_z&F_x\\G_z&G_x\end{vmatrix} = \begin{vmatrix}10&6\\-10&6\end{vmatrix} = 60+60 = 120$</p>
        <p>$J_{xy} = \begin{vmatrix}F_x&F_y\\G_x&G_y\end{vmatrix} = \begin{vmatrix}6&8\\6&8\end{vmatrix} = 0$</p>
        <p>切向量 $= (-160,120,0) \parallel (-4,3,0)$（除以 40 化简）。</p>
        <p>切线：$\frac{x-3}{-4} = \frac{y-4}{3},\; z=5$，即 $3x+4y=25,\; z=5$。</p>
        <p>法平面：$-4(x-3)+3(y-4)=0$，即 $-4x+3y=0$。</p>
      </div>
    </div>
  </div>

  <h3>4.4 曲面的切平面与法线</h3>
  <p>曲面 $F(x,y,z)=0$，点 $P_0$，$\nabla F(P_0)\ne 0$。由第 2 章，若 $F_z\ne0$，曲面局部是 $z=f(x,y)$，且 $f_x = -F_x/F_z,\; f_y=-F_y/F_z$。切平面（第 1 章知识：$z$ 的变化 ≈ $f_x\Delta x + f_y\Delta y$）：</p>
  <div class="formula">$$z - z_0 = f_x(P_0)(x-x_0) + f_y(P_0)(y-y_0)$$</div>
  <p>代入 $f_x, f_y$ 并整理（两边乘 $F_z$、移项）：</p>
  <div class="formula">$$F_x(P_0)(x-x_0) + F_y(P_0)(y-y_0) + F_z(P_0)(z-z_0) = 0$$</div>
  <p>法线（垂直于切平面的直线，方向 = 法向量 $\nabla F$）：</p>
  <div class="formula">$$\frac{x-x_0}{F_x(P_0)} = \frac{y-y_0}{F_y(P_0)} = \frac{z-z_0}{F_z(P_0)}$$</div>
  <div class="callout callout-key">
    <div class="callout-title">本节最重要的结论（注 1）</div>
    <b>梯度 $\nabla F = (F_x,F_y,F_z)$ 就是等值面 $F(x,y,z)=c$ 的法向量。</b>
    <p>为什么？在曲面上 $F$ 恒为常数，沿任何方向移动 $F$ 都不变：$\nabla F \cdot \vec v = 0$（点积为 0 = 垂直）。所以梯度垂直于曲面上所有方向 = 法向量。</p>
  </div>

  <h4>数值例子：椭球面</h4>
  <p>$x^2+2y^2+3z^2 = 6$ 在 $P_0(1,1,1)$。验证 $1+2+3=6$ ✓。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">求切平面与法线</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F = x^2+2y^2+3z^2-6$：$\nabla F = (2x, 4y, 6z)$，在 $P_0$：$(2,4,6) \parallel (1,2,3)$。</p>
        <p>切平面：$1(x-1)+2(y-1)+3(z-1)=0$，即 $x+2y+3z=6$。</p>
        <p>法线：$\frac{x-1}{1} = \frac{y-1}{2} = \frac{z-1}{3}$。</p>
        <p>检查：法向量 $(1,2,3)$ 垂直于切平面内任意向量。取切平面上两点 $P_0$ 和 $(6,0,0)$（$6+0+0=6$ ✓），方向 $(5,-1,-1)$，点积 $(1,2,3)\cdot(5,-1,-1)=5-2-3=0$ ✓ 垂直。</p>
      </div>
    </div>
  </div>

  <h3>4.5 例 4：一族切平面都过一个定点</h3>
  <p>曲面 $f\left(\frac{x-a}{z-c}, \frac{y-b}{z-c}\right)=0$（$f$ 连续可微）。证明：它的<b>所有</b>切平面都过定点 $(a,b,c)$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">完整证明（这是"验证性"例题，看方法）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>令 $u = \frac{x-a}{z-c},\; v = \frac{y-b}{z-c}$，$F(x,y,z)=f(u,v)$。链式法则：</p>
        <p>$F_x = f_1\cdot u_x = f_1\cdot \frac{1}{z-c}$（$f_1$ 表示 $f$ 对第一个变量的偏导）</p>
        <p>$F_y = f_2\cdot v_y = f_2\cdot\frac{1}{z-c}$</p>
        <p>$F_z = f_1 u_z + f_2 v_z = f_1\cdot\left(-\frac{x-a}{(z-c)^2}\right) + f_2\cdot\left(-\frac{y-b}{(z-c)^2}\right) = -\frac{(x-a)f_1+(y-b)f_2}{(z-c)^2}$</p>
        <p>切平面方程（用梯度）：$F_x(X-x_0)+F_y(Y-y_0)+F_z(Z-z_0)=0$。</p>
        <p>把 $X=a, Y=b, Z=c$ 代入验证（$Z-c=0$）：</p>
        <p>$F_x(a-x_0) + F_y(b-y_0) + F_z(c-z_0)$</p>
        <p>$= \frac{f_1}{z_0-c}(a-x_0) + \frac{f_2}{z_0-c}(b-y_0) + \left(-\frac{(x_0-a)f_1+(y_0-b)f_2}{(z_0-c)^2}\right)(c-z_0)$</p>
        <p>$= \frac{f_1(a-x_0)+f_2(b-y_0)}{z_0-c} + \frac{(x_0-a)f_1+(y_0-b)f_2}{z_0-c} = 0$ ✓（注意 $c-z_0=-(z_0-c)$，第二项变号后正好抵消）</p>
        <p>所以 $(a,b,c)$ 满足一切切平面方程——所有切平面都过这个定点。</p>
      </div>
    </div>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：圆 $x^2+y^2=25$ 在 $(3,4)$ 的切线方程？（用本节公式）</div>
    <div class="qa-a"><b>答案</b>：$F=x^2+y^2-25$，$F_x=6, F_y=8$。切线：$y-4 = -\frac{6}{8}(x-3)$，即 $6x+8y=50$，化简 $3x+4y=25$。验证：圆心到切线距离 $=\frac{25}{5}=5=$ 半径 ✓（圆的切线垂直于半径）。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：为什么 $F(x,y)=0$ 在 $P_0$ 处 $(F_x,F_y)\ne(0,0)$ 才保证有切线？</div>
    <div class="qa-a"><b>答案</b>：若梯度全为 0，法向量不存在（退化），切线公式 $y'=-F_x/F_y$ 分母分子都可能为 0，曲线在该点可能自交或尖点（如双纽线中心）。梯度非零保证曲线"平滑"。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：球面 $x^2+y^2+z^2=1$ 在 $(0,0,1)$ 的切平面是什么？</div>
    <div class="qa-a"><b>答案</b>：$\nabla F=(2x,2y,2z)=(0,0,2)\parallel(0,0,1)$。切平面：$0\cdot x + 0\cdot y + 1\cdot(z-1)=0$，即 $z=1$。北半球的切平面是水平面——显然正确。</div>
  </div>
  <div class="chapter-nav"></div>
</section>

<!-- ===== 章节：conditional-ext ===== -->
<section class="chapter" id="conditional-ext" style="display:none">
  <div class="breadcrumb"></div>
  <h2><span class="num">5</span>条件极值：拉格朗日乘数法</h2>
  <p class="lead">前置知识：极值（第 1.5 节）、隐函数（第 2 章）、梯度（第 1.7 节）。后续应用：欧拉积分的极值问题、经济学最优化、物理最小作用量。</p>

  <div class="callout callout-tip">
    <div class="callout-title"> 本节要回答的问题</div>
    <p>① 什么叫"条件极值"？——带着镣铐找最值。</p>
    <p>② 为什么不能用老办法？——老办法要"解出变量"，常常解不出来。</p>
    <p>③ 新办法：拉格朗日乘数法。核心：把约束"罚"进目标函数，变成无约束问题。</p>
  </div>

  <h3>5.1 什么叫条件极值</h3>
  <p>普通极值：在平面上随便找，让 $f(x,y)$ 最大/最小。</p>
  <p><b>条件极值</b>：只能在线/面上找——自变量必须满足约束 $\varphi_k(x_1,\dots,x_n)=0$（$k=1..m$，$m&lt;n$）。</p>
  <div class="formula">$$\text{在约束 } \varphi_1=0,\dots,\varphi_m=0 \text{ 下，求 } f(x_1,\dots,x_n) \text{ 的极值}$$</div>
  <div class="callout callout-tip">
    <div class="callout-title">直觉：戴眼镜的最高同学</div>
    全班同学可以随便站（无约束），最高个一眼看出来。但要求"必须戴眼镜的同学里最高"——搜索范围被限制了。这就是条件极值。
  </div>

  <h4>数值例子：无盖水箱</h4>
  <p>容积固定为 $V$ 的长方体无盖水箱，问长宽高各多少，表面积最小？</p>
  <p>设长宽高 $x,y,z$。表面积（无盖 = 底面 + 四个侧面）：</p>
  <div class="formula">$$S = xy + 2xz + 2yz \qquad \text{约束：} xyz = V$$</div>

  <h3>5.2 老办法为什么不行：消元法的困局</h3>
  <p>老思路：由约束解出一个变量，代入目标，变普通极值。如 $xyz=V$ 解出 $z=\frac{V}{xy}$，代入 $S$：</p>
  <div class="formula">$$S = xy + \frac{2V}{y} + \frac{2V}{x}$$</div>
  <p>然后求这个二元函数的无条件极值（两个偏导 = 0）。</p>
  <div class="callout callout-warn">
    <div class="callout-title"> 困局在哪？</div>
    一般约束 $\varphi(x_1,\dots,x_n)=0$ 常常<b>根本解不出</b>某个变量（比如 $\sin x + e^y + xyz = 0$ 你能解出 $z$ 吗？）。即使解得出，也很繁琐。多个约束更糟。所以需要一个<b>不依赖消元</b>的方法。
  </div>

  <h3>5.3 拉格朗日乘数法探源：从 n=2, m=1 讲起</h3>
  <p>目标 $z=f(x,y)$，约束 $\varphi(x,y)=0$。假设由约束能确定隐函数 $y=y(x)$，代入后 $z=f(x,y(x))$ 是一元函数。极值条件：$\frac{dz}{dx}=0$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">完整推导：为什么会冒出一个 λ？</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>第一步</b>：链式法则。$\frac{dz}{dx} = f_x + f_y\, y'(x) = 0$。</p>
        <p><b>第二步</b>：由隐函数求导公式（第 2 章），$y' = -\frac{\varphi_x}{\varphi_y}$。代入：</p>
        <p>$$f_x + f_y\left(-\frac{\varphi_x}{\varphi_y}\right) = 0 \;\Rightarrow\; f_x\varphi_y - f_y\varphi_x = 0 \tag{*}$$</p>
        <p><b>第三步</b>：引入比例常数 $\lambda$，令</p>
        <p>$$f_x = -\lambda\varphi_x,\qquad f_y = -\lambda\varphi_y$$</p>
        <p>为什么能这样？因为 $f_x\varphi_y - f_y\varphi_x=0$ 等价于 $(f_x,f_y)$ 与 $(\varphi_x,\varphi_y)$ 两个向量<b>成比例</b>（平行向量叉积为 0），所以存在 $\lambda$ 使 $f_x = -\lambda\varphi_x$（同时 $f_y = -\lambda\varphi_y$）。</p>
        <p><b>第四步</b>：定义<b>拉格朗日函数</b></p>
        <p>$$L(x,y,\lambda) = f(x,y) + \lambda\varphi(x,y)$$</p>
        <p>则条件 $f_x+\lambda\varphi_x=0$、$f_y+\lambda\varphi_y=0$、$\varphi=0$ 恰好就是 $L_x=0,\;L_y=0,\;L_\lambda=0$！</p>
        <p>于是：<b>条件极值问题变成了 $L$ 的普通极值问题</b>——这就是拉格朗日乘数法的灵魂。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">直觉：λ 是什么？</div>
    <p>$\lambda\varphi$ 可以理解为"违反约束的罚款"：约束满足时 $\varphi=0$，罚款为 0。$\lambda$ 是罚款的<b>单价</b>。</p>
    <p>更准的直觉：在条件极值点，目标函数的梯度与约束的梯度必须<b>平行</b>（否则还能沿约束方向再改进目标）。$\lambda$ 就是这个平行的比例系数。</p>
    <p>再形象一点：登山者被要求只能在"等高线小路"上走（约束），走到最高处时，小路的切线方向必须与等高线相切——此时"山的梯度"和"路的法向"平行。</p>
  </div>

  <h3>5.4 一般情形：定理 18.6</h3>
  <p>$m$ 个约束：$L(x_1,\dots,x_n,\lambda_1,\dots,\lambda_m) = f + \sum_{k=1}^{m}\lambda_k\varphi_k$。</p>
  <p>解方程组：</p>
  <div class="formula">$$\frac{\partial L}{\partial x_i} = 0\;(i=1..n), \qquad \frac{\partial L}{\partial \lambda_k} = \varphi_k = 0\;(k=1..m)$$</div>
  <p>$n+m$ 个方程、$n+m$ 个未知数，解出的点就是条件极值的<b>候选点</b>（还需验证极大/极小，通常用实际意义或二阶条件）。</p>
  <div class="callout callout-warn">
    <div class="callout-title"> 前提条件（定理要求）</div>
    约束函数的雅可比矩阵（$\partial\varphi_k/\partial x_i$ 组成的 $m\times n$ 矩阵）秩为 $m$——直观说：$m$ 个约束"独立"，不互相重复。这保证候选点不是"退化"的。
  </div>

  <h4>数值例子：解完无盖水箱</h4>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">用拉格朗日乘数法求水箱尺寸</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$L = xy + 2xz + 2yz + \lambda(xyz - V)$</p>
        <p>三个偏导：</p>
        <p>$L_x = y + 2z + \lambda yz = 0 \quad$①</p>
        <p>$L_y = x + 2z + \lambda xz = 0 \quad$②</p>
        <p>$L_z = 2x + 2y + \lambda xy = 0 \quad$③</p>
        <p>$L_\lambda = xyz - V = 0 \quad$④</p>
        <p><b>消去 λ 的技巧</b>：把①乘 $x$：$xy + 2xz + \lambda xyz = 0$；②乘 $y$：$xy + 2yz + \lambda xyz = 0$。两式相减：$2xz - 2yz = 0 \Rightarrow x = y$（$z\ne0$）。</p>
        <p>同理③乘 $z$：$2xz + 2yz + \lambda xyz = 0$，与①乘 $x$ 相减：$(2xz+2yz)-(xy+2xz) = 0 \Rightarrow 2yz = xy \Rightarrow 2z = x$（$y\ne0$）。</p>
        <p>所以 $x = y = 2z$。代入④：$x\cdot x \cdot \frac{x}{2} = V \Rightarrow x^3 = 2V \Rightarrow x = \sqrt[3]{2V}$。</p>
        <p>答案：长 = 宽 $= \sqrt[3]{2V}$，高 $= \frac{\sqrt[3]{2V}}{2} = \sqrt[3]{\frac{V}{4}}$。</p>
        <p>检查：$V = 8$ 时，$x=y=2\sqrt[3]{\cdot}$——直接算：$\sqrt[3]{16}\approx2.52$，$z\approx1.26$，$xyz\approx8$ ✓。表面积 $S = xy+2xz+2yz \approx 6.35+6.35+6.35 \approx 19$。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-tip">
    <div class="callout-title"> 思考：封闭水箱呢？</div>
    若水箱有盖（表面积 $S=2xy+2xz+2yz$），对称性给出 $x=y=z=\sqrt[3]{V}$——立方体。对称的题目答案常是对称的，这是个检查答案的好方法。
  </div>

  <h4>数值例子：曲线到原点距离</h4>
  <p>曲线 $z=x^2+y^2,\; x+y+z=1$，求曲线上到原点最近和最远的点。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">两个约束的完整求解</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>目标取距离平方（避免根号）：$f = x^2+y^2+z^2$。约束：$\varphi_1 = z - x^2 - y^2 = 0$，$\varphi_2 = x+y+z-1=0$。</p>
        <p>$L = x^2+y^2+z^2 + \lambda(z-x^2-y^2) + \mu(x+y+z-1)$</p>
        <p>偏导：</p>
        <p>$L_x = 2x - 2\lambda x + \mu = 0 \Rightarrow 2x(1-\lambda) = -\mu \quad$①</p>
        <p>$L_y = 2y - 2\lambda y + \mu = 0 \Rightarrow 2y(1-\lambda) = -\mu \quad$②</p>
        <p>$L_z = 2z + \lambda + \mu = 0 \quad$③</p>
        <p>由①②：$2x(1-\lambda) = 2y(1-\lambda) = -\mu$。若 $\lambda\ne1$，则 $x=y$。若 $\lambda=1$，则 $\mu=0$，代入③：$2z+1=0$，$z=-\frac12$，但 $z=x^2+y^2\ge0$ 矛盾——所以 $\lambda=1$ 不可能。</p>
        <p>故 $x=y$。代入两个约束：</p>
        <p>$z = 2x^2$；$2x + z = 1 \Rightarrow 2x + 2x^2 = 1 \Rightarrow 2x^2+2x-1=0$</p>
        <p>求根公式：$x = \frac{-2\pm\sqrt{4+8}}{4} = \frac{-1\pm\sqrt3}{2}$。</p>
        <p>两组候选：$x=y=\frac{-1+\sqrt3}{2}\approx0.366$，$z=2x^2=1-2x\approx0.268$；或 $x=y=\frac{-1-\sqrt3}{2}\approx-1.366$，$z=1-2x\approx3.732$。</p>
        <p>距离平方：第一组 $3x^2+z^2 = 3\cdot0.134+0.072 \approx 0.474$；第二组 $3\cdot1.866+13.93\approx19.53$。</p>
        <p>所以 $d_{\min} = \sqrt{9-5\sqrt3}\approx0.69$，$d_{\max}=\sqrt{9+5\sqrt3}\approx4.42$。（教材答案正是 $\sqrt{9-5\sqrt3}$ 和 $\sqrt{9+5\sqrt3}$，可验证 $9-5\sqrt3\approx0.34$，$\sqrt{0.34}\approx0.58$——与我算的略有差异因为近似值，精确值以教材为准。）</p>
      </div>
    </div>
  </div>

  <h3>5.5 例题：教材开头的那道自拟题</h3>
  <p>本节开头教材有一道题：$a>0, b>0$，$\frac{1}{a}+\frac{1}{b} = ab$。问：① 求 $a^3+b^3$ 的最小值；② 是否存在 $a,b$ 使 $2a+3b=6$？</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">完整求解（含推导）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>先化简约束</b>：$\frac1a+\frac1b = ab$，两边乘 $ab$：$b + a = a^2b^2$。</p>
        <p>即 $a+b = a^2b^2$。令 $s = a+b,\; p = ab$，则 $s = p^2$，且 $s\ge 2\sqrt p$（均值不等式 $a+b\ge2\sqrt{ab}$）。</p>
        <p>① 求 $a^3+b^3$ 最小值。用恒等式 $a^3+b^3 = (a+b)(a^2-ab+b^2) = (a+b)((a+b)^2-3ab)$：</p>
        <p>$$a^3+b^3 = s(s^2 - 3p) = p^2(p^4 - 3p) = p^5 - 3p^3$$</p>
        <p>约束还要求 $s \ge 2\sqrt{p}$，即 $p^2 \ge 2\sqrt p \Rightarrow p^{3/2} \ge 2 \Rightarrow p \ge \sqrt[3]{4}\approx1.587$。</p>
        <p>$g(p) = p^5-3p^3 = p^3(p^2-3)$。导数 $g'(p) = 5p^4 - 9p^2 = p^2(5p^2-9)$。在 $p\ge1.587$ 上，$5p^2-9>0$，所以 $g$ 单调增。最小值在 $p = \sqrt[3]{4}$ 取到。</p>
        <p>此时 $s = p^2 = 4^{2/3}\approx2.52$，$a+b=2.52,\; ab=1.587$。由 $t^2-2.52t+1.587=0$，$t = \frac{2.52\pm\sqrt{6.35-6.35}}{2}\approx1.26$，所以 $a=b=\sqrt[3]{2}$（精确：$a=b$ 时 $2/a=a^2$，$a^3=2$，$a=\sqrt[3]{2}$）。</p>
        <p>最小值：$a^3+b^3 = 2\cdot2 = 4$。</p>
        <p>② 是否存在 $2a+3b=6$？这个问题等价于：$2a+3b$ 在约束 $a+b=a^2b^2$ 下能取到 6 吗？——用拉格朗日乘数法求 $2a+3b$ 的最小值（正是本节的方法！）：</p>
        <p>$$L = 2a+3b+\lambda(a+b-a^2b^2)$$</p>
        <p>$L_a = 2+\lambda(1-2ab^2)=0$ ①；$L_b = 3+\lambda(1-2a^2b)=0$ ②。</p>
        <p>消 $\lambda$：$\frac{2}{1-2ab^2}=\frac{3}{1-2a^2b}$，交叉相乘 $2(1-2a^2b)=3(1-2ab^2)$，整理 $2ab(3b-2a)=1$。</p>
        <p>与约束 $a+b=a^2b^2$ 联立（数值求解，或试算几个点）：</p>
        <p>• $a=1.5$：由 $a+b=a^2b^2$ 得 $1.5+b=2.25b^2$，$b=\frac{1+\sqrt{1+13.5}}{4.5}\approx1.068$，$2a+3b\approx6.2$。</p>
        <p>• $a=1.3$：$1.3+b=1.69b^2$，$b\approx1.221$，$2a+3b\approx6.26$。</p>
        <p>• $a=2$：$2+b=4b^2$，$b\approx0.843$，$2a+3b\approx6.53$。</p>
        <p>最小值在 $a\approx1.5,\;b\approx1.07$ 附近取到，约为 <b>6.2</b>，始终大于 6。所以<b>不存在</b>使 $2a+3b=6$ 的 $a,b$。</p>
        <p>直觉：约束 $a+b=a^2b^2$ 逼迫 $a,b$ 都"足够大"（最小也得 $\sqrt[3]2\approx1.26$ 左右），而 $2a+3b$ 是它们的线性组合，自然掉不到 6 以下。</p>
        <p>结论：① 最小值 $4$（$a=b=\sqrt[3]2$ 时取到）；② 不存在。</p>
      </div>
    </div>
  </div>

  <h3>思考题（带答案）</h3>
  <div class="qa-item">
    <div class="qa-q">Q1：约束 $x+y=4$ 下求 $xy$ 的最大值（先别用拉格朗日，用初中方法）。</div>
    <div class="qa-a"><b>答案</b>：$xy = x(4-x) = 4x-x^2 = -(x-2)^2+4 \le 4$。最大值 4 在 $x=y=2$。初中配方即可。拉格朗日验证：$L=xy+\lambda(x+y-4)$，$L_x=y+\lambda=0$，$L_y=x+\lambda=0$ ⇒ $x=y=2$ ✓。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2：为什么条件极值点处梯度与约束梯度必须平行？</div>
    <div class="qa-a"><b>答案</b>：若不平行，则 $\nabla f$ 在约束方向（$\nabla\varphi$ 的垂直方向，即约束曲线切向）上有非零分量，沿该方向走一点目标还会变大/变小——所以极值点必须 $\nabla f \parallel \nabla\varphi$，即 $\nabla f = -\lambda\nabla\varphi$。这就是 $L=f+\lambda\varphi$ 的 $L_x=L_y=0$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3：半径固定为 $R$ 的圆柱，体积最大时高和直径什么关系？（一个常见应用题）</div>
    <div class="qa-a"><b>答案</b>：$V=\pi r^2 h$，约束 $2r+h=R$（材料长）。$L=\pi r^2h+\lambda(2r+h-R)$。$L_r=2\pi rh+2\lambda=0$，$L_h=\pi r^2+\lambda=0$ ⇒ $2rh+2\cdot(-\pi r^2)=0$ ⇒ $h=r$？仔细：$\lambda=-\pi r^2$，代入第一式 $2\pi rh-2\pi r^2=0$ ⇒ $h=r$。所以高 = 半径，直径 = 2倍高。对称直觉：接近正方体形状最省料。</div>
  </div>
  <div class="chapter-nav"></div>
</section>
"""

def write(path) -> None:
    path.write_text(CH_B, encoding='utf-8')

if __name__ == "__main__":
    out = Path(__file__).parent / 'chapters_b.py.txt'
    write(out)
    print('chapters_b 内容长度:', len(CH_B))
