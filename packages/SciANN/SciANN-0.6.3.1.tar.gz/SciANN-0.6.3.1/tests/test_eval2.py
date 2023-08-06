import numpy as np 
import sciann as sn 

x = sn.Variable('x')
# y = sn.Variable('y')

f = sn.Functional('f', [x])

m = sn.SciModel([x], f)


x_data = np.linspace(0,1,100)
y_data = np.linspace(0,1,100)
t_data = np.linspace(0,1,100)

x_data, y_data, t_data = [x for x in np.meshgrid(x_data, y_data, t_data)]
input_data = [x_data]

print(isinstance(input_data, list))

f_pred = m.eval(input_data)
print(f_pred.shape)
print(isinstance(input_data, list))

f2_pred = f.eval(m, input_data)
print(f2_pred.shape)
print(isinstance(input_data, list))


