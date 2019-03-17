function [myPi]=monteCarlo(n)
    r = 1;
    centerX = 0;
    centerY = 0;
    s = rng;
    rng(s);
    points = rand(2, n);
    inCircle = 0;
    for i=1:n
        dist = sqrt((points(1, i)-0)^2+(points(2, i)-0)^2);
        if dist < 1
            inCircle = inCircle + 1;
        end
    end
    myPi = inCircle/n*4;
    error=abs((pi-myPi)/pi);

    % ��ʼ��ͼ
    % figure;
    % inCirX = [];
    % inCirY = [];
    % outCirX = [];
    % outCirY = [];
    % for i=1:n
    %     dist = sqrt((points(1, i)-0)^2+(points(2, i)-0)^2);
    %     if dist < 1
    %         inCirX(end+1) = points(1, i);
    %         inCirY(end+1) = points(2, i);
    %     else
    %         outCirX(end+1) = points(1, i);
    %         outCirY(end+1) = points(2, i);
    %     end
    % end
    % scatter(inCirX, inCirY,'ro');hold on
    % scatter(outCirX, outCirY, 'go');hold on
    % circle(1, [0,0]);
    % title('Monte Carlo��������Բ���ʦ�'),xlabel('x'),ylabel('y');
    % axis([0,1,0,1])
end