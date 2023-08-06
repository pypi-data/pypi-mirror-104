"""Create a RequestModel to execute a Relative Constant corruption."""

from aidkitcli.core.analyses.relative_constant import relative_constant as request_factory
from aidkitcli.core.execute_analysis import execute_analysis
from aidkitcli.core.report import Report


def relative_constant(data: str,
                      model: str,
                      variable_name: str,
                      relative_constant: float,
                      start_index: int = 0,
                      perturbation_length: int = 100000,
                      title: str = "Config Relative Constant Corruption"
                      ) -> Report:
    """
    Execute a Relative Constant Corruption and return a plot showing the
    performance of the model on the corrupted data.

    The values of the selected variable are increased or decreased by a
    constant value relative_constant.

    This corruption can only be applied to quantitative input variables. The
    supported ML models are:

    - Keras regression recurrent models
    - Keras classification feedforward models
    - scikit-learn classification feedforward models

    :param data: name of the data set
    :param model: path to the configuration file (.toml file) that contains
        the metadata of the model
    :param variable_name: name of the variable to corrupt
    :param relative_constant: constant value added to the original data
    :param start_index: data points before this index will not be perturbed
    :param perturbation_length: number of data points perturbed
    :param title: title of the configuration (default: "Config Relative
        Constant Corruption")
    """
    request_model = request_factory(
        title=title,
        data=data,
        model=model,
        variable_name=variable_name,
        relative_constant=relative_constant,
        start_index=start_index,
        perturbation_length=perturbation_length,
    )
    return execute_analysis(request_model=request_model)
