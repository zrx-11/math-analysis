# 速查表（上册）

## 极限

| 场景 | 内容 |
|---|---|
| ε-N 定义 | 任给 ε>0，存在 N，n>N 时 \|a_n-a\|<ε |
| ε-δ 定义 | 任给 ε>0，存在 δ，0<\|x-x0\|<δ 时 \|f(x)-A\|<ε |
| 两个重要极限 | $\lim_{x\to0}\frac{\sin x}{x}=1$，$\lim_{x\to0}(1+x)^{1/x}=e$ |
| 等价无穷小 | $x\sim\sin x\sim\tan x$，$1-\cos x\sim\frac{x^2}{2}$，$\ln(1+x)\sim x$ |
| 常见极限 | $\lim_{x\to\infty}(1+\frac{a}{x})^x=e^a$，$\lim_{x\to0}\frac{a^x-1}{x}=\ln a$ |

## 导数

| 函数 | 导数 |
|---|---|
| $x^\alpha$ | $\alpha x^{\alpha-1}$ |
| $\sin x,\cos x$ | $\cos x,-\sin x$ |
| $e^x,a^x$ | $e^x,a^x\ln a$ |
| $\ln x$ | $1/x$ |
| $\arctan x,\arcsin x$ | $\frac{1}{1+x^2},\frac{1}{\sqrt{1-x^2}}$ |
| 参变量 | $\frac{dy}{dx}=\frac{\psi'(t)}{\varphi'(t)}$ |
| 微分 | $dy=f'(x)dx$ |

## 中值定理与泰勒

| 定理 | 结论 |
|---|---|
| 罗尔 | $f(a)=f(b)$ 时存在 $\xi$，$f'(\xi)=0$ |
| 拉格朗日 | $f(b)-f(a)=f'(\xi)(b-a)$ |
| 柯西 | 两函数差分之比等于导数之比 |
| 泰勒（佩亚诺） | $R_n=o((x-x_0)^n)$ |
| 泰勒（拉格朗日） | $R_n=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$ |

## 积分

| 场景 | 内容 |
|---|---|
| 换元 | $\int f(\varphi(x))\varphi'(x)dx=\int f(u)du$ |
| 分部 | $\int u\,dv=uv-\int v\,du$ |
| 变限求导 | $\frac{d}{dx}\int_a^{\varphi(x)}f(t)dt=f(\varphi(x))\varphi'(x)$ |
| 牛顿-莱布尼茨 | $\int_a^b f=F(b)-F(a)$ |
| 极坐标面积 | $\frac12\int r^2d\theta$ |
| 旋转体体积 | $\pi\int f^2dx$（绕 x 轴） |
| 弧长 | $\int\sqrt{1+y'^2}dx$ |

## 反常积分敛散

| 积分 | 条件 |
|---|---|
| $\int_1^\infty x^{-p}dx$ | $p>1$ 收敛 |
| $\int_0^1 x^{-p}dx$ | $p<1$ 收敛 |
| $\int_1^\infty\frac{dx}{x\ln^q x}$ | $q>1$ 收敛 |
| $\int_1^\infty\frac{\sin x}{x}dx$ | 条件收敛 |
