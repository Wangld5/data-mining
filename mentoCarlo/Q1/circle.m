function circle(R, Center)
    alpha = 0:pi/50:pi/2;
    x=R*cos(alpha)+Center(1);
    y=R*sin(alpha)+Center(2);
    plot(x,y,'b-','LineWidth',1)
end