data = imread('test.jpg');%测试用的截图
gdata = rgb2gray(data); 
bw=im2bw(gdata,0.5);%对图像二值化
imshow(bw); 
imwrite(bw, 'c1.jpg');