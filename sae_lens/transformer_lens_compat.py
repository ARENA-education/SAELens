"""Imports from transformer-lens whose location differs between supported versions."""

# transformer_lens.HookedTransformer re-exports HookedRootModule in every version
# before 4.0, while the top-level export only exists from mid-3.x onwards.
try:
    from transformer_lens.HookedTransformer import HookedRootModule
except ImportError:  # transformer-lens >= 4.0 removed the HookedTransformer module
    from transformer_lens import HookedRootModule  # type: ignore

try:
    from transformer_lens.utilities import (
        USE_DEFAULT_VALUE,
        get_tokens_with_bos_removed,
        lm_cross_entropy_loss,
    )
except ImportError:  # transformer-lens < 3.0 has these in transformer_lens.utils
    from transformer_lens.utils import (  # type: ignore
        USE_DEFAULT_VALUE,
        get_tokens_with_bos_removed,
        lm_cross_entropy_loss,
    )

__all__ = [
    "HookedRootModule",
    "USE_DEFAULT_VALUE",
    "get_tokens_with_bos_removed",
    "lm_cross_entropy_loss",
]
