
def encontrar_ruta(C):


    if C[0][0] == 1:
        return []

    elif C[0][1] == 1 and C[1][0] == 1:
        return []

    else:
        C[0][0] = "R"
    
    i=0
    j=0
    solucion=True 

    while C[len(C)-1][len(C[0])-1] != "R":
        if solucion == False:
            break
        
        elif j+1 <= (len (C[0])-1) and C[i][j+1] == 0:
            j += 1
            C[i][j]= "R"
            
        elif i+1 <= (len (C)-1) and C[i+1][j] == 0:
            i += 1
            C[i][j]= "R"

        else:
            C[i][j]= "R"
            
            if C[i][j-1]==0:
                j -= 1
                C[i][j]= "R"
                
            else:
                C, i, j, solucion = devolverse(C,i,j,solucion)
                    
                if solucion == False:
                    return []
       
    for h in range(len(C)):

        for k in range(len(C[h])):

            if C[h][k] == 1:
                C[h][k] = 0
                            
            elif C[h][k] == "R":
                C[h][k] = 1

    return C     
                                

def devolverse(C, i, j, solucion):

    while C[i+1][j] != 0:
       
        if C[i][j] == "X":
            solucion = False
            break

        elif C[i-1][j] == "R":
            i -= 1
            C[i][j] = "X"
        
        elif C[i][j-1]== "R":
            j -= 1
            C[i][j] = "X"

    return C, i, j, solucion