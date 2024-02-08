
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
    k=2
    r=1
    l=1
    wa=-0.5
    wb=0.5
    Gamma=1
    print(x3_i(k,r,l,wa,wb,Gamma))

    pass

if __name__=="__main__":
    main()
