 x1 = 1
    y1 = 1
    x2 = 500
    y2 = 400
    x = x1
    y = y1

    #hitung dx dan dy
    dx = x2 - x1;
    dy = y2 - y1;

    #hitung steps
    if (dx > dy):
        steps = dx
    else:
        steps = dy;

    #hitung perubahan nilai x (x_inc) dan y (y_inc)
    x_inc = dx / steps
    y_inc = dy / steps

    #gambar titik awal
    glBegin(GL_POINTS);
    glVertex2i(x, y); #gambar titik awal

    #perulangan untuk menggambar titik-titik
    
    while x < x2:
        x += x_inc
        y += y_inc
        glVertex2i(x,y); #gambar titik