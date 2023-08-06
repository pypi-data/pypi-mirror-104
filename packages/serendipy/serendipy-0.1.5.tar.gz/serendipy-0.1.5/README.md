This is a package of Bi-level optimization designed for `gurobi`

## How to Install

```bash
pip install serendipy
```

## How to Use

It can automatically write the KKT condition of the lower problem, for example:

```
min    f(x, y) 
s.t    g(x) >= 0 
       y = argmin  h(x, y) 
              s.t  u(x,y) >= 0
```

KKT condition is composed with **Complementary slackness**, **Primal feasibility**,**Dual feasibility**,and **Stationarity condition**, more  information about **`Karush–Kuhn–Tucker`** conditions can be found at https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions . 

we can get the first three conditions of lower problem simply as :

```python
from serendipy import Complementary_great, Complementary_equal, MyExpr, tonp, to_value
# build model
model = gurobi.Model()
Dual_expression = []
Dual_objective = []
# build lower objective and variables
lower_objective = xxx
all_lower_level_vars = [xxx]
# build lower constraints
expr = u(x, y)
dual_var = Complementary_great(expr, model, Dual_expression, Dual_objective, 'name')
```

> Note: the key function is `Complementary_great`, its similar pair is `Complementary_equal`, `Complementary_great` and its pair both have same signature. Take `Complementary_great` for example, the first parameter is `gurobi.Expr`, which denotes the Primal constraint, and the expression is expected to be greater than zero(`Complementary_equal` expect its expr to be equal to zero). The second parameter `gurobi.Model` denotes the model which the `expr` belongs to. The third parameter `Dual_expression` is a list, which collects the Lagrange term constraint by constraint. The forth parameter `Dual_objective` is a list, which collects the dual object constraint by constraint. The last parameter is the name of the constraint. After add all the constraints, `Dual_expression` contains all the constraint-related Lagrange terms, and  `Dual_objective`  contains all the dual objective terms.

> Note: In `Complementary_great`, the **Complementary slackness** is handled by the big M method. Specifically, 
>
> ```
> A E = 0
> ```
>
> is linearized as 
>
> ```
> A <= M * B 
> E <= M * (1-B)
> ```
>
> where B is a binary variable.

after add all the constraints, we can get the **Stationarity condition** through "automatic derivation"

```python
my_expr = MyExpr(Dual_expression + lower_objective)
for var in all_lower_level_vars:
    expr = my_expr.getCoeff(var)
    my_expr.addConstr(expr, model)
```

As the snippet shows, we first construct the Lagrange expression as  `my_expr` , then for all the lower level variables, we get the derivation through  `my_expr.getCoeff(var)` as `expr`, then we add `expr = 0` to `model` as the last line.

Now, we have got all the KKT conditions of lower problem, combined with the upper constraints and objective, we can solve the whole program !

## A complete example

Now let look at a complete example, the original example comes from  https://static1.squarespace.com/static/5492d7f4e4b00040889988bd/t/57c06dfdd482e91c235c418b/1472229009395/9_PyomoBilevel.pdf page 6:

```python
def example():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(lb=-1 * INF, ub= INF, name='y')

    lower_obj = y + 0
    DE = []
    Dobj = []
    expr1 = -3 + x + y
    expr2 = 0 + 2 * x - y
    expr3 = 12 - 2 * x - y
    expr4 = -4 + 3*x - 2 * y
    expr5 = y

    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')

    model.update()

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    # model.setParam("IntegralityFocus", 1)
    model.setObjective(x - 4 * y)
    model.optimize()
```

It has same result with the code written by `yalmip`, Cool🐒!

## Utility functions

Beside the KKT-related function, this package also provide three utility function as `tonp`,`to_value`,`to_value_np` , because the variables got from `model.addVars()` don't support slice as `numpy`, so `tonp` can convert a value of `gurobi.tuple_dict` to `numpy.narray` to support such slice, and `to_value` support convert a variable with type `gurobi.tuple_dict` to its value which is  stored as `numpy.narray`, `to_value_np` can convert a variable with type `gurobi.narray` to its value which is stored as `numpy.narray`.

Let's look at an example.

```bash
In [1]: import gurobipy as gurobi
In [2]: model = gurobi.Model()
In [3]: var33 = model.addVars(3,3)
In [4]: var33[:,1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-87bcf4f6f185> in <module>
----> 1 var33[:,1]
TypeError: unhashable type: 'slice'
```

In order to maintain compatibility with `numpy`, we can rewrite the code as :

```python
In [1]: model = gurobi.Model()
In [2]: var33 = tonp(model.addVars(3,3))
In [3]: var33[:,1]
Out[3]:
array([<gurobi.Var *Awaiting Model Update*>,
       <gurobi.Var *Awaiting Model Update*>,
       <gurobi.Var *Awaiting Model Update*>], dtype=object)
```

That all.



Maybe you will be curious about the name of this package `serendipy`, because I just write this package for one of my XUE MEI  `serendipity`👧 LOL!  God bless her to be admitted to her ideal university. 

