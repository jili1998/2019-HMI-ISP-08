data = imread('test.jpg');%�����õĽ�ͼ
gdata = rgb2gray(data); 
bw=im2bw(gdata,0.5);%��ͼ���ֵ��
imshow(bw); 
imwrite(bw, 'c1.jpg');