# -*- coding: utf-8 -*-


def effective_interest_rate(r, n):
    """
    Calculate the effective interest rate given the annual interest rate 
    and number of times during a year that the interest rate is added to the 
    principle amount.

    Parameters
    ----------
    r : float
        Yearly interest rate.
    n : integer
        Number of times that the interest rate is added during a year.

    Returns
    -------
    float
        Effective annual interest rate.

    """
    
    return (1 + r/n)**n - 1


# Print offer (i)
int_rate1 = 5.9
print(f'Offer (i): interest rate of {int_rate1:.2f}% paid quarterly')
eff_rate1 = effective_interest_rate(int_rate1/100, 4)
print(f'Effective interest rate is {100*eff_rate1:.2f}%\n')

# Print offer (ii)
int_rate2 = 6
print(f'Offer (ii): interest rate of {int_rate1:.2f}% paid twice a year')
eff_rate2 = effective_interest_rate(int_rate2/100, 2)
print(f'Effective interest rate is {100*eff_rate2:.2f}%\n')

# Print conclusion
if eff_rate1 > eff_rate2:
    print('Offer (i) is better than offer (ii)')
elif eff_rate1 < eff_rate2:
    print('Offer (ii) is better than offer (i)')
else:
    print('Offer (i) and (ii) are equally good')