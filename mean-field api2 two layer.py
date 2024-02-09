
import numpy as np
def p_i(k,r,l,wa,wb,Gamma):
    return complex((-pow(k,2)*pow(r,2)-2*pow(l,2)+2*l*(wa+wb-2*Gamma))/(2*pow(l,2)))
def q_i(k,r,l,wa,wb,Gamma):
    return complex((-pow(wb-wa,2)-4*l*(wa+wb-2*Gamma)+pow(wa+wb-2*Gamma,2))/(4*pow(l,2)))
def r_i(k,r,l,wa,wb,Gamma):
    return complex((2*pow(k,2)*pow(r,2)-pow(wb-wa,2)-pow(wa+wb-2*Gamma,2))/(4*pow(l,2)))

def a_i(k,r,l,wa,wb,Gamma):
    return complex((3*q_i(k,r,l,wa,wb,Gamma)-pow(p_i(k,r,l,wa,wb,Gamma),2))/3)
def b_i(k,r,l,wa,wb,Gamma):
    return complex((2*pow(p_i(k,r,l,wa,wb,Gamma),3)-9*p_i(k,r,l,wa,wb,Gamma)*q_i(k,r,l,wa,wb,Gamma)+27*r_i(k,r,l,wa,wb,Gamma))/27)

def U_i(k,r,l,wa,wb,Gamma):
    return complex(pow(-b_i(k,r,l,wa,wb,Gamma)/2+pow(pow(b_i(k,r,l,wa,wb,Gamma),2)/4+pow(a_i(k,r,l,wa,wb,Gamma),3)/27,1/2),1/3))
def V_i(k,r,l,wa,wb,Gamma):
    return complex(pow(-b_i(k,r,l,wa,wb,Gamma)/2-pow(pow(b_i(k,r,l,wa,wb,Gamma),2)/4+pow(a_i(k,r,l,wa,wb,Gamma),3)/27,1/2),1/3))

def x3_i(k,r,l,wa,wb,Gamma):
    return complex(-(U_i(k,r,l,wa,wb,Gamma)+V_i(k,r,l,wa,wb,Gamma))/2-((pow(3,1/2)*(U_i(k,r,l,wa,wb,Gamma)-V_i(k,r,l,wa,wb,Gamma)))/2)*1j-p_i(k,r,l,wa,wb,Gamma)/3)

def main():
    k=2.6
    l=10
    N=1000
    
    file = open("omega.txt", "w")
    file.write('r\tGamma\n')
    for rr in range (0,100):
        r=rr/100
        for g in range (0,1000):
            Gamma=g/100#9.4375

            sum_gamma=0
            for i in range (1,N+1):
                wa=-0.5+(i-1)/(N-1)
                wb=-wa
                #print(f'wa={wa}\tx3_({i+5})={x3_i(k,r,l,wa,wb,Gamma)}')
                sum_gamma+=(wa+l*x3_i(k,r,l,wa,wb,Gamma))
            sum_gamma=sum_gamma/N
            check=0
            if (Gamma==round(np.real(sum_gamma),2)):
                check=1
                file.write(f'{r}\t{Gamma}\n')
                print(f'gamma_total=\t{round(np.real(sum_gamma),2)}\t{r}\t{check}')

    '''r_last=0
    for i in range (1,N+1):
        wa=-0.5+(i-1)/(N-1)
        tetha=-np.arcsin((sum_gamma-wa-l*x3_i(k,r,l,wa,wb,Gamma))/k*r)
        #print(f'wa={wa}\ttetha-say={tetha}')
        r_last+=np.cos(tetha)
    r_last=r_last/N
    print(f'\r_last={r_last}')'''
    pass

if __name__=="__main__":
    main()
