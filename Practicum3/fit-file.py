import numpy as np
from scipy.optimize import minimize, root_scalar
import matplotlib.pyplot as plt
from scipy.stats import chi2 as chi_2_sci

def X_sq(x, y, dy, dx=None):
    '''
    INFO: define model and parameters
    '''
    param_names = ['a', 'b']
    initial_guess = [1, 1, 1, 1]

    def model(params, x):
        #a, b, c, d = params
        #return a*np.sin(b*x) + c*x +d
        a, b = params
        return a*x + b
        
        
    '''
    INFO: def of X^2:
    '''
    def chi2(params, x, y, dy):
        return np.sum((y - model(params, x))**2/(dy**2))

    '''
    INFO: analyse
    '''
    print('---------START---------')
    if not initial_guess or len(initial_guess) != len(param_names):
        initial_guess = np.ones(len(param_names))
        print("WARN: No or invalid initial guess, all 1s were taken.\n-----------------------")
    else:
        initial_guess = np.array(initial_guess)

    # Minimize the chi-squared function to find the best-fit parameters
    optimised = minimize(chi2, initial_guess, args=(x, y, dy))
    X_min = optimised.fun
    params_opt = optimised.x
    for name, param_opt in zip(param_names, params_opt):
        print(f"Optimized {name}: {param_opt}")

    def plot_fit(x_val, y_val, dx, dy):
        model_x = np.linspace(0.9*np.min(x_val), 1.1*np.max(x_val), 120)
        model_y = np.array([])
        for x in model_x:
            model_y = np.array(list(model_y) + [model(params_opt, x)])
        fig, ax = plt.subplots(nrows=1, ncols=1, dpi=120, figsize=(5, 3))

        ax.errorbar(x_val, y_val, xerr=dx, yerr=dy, label="data",
                marker="o", markersize=4, fmt=" ", color="black", ecolor="black", capsize=2, capthick=0.6, linewidth=0.6)
        plt.plot(model_x, model_y)
        
        plt.tight_layout() ; plt.show()

    plot_fit(x, y, dx, dy)
    '''
    INFO: analysis of minimum:
    '''
    vaste_waarden = params_opt
    # Chi-squared threshold (68% confidence level)
    lijn_y = X_min + chi_2_sci.ppf(0.68, df=len(param_names))

    num_params = len(param_names)


    num_cols = 2
    num_rows = (num_params + num_cols - 1) // num_cols
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 5 * num_rows))
    axs = axs.flatten()

    # Iterate over each parameter to adjust one at a time
    for param, index in zip(param_names, range(len(param_names))):
        #print(f"-----Varying {param} while keeping others fixed-----")

        def single_var_model(var, i, params, x):
            # Adjust only the i-th parameter and return the model
            params[i] = var
            return model(params, x)

        def chi2_adjusted(var, i, params, x):
            # Compute chi-squared by varying one parameter
            chi2_val = np.sum((y - single_var_model(var, i, params.copy(), x)) ** 2 / (dy ** 2))
            return chi2_val

        # Define the function whose root we want to find (difference between chi^2 and lijn_y)
        def objective(var):
            params_copy = vaste_waarden.copy()
            chi2_val = chi2_adjusted(var, index, params_copy, x)
            return chi2_val - lijn_y

        # Define a helper function to find root by expanding the bracket
        def find_root_in_bracket(objective_func, initial_bracket, expand_limit=20):
            a, b = initial_bracket
            # Try to find the root in the initial bracket
            try:
                return root_scalar(objective_func, bracket=[a, b], method='brentq')
            except ValueError:
                # Expand the bracket if necessary
                for _ in range(expand_limit):
                    a -= 1  # Expand left
                    b += 1  # Expand right
                    try:
                        return root_scalar(objective_func, bracket=[a, b], method='brentq')
                    except ValueError:
                        continue
                raise ValueError("Could not find root after expanding the bracket")

        # Try to find the root (intersection point)
        try:
            sol_left = find_root_in_bracket(objective, [vaste_waarden[index] - 5, vaste_waarden[index]])
            sol_right = find_root_in_bracket(objective, [vaste_waarden[index], vaste_waarden[index] + 5])

            sigma_L = sol_left.root
            sigma_R = sol_right.root

            print(f"For parameter {param}: 68% CI =  [{sigma_L}, {sigma_R}] , center at {vaste_waarden[index]}")

            # Optional: Plot the chi-squared curve and intersection points
            chi_x = np.linspace(
                vaste_waarden[index] - 1.4*np.abs(vaste_waarden[index] - sigma_L),
                vaste_waarden[index] + 1.4*np.abs(vaste_waarden[index] - sigma_R),
                200)
            chi_y = np.array([chi2_adjusted(p, index, vaste_waarden.copy(), x) for p in chi_x])

            axs[index].plot(chi_x, chi_y, label=r"$\chi^2$" + f" curve for {param}")
            axs[index].axhline(y=lijn_y, color='black', linestyle='--', label=r"$\chi^2_{\text{min}}$")
            axs[index].scatter([sigma_L, sigma_R], [lijn_y, lijn_y], color='red', zorder=5, label='Intersections')
            
            # Set subplot labels and titles
            axs[index].set_xlabel(f'{param}')
            axs[index].set_ylabel(r'$\chi^2$')
            axs[index].set_title(f'Chi-squared Curve for {param}')
            axs[index].legend()


        except ValueError as e:
            print(f"Failed to find root for parameter {param}: {str(e)}")

    # Remove any unused subplots if num_params is odd
    for i in range(num_params, num_rows * num_cols):
        fig.delaxes(axs[i])
    plt.tight_layout()
    plt.show()
    print('----------END----------')


data = np.loadtxt("kirchhoff_demo.dat", delimiter=",").T
I, dI = data[0], data[1]
V, dV = data[2], data[3]
#X_sq(I, V, dV, dI) #NOTE: lineair
x = np.array([2.7925, 3.4907, 4.1888, 4.8869])
y = np.array([0.34, -0.29, -0.77, -1.03])
dx = np.array([0.02, 0.01, 0.01, 0.01])
dy = np.array([0.05, 0.04, 0.06, 0.05])
X_sq(x, y, dy, dx) #NOTE: sinus