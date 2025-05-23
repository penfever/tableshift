from rtdl_revisiting_models import FTTransformer
import torch


def get_optimizer(estimator: torch.nn.Module,
                  config) -> torch.optim.Optimizer:
    optimizer = (
        estimator.make_default_optimizer()
        if isinstance(estimator, FTTransformer)
        else torch.optim.AdamW(estimator.parameters(), lr=config["lr"],
                               weight_decay=config["weight_decay"])
    )
    return optimizer
