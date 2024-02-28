import numpy as np
def Omega(N,l,arr_i,arr_x):
    Om=0
    N_locked=len(arr_x)
    for j in range (0,N_locked):
        wa=-0.5+(arr_i[j]-1)/(N-1)
        Om+=wa+l*arr_x[j]
    return Om/N_locked

def Sync(N,omega,r,k,l,arr_i,arr_x):
    Syn=0
    N_locked=len(arr_x)
    for j in range (0,N_locked):
        wa=-0.5+(arr_i[j]-1)/(N-1)
        in_arcsin=(omega-wa-l*arr_x[j])/(k*r)
        if in_arcsin > 1 or in_arcsin < -1:
            in_arcsin=round(in_arcsin)
        Syn+=np.cos(-np.arcsin(in_arcsin))
    return Syn/N

def main():

    k=2.94
    N=5000
    l=10
    step=100

    for k_loop in range (97,74,-1):
        k=np.round((k_loop/step)*3,3)
        file = open(f'./Output2/{N}-{l}-{k}.txt', "w")
        file.write('omega\tOmega_origin\tr\tr_origin\td(omega)\td(r)\td(omega-r)\n')
        for r_loop in range (1,step+1,1):
            r=np.round(r_loop/step,3)
            for omega_loop in range (0,(step)+1,1):
                omega=np.round((omega_loop/step)*l,3)
                #omega=6.4
                #r=0.5
                filename=f'./Output/{k}/{r}-{omega}-{N}-{l}-{k}.txt'
                arr_x=[]
                arr_i=[]
                with open(filename, 'r') as current_file:
                    conter_i=1
                    for line in current_file.readlines():
                        point = line.split('\t')
                        x = float(point[0])
                        y = float(point[1])
                        if y==0 and x>0 and x<1:
                            arr_x.append(x)
                            arr_i.append(conter_i)
                        conter_i+=1
                print(k,omega,r)
                Omega_origin=Omega(N,l,arr_i,arr_x)
                r_origin=Sync(N,omega,r,k,l,arr_i,arr_x)
                file.write(f'{omega}\t{Omega_origin}\t{r}\t{r_origin}\t{np.abs(Omega_origin-omega)}\t{np.abs(r_origin-r)}\t{np.abs(Omega_origin-omega)+np.abs(r_origin-r)}\n')
        file.close()
    pass


if __name__=="__main__":
    main()
