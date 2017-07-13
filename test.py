import os
import fileinput
#print('请确保在该在的地方！')

print('现在的位置是'+os.getcwd())
#flag=input('是否生成文件?')
#if(flag=='true'):f=open('结果.txt','w')
#filenames=[]
for j in os.walk('.'):
	#print('如下：')
    flag1='false'
    print(j)
    print('欧拉')
    j=str(j)
    #for j in os.listdir('.'):
    #if j.find('.')==-1:continue
    #if os.path.isdir('.'+os.pathsep+j):flag1='ture'
    if j[3]!='\'':break
    string=j[5:-1]#.split()[0]
    print (string);#+' ',end='');
    #if(flag=='true'):f.write(string+'\n')
    if(flag1=='true'):continue
#if(flag=='true'):f.close()
os.system("PAUSE")