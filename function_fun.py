#Function assignment, week2

#function 0
def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

#function 1
def sq(x):
    """ output: sq returns square of input
         input x: a number (int or float)
    """
    return x*x

#function 2
def interp(low,hi,fraction):
    """ output: float that is 'fraction' of the way between low and hi
         input: low, high, fraction (all can be float or int)
    """
    return float(((hi-low)*fraction)+low)

#function 3
def checkends(s):
    """ output: True/False indicating if first digit in string s ==  last digit in string s
         input s: string
    """
    return s[0] == s[-1] 
  
#function 4
def flipside(f):
    """ output: half-inverted string
        input f: string of any length
    """
    if len(f)%2==0:
    	back_count=len(f)/2
    else:
    	back_count=len(f)/2+1

    return f[0:back_count]+f[-back_count-1:-1:-1]

#function 5
def flipside(convertFromSeconds(s)):
    """ output: list (L) of numbers, representing: days, hours, minutes, seconds
        input f: non-negative int
    """
    day=s/(24*60*60)
    hr=
    mins=
    sec=(s-(day*24*60*60)-(hr*60**2)-(mins*60))

    return [day, hr, mins, sec]