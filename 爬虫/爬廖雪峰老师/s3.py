#  博客园代码
from bs4 import BeautifulSoup

bokeyuan ='''

'''

s1= '''
<pre class="prettyprint" style="overflow: hidden; font-family: &quot;courier new&quot;; font-size: 12px; padding: 10px 15px; margin-top: 20px; margin-bottom: 20px; line-height: 20px; color: rgb(248, 248, 212); background: rgb(39, 40, 34); border-width: initial; border-style: none; border-color: initial; font-stretch: normal;"><code class="cpp" title="果冻想 | 一个原创文章分享网站"><span class="kwd" style="color: rgb(249, 38, 89);">typedef</span><span class="pln" style="color: rgb(102, 217, 239);"> </span><span class="kwd" style="color: rgb(249, 38, 89);">enum</span><span class="pln" style="color: rgb(102, 217, 239);"> </span><span class="typ" style="color: rgb(166, 226, 46);">MANTYPETag</span><span class="pln" style="color: rgb(102, 217, 239);">
</span><span class="pun" style="color: rgb(248, 248, 242);">{</span><span class="pln" style="color: rgb(102, 217, 239);">
	kFatMan</span><span class="pun" style="color: rgb(248, 248, 242);">,</span><span class="pln" style="color: rgb(102, 217, 239);">
	kThinMan</span><span class="pun" style="color: rgb(248, 248, 242);">,</span><span class="pln" style="color: rgb(102, 217, 239);">
	kNormal
</span><span class="pun" style="color: rgb(248, 248, 242);">}</span><span class="pln" style="color: rgb(102, 217, 239);">MANTYPE</span><span class="pun" style="color: rgb(248, 248, 242);">;</span></code></pre>
'''
'''
<pre class="prettyprint" style="overflow: hidden; font-family: &quot;courier new&quot;; font-size: 12px; padding: 10px 15px; margin-top: 20px; margin-bottom: 20px; line-height: 20px; color: rgb(248, 248, 212); background: rgb(39, 40, 34); border-width: initial; border-style: none; border-color: initial; font-stretch: normal;"><code class="cpp" title="果冻想 | 一个原创文章分享网站"><span class="com" style="color: rgb(147, 161, 161);">#include</span><span class="pln" style="color: rgb(102, 217, 239);"> </span><span class="str" style="color: rgb(230, 219, 116);">&lt;iostream&gt;</span><span class="pln" style="color: rgb(102, 217, 239);"></span><span class="kwd" style="color: rgb(249, 38, 89);">using</span><span class="pln" style="color: rgb(102, 217, 239);"> </span><span class="kwd" style="color: rgb(249, 38, 89);">namespace</span><span class="pln" style="color: rgb(102, 217, 239);"> std</span><span class="pun" style="color: rgb(248, 248, 242);">;</span></code></pre>\
'''
text = BeautifulSoup(s1,'lxml')
# print(text.pre)
if text.pre:
    tt= text.pre.text
    text.pre.clear()
    text.pre.append('<code>'+tt+'</code>')
        # ='<pre class="prettyprint prettyprinted"><code>'+text.pre.text+'</code></pre>'

print(text.pre)
print(str(text))
# print(text.pre.text)