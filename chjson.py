#python D:\code\chjson.py 12
import sys
#jsonpath = ""
print("第一个参数：" + sys.argv[1])
jsonpath = sys.argv[1]
ecuId = sys.argv[2]
soft = sys.argv[3]
compare1 = "ecuId"
compare2 = "soft"
writeecu = '    "ecuId": "' + str(ecuId) + '",\n'
writesoft = '    "soft": "' + str(soft) + '",\n'

print(jsonpath)
print(writeecu)
print(writesoft)

#print "读取的数据为: %s" % (line)
fp1 = open(jsonpath, 'r+', encoding='utf-8')
#文件指针得归0
fp1.seek(0,0)
print("在这一步1")
lines = []
lines = fp1.readlines()
print(lines)
print("在这一步2")
lines[1] = writeecu
lines[2] = writesoft
fp1.seek(0,0)
for line in lines:
	fp1.write(line)
#	if compare1 and compare2 not in line:
#		fp1.write(line)
#	if compare1 in line:
#		fp1.write(writeecu)
#	if compare2 in line:
#		fp1.write(writesoft)

fp1.close()