"""Simplified split-apply-combine paradigm on dataframes for internal use."""
from __future__ import annotations
from typing import cast, Iterable
import pandas as pd
from seaborn._core.rules import categorical_order
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable
    from pandas import DataFrame, MultiIndex, Index

class GroupBy:
    """
    Interface for Pandas GroupBy operations allowing specified group order.

    Writing our own class to do this has a few advantages:
    - It constrains the interface between Plot and Stat/Move objects
    - It allows control over the row order of the GroupBy result, which is
      important when using in the context of some Move operations (dodge, stack, ...)
    - It simplifies some complexities regarding the return type and Index contents
      one encounters with Pandas, especially for DataFrame -> DataFrame applies
    - It increases future flexibility regarding alternate DataFrame libraries

    """

    def __init__(self, order: list[str] | dict[str, list | None]):
        """
        Initialize the GroupBy from grouping variables and optional level orders.

        Parameters
        ----------
        order
            List of variable names or dict mapping names to desired level orders.
            Level order values can be None to use default ordering rules. The
            variables can include names that are not expected to appear in the
            data; these will be dropped before the groups are defined.

        """
        if not order:
            raise ValueError('GroupBy requires at least one grouping variable')
        if isinstance(order, list):
            order = {k: None for k in order}
        self.order = order

    def _get_groups(self, data: DataFrame) -> tuple[str | list[str], Index | MultiIndex]:
        """Return index with Cartesian product of ordered grouping variable levels."""
        pass

    def _reorder_columns(self, res, data):
        """Reorder result columns to match original order with new columns appended."""
        pass

    def agg(self, data: DataFrame, *args, **kwargs) -> DataFrame:
        """
        Reduce each group to a single row in the output.

        The output will have a row for each unique combination of the grouping
        variable levels with null values for the aggregated variable(s) where
        those combinations do not appear in the dataset.

        """
        pass

    def apply(self, data: DataFrame, func: Callable[..., DataFrame], *args, **kwargs) -> DataFrame:
        """Apply a DataFrame -> DataFrame mapping to each group."""
        pass