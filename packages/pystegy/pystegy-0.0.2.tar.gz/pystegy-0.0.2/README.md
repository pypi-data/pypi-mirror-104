# stegy             -           Release 0.0.2

a small steganography utility that inserts text messages into images


## lets start !


```python
stegy = stegyImage()
message = "a secret message"
filepath = stegy.encode(message )
    
```
this code return `filepath` with '**./data/result.pgn**' 
That randomly generated PNG-file contains your secret message.


you can decode hidden message in '**./data/result.pgn**' with :

```
decoded  = stegy.decode(filepath)
```
return `decoded` str containing : **a secret message**

## options

* dest :

  set the filepath of result by adding **dest** parameter to encode
    
  ```python
  filepath = stegy.encode(message , dest = './tmp/my.png' )
  ```
  create PNG file according your **dest** parameter
  return  `filepath` with '**./tmp/my.png**'


* src :

  give your own image file  by adding **src** parameter to encode
  ```python
  filepath = stegy.encode(message , src = './srcImage/boat.jpg' )
  ```
  create PNG file according your **dest** parameter
  return  `filepath` relative to a downscaled PNG-file build from your **src**


* topics :
  this parameter is inactive if  **scr** parameter is set.
  give a topic list for randomly choosen image ( str comma-separated)

  ```python
  filepath = stegy.encode(message , topics = 'cat,boat' )
  ```
  the generated PNG should represent either a 'cat' or a 'boat'
  
  
* key :
  a key for message encryption (override default one)
  
  __a png generated with *key* parameter can only be decoded with the same *key*.__
  ```python
  filepath = stegy.encode("lorem ipsum sic dolores amet..." , key = 'MySecretKey' )
  decoded = stegy.decode(filepath , key = 'MySecretKey' )
  ```
  



> Release Note v 0.0.2
> # Added 2 exceptions on 'decode' 
> - `NoMessage` exception : if given image have no message in it
> - `BadKey` exception : if a message is found but the decode key doesn't fit.
  
  





