#Code to find the shortest distance between two connected pixels
#depending of the adjacency type and the predifined pixel vector

def shortestpath(image_matrix,V,p,q,path_type):

    rows=len(image_matrix)
    cols=len(image_matrix[0])

    #print image_matrix

    #Doing Sanity Checks of inputs
    if (len(V)==0):
        print 'Invalid input in vector V'

    if (p[0]<0 or p[0]>rows-1 or p[1]<0 or p[1]>cols-1 ):
        print 'Source Pixel co-ordinates invalid'

    if (q[0]<0 or q[0]>rows-1 or q[1]<0 or q[1]>cols-1 ):
        print 'Destination Pixel co-ordinates invalid'

    if (path_type not in (4,8,'m')):
        print 'Invalid path Type'

    #Creating the Graphical representation of the image matrix

    for i in range(0,rows):
        for j in range(0,cols):
            if (image_matrix[i][j] not in V):
                image_matrix[i][j]=-1


    # Storing the valid co-ordinates of the image_graph

    valid_image_matrix=[]
    if (path_type==4):

        for i in range(0,rows):
            for j in range(0,cols):
                # Checking boundary conditions along top row
                if((i==0) and (j==0)):

                    if((image_matrix[i][j] in V) and ((image_matrix[i][j+1] in V) or (image_matrix[i+1][j] in V))):

                        valid_image_matrix.append([i,j])


                elif ((i == 0) and (j == cols-1)):

                    if ((image_matrix[i][j] in V) and ((image_matrix[i][j-1] in V) or (image_matrix[i + 1][j] in V))):

                        valid_image_matrix.append([i, j])
                elif((i==0) and (j>=0) and (j<cols-1)):


                    if((image_matrix[i][j] in V) and ((image_matrix[i][j-1] in V) or
                                                          (image_matrix[i][j+1] in V) or (image_matrix[i+1][j] in V))):

                        valid_image_matrix.append(([i,j]))





                #***********************************************
                # Checking boundary conditions along bottom row
                if (i == rows-1 and j == 0):
                    if ((image_matrix[i][j] in V) and ((image_matrix[i][j + 1] in V) or (image_matrix[i - 1][j] in V))):

                        valid_image_matrix.append([i, j])


                elif ((i == rows-1) and (j == cols-1)):
                    if ((image_matrix[i][j] in V) and ((image_matrix[i][j - 1] in V) or (image_matrix[i -1][j] in V))):

                        valid_image_matrix.append([i, j])
                elif ((i == rows-1) and (j != 0) and (j != cols-1)):
                    if ((image_matrix[i][j] in V) and ((image_matrix[i][j - 1] in V) or (image_matrix[i][j + 1] in V) or
                                                           (image_matrix[i - 1][j]))):

                        valid_image_matrix.append(([i, j]))

                #************************************************
                # Checking boundary conditions along left column

                if ((i >0) and (i<=rows-2) and (j==0)):
                    if ((image_matrix[i][j] in V) and ((image_matrix[i-1][j] in V) or (image_matrix[i+1][j] in V) or
                                                           (image_matrix[i][j+1] in V))):

                        valid_image_matrix.append([i, j])
                #************************************************

                # Checking boundary conditions along right column

                if ((i >0) and (i<=rows-2) and (j==cols-1)):
                    if ((image_matrix[i][j] in V) and ((image_matrix[i-1][j] in V) or
                                                           (image_matrix[i+1][j] in V) or (image_matrix[i][j-1] in V))):

                        valid_image_matrix.append([i, j])


                #************************************************************

                #************************************************************
                elif ((i > 0) and (i <=rows - 2) and (j > 0) and (j <=cols - 2)):
                    if (image_matrix[i][j] in V and (image_matrix[i][j - 1] in V or image_matrix[i][j + 1] in V or
                            image_matrix[i - 1][j] in V or image_matrix[i + 1][j] in V)):

                        valid_image_matrix.append([i, j])
                #*************************************************************




    valid_image_matrix = []
        if (path_type == 8):

                    for i in range(0, rows):
                        for j in range(0, cols):
                            # Checking boundary conditions along top row
                            if ((i == 0) and (j == 0)):

                                if ((image_matrix[i][j] in V) and (
                                                (image_matrix[i][j + 1] in V) or (image_matrix[i + 1][j] in V) or (
                                                    image_matrix[i + 1][j + 1] in V))):
                                    valid_image_matrix.append([i, j])


                            elif ((i == 0) and (j == cols - 1)):

                                if ((image_matrix[i][j] in V) and (
                                                (image_matrix[i][j - 1] in V) or (image_matrix[i + 1][j] in V) or (
                                                image_matrix[i + 1][j - 1]))):
                                    valid_image_matrix.append([i, j])
                            elif ((i == 0) and (j >= 0) and (j < cols - 1)):

                                if ((image_matrix[i][j] in V) and ((image_matrix[i][j - 1] in V) or
                                                                       (image_matrix[i][j + 1] in V) or (
                                            image_matrix[i + 1][j] in V) or (image_matrix[i + 1][j - 1]) or (
                                        image_matrix[i + 1][j + 1]))):
                                    valid_image_matrix.append(([i, j]))

                            # ***********************************************
                            # Checking boundary conditions along bottom row
                            if (i == rows - 1 and j == 0):
                                if ((image_matrix[i][j] in V) and (
                                                (image_matrix[i][j + 1] in V) or (image_matrix[i - 1][j] in V) or (
                                                image_matrix[i - 1][j + 1]))):
                                    valid_image_matrix.append([i, j])


                            elif ((i == rows - 1) and (j == cols - 1)):
                                if ((image_matrix[i][j] in V) and (
                                                (image_matrix[i][j - 1] in V) or (image_matrix[i - 1][j] in V) or (
                                                image_matrix[i - 1][j - 1]))):
                                    valid_image_matrix.append([i, j])
                            elif ((i == rows - 1) and (j != 0) and (j != cols - 1)):
                                if ((image_matrix[i][j] in V) and (
                                                        (image_matrix[i][j - 1] in V) or (
                                                                image_matrix[i][j + 1] in V) or
                                                    (image_matrix[i - 1][j]) or (image_matrix[i - 1][j + 1]) or (
                                                image_matrix[i - 1][j - 1]))):
                                    valid_image_matrix.append(([i, j]))

                            # ************************************************
                            # Checking boundary conditions along left column

                            if ((i > 0) and (i <= rows - 2) and (j == 0)):
                                if ((image_matrix[i][j] in V) and (
                                                (image_matrix[i - 1][j] in V) or (image_matrix[i + 1][j] in V) or
                                            (image_matrix[i][j + 1] in V)) or (image_matrix[i - 1][j + 1]) or (
                                        image_matrix[i + 1][j + 1])):
                                    valid_image_matrix.append([i, j])
                            # ************************************************

                            # Checking boundary conditions along right column

                            if ((i > 0) and (i <= rows - 2) and (j == cols - 1)):
                                if ((image_matrix[i][j] in V) and ((image_matrix[i - 1][j] in V) or
                                                                       (image_matrix[i + 1][j] in V) or (
                                            image_matrix[i][j - 1] in V) or (image_matrix[i - 1][j - 1]) or (
                                        image_matrix[i + 1][j - 1]))):
                                    valid_image_matrix.append([i, j])


                            # ************************************************************

                            # ************************************************************
                            elif ((i > 0) and (i <= rows - 2) and (j > 0) and (j <= cols - 2)):
                                if (image_matrix[i][j] in V and (
                                                        image_matrix[i][j - 1] in V or image_matrix[i][j + 1] in V or
                                                    image_matrix[i - 1][j] in V or image_matrix[i + 1][j] in V) or (
                                        image_matrix[i - 1][j + 1])
                                    or (image_matrix[i - 1][j - 1]) or (image_matrix[i + 1][j - 1]) or (
                                        image_matrix[i + 1][j + 1])):
                                    valid_image_matrix.append([i, j])

    #Numbering the Nodes
    Node_Numbers=[]
    for i in range(0,len(valid_image_matrix)):
        Node_Numbers.append([valid_image_matrix[i],i])
    #print Node_Numbers

    for i in range(0,len(Node_Numbers)):
        if (Node_Numbers[i][0]==p):
            Source_Node_Number=Node_Numbers[i][1]
        if(Node_Numbers[i][0]==q):
            Dest_Node_Number=Node_Numbers[i][1]
    #print 'Source Node Number=',Source_Node_Number,'Destination Node_Number',Dest_Node_Number




    #Creating Python Dictionary to store nodes and neighbours
            Graph1={}
            for i in range(0,len(Node_Numbers)):
                Neighbours1=[]
                x=valid_image_matrix[i][0]


                y=valid_image_matrix[i][1]


                node_number=Node_Numbers[i][1]



                for j in range(0,len(Node_Numbers)):
                    x_t=valid_image_matrix[j][0]

                    y_t=valid_image_matrix[j][1]

                    flag=0

                    if((((x==x_t) and (y==y_t-1))or((x==x_t) and (y==y_t+1)) or ((x==x_t-1) and (y==y_t)) or ((x==x_t+1) and (y==y_t)))):
                        flag=1
                        if(flag==1):
                           Graph1.setdefault(node_number, []).append(Node_Numbers[j][1])




            #print Graph1



        for i in range(0,len(Node_Numbers)):
            if(Node_Numbers[i][0]==p):
                start=Node_Numbers[i][1]

            if(Node_Numbers[i][0]==q):
                end=Node_Numbers[i][1]




        def func(Graph1,start,end,path=[]):
            path=path+[start]



            if(start==end):
                return path
            if not Graph1.has_key(start):
                return None
            shortest=None
            for node in Graph1[start]:
                if node not in path:
                    newpath = func(Graph1, node, end, path)
                    if newpath:
                        if (not shortest or len(newpath)<len(shortest)):
                            shortest=newpath


            return shortest



    #print Shortest_Path_Coordinates






image_matrix=[[3,1,2,1],
              [2,2,0,2],
              [1,2,1,1],
              [1,0,1,2]]
V=[0,1]
p=[3,0]
q=[2,2]
path_type=8
shortestpath(image_matrix,V,p,q,path_type)