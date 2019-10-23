data = imread('test2.jpg');%测试用的截图，注意编号
gdata = rgb2gray(data);
bw1=imresize(gdata, [150 150]);%将原图像缩小到150*150的固定大小
RGB1=imcrop(bw1,[1,70,150,150]);%截取下半部分，只保留赛道消息，图像变成80*150
b=im2bw(RGB1,0.5);%对图像二值化
bw=1-b;
A=sum(sum(bw(25:40,1:25))); %检测路标是否存在
%先求出可能区域的元素和（看1的多少）
B=sum(sum(bw(25:40,126:150)));
LR=A/B
if LR<=0.92  
    disp('右');
else
    if LR<=0.98 
        disp('不变');
    else
        disp('左');
    end
end
%没有必要在全程都判断正确是左是右，只需要正确一次便保持一段时间
imwrite(bw, 'c2.jpg');%保存二值化后图像