# KoreaDevConf

한국 개발자 컨퍼런스 모음

http://aws-website-kordevconf-f3zmu.s3-website-us-east-1.amazonaws.com/services.html

## Tools

python 3.6.2

flask 0.12.2 

    $ pip3 install flask

beautifulsoup4 4.6.0

    $ pip3 install beatifulsoup4

OSX 사용자이면서 python 3.6+ 버전을 사용한다면 ssl 

    $ /Applications/Python\ 3.6/Install\ Certificates.command

validators 0.12.0

    $ pip3 install validators

## Test

    $ cd /KoreaDevConf

    $ python3 -m unittest discover test

## How to start? 

    $ export FALSK_APP=main.py

    $ flask run