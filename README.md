
### Introduction

In this lesson, we'll get some more practice with partial derivatives.

### Breaking down multivariable functions

In our explanation of derivatives, we discussed how taking the derivative of multivariable functions is similar to taking the derivatives of a multivariable function like $f(x)$.  In the first section we'll work up to taking the partial derivative of the multilinear function $ f(x,y) = 3xy $.  Here's what the function looks like in a 3d graph.

![](./plot3xy.png)

Before we get there, let's first just first break this function down into it's equivalent of different slices, like we have done previously.  We'll do this by taking different slices of the function, stepping through various values of $y$. So instead of considering the entire function, $f(x, y) = 3xy $ we can think about the function $f(x, y)$ evaluated at various points, where $y = 1$, $y = 3$, $y = 6$, and $y = 9$.

Write out Python functions that return the values $f(x, y)$ for $f(x, 1)$, $f(x, 3)$, $f(x, 6)$, and $f(x, 9)$ for the function $f(x, y) = 3xy $.


```python
def three_x_y_at_one(x):
    return 3*x

def three_x_y_at_three(x):
    return 3*3*x

def three_x_y_at_six(x):
    return 3*6*x

def three_x_y_at_nine(x):
    return 3*9*x
```


```python
three_x_y_at_one(3) # 9
three_x_y_at_three(3)# 27
three_x_y_at_six(1) # 18
three_x_y_at_six(2) # 36
```




    36



Now that we have our functions written, we can write functions that provided an argument of `x_values`, return the associated `y_values` that our four functions return.  


```python
zero_to_ten = list(range(0, 11))
zero_to_four = list(range(0, 5))

def y_values_for_at_one(x_values):
    return list(map(lambda x_value: three_x_y_at_one(x_value), x_values))

def y_values_for_at_three(x_values):
    return list(map(lambda x_value: three_x_y_at_three(x_value), x_values))

def y_values_for_at_six(x_values):
    return list(map(lambda x_value: three_x_y_at_six(x_value), x_values))

def y_values_for_at_nine(x_values):
    return list(map(lambda x_value: three_x_y_at_nine(x_value), x_values))
```


```python
y_values_for_at_one(zero_to_four) # [0, 3, 6, 9, 12]
y_values_for_at_one(zero_to_ten) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

y_values_for_at_three(zero_to_four) # [0, 9, 18, 27, 36]
y_values_for_at_three(zero_to_ten) # [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]

y_values_for_at_six(zero_to_four) # [0, 18, 36, 54, 72]
y_values_for_at_six(zero_to_ten) # [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180]

y_values_for_at_nine(zero_to_four) # [0, 27, 54, 81, 108]
y_values_for_at_nine(zero_to_ten) #[0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270]
```




    [0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270]



Now we are ready to plot the function $f(x) = x $, $f(x) = 3x $, $f(x) = 6x $ and $f(x) = 9x $


```python
from graph import trace_values

y_at_one_trace = trace_values(zero_to_ten, y_values_for_at_one(zero_to_ten), mode = 'lines', name = 'f(x, y) at y=1')

y_at_three_trace = trace_values(zero_to_ten, y_values_for_at_three(zero_to_ten),  mode = 'lines',  name = 'f(x, y) at y=3')

y_at_six_trace = trace_values(zero_to_ten, y_values_for_at_six(zero_to_ten),  mode = 'lines', name = 'f(x, y) at y=6')

y_at_nine_trace = trace_values(zero_to_ten, y_values_for_at_nine(zero_to_ten),  mode = 'lines', name = 'f(x, y) at y=9')

```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



```python
import plotly
from plotly.graph_objs import Scatter, Layout
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

init_notebook_mode(connected=True)

fig_constants_lin_functions = {
    "data": [y_at_one_trace, y_at_three_trace, y_at_six_trace, y_at_nine_trace],
    "layout": Layout(title="constants with linear functions")
}
plotly.offline.iplot(fig_constants_lin_functions)
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="53e562ab-c5e3-4f83-918f-7823b81e93b5" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("53e562ab-c5e3-4f83-918f-7823b81e93b5", [{"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30], "mode": "line", "name": "f(x, y) at y=1", "text": []}, {"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90], "mode": "line", "name": "f(x, y) at y=3", "text": []}, {"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180], "mode": "line", "name": "f(x, y) at y=6", "text": []}, {"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270], "mode": "line", "name": "f(x, y) at y=9", "text": []}], {"title": "constants with linear functions"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


So as you can see, plotting our multivariable $f(x, y)$ at different values of $y$ above lines up conceptually to having one plot step through these values of $y$. 

![](./plot3xy.png)

### Evaluating the partial derivative

So in the above section, we saw how we can think of representing our multivariable functions as a function evaluated at different value of $y$.


```python
plotly.offline.iplot(fig_constants_lin_functions)
```


<div id="a1de7b62-97b5-46ce-8b15-8d57010b4106" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("a1de7b62-97b5-46ce-8b15-8d57010b4106", [{"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30], "mode": "line", "name": "f(x, y) at y=1", "text": []}, {"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90], "mode": "line", "name": "f(x, y) at y=3", "text": []}, {"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180], "mode": "line", "name": "f(x, y) at y=6", "text": []}, {"x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270], "mode": "line", "name": "f(x, y) at y=9", "text": []}], {"title": "constants with linear functions"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Now let's think of how to take the derivative of our $ \frac{\delta f}{\delta x} f(x, y)$ at values of $y$.  Knowing how to think about partial derivatives of multivarivable functions, what is $ \frac{\delta f}{\delta x} $ at the following values of $y$.


```python
def df_dx_when_y_equals_one():
    return 3
```


```python
def df_dx_when_y_equals_three():
    return 9
```


```python
def df_dx_when_y_equals_six():
    return 18
```


```python
def df_dx_when_y_equals_nine():
    return 27
```

So notice that there is a pattern here, in taking $ \frac{\delta f}{\delta x}$ for our function $f(x, y) = 3xy$.  Now write a function that calculates $ \frac{\delta f}{\delta x}$ for our function $f(x,y)$ at any provided $x$ and $y$ value. 


```python
def df_dx_3xy(x_value, y_value):
    return 3*y_value
```


```python
df_dx_3xy(2, 1) # 3
```




    3




```python
df_dx_3xy(2, 2) # 6
```




    6




```python
df_dx_3xy(5, 2) # 6
```




    6



So as you can see, our $y$ value influences the function, and from there it's a calculation of $\frac{\Delta f}{\Delta x}$, which in this case is constant.

## Using our partial derivative rule

Now let's consider the function $ f(x, y) = 4x^2y + 3x + y$.  Now soon we will want to take the derivative of this function with respect to $x$.  We know that in doing something like that, we will need to translate this function into code, and that when we do so, we will need to capture the exponent of any terms as well as.

Remember that the way we expressed a single variable function, $f(x)$ in Python was to represent the constant, and $x$ exponent for each term.  For example, the function $f(x) = 3x^2 + 2x$ can be represented as the following:


```python
three_x_squared_plus_two_x = [(3, 2), (2, 1)]
```

Now let's talk about representing our multivariable function $ f(x, y) =4x^2y + 3x + y$ in Python.  Instead of using a tuple with two elements, we'll use a tuple with three elements and with that third element the exponent related to the $y$ variable.  So our function $ f(x, y) = 4x^2y + 3x  + y$ looks like the following:


```python
four_x_squared_y_plus_three_x_plus_y = [(4, 2, 1), (3, 1, 0), (1, 0, 1)]
```

Let's get started by writing a function `multivariable_output_at` that takes in a multivariable function and returns the value $f(x, y)$ evaluated at a specific value of $x$ and $y$ for the function.


```python
def multivariable_output_at(list_of_terms, x_value, y_value):
    output = []
    for term in list_of_terms:
        constant = term[0]
        x_exponent = term[1]
        y_exponent = term[2]
        term_output = constant*x_value**x_exponent*y_value**y_exponent
        output.append(term_output)
    return sum(output)
