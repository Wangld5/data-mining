function [result] = Q1()
    myMean = [];
    myVar = [];
    allparameter = [20, 50, 100, 200, 300, 500, 1000, 5000];
    for i=1:8
        result = [];
        for j=1:20
            myPi = monteCarlo(allparameter(i));
            result(end+1) = myPi;
        end
        myMean(end+1) = mean(result);
        myVar(end+1) = sum((result(1,:)-mean(result)).^2)/length(result);
    end
    result = [allparameter;myMean;myVar];


    figure
    b=bar(myMean);
    grid on;
    set(gca,'XTickLabel',allparameter)
    legend('��ֵ');
    xlabel('ȡ����� ');
    ylabel('�����ֵ');
    
    figure
    c=bar(myVar);
    grid on;
    set(gca,'XTickLabel',allparameter)
    legend('����');
    xlabel('ȡ����� ');
    ylabel('�������');
end