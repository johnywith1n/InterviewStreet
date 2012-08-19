import sys

def getPrimeNumbers (upperBound):
    result = [True] * (upperBound + 1)
    primes = [i for i in range(2, upperBound+1) if i*i <= upperBound]
    for i in primes:
        if result[i]:
            for j in range(i*i, upperBound + 1, i):
                result[j] = False;
    return [i for i in range(2, upperBound+1) if result[i]]
    
"""
Returns Multiplicity of PRIME in the prime factorization of N
see http://homepage.smc.edu/kennedy_john/NFACT.PDF
"""
def getMultiplicity (n, prime):
    scratch = n
    multiplicity = 0
    while scratch > 0:
        scratch = scratch // prime
        multiplicity += scratch
    return multiplicity
    
"""
Input: N for the equation (1/x) + (1/y) = 1/(N!)
Output: the number of integral solutions to the aforementioned equation

Returns (2*m1 + 1) * (2*m2 +1) * ... * (2*m_n + 1) where m_i is the 
multiplicity of the i^th prime in the prime factorization of N
"""
def getNumberOfSolutions (n):
    # There will be no prime numbers if n is 1, might as well skip all that work.
    if n == 1:
        return 2 * 0 + 1
    primes = getPrimeNumbers(n)
    primeMultiplicities = []
    for p in primes:
        primeMultiplicities.append(getMultiplicity(n, p))
    return reduce(lambda x,y: x*y, [2*x+1 for x in primeMultiplicities])
    
def getAnswer (n):
    return getNumberOfSolutions(n) % 1000007
    
def main(*args):
    N = int(raw_input())
    print getAnswer(N)
        
if __name__ == '__main__':
    sys.exit(main(*sys.argv))