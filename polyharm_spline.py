import math as m

class PolyHarmSpline(GenericRBF):
    def __call__(self, x):
        k=2
	r=m.sqrt(x[0]**2+x[1]**2+x[2]**2)
	if k%2==0
            return r**k*m.ln(r)     
	else
	    return r**k
    
    def plot(self, a=0, b=1):
        pass
