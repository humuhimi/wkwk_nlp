
#unicode japanese katakana
re_words=re.compile(u"[\u30a0-\u30ff]+")
m =  re_words.search(s,0)
print "unicode 日文 片假名"
print "--------"
print m
print m.group()
print "--------\n"
 
 
#unicode japanese hiragana
re_words=re.compile(u"[\u3040-\u309f]+")
m =  re_words.search(s,0)
print "unicode 日文 平假名"
print "--------"
print m
print m.group()

--------------------- 
作者：JeanCheng 
来源：CSDN 
原文：https://blog.csdn.net/gatieme/article/details/43235791 
版权声明：本文为博主原创文章，转载请附上博文链接！

