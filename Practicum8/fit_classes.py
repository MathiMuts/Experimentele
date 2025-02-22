import numpy as np
from scipy.optimize import minimize as scipy_minimise
from scipy.optimize import root_scalar as scipy_root_scalar
from scipy.stats import chi2 as scipy_chi2
import matplotlib.pyplot as plt
import inspect

class Data:
    """
    Initialize the Data class.

    Parameters:
    - x (list or numpy.ndarray): Independent variable data points.
    - y (list or numpy.ndarray): Dependent variable data points.
    - dy (list, numpy.ndarray, or scalar): Errors in the dependent variable (y).
    - dx (list, numpy.ndarray, scalar, or None, optional): Errors in the independent variable (x). Defaults to None.
    - name (str, optional): Name of the dataset. Defaults to 'Dataset'.

    Raises:
    - ValueError: If input arrays have inconsistent lengths or invalid types.
    """
    def __init__(self, x, y, dy, dx=None, name='Dataset'):
        self.name = name
        self.x = np.array(x) if isinstance(x, list) else x
        self.y = np.array(y) if isinstance(y, list) else y
        self.dx = np.abs(np.array(dx) if isinstance(dx, list) else dx) if dx is not None else np.zeros_like(x)
        self.dy = np.abs(np.array(dy) if isinstance(dy, list) else dy)
        self._check_data()
                 
    def _check_data(self):
        for array in (self.x, self.y, self.dx, self.dy):
            if not isinstance(array, np.ndarray):
                raise ValueError(f"Input {array} must be a list or numpy array.")
        
        if len(self.x) != len(self.y) or len(self.x) != len(self.dx) or len(self.y) != len(self.dy):
            raise ValueError(f"The input arrays must have the same dimensions")

    def __str__(self):
        """
        Displays a string representation of the dataset, including its name and data points.

        Returns:
        - str: A formatted string showing the dataset name and its data points.
        """
        string = str(self.name) + ':\n'
        for x, y in zip(self.x, self.y):
            string += str(x) + '\t' + str(y) + '\n'
        return(string)
    
    def fit(self, model=None, initial_guess=None):
        """
        Perform a fit using the specified model.

        Parameters:
        - model (callable, optional): The model function to fit. If None, a default linear model is used.
        - initial_guess (list, numpy.ndarray, or None, optional): Initial parameter guesses. Defaults to ones.

        Returns:
        - Fit: A Fit object containing the fitting results and methods for further analysis.
        - The string method contains all the very usefull info.
        """
        return Fit(self, model, initial_guess)
    
    def show(self, data_color='black', size=4, title="Titel", data_label="data", x_label="x-label", y_label="y-label"):
        """
        Plot the dataset with error bars.

        Parameters:
        - data_color (str, optional): Color for the data points and error bars. Defaults to 'black'.
        - size (float, optional): Marker size for the data points. Defaults to 4.
        - title (str, optional): Title of the plot. Defaults to "Titel".
        - data_label (str, optional): Label for the dataset. Defaults to "data".
        - x_label (str, optional): Label for the x-axis. Defaults to "x-label".
        - y_label (str, optional): Label for the y-axis. Defaults to "y-label".
        """
        fig, ax = plt.subplots(nrows=1, ncols=1, dpi=120, figsize=(5, 3))
        ax.errorbar(self.x, self.y, xerr=self.dx, yerr=self.dy, label=data_label,
                marker="o", markersize=size, fmt=" ", color=data_color, ecolor=data_color, capsize=2, capthick=0.6, linewidth=0.6)
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.legend()
        plt.tight_layout()
        plt.show()
    
class Fit:
    """
    Initialize the Fit class.

    Parameters:
    - data (Data): A Data object containing the dataset to fit.
    - model (callable): The model function to use for the fit.
    - initial_guess (list, numpy.ndarray, or None, optional): Initial parameter guesses. Defaults to None.
    - root_attempts (int, optional): Maximum attempts to find roots for parameter uncertainties. Defaults to 100000.

    Raises:
    - ValueError: If the data or model are invalid, or if parameter count mismatches.
    """
    def __init__(self, data, model, initial_guess=None, root_attempts=100):
        self.data = data
        self.model = model if model else self._lineair_model
        self.root_attempts = root_attempts
        self.param_names = self._get_params()
        self.num_params = len(self._get_params())
        self.initial_guess = self._initial_guess_init(initial_guess)
        self.minima = self._minimise().x
        self.chi2 = self._minimise().fun
        self.minima_errors = self._minima_errors()
        self.minima_errors_R = [tup[0] for tup in self.minima_errors]
        self.minima_errors_L = [tup[1] for tup in self.minima_errors]
        self.chi2_red = self._chi2_red()
        self.p_value = self._p_value()
        self._check_data()
        self.init = None

    def _check_data(self):
        if not isinstance(self.data, Data):
            ValueError(f"data must be a data-class object")

        try:
            self.model(self.initial_guess, 1)
        except Exception as e:
            raise ValueError(
                "The amount of items in `param_names` does not match the number of parameters expected by the `model` function."
            ) from e
        
    def _lineair_model(self, params, x):
        A, B = params
        return A+B*x

    def _initial_guess_init(self, initial_guess):
        if initial_guess is None or len(initial_guess) != self.num_params:
            return np.ones(self.num_params)
        else:
            return np.array(initial_guess) if isinstance(initial_guess, list) else initial_guess

    def _get_params(self):
        source = inspect.getsource(self.model)
        for line in source.splitlines():
            if "params" in line and "=" in line:
                param_string = line.split("=")[0].strip()
                param_list = [var.strip() for var in param_string.split(",")]
                return param_list
        return None

    def _chi2(self, params):
        return np.sum((self.data.y - self.model(params, self.data.x))**2/(self.data.dy**2))
    
    def _minimise(self):
        return scipy_minimise(self._chi2, self.initial_guess)
    
    def show(self, data_color='black', model_color="royalblue", size=4, title="Titel", x_label="x-label", y_label="y-label", data_label="data", model_label="model", fit_guess=False):
        """
        Display the dataset and fitted model on a plot.

        Parameters:
        - data_color (str, optional): Color for the data points and error bars. Defaults to 'black'.
        - model_color (str, optional): Color for the fitted model line. Defaults to "royalblue".
        - size (float, optional): Marker size for the data points. Defaults to 4.
        - title (str, optional): Title of the plot. Defaults to "Titel".
        - x_label (str, optional): Label for the x-axis. Defaults to "x-label".
        - y_label (str, optional): Label for the y-axis. Defaults to "y-label".
        - data_label (str, optional): Label for the dataset. Defaults to "data".
        - model_label (str, optional): Label for the fitted model. Defaults to "model".
        """
        model_x = np.linspace(0.9*np.min(self.data.x), 1.1*np.max(self.data.x), 1200)
        model_y = self.model(self.minima, model_x)
        
        fig, ax = plt.subplots(nrows=1, ncols=1, dpi=120, figsize=(5, 3))
        ax.errorbar(self.data.x, self.data.y, xerr=self.data.dx, yerr=self.data.dy, label=data_label,
                marker="o", markersize=size, fmt=" ", color=data_color, ecolor=data_color, capsize=2, capthick=0.6, linewidth=0.6)
        plt.plot(model_x, model_y, label=model_label, color=model_color)
        if self.init and fit_guess:
            plt.plot(model_x, self.model(self.init, model_x), label="estimated_model", color="red")
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.legend()
        plt.tight_layout()
        plt.show()

    def _chi2_hypercontour(self):
        return self.chi2 + scipy_chi2.ppf(0.68, df=self.num_params)
    
    def _single_var_model(self, var, index):
        params_copy = self.minima.copy()
        params_copy[index] = var
        return self.model(params_copy, self.data.x)
    
    def _chi2_single_var(self, var, index):
        return np.sum((self.data.y - self._single_var_model(var, index)) ** 2 / (self.data.dy ** 2))
        
    def _analyse_single_var(self, var, index):
        return self._chi2_single_var(var, index) - self._chi2_hypercontour()
    
    def _find_root_in_bracket(self, objective_func, index, L=False, R=False):
        a = b = self.minima[index]
        for _ in range(self.root_attempts):
            if L:
                a -= self.minima[index]*0.1
            elif R:
                b += self.minima[index]*0.1
            try:
                return scipy_root_scalar(lambda var: objective_func(var, index), bracket=[a, b], method='brentq')
            except ValueError:
                continue
        raise ValueError(f"Roots were not found for parameter `{self.param_names[index]}` after expanding the bracket. Try expanding the bracket search by using `fit(root_attempts=10000000)`.")

    def _minima_errors(self):
        sigmas = []
        for param, index in zip(self.param_names, range(self.num_params)):
            try:
                sigma_left  = self._find_root_in_bracket(self._analyse_single_var, index, L=True).root
                sigma_right = self._find_root_in_bracket(self._analyse_single_var, index, R=True).root
                if sigma_left > sigma_right:
                    sigma_left, sigma_right = sigma_right, sigma_left
                sigmas.append( (np.abs(sigma_left - self.minima[index]), np.abs(sigma_right - self.minima[index])) )
            except Exception as e:
                raise ValueError(
                    f"Failed to find root for parameter: {param}"
                ) from e
        return sigmas
    
    def _chi2_red(self):
        x = self.data.x[:-1] if (len(self.data.x) == self.num_params) else self.data.x
        return self.chi2/(len(x)-self.num_params)
    
    def _p_value(self):
        x = self.data.x[:-1] if (len(self.data.x) == self.num_params) else self.data.x
        return scipy_chi2.sf(self.chi2, (len(x)-self.num_params))
    
    def show_chi2(self):
        """
        Display chi-squared curves for each parameter.

        The function plots the chi-squared distribution for each parameter against its value, including intersections and hypercontour levels.

        Raises:
        - ValueError: If roots for parameter uncertainties are not found within the bracket range.
        """
        num_params = self.num_params
        num_cols = 2 if self.num_params <= 8 else 3
        num_rows = (num_params + num_cols - 1) // num_cols
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 5 * num_rows))
        axs = axs.flatten()
        ###########
        for index in range(self.num_params):
            chi_x = np.linspace(
                 np.abs(self.minima[index] - 1.4*self.minima_errors_L[index]),
                 np.abs(self.minima[index] + 1.4*self.minima_errors_R[index]),
                200)
            chi_y = [self._chi2_single_var(val, index) for val in chi_x]

            axs[index].plot(chi_x, chi_y, label=r"$\chi^2$" + f" curve for {self.param_names[index]}")
            axs[index].axhline(y=self._chi2_hypercontour(), color='black', linestyle='--', label=r"$\chi^2_{min} + ppf(0.68)$")
            axs[index].scatter([self.minima[index] - self.minima_errors_L[index], self.minima[index] + self.minima_errors_R[index]], [self._chi2_hypercontour(), self._chi2_hypercontour()], color='black', zorder=5, label='Intersections')
            axs[index].scatter([self.minima[index]], [self._chi2_single_var(self.minima[index], index)],
                color='royalblue', zorder=5, label='mimimum')
            
            # Set subplot labels and titles
            axs[index].set_xlabel(f'{self.param_names[index]}')
            axs[index].set_ylabel(r'$\chi^2$')
            axs[index].set_title(f'Chi-squared Curve for {self.param_names[index]}')
            axs[index].legend()
        ###########
        for i in range(num_params, num_rows * num_cols):
            fig.delaxes(axs[i])
        plt.tight_layout()
        plt.show()

    def __str__(self):
        """
        Display a summary of the fit results.

        Returns:
        - str: A formatted string showing fit parameters, their uncertainties, χ² values, and p-value.
        """
        string='----------------------------------------------------------------------------------------------------------------\n'
        for param, index in zip(self.param_names, range(self.num_params)):
            # Check if the error bounds are symmetric (if the difference between upper and lower error bounds is less than 1% of the lower bound)
            # If the errors are symmetric, calculate the average of the left and right errors
            if self.minima_errors_R[index] - self.minima_errors_L[index] < 0.01 * self.minima_errors_L[index]:
                sigma = (self.minima_errors_L[index] + self.minima_errors_R[index])/2

                string += f"For parameter {param:<8} :     $ {self.minima[index]:>12.5f}" + ' \pm ' + f"{sigma:>12.5f} $"
            else:
                string += f"For parameter {param:<8} :     $ {self.minima[index]:>12.5f}" + "_{-" + f"{self.minima_errors_L[index]:>12.5f}" + "}^{+" + f"{self.minima_errors_R[index]:>10.5f}" + "} $"
                # If the errors are not symmetric, print them as separate upper and lower bounds in LaTeX format
            string += "\n"
        string += '----------------------------------------------------------------------------------------------------------------\n'
        string += f"Minimal χ² value       :     χ²_min     {self.chi2:>16.8f}\n"
        string += f"Reduced χ² value       :     χ²_red     {self.chi2_red:>16.8f}\n"
        string += f"P-value                :     p-value    {self.p_value:>16.8f}\n"
        string += '----------------------------------------------------------------------------------------------------------------\n'
        return string