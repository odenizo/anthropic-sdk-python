# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .prompt_caching_beta_cache_control_ephemeral_param import PromptCachingBetaCacheControlEphemeralParam

__all__ = ["PromptCachingBetaTextBlockParam"]


class PromptCachingBetaTextBlockParam(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[PromptCachingBetaCacheControlEphemeralParam]