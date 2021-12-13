""" -------------------------------------------------------------------------------------------------
    Expected Value
    -------------------------------------------------------------------------------------------------
    
    Source:  https://github.com/d-insight/code-bank.git 
    License: MIT License - https://opensource.org/licenses/MIT 
    
    Sections of code adapted from: https://matplotlib.org/gallery/widgets/slider_demo.html

    OVERVIEW:
    
    The following module executes much of the same illustration as the expected-value notebook, 
    but allows for interactive setting of the cost structure of False Positivea and False Negatives.

    -------------------------------------------------------------------------------------------------
"""

import numpy                 as np
import matplotlib.pyplot     as plt
from   matplotlib.widgets    import Slider, Button
import pandas                as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model    import LinearRegression

# =================

C_FN_0 = 4
C_FP_0 = 2

# =================

# load data
data = pd.read_csv('data/credit_data.csv')

# Select target
y = np.array(data['customer_default'])

# Select features
features = list(set(list(data.columns)) - set(['customer_default']))
X = data.loc[:, features]

# Divide data into a training set and a testing set using the train_test_split() function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1, stratify=y)

# Fit an OLS linear regression
ols_model = LinearRegression()
ols_model.fit(X_train, y_train)
y_hat_ols_prob = ols_model.predict(X_test)  # Precict the probability

# =================

# Initial graph
results = []
for i in range(1, 50):
    threshold = 0.02 * i
    y_hats = [int(v >= threshold) for v in y_hat_ols_prob]
    errors = []
    for r in zip(y_test, y_hats):
        actual_value = r[0]
        predicted_value = r[1]
        # Incorrect prediction
        if predicted_value != actual_value:

            # False positve
            if predicted_value:
                errors.append(C_FP_0)

            # False negative
            else:
                errors.append(C_FN_0)
        # Correct prediction
        else:
            errors.append(0)
    total_error = sum(errors)
    results.append((total_error, threshold))
optimal_p = sorted(results)[0][1]
optimal_acc = sorted(results)[0][0]

print('Optimal probability threshold = {} with costs = {}\n'.format(round(optimal_p, 4), round(optimal_acc, 4)))

# =================
# Plot initial graph
y, x = zip(*results)

fig, ax = plt.subplots(figsize = (7, 8))
plt.subplots_adjust(left=0.25, bottom=0.35)
ax.set_ylabel('Weighted Count of Error')
ax.set_xlabel('Probability Threshold')
l, = plt.plot(x, y, lw=2)
plt.grid()
ax.margins(x=0.1, y = 0.0001*max(y))

axcolor = 'white'
axFP = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axFN = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

c_fn = Slider(axFN, 'Costs False Negative', 1, 15.0, valinit=C_FN_0)
c_fp = Slider(axFP, 'Costs False Positive', 1, 10.0, valinit=C_FP_0)


def update(val):

    fn = c_fn.val
    fp = c_fp.val

    results = []
    for i in range(1, 50):
        threshold = 0.02 * i
        y_hats = [int(v >= threshold) for v in y_hat_ols_prob]
        errors = []
        for r in zip(y_test, y_hats):
            actual_value = r[0]
            predicted_value = r[1]
            # Incorrect prediction
            if predicted_value != actual_value:

                # False positve
                if predicted_value:
                    errors.append(fp)

                # False negative
                else:
                    errors.append(fn)
            # Correct prediction
            else:
                errors.append(0)
        total_error = sum(errors)
        results.append((total_error, threshold))
    optimal_p = sorted(results)[0][1]
    optimal_costs = sorted(results)[0][0]

    print('Optimal probability threshold = {} \twith costs = {}'.format(round(optimal_p, 4), round(optimal_costs, 1)))

    y, x = zip(*results)
    l.set_ydata(y)
    fig.canvas.draw_idle()


c_fp.on_changed(update)
c_fn.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    c_fp.reset()
    c_fn.reset()
button.on_clicked(reset)

plt.show()
