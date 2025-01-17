"""
tangible_assets.py
"""

from asset import Asset


class TangibleAsset(Asset):
    def __init__(self, name: str, life: int, value: float, s_value: float = 0.0):
        """
        :param name: The name of the asset.
        :param life: The life of the asset (months).
        :param value: The value of the asset ($).
        :param s_value: The salvage value of the asset ($).
        """
        super().__init__(name=name, life=life, value=value)
        self.S_VALUE = s_value

        self.depr_value = None
        self.rem_life = None
        self.prev_depr = 0

        self.define_asset()
    
    def define_asset(self) -> None:
        """
        Defines the asset or resets it to its original state.
        :return: Nothing.
        """
        self.value = self.DEF_VALUE
        # The depreciable value.
        self.depr_value = self.value - self.S_VALUE

        # The remaining life of the asset.
        self.rem_life = self.LIFE

    def depreciate(self, method: int, periods: int = 1) -> None:
        """
        [Supported Depreciation Methods] \n
        1: Straight Line Method \n
        2: Declining Balance Method \n
        3: Double Declining Balance Method \n
        4: Sum of the Years' Digits Method \n
        5: Units of Production Method \n
        It is recommended that you only use one type of depreciation method to avoid weird results.
        :param method: The depreciation method.
        :param periods: The number of periods (months) to depreciate.
        :return: Nothing.
        """
        if self.depr_value > 0:

            # Straight Line
            if method == 1:
                self.value -= periods * (self.depr_value / self.LIFE)
                self.rem_life -= periods

                self.depr_value = self.value - self.S_VALUE

            # Declining Balance
            elif method == 2:
                self.prev_depr = 2 * ((self.depr_value - self.prev_depr) / self.LIFE)
                self.value -= self.prev_depr

                self.depr_value = self.value - self.S_VALUE

            # Double Declining Balance
            elif method == 3:
                self.value -= (((self.DEF_VALUE - self.S_VALUE) / self.LIFE) * 2) * self.value

            # Sum of the Years' Digits
            elif method == 4:
                pass

            # Units of Production
            elif method == 5:
                pass

            else:
                print(f"{method} is not a valid option. Options for depreciation range from 1 - 5.")

        else:
            print(f"Asset \"{self.name}\" is fully depreciated! Current value = {self.value}.")


