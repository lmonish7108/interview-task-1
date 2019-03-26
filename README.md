<h2>interview-task-1</h2>
Fibonacci Series hosted with PythonAnywhere


Github Link:
https://github.com/lmonish7108/interview-task-1

Project hosted on AWS lightsails:
Server: Nginx, using python uwsgi protocol

Project url:   http://13.233.8.185
Admin url: http://13.233.8.185/admin   
username: admin 
password: admin123

you can submit the same number again to see how much less time it took to execute he same again.

There are various ways of Optimization you can do on this:

method 1: I implemented it.
Save user data, so next time instead of looping all over again, just retrieve the same input if available.

method 2:
Like method 1 you could just store the entire list Fibonacci with highest user input and next time if the input is less then you could just fetch from this list.
