"""Create a RequestModel to execute a CDC attack."""
from typing import List, Optional

from aidkitcli.core.analyses.cdc import cdc as request_factory
from aidkitcli.core.execute_analysis import execute_analysis
from aidkitcli.core.report import Report


def cdc(
        data: str,
        model: str,
        distance_weights: Optional[List[float]] = None,
        iteration_step: int = 10,
        target_category: int = 0,
        mask: List[int] = [],
        title: str = "Config CDC Attack",
) -> Report:
    """
    Execute a Coordinate Descent Classification attack that creates a
    perturbation per eligible data point in each file of the data set and
    returns a plot showing the performance of the model on the clean and
    the perturbed data. The Coordinate Descend Classification attack follows
    a black-box approach in that it does not use any gradient information.

    The perturbation is crafted to make the model classify the data point
    as the category given by target_category while minimizing the perturbation
    size. More specifically, the algorithm tries to keep the sum over the
    coordinates of the distance between the respective coordinate
    of the perturbed and the original data point small. If the nth feature
    is qualitative, the distance between the nth coordinate of a point x
    and a point x' is

    * 0 if x'[n] == x[n]
    * distance_weights[n] if x'[n] != x[n]

    Conversely, if the nth feature in quantitative, the distance between the
    nth coordinate of a point x and a point x' is calculated as

    distance_weights[n] * abs(x'[n] - x[n])

    The algorithm finds the point by estimating which coordinate should be
    changed to find the best point, and then changing the value of only this
    coordinate. It repeats this process until it cannot find a better point,
    but at most iteration_steps times.

    Currently, this attack strategy can be applied to classification models.
    The data set may consist of both quantitative and qualitative
    variables.

    :param data: name of the data set
    :param model: path to the configuration file (.toml file) that contains
        the metadata of the model
    :param distance_weights: array of weights to multiply the distance
        in each coordinate with. If set to None, reasonable default values are
        calculated depending on the value range for quantitative and the
        number of features for categorical features.
    :param iteration_step: number of iterations in the attack
    :param target_category: the target category this algorithm tries to get
        the points classified as
    :param mask: list of binary values that decide whether a variable can be
        perturbed by the attack, the list length must be the number of
        variables
    :param title: title of the configuration
    """
    request_model = request_factory(
        title=title,
        data=data,
        model=model,
        distance_weights=distance_weights,
        iteration_step=iteration_step,
        target_category=target_category,
        mask=mask,
    )
    return execute_analysis(request_model=request_model)
