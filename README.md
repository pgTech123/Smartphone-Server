Cellphone Server
===================

This project contains information and code to transform old unused cellphones into active web servers. The goal of this project is to reduce pollution caused by "old" smartphones when they are not good enough for consumers (not "cool" anymore, cracked screen, broken headphone jack, ...). Instead of recycling some part of the phone and disposing of the rest, the solution proposed is to extend the life of smartphones by a few years by turning it into a web server. 

Proof of Concept
--------------------
This project is in the phase of "proof of concept".

What You'll Need
-------------------------
- Old android smartphone(s)
- Web Server: This is used as a backup and as a monitor for our smartphone server
- Router(s)
- Internet connection

Architecture
-----
Currently, the strategy is to use a third party server as a man in the middle. If everything work as expected, the server will act as a proxy and redirect every request to our cellphone server. Although, if the smartphone server stop responding, the web server will take the relay and redirect all request to itself. That way, we make sure the website is never down because of a technical problem, and still, we can prove the concept by collecting statistics about up time vs down time of our cellphone servers, and improve the design. 

Getting Started
-----------
See [Getting Started](Getting_Started.md)

Feel free to contribute to make the world a better place :)
----

