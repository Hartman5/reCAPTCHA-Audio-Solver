# reCAPTCHA-Audio-Solver
Solve google reCAPTCHA with selenium in 5 seconds at no cost

#How To Use
When a captcha comes up on the page you are trying to automate call the solve function with no parameters. The captcha will be solved automatically and the function will return with either True or False. If the response is True then the captcha was solved, If the response was False then there was no captcha or it failed to solve.

#Examples
```python
#put this where a captcha is in your code. (Ex. After filling out signup form)
response = solve()
if response == True:
  print('Captcha Solved')
elif response == False:
  print('Captcha Not Present / Failed')
else:
  print('No Response')
```