```


```python
multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 1, 1) # 8
```




    8




```python
multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 2, 2) # 40
```




    40



Let's also try this with another function $g(x, y) = 2x^3y + 3yx + x $.


```python
two_x_cubed_y_plus_three_y_x_plus_x = [(2, 3, 1), (3, 1, 1), (1, 1, 0)]
```


```python
multivariable_output_at(two_x_cubed_y_plus_three_y_x_plus_x, 1, 1) # 6
```




    6




```python
multivariable_output_at(two_x_cubed_y_plus_three_y_x_plus_x, 2, 2) # 46
```




    46



So now we want to write a Python function that calculates $\frac{\delta f}{\delta x}$ of a multivariable function.  Let's start by writing a function that just calculates $\frac{\delta f}{\delta x}$ of a single term.


```python
def term_df_dx(term):
    constant = term[0]*term[1]
    exponent = term[1] - 1
    return (constant, exponent,term[2])
```


```python
four_x_squared_y = four_x_squared_y_plus_three_x_plus_y[0]
term_df_dx(four_x_squared_y)
# (8, 1, 1) 
```




    (8, 1, 1)



> This solution represents $8xy$


```python
y = four_x_squared_y_plus_three_x_plus_y[2]
term_df_dx(y) # (0, -1, 1)
```




    (0, -1, 1)



> This solution represents $0$, as the first element indicates we are multiplying the term by zero.

Now write a function that finds the derivative of all terms, $\frac{\delta f}{\delta x}$ of a function $f(x, y)$.


```python
def df_dx(list_of_terms):
    derivative_terms = list(map(lambda function_term: term_df_dx(function_term),list_of_terms))
    return list(filter(lambda derivative_term: derivative_term[0] > 0, derivative_terms))
```


```python
df_dx(four_x_squared_y_plus_three_x_plus_y)
```




    [(8, 1, 1), (3, 0, 0)]



Now that we have done this for $\frac{\delta f}{\delta x}$, lets work on taking the derivative $\frac{\delta f}{\delta y}$.  Once again, we can use as an example our function $ f(x, y) = 4x^2y + 3x + y$.  Let's start with writing the function `term_df_dy`, which takes the partial derivative $\frac{\delta f}{\delta y}$ of a single term.


```python
def term_df_dy(term):
    constant = term[0]*term[2]
    exponent = term[2] - 1
    return (constant, term[1], exponent)
```


```python
four_x_squared_y
```




    (4, 2, 1)




```python
term_df_dy(four_x_squared_y) # (4, 2, 0)
```




    (4, 2, 0)



> This represents that $\frac{\delta f}{\delta y}4x^2y = 4x^2$


```python
term_df_dy(y) # (1, 0, 0)
```




    (1, 0, 0)



> This represents that $\frac{\delta f}{\delta y}y = 1$


```python
three_x = four_x_squared_y_plus_three_x_plus_y[1]
term_df_dy(three_x) # (0, 1, -1)
```




    (0, 1, -1)



> This represents that $\frac{\delta f}{\delta y}3x = 0$

Now let's write a function `df_dy` that takes multiple terms and returns an list of tuples that represent the derivative of our multivariable function.  So here is our function: $ f(x, y) = 4x^2y + 3x + y$.


```python
four_x_squared_y_plus_three_x_plus_y
```




    [(4, 2, 1), (3, 1, 0), (1, 0, 1)]




```python
def df_dy(list_of_terms):
    derivative_terms = list(map(lambda function_term: term_df_dy(function_term),list_of_terms))
    return list(filter(lambda derivative_term: derivative_term[0] > 0, derivative_terms))
```


```python
df_dy(four_x_squared_y_plus_three_x_plus_y) # [(4, 2, 0), (1, 0, 0)]
```




    [(4, 2, 0), (1, 0, 0)]




```python
two_x_cubed_y_plus_three_y_x_plus_x = [(2, 3, 1), (3, 1, 1), (1, 1, 0)]
df_dy(two_x_cubed_y_plus_three_y_x_plus_x) # [(2, 3, 0), (3, 1, 0)]
```




    [(2, 3, 0), (3, 1, 0)]



Great job! Hopefully, now you understand a little more about multivariable functions and derivatives!


```python

```
