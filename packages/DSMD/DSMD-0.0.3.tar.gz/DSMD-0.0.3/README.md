# DSMD

DSMD is a superset of **Markdown**. When you run it, it will start a while loop for you to start writing DSMD! 

Here is how you should install it!

|Manager          |Command                                       |
|:----------------|:---------------------------------------------|
|**pip**          |`pip install DSMD`                          |
|**poetry**       |`python -m poetry add DSMD`                 |
|**Repl.it**      |Search `DSMD` in the package tab and add it.(coming soon)|     |

After you have done one of those things(or you have your own way of getting it), you can start writing DSMD! Here is a sample!

``` python
from DSMD import parse # parse is the only function in the module
parse("README")
```
Unlike the first version of DSMD, you don't have to put DSMD as the end. DSMD trusts you to put the correct file path. To help you, DSMD puts your files at the root of your repository. Like say your file structure looks like this:
```
-src:
--main.py 
README.dsmd 
README.md 

```

You would put in your main.py:
``` python
from DSMD import parse 
parse("README")
```
DSMD puts you at the start of your repository when you say what file. So be on the lookout!

Once you run your main.py file with a README.dsmd. You'll see a README.md come up. DSMD automaticly creates a md file for you if you didn't make the md file yourself. Then anything in the md file gets emtpied out. So make sure nothing importants in it. Then, while loop starts. And every three seconds, DSMD will parse your DSMD file and puts the parsed code into the md file. Then one your are done editing. Just do ctrl + c to end the process. But if you don't like it updating every three seconds, in the parse function that is given to you, you can specify the time you want to be updated on like this:
``` python
parse("README", 10)
```
Then DSMD will update every 10 seconds! Cool right. Then after this setup is done, you can go crazy with DSMD! 

But you might think *`But I don't know any DSMD`*. Well never fear! If you go [here](https://github.com/whippingdot/Language-Tutorials/tree/main/DSMD), you can see a full tutorial on DSMD.

And the docs for DSMD will be coming out soon, so you can get the creators full point of view on DSMD.

Thanks for reading this and I'll see you in the next version...

# BAII!!

