import numpy as np
from scipy.optimize import minimize, root_scalar
import matplotlib.pyplot as plt
from scipy.stats import chi2 as chi_2_sci


def X_sq(data, param_names, initial_guess, model,
        root_attempts=None, PLOT=True, datafile=None,
        graf1_title=None, graf1_y_label=None, graf1_x_label=None
        ):
    """
    INFO: Processes input data to separate values and their associated errors.

    The input `data` is expected to be a tuple that contains two elements. Each element can either be:
    - A tuple containing two NumPy arrays: the first array represents the values, and the second array represents their associated errors.
    - A single NumPy array: in this case, the array represents the values, and the associated errors are assumed to be 1% of the associated value for all entries.

    The function extracts and assigns the appropriate arrays to the variables `x`, `dx`, `y`, and `dy`:
    - `x`: The first set of values.
    - `dx`: The errors associated with `x`. If no errors are provided, it defaults to an array of 1% of x of the same length as `x`.
    - `y`: The second set of values.
    - `dy`: The errors associated with `y`. If no errors are provided, it defaults to an array of 1% of y of the same length as `y`.

    Parameters:
    ----------
    data : tuple ((x, dx), (y, dy)) or (x, y)
        A tuple containing either:
        - Two NumPy arrays representing values and associated errors, respectively (for both `x` and `y`).
        - A single NumPy array representing values without any associated errors.

    Returns:
    -------
    tuple
        A tuple `(x, y, dx, dy)` where:
        - `x`: NumPy array representing the first set of values.
        - `dx`: NumPy array representing the errors for `x` (or 1% value if not provided).
        - `y`: NumPy array representing the second set of values.
        - `dy`: NumPy array representing the errors for `y` (or 1% value if not provided).
    """
    def process_data(data):
        x, dx, y ,dy = None, None, None, None

        if not isinstance(data, tuple) or len(data) != 2:
            raise ValueError("Input data must be a tuple of two elements (for x and y).")

        for i, element in enumerate(data):
            if isinstance(element, tuple):
                if len(element) != 2 or not all(isinstance(arr, np.ndarray) for arr in element):
                    raise ValueError(f"Element {i} in data must be a tuple of two NumPy arrays.")
                if i == 0:
                    x, dx = element
                    dx = np.abs(dx)
                elif i == 1:
                    y, dy = element
                    dy = np.abs(dy)
            elif isinstance(element, np.ndarray):
                if i == 0:
                    x = element
                    dx = np.abs(x*0.01)
                elif i == 1:
                    y = element
                    dy = np.abs(y*0.01)
            else:
                raise ValueError(f"Element {i} must be either a tuple of two NumPy arrays or a single NumPy array.")
            

        if x is None or y is None:
            raise ValueError("x and y values must be provided as NumPy arrays.")
        if len(x) != len(dx):
            raise ValueError("Length of x and dx must be the same.")
        if len(y) != len(dy):
            raise ValueError("Length of y and dy must be the same.")
        if len(x) != len(y):
            raise ValueError("Length of x and y must be the same.")
        
        return x, y, dx, dy
    

    def init(initial_guess, param_names):
        if not initial_guess or len(initial_guess) != len(param_names):
            initial_guess = np.ones(len(param_names))
            print("WARN: No or invalid initial guess, all 1s were taken.\n-----------------------")
        else:
            initial_guess = np.array(initial_guess)
        return initial_guess


    def chi2(params, x, y, dy):
        return np.sum((y - model(params, x))**2/(dy**2))


    def plot_fit(x_val, y_val, dx, dy, title, y_label, x_label):
        model_x = np.linspace(0.9*np.min(x_val), 1.1*np.max(x_val), 120)
        model_y = np.array([])
        for x in model_x:
            model_y = np.array(list(model_y) + [model(vaste_waarden, x)])
        fig, ax = plt.subplots(nrows=1, ncols=1, dpi=120, figsize=(5, 3))

        ax.errorbar(x_val, y_val, xerr=dx, yerr=dy, label="datapunten",
                marker="o", markersize=4, fmt=" ", color="black", ecolor="black", capsize=2, capthick=0.6, linewidth=0.6)
        plt.plot(model_x, model_y)

        if y_label:
            ax.set_ylabel(y_label)
        if x_label:
            ax.set_xlabel(x_label)
        if title:
            ax.set_title(title)
        ax.legend()  
        plt.tight_layout() ; plt.show()


    def optimise(optimise_output):
        return optimise_output, optimise_output.fun, optimise_output.x

    
    def init_fig():
        num_params = len(param_names)
        num_cols = 2
        num_rows = (num_params + num_cols - 1) // num_cols
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 5 * num_rows))
        axs = axs.flatten()
        return fig, axs, num_params, num_rows, num_cols
    

    def finish_fig(num_params_f, num_rows_f, num_cols_f):
        for i in range(num_params_f, num_rows_f * num_cols_f):
            fig.delaxes(axs[i])
        plt.tight_layout()
        plt.show()
        return fig, axs


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


    def add_subplot(axs, vaste_waarden, index, param, sigma_L, sigma_R, lijn_y, x):
        chi_x = np.linspace(
            vaste_waarden[index] - 1.4*np.abs(vaste_waarden[index] - sigma_L),
            vaste_waarden[index] + 1.4*np.abs(vaste_waarden[index] - sigma_R),
            200)
        chi_y = np.array([chi2_adjusted(p, index, vaste_waarden.copy(), x) for p in chi_x])

        axs[index].plot(chi_x, chi_y, label=r"$\chi^2$" + f" curve for {param}")
        axs[index].axhline(y=lijn_y, color='black', linestyle='--', label=r"$\chi^2_{\text{min}} + \text{ppf}(0.68)$")
        axs[index].scatter([sigma_L, sigma_R], [lijn_y, lijn_y], color='black', zorder=5, label='Intersections')
        axs[index].scatter([vaste_waarden[index]], [chi2_adjusted(vaste_waarden[index], index, vaste_waarden.copy(), x)],
            color='royalblue', zorder=5, label='mimimum')
        
        # Set subplot labels and titles
        axs[index].set_xlabel(f'{param}')
        axs[index].set_ylabel(r'$\chi^2$')
        axs[index].set_title(f'Chi-squared Curve for {param}')
        axs[index].legend()
        return axs

    # Define a helper function to find root by expanding the bracket
    def find_root_in_bracket(objective_func, initial_bracket, expand_limit, expand_amount, vaste_waarden, L=False, R=False):
        a, b = initial_bracket
        # Try to find the root in the initial bracket
        try:
            return root_scalar(objective_func, bracket=[a, b], method='brentq')
        except ValueError:
            # Expand the bracket if necessary
            for _ in range(expand_limit):
                if L:
                    a -= expand_amount
                elif R:
                    b += expand_amount
                try:
                    return root_scalar(objective_func, bracket=[a, b], method='brentq')
                except ValueError:
                    continue
            raise ValueError(f"Could not find root after expanding the bracket to [{a}, {b}]\nOptimised parameter was around {vaste_waarden[index]}")
            

    def find_sigmas(objective, vaste_waarden, index, root_attempts):
                if root_attempts:
                    root_attempts = root_attempts*10
                else:
                    root_attempts = 1000
                sol_left = find_root_in_bracket(objective, [vaste_waarden[index]*0.9, vaste_waarden[index]], root_attempts, vaste_waarden[index]*0.1, vaste_waarden, L=True)
                sol_right = find_root_in_bracket(objective, [vaste_waarden[index], vaste_waarden[index]*1.1], root_attempts, vaste_waarden[index]*0.1, vaste_waarden, R=True)
                return sol_left.root, sol_right.root
    

    '''
    INFO: EXECUTE!
    '''
    print('\n---------START--------------------------------------------------------------------------------------------------')
    if datafile:
        print(datafile)
        print('----------------------------------------------------------------------------------------------------------------')
    # INFO: calculate minimum
    x, y, dx, dy = process_data(data)
    initial_guess = init(initial_guess, param_names)
    optimised, X_min, vaste_waarden = optimise(minimize(chi2, initial_guess, args=(x, y, dy)))
    if PLOT:
        plot_fit(x, y, dx, dy, graf1_title, graf1_y_label, graf1_x_label)
    # INFO: analysis of minima
    lijn_y = X_min + chi_2_sci.ppf(0.68, df=len(param_names)) # Chi-squared threshold (68% confidence level)
    if PLOT:
        fig, axs, num_params, num_rows, num_cols = init_fig()
    
    for param, index in zip(param_names, range(len(param_names))):
        try:
            sigma_L, sigma_R = find_sigmas(objective, vaste_waarden, index, root_attempts)
            #print(f"For parameter {param}:\tMinimum at {vaste_waarden[index]} \t68% CI = [{sigma_L}, {sigma_R}]")
            print(f"For parameter {param:<8} :     Minimum at {vaste_waarden[index]:>16.8f}     ;     68% CI = [{sigma_L:>16.8f}, {sigma_R:>16.8f}]")
            if PLOT:
                add_subplot(axs, vaste_waarden, index, param, sigma_L, sigma_R, lijn_y, x)
        except ValueError as e:
            print(f"Failed to find root for parameter {param}: {str(e)}")
    if PLOT: 
        finish_fig(num_params, num_rows, num_cols)
    print('----------END---------------------------------------------------------------------------------------------------\n')


#NOTE: model setup
"""
    --------------
    INFO: Defines a mathematical model that takes input parameters and returns values based on the given data points `x`.
    --------------

        You can customize the model and its parameters to suit your specific equation by adjusting:
        - `param_names`: The list of parameter names corresponding to the model.
        - `initial_guess`: The initial guesses for the parameter values, which can be used for optimization.
        - The actual `model()` function itself to reflect your desired mathematical relationship.

        Parameters:
        -----------
        params : list or array-like
            A list or array containing the parameter values used in the model.
            
        x : array-like
            The independent variable, typically an array of values, where the model is evaluated.

        Returns:
        --------
        y : array-like
            The computed dependent variable values based on the model equation.

    --------------
    TODO: Customization:
    --------------
        1. **param_names**: Update this list to match the parameters used in your model equation.
        - Example: `param_names = ['a', 'b', 'c', 'd']` for a model with four parameters.

        2. **initial_guess**: Set the initial guesses for your parameters.
        - Example: `initial_guess = [1, 0.5, 2, -1]` for a four-parameter model.

        3. **model() function**: Modify the mathematical relationship within the `model()` function to match your desired model.
        - Example: For a model `y = a * sin(b * x) + c * x + d`, you would:
            - Update `param_names` to `['a', 'b', 'c', 'd']`
            - Modify the `model()` function to:
            ```python
            def model(params, x):
                a, b, c, d = params
                return a * np.sin(b * x) + c * x + d
            ```
    --------------
    NOTE: Example:
    --------------
        param_names = ['x0', 'gamma', 'A', 'y0']
        initial_guess = [0.1, 3, 1000, 100]
        def model(params, x):
            a, b, c, d = params
            return (c/np.pi)*(b/((x-a)**2 + b**2))+d
    """
param_names = ['x0', 'gamma', 'A', 'y0']
initial_guess = [0.01, 3, 900, 100]
def model(params, x):
    a, b, c, d = params
    return (c/np.pi)*(b/((x-a)**2 + b**2))+d

# NOTE: data load
#for i in range(20):
file = f"Datasets_fitopdracht/{4}.txt"
data = np.loadtxt(file).T
x = data[0]
y = data[1]
data = (x), (y ,np.sqrt(y))
# X_sq(data, param_names, initial_guess, model, PLOT=True, datafile=file)
X_sq(data, param_names, initial_guess, model,
        root_attempts=None, PLOT=True, datafile=file,
        graf1_title='testtitel', graf1_y_label='een y label', graf1_x_label='een x label'
        )