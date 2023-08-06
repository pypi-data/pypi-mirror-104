"""aidkit supports models with the following characteristics:

- Frameworks: Keras, scikit-learn
- Types: recurrent, feedforward
- Tasks: regression, multiregression, binary classification, multiclass \
    classification

You only need to configure and upload your model once and then you'll be able
to reuse it for future quality analyses (:ref:`example-configure-model`).
"""
from aidkitcli.core.utils import configure_model
from aidkitcli.core.stored_model import DataColumn
from aidkitcli.data_access.upload import upload_model, list_models
