# 速查表（下册）

## 级数与函数项级数

| 场景 | 内容 |
|---|---|
| 收敛必要条件 | $u_n\to0$ |
| p 级数 | $\sum n^{-p}$：$p>1$ 收敛 |
| 比值法 | $\lim u_{n+1}/u_n=q$：$q<1$ 收敛，$q>1$ 发散 |
| 根值法 | $\lim\sqrt[n]{u_n}=q$，判据同上 |
| 拉贝法 | $\lim n(u_n/u_{n+1}-1)=r$：$r>1$ 收敛 |
| 莱布尼茨 | $u_n$ 单调递减趋于 0，交错级数收敛 |
| M 判别法 | 通项被收敛的数项级数一致控制 |

## 幂级数与傅里叶

| 场景 | 内容 |
|---|---|
| 收敛半径 | $R=1/L$，$L=\lim\|a_{n+1}/a_n\|$ 或 $\lim\sqrt[n]{\|a_n\|}$ |
| 逐项求导 | 区间内部可，半径不变 |
| 泰勒展开 | $e^x$、$\sin x$、$\cos x$、$\ln(1+x)$、$(1+x)^\alpha$ |
| 傅里叶系数 | $a_n=\frac1\pi\int f\cos nx$，$b_n=\frac1\pi\int f\sin nx$ |
| 收敛定理 | 连续点收敛 $f$，间断点收敛左右平均 |

## 多元微分

| 场景 | 内容 |
|---|---|
| 全微分 | $dz=f_xdx+f_ydy$ |
| 链式 | $z_x=f_u u_x+f_v v_x$ |
| 方向导数 | $\nabla f\cdot\mathbf l$ |
| 隐函数 | $y'=-F_x/F_y$ |
| 极值 | 驻点 + 黑塞矩阵正定/负定 |

## 积分

| 场景 | 内容 |
|---|---|
| 格林 | $\oint Pdx+Qdy=\iint(Q_x-P_y)d\sigma$ |
| 高斯 | $\oiint=\iiint(P_x+Q_y+R_z)dV$ |
| 斯托克斯 | $\oint_\Gamma=\iint(\nabla\times F)\cdot n\,dS$ |
| 极坐标 | $dxdy=r\,drd\theta$ |
| 柱面 | $dV=r\,drd\theta dz$ |
| 球面 | $dV=\rho^2\sin\varphi\,d\rho d\varphi d\theta$ |
| 曲面面积 | $\iint\sqrt{1+z_x^2+z_y^2}d\sigma$ |
| Γ 函数 | $\Gamma(s+1)=s\Gamma(s)$，$\Gamma(1/2)=\sqrt\pi$ |
| B 函数 | $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$ |
