Run
===

Simple and easy-to-use runner for Python scripts

Usage
=====
* <code>python setup.py build</code>
* <code>sudo python setup.py install</code>
And then:

<pre style='color:#000000;background:#ffffff;'><html><body style='color:#000000; background:#ffffff; '><pre>
Python <span style='color:#008000; '>2.7</span><span style='color:#808030; '>.</span><span style='color:#008c00; '>4</span> <span style='color:#808030; '>(</span>default<span style='color:#808030; '>,</span> Apr <span style='color:#008c00; '>19</span> <span style='color:#008c00; '>2013</span><span style='color:#808030; '>,</span> <span style='color:#008c00; '>18</span><span style='color:#808030; '>:</span><span style='color:#008c00; '>28</span><span style='color:#808030; '>:</span><span style='color:#008c00; '>01</span><span style='color:#808030; '>)</span> 
<span style='color:#808030; '>[</span>GCC <span style='color:#008000; '>4.7</span><span style='color:#808030; '>.</span><span style='color:#008c00; '>3</span><span style='color:#808030; '>]</span> on linux2
Type <span style='color:#0000e6; '>"help"</span><span style='color:#808030; '>,</span> <span style='color:#0000e6; '>"copyright"</span><span style='color:#808030; '>,</span> <span style='color:#0000e6; '>"credits"</span> <span style='color:#800000; font-weight:bold; '>or</span> <span style='color:#0000e6; '>"license"</span> <span style='color:#800000; font-weight:bold; '>for</span> more information<span style='color:#808030; '>.</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> <span style='color:#800000; font-weight:bold; '>from</span> Runner <span style='color:#800000; font-weight:bold; '>import</span> Run
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> result <span style='color:#808030; '>=</span> Run<span style='color:#808030; '>.</span>command<span style='color:#808030; '>(</span><span style='color:#0000e6; '>"cat /etc/passwd"</span><span style='color:#808030; '>)</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> result
<span style='color:#808030; '>&lt;</span>Run<span style='color:#808030; '>-</span><span style='color:#808030; '>></span><span style='color:#008c00; '>0</span> stdout<span style='color:#808030; '>=</span><span style='color:#0000e6; '>'root:x:0:0:root:...'</span> stderr<span style='color:#808030; '>=</span><span style='color:#0000e6; '>'...'</span><span style='color:#808030; '>></span>
<span style='color:#808030; '>(</span>you see the strings are trimmed here just to be clean<span style='color:#808030; '>)</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> result<span style='color:#808030; '>.</span>rc
<span style='color:#008c00; '>0</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> result<span style='color:#808030; '>.</span>stdout
<span style='color:#0000e6; '>'CONTENT OF MY /ETC/PASSWD FILE :)'</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> result<span style='color:#808030; '>.</span>stderr
<span style='color:#0000e6; '>''</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> bool<span style='color:#808030; '>(</span>result<span style='color:#808030; '>)</span>
<span style='color:#e34adc; '>True</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> newrun <span style='color:#808030; '>=</span> result<span style='color:#808030; '>.</span>rerun<span style='color:#808030; '>(</span><span style='color:#808030; '>)</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> newrun  <span style='color:#696969; '># Old one is preserved</span>
<span style='color:#808030; '>&lt;</span>Run<span style='color:#808030; '>-</span><span style='color:#808030; '>></span><span style='color:#008c00; '>0</span> stdout<span style='color:#808030; '>=</span><span style='color:#0000e6; '>'root:x:0:0:root:...'</span> stderr<span style='color:#808030; '>=</span><span style='color:#0000e6; '>'...'</span><span style='color:#808030; '>></span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> will_fail <span style='color:#808030; '>=</span> Run<span style='color:#808030; '>.</span>command<span style='color:#808030; '>(</span><span style='color:#0000e6; '>"cat asdfasdf"</span><span style='color:#808030; '>)</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> will_fail
<span style='color:#808030; '>&lt;</span>Run<span style='color:#808030; '>-</span><span style='color:#808030; '>></span><span style='color:#008c00; '>1</span> stdout<span style='color:#808030; '>=</span><span style='color:#0000e6; '>'...'</span> stderr<span style='color:#808030; '>=</span><span style='color:#0000e6; '>'cat: asdfasdf: N...'</span><span style='color:#808030; '>></span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> bool<span style='color:#808030; '>(</span>will_fail<span style='color:#808030; '>)</span>
<span style='color:#e34adc; '>False</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> will_fail<span style='color:#808030; '>.</span>stderr
<span style='color:#0000e6; '>'cat: asdfasdf: No such file or directory\n'</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> last_one <span style='color:#808030; '>=</span> Run<span style='color:#808030; '>.</span>bash<span style='color:#808030; '>(</span><span style='color:#0000e6; '>"cat /etc/passwd | grep -E root"</span><span style='color:#808030; '>)</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> bool<span style='color:#808030; '>(</span>last_one<span style='color:#808030; '>)</span>
<span style='color:#e34adc; '>True</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span> last_one<span style='color:#808030; '>.</span>stdout
<span style='color:#0000e6; '>'root:x:0:0:root:/root:/bin/bash\n'</span>
<span style='color:#808030; '>></span><span style='color:#808030; '>></span><span style='color:#808030; '>></span>
</pre>


And that's it.