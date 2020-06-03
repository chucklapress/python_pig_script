# Oink, oink little piggy

Fun little distraction script I wrote to call a pig latin script with python

## Setup on Ubuntu server
follow instructions here:
[Hadoop](https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-18-04)
and here:
[Pig](https://data-flair.training/blogs/apache-pig-installation-ubuntu-tutorial/)

## What I did
On the server I have a text file test.txt which is approximately 14000 words
long its Chapter 21 of JRR Tolkiens The Silmarillion “Of Túrin Turambar”
The pig latin script runs local and splits and counts and provides a list of
 the number of instances of each word used.

## Usage
I have modified the script to run globally using chmod 755 so I call it 
```python3
./oink.py
```
You can certainly play around with it as it was simply a learning fun project for me
## Contributing
Pull requests are welcome. feel free to let your self go nuts

## License
[MIT](https://choosealicense.com/licenses/mit/)
