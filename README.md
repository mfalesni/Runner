Run
===

Simple and easy-to-use runner for Python scripts

Usage
=====
* <code>pip install Runner</code>
And then:

<pre>
    Python 2.7.4 (default, Apr 19 2013, 18:28:01) 
    [GCC 4.7.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from Runner import Run
    >>> result = Run.command("cat /etc/passwd")
    >>> result
    <Run->0 stdout='root:x:0:0:root:...' stderr='...'>
    (you see the strings are trimmed here just to be clean)
    >>> result.rc
    0
    >>> result.stdout
    'CONTENT OF MY /ETC/PASSWD FILE :)'
    >>> result.stderr
    ''
    >>> bool(result)
    True
    >>> newrun = result.rerun()
    >>> newrun  # Old one is preserved
    <Run->0 stdout='root:x:0:0:root:...' stderr='...'>
    >>> will_fail = Run.command("cat asdfasdf")
    >>> will_fail
    <Run->1 stdout='...' stderr='cat: asdfasdf: N...'>
    >>> bool(will_fail)
    False
    >>> will_fail.stderr
    'cat: asdfasdf: No such file or directory\n'
    >>> last_one = Run.bash("cat /etc/passwd | grep -E root")
    >>> bool(last_one)
    True
    >>> last_one.stdout
    'root:x:0:0:root:/root:/bin/bash\n'
>>>
</pre>


And that's it.

py.test extension:
==================

If you install <code>Runner-pytest</code> package, you will be able to use the fixture named <code>Run</code> in py.test environment.