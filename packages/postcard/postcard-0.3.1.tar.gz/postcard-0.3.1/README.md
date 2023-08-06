## Postcard

POP3/IMAP/SMTP client and more!

Thanks for use.


## How to use
### POP3
#### For decorator
```python
from postcard import Pop3

pop = Pop3()

@pop.process(user="xxx", pwd="xxx")
def get_content():
    content = pop.retrieve()["content"]
    print(content)
```


#### For usual
```python
from postcard import Pop3

pop = Pop3()

pop.login(user="xxx", pwd="xxx")
...
pop.close()
```


### SMTP
```python
from postcard import Smtp

smtp = Smtp()

@smtp.process(user="xxx", pwd="xxx")
def send():
    ret = smtp.send_mail(subject="xx", content="xx", receiver="xx")
    print(ret)
```


### IMAP
```python
from postcard import Imap

imap = Imap()

@imap.process(user="xxx", pwd="xxx")
def get_content():
    content = imap.retrieve()["content"]   # If you want to mark as read, please set readonly to False.
    print(content)
```