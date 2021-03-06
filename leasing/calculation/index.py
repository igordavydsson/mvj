from decimal import ROUND_HALF_UP, Decimal

from django.utils.translation import ugettext_lazy as _

from leasing.enums import IndexType

from .explanation import ExplanationItem


def int_floor(value, precision):
    return value // precision * precision


class IndexCalculation:
    def __init__(self, amount=None, index=None, index_type=None, precision=None, x_value=None, y_value=None):
        self.explanation_items = []
        self.amount = amount
        self.index = index
        self.index_type = index_type
        self.precision = precision
        self.x_value = x_value
        self.y_value = y_value

    def _add_ratio_explanation(self, ratio):
        ratio_explanation_item = ExplanationItem(subject={
            "subject_type": "ratio",
            "description": _("Ratio {ratio}").format(ratio=ratio),
        })
        self.explanation_items.append(ratio_explanation_item)

    def calculate_type_1_2_3_4(self, index_value, precision, base):
        ratio = Decimal(int_floor(index_value, precision) / base).quantize(Decimal('.01'))

        self._add_ratio_explanation(ratio)

        return ratio * self.amount

    def calculate_type_5_7(self, index_value, base):
        ratio = Decimal(index_value / base).quantize(Decimal('.01'))

        self._add_ratio_explanation(ratio)

        return ratio * self.amount

    def calculate_type_6(self, index_value, base):
        if index_value <= self.x_value:
            return self.calculate_type_6_v2(index_value, base)

        rounded_index = int_floor(index_value, 10)

        # Decimal.quantize(Decimal('.01'), rounding=ROUND_HALF_UP) is used to round to two decimals.
        # see https://docs.python.org/3/library/decimal.html
        if rounded_index < self.y_value:
            dividend = Decimal(self.x_value + (index_value - self.x_value) / 2).quantize(Decimal('.01'),
                                                                                         rounding=ROUND_HALF_UP)
            ratio = (dividend / 100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

            self._add_ratio_explanation(ratio)

            return ratio * self.amount
        else:
            dividend = Decimal(self.y_value - (self.y_value - self.x_value) / 2).quantize(Decimal('.01'),
                                                                                          rounding=ROUND_HALF_UP)
            ratio = (dividend / 100).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

            self._add_ratio_explanation(ratio)

            new_base_rent = (ratio * self.amount).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

            new_base_rent_explanation_item = ExplanationItem(subject={
                "subject_type": "new_base_rent",
                "description": _("New base rent"),
            }, amount=new_base_rent)
            self.explanation_items.append(new_base_rent_explanation_item)

            y_ratio = Decimal(rounded_index / self.y_value).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

            # TODO: Different name for this ratio
            self._add_ratio_explanation(y_ratio)

            return new_base_rent * y_ratio

    def calculate_type_6_v2(self, index_value, base):
        ratio = Decimal(int_floor(index_value, 10) / base).quantize(Decimal('.01'))

        self._add_ratio_explanation(ratio)

        return ratio * self.amount

    def calculate(self):
        if self.index.__class__ and self.index.__class__.__name__ == 'Index':
            index_value = self.index.number
        else:
            index_value = self.index

        if self.index_type == IndexType.TYPE_1:
            assert self.precision
            return self.calculate_type_1_2_3_4(index_value, self.precision, 50620)

        elif self.index_type == IndexType.TYPE_2:
            assert self.precision
            return self.calculate_type_1_2_3_4(index_value, self.precision, 4661)

        elif self.index_type == IndexType.TYPE_3:
            return self.calculate_type_1_2_3_4(index_value, 10, 418)

        elif self.index_type == IndexType.TYPE_4:
            return self.calculate_type_1_2_3_4(index_value, 20, 418)

        elif self.index_type == IndexType.TYPE_5:
            return self.calculate_type_5_7(index_value, 392)

        elif self.index_type == IndexType.TYPE_6:
            if not self.x_value or not self.y_value:
                return self.calculate_type_6_v2(index_value, 100)

            return self.calculate_type_6(index_value, 100)

        elif self.index_type == IndexType.TYPE_7:
            return self.calculate_type_5_7(index_value, 100)

        else:
            raise NotImplementedError('Cannot calculate index adjusted value for index type {}'.format(self.index_type))
