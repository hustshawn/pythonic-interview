Question2
===

## Fill in the missing code:
```python
def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    fill_this_in
```
### Answer

```python
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
```
## Pay Special Attention

Be consistent with your naming conventions. If there is a naming convention evident in any sample code, stick to it. Even if it is not the naming convention you usually use
Recursive functions need to recurse and terminate. Make sure you understand how this happens so that you avoid bottomless callstacks
We use the os module for interacting with the operating system in a way that is cross platform. You could say `sChildPath = sPath + '/' + sChild` but that wouldn't work on windows
Familiarity with base packages is really worthwhile, but don't break your head trying to memorize everything, Google is your friend in the workplace!
Ask questions if you don't understand what the code is supposed to do
KISS! Keep it Simple, Stupid!
Why This Matters:

Displays knowledge of basic operating system interaction stuff
Recursion is hella useful