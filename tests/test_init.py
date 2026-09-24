import pytest

import sae_lens


def test_accessing_HookedSAETransformer_without_HookedTransformer_raises_helpful_error(
    monkeypatch: pytest.MonkeyPatch,
):
    # transformer-lens >= 4.0 removed HookedTransformer, so HookedSAETransformer
    # isn't defined and module __getattr__ is used instead
    # hasattr() would call __getattr__, so remove the attribute via the module dict
    monkeypatch.delitem(vars(sae_lens), "HookedSAETransformer", raising=False)
    with pytest.raises(ImportError, match="Use SAETransformerBridge instead"):
        getattr(sae_lens, "HookedSAETransformer")  # noqa: B009


def test_accessing_unknown_attribute_raises_attribute_error():
    with pytest.raises(AttributeError):
        getattr(sae_lens, "not_a_real_attribute")  # noqa: B009
