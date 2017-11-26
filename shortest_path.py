def shortest_path(image_segment):
    rows=len(image_segment[:,1])
    cols=len(image_segment[1,:])

    print rows,cols

image_segment=[[0,1,1,0]
               [1,0,0,1]
               [1,0,0,1]]

print image_segment
