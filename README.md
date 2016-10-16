Cellphone Server
===================

This project contains information and code to transform old unused cellphone into active web servers. The goal of this project is to reduce pollution caused by "old" smartphones when they are not good enough for consumers (not "cool" anymore, cracked screen, broken headphone jack, ...). Instead of recycling some part of the phone and disposing of the rest, the solution proposed is to extend the life of smartphones by a few years by turning it into a web server. 

Proof of Concept
--------------------
This project is in the phase of "proof of concept".

What You'll Need
-------------------------
- Old android smartphone(s)
- Web Server (not the phone): This is used as a backup and as a monitor for our smartphone server
- Router with an internet connection

Architecture
-----
Currently, the strategy is to use a server as a man in the middle. If everything work as expected, the server will act as a proxy and redirect every request to our cellphone server. Although, if the smartphone server stop responding, the web server will take the relay and deliver the website (backup copy of the website(s) hosted on our servers). The web server acting as a proxy can also be used to collect stats about up/down time of the smartphone server, latency, ...

Feel Free to Contribute or to Use The Information Contained Here to Make The World a Better Place :)
----

