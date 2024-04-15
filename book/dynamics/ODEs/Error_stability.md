# Numerical error

In the previous section we have seen how to approximate a function using a Taylor series. In this section we will lear how to quantify the error introduced by this approximation.

Here we will still consider the model problem of a second-order ODE that satisfies the equation of motion.

$$ m\ddot{u}(t)+c\dot{u}(t)+ku(t)=F(t). $$

The Taylor expansion of solution $u$ and its time derivative $\dot{u}$ at a given time $t_{n+1}$ is

$$ u_{n+1}=u_n + \Delta t \dot{u}_n + \frac{\Delta t^2}{2}\ddot{u}_n + \frac{\Delta t^3}{3!}\dddot{u}_n+\ldots, $$

$$ \dot{u}_{n+1}=dot{u}_n + \Delta t \ddot{u}_n + \frac{\Delta t^2}{2}\dddot{u}_n + \ldots. $$

If we truncate the series keeping the terms involving quantities that we know, that is $u_n$, $\dot{u}_n$ and $\ddot{u}_n$, we have the approximated solution:

$$ u_{n+1} ≈ \tilde{u}_{n+1} = u_n + \Delta t \dot{u}_n + \frac{\Delta t^2}{2}\ddot{u}_n, $$

$$ \dot{u}_{n+1} \approx \dot{\tilde{u}}_{n+1} = \dot{u}_n + \Delta t \ddot{u}_n. $$

The error of the approximated solution $\tilde{u}$ and its time derivative $\dot{\tilde{u}}$ at $t_{n+1}$ are defined as $\epsilon_u = \left|u_{n+1}-\tilde{u}_{n+1}\right|$ and $\epsilon_{\dot{u}} = \left|\dot{u}_{n+1}-\dot{\tilde{u}}_{n+1}\right|$. That is

$$\epsilon_u = \left|\frac{\Delta t^3}{3!}\dddot{u}_n+\ldots\right|\sim\mathcal{O}(\Delta t^3)$$

$$\epsilon_{\dot{u}} = \left|\frac{\Delta t^2}{2}\dddot{u}_n + \ldots\right|\sim\mathcal{O}(\Delta t^2)$$

Note that the error is reduced, i.e. the solution converges, as $\Delta t$ decreases. We say that the solution converges with a convergence rate (order) $r$ if $\epsilon\sim\mathcal{O}(\Delta t^r)$. Therefore the approximated solution has an error at each time step of order $3$ and its time derivative of order $2$.

Both errors, $\epsilon_u$ and $\epsilon_{\dot{u}}$, are added together when evaluating the acceleration (second derivative). Then

$$\ddot{u}_n = \frac{1}{m}\left(F_n-c\dot{u}_n-ku_n\right) = \frac{1}{m}\left(F_n-c(\dot{\tilde{u}}_n+\epsilon_{\dot{u}})-k(\tilde{u}_n+\epsilon_{u})\right)\sim\mathcal{O}(\Delta t^2 + \Delta t^3)\sim\mathcal{O}(\Delta t^2).$$

Therefore, the error in the acceleration will be governed by the error on the velocity, wich is second order. In that case, we can also define the approximation of the solution $\tilde{u}$ in a way that results in a second order local truncation error:

$$\begin{cases}
\tilde{u}_{n+1}= u_n + \Delta t\dot{u}_n\\ 
\dot{\tilde{u}}_{n+1}= \dot{u}_n + \Delta t\ddot{u}_n
\end{cases}$$

## The Forward-Euler method

The previous system can be re-arranged in vector notation, using $\mathbf{q}=\left[u,\dot{u}\right]^T$, as follows

$$\tilde{\mathbf{q}}_{n+1}=\mathbf{q}_n + \Delta t\dot{\mathbf{q}}.$$

This is precisely what is called as the Forward Euler method. 

```{prf:algorithm} Forward-Euler method
:label: alg-forward_euler

**Input:** 
- solution at $t_n$ ($\mathbf{q}_n$)
- solution time derivative at $t_n$ ($\dot{\mathbf{q}}_n$)
- Time step size $\Delta t$

**Output:** solution at $t_{n+1}$ ($\mathbf{q}_{n+1}$)

$$\mathbf{q}_{n+1} = \mathbf{q}_{n} + \Delta t\dot{\mathbf{q}}_{n}$$
```

For a practical implementation of the Forward-Euler method, you can follow [Tutorial 1.1](w1_t1.ipynb).

## Local and global truncation error

The Forward-Euler method has a local truncation error with a quadratic order of convergence ($\mathcal{𝑂}(\Delta 𝑡^2)$).

The global error of convergence is the error at the final step, which will have all the local step error accumulation. For a solution from $𝑡=[0,𝑇]$ with $𝑁$ time steps, i.e. $\Delta 𝑡=𝑇/𝑁$, we have that the total error will be:

$$\epsilon(𝑇)=\sum_{𝑖=1}^𝑁 \epsilon_𝐿 \sim 𝑁\epsilon_𝐿 = \frac{𝑇}{\Delta 𝑡}\epsilon_𝐿 \sim \frac{1}{Δ𝑡}\mathcal{𝑂}(\Delta 𝑡^2) \sim \mathcal{O}(\Delta 𝑡)$$

Then, the global error of the Forward-Euler method is of order 1, $\mathcal{O}(\Delta 𝑡)$.

# Stability

Numerical stability deals with the impact of approximation errors introduced in simplifying a differential equation (in our case). A numerical method (or a solver) is stable if it does not magnify these truncation errors unboundedly as the computation proceeds. Mathematically, numerical stability can be defined with the following example.

Consider the Cauchy differential equation again:

$$y' = f(t,y)$$

that is being solved using finite time steps. The solution at the time-step $n + 1$ is approximated as $y_{n+1}$ as a function of the solution $y_n$ that was obtained at the time-step $n$ using the step size $h$.

$$y_{n+1} = F(t_n, y_n, h)$$

In the equation above, $F$ is the discretized form of the continuous equation $f$. The approximation is numerically stable if, for any initial condition $y_0$ and any time step size $h$, the error between the numerical solution and the true solution remains bounded as $n$ (the number of time steps) increases. In formal terms, there exists a real number $C$, independent of $n$, such that:

$$|y_n - y(t_n)| \leq C$$

Let’s consider a simple example. For $y(0) = 1$, the equation

$$y' = -\alpha y \quad (\text{where } \alpha > 0)$$

has the solution

$$y(t) = e^{-\alpha t}$$