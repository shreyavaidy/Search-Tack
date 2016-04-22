Search Task	
===========

CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * Installation
 * Working

Introduction
============

This is python client that fetches the search results from the chrome webstore having specific keywords (Facebook, YouTube, Instagram, Pinterest and Twitter) using Google's Custom Search API.

Requirements
============
	1. Google API Developer Key AND Credentials
	2. Google Custom Search API - Python Client 
	
Installation
============

To install, using pip:

   $ pip --upgrade google-api-python-client

   $ easy_install --upgrade google-api-python-client

Working
=======

Search Task performed : 
	To fetch Google search results to find extensions on
 	chrome webstore (https://chrome.google.com/webstore/category/extensions)
 	which have the following keywords in their description - 
 	Facebook, Twitter, Youtube, Instagram, Pinterest.
	To get the chrome store URLs from
	the search results and save the URLs in a 
 	separate text file with one URL per line. 

	* search.py runs the main() and stores the search responses in a JSON file (within output directory) called 'searchresponse.json'
	* The URLs of extensions which have been queried are stored in a text file (within output directory) called 'URLs.txt'