
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

def x1_i(k,r,l,wa,wb,Gamma):
    return complex(U_i(k,r,l,wa,wb,Gamma)+V_i(k,r,l,wa,wb,Gamma)-p_i(k,r,l,wa,wb,Gamma)/3)
def x2_i(k,r,l,wa,wb,Gamma):
    return complex(-(U_i(k,r,l,wa,wb,Gamma)+V_i(k,r,l,wa,wb,Gamma))/2+((pow(3,1/2)*(U_i(k,r,l,wa,wb,Gamma)-V_i(k,r,l,wa,wb,Gamma)))/2)*1j-p_i(k,r,l,wa,wb,Gamma)/3)
def x3_i(k,r,l,wa,wb,Gamma):
    return complex(-(U_i(k,r,l,wa,wb,Gamma)+V_i(k,r,l,wa,wb,Gamma))/2-((pow(3,1/2)*(U_i(k,r,l,wa,wb,Gamma)-V_i(k,r,l,wa,wb,Gamma)))/2)*1j-p_i(k,r,l,wa,wb,Gamma)/3)

def main():

    
    l=10
    N=5000
    step=100

    for k_loop in range (75,step+1,1):
        k=np.round((k_loop/step)*3,3)
        for r_loop in range (1,step+1,1):
            r=np.round(r_loop/step,3)
            for omega_loop in range (0,(step)+1,1):
                omega=np.round((omega_loop/step)*l,3)
                print(f'r={r}\tomega={omega}\n')
                file1 = open(f'./Output/{k}/{r}-{omega}-{N}-{l}-{k}.txt', "x")
                for i in range (1,N+1):
                    wa=-0.5+(i-1)/(N-1)
                    wb=-wa
                    #x1=x1_i(k,r,l,wa,wb,omega)
                    #x2=x2_i(k,r,l,wa,wb,omega)
                    x3=x3_i(k,r,l,wa,wb,omega)
                    file1.write(f'{np.round(np.real(x3),4)}\t{np.round(np.imag(x3),4)}\n')
                file1.close()
    pass


if __name__=="__main__":
    main()
