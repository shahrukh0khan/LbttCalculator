# -----------------------------------------------------------
# calculates Land and building transaction tax - takes property's value as an arguement
# -----------------------------------------------------------


from functools import reduce
#from logging import raiseExceptions

class TaxBands:
    """Object to store higher and lower limits for a tax amount, its tax rate for the given range of limits, and calculate taxable amount."""
    
    def __init__(self, low, high, rate):
        self.low = low
        self.high = high
        self.rate = rate
        self.tax = (high - low) * rate

NON_TAXABLE_PRICE = 145000

def get_taxable_bands(property_value):
    """Helper function to extract required bounds only, based on the property value.
e.g. if property value is lower than any of the bounds, we do not need to include any bounds after that."""

    low_band = TaxBands(NON_TAXABLE_PRICE, 250000, 0.02)
    mid_band = TaxBands(low_band.high, 325000, 0.05)
    high_band = TaxBands(mid_band.high, 750000, 0.10)
    max_band = TaxBands(high_band.high, float('inf'), 0.12)

    bands = [low_band, mid_band, high_band, max_band]
    
    # extracts the required bounds and stores them in a list 
    # if lower limit of the current bound is less than propertyValue

    #-------------------------alternate
    # taxable_bands = [band for band in bands if band.low < property_value]

    taxable_bands = filter(lambda band: band.low < property_value, bands)

    return taxable_bands

def calculate_lbtt(property_value):
    """Returns Land and Building Transaction Tax with price of property as input."""

    # edge case if property value is lower than the taxable bound, no tax is incurred
    if property_value <= 145000: return 0

    taxable_bands = get_taxable_bands(property_value)

    tax_amount = reduce(lambda sum, band: sum + band.tax if band.high < property_value else sum + (property_value - band.low)*band.rate, taxable_bands, 0)
    
    #-------------------------alternate
    # tax_amount = 0
    # for bound in taxable_bands:
    #     tax_amount += bound.tax if property_value > bound.high else (property_value - bound.low)*bound.rate

    return round(tax_amount, 2)


if __name__ == '__main__':

    try:
        property_value = float(input("Please enter the purchase price of your property: £ ").replace(",", ""))
        property_value = round(property_value, 2)
        if property_value < 0: 
            print("Purchase price can not be negative.")
            raise ValueError
    except ValueError as err:
        print("Please enter the correct property purchase price.")
    else:
        tax = calculate_lbtt(property_value)
        print("LBTT incurred on property of value £", property_value, "is £", tax)
