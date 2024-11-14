# Overview #

## Background Context ##
The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.


## Reference Materials ##
The following can be used for referencing these areas, curated for optimized understanding:
- [HTTP Requests in JavaScript](https://www.memberstack.com/blog/node-http-request):
  - Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
- [Working with APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction):
  - Understanding the basics of RESTful APIs and how to interact with them.
  - Parsing JSON data returned by APIs.
- [Asynchronous Programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous):
  - Managing asynchronous operations with callbacks, promises, and async/await syntax.
  - Handling API response data asynchronously.
- [Command Line Arguments in Node.js](https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/):
  - Using the process.argv array to access command-line arguments passed to a Node.js script.
- [Array Manipulation and Iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array):
  - Iterating over arrays and manipulating data structures to format and display character names.

### A Little Extra ###
- [Mock Interviews](https://www.youtube.com/watch?v=bmqZ5AhNr3g)


## Folder Details ###
- **Date Created:** Wed Nov. 13 2024 7:19am
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
- **Released:** Mon Nov 11 2024 - 6am.
  - **1st Deadline** Thur Nov. 14 2024 - 6am.
  - **Duration:** 96hrs
  - **Completed:** Thur Nov 14 - 4:38am.


## Development Environment ##
### Install Node 10 ###

``` sh
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install Semistandard ###

``` sh
$ sudo npm install semistandard --global
```
**[Documentation](https://github.com/standard/semistandard)**

### Install `request` module and use it ###

``` sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**[Documentation](https://github.com/request/request)**


## Files  ###
*This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|----------------------------------------------------|---------------------------------------|
| 1. | [0-starwars_characters.js](https://github.com/thecypherzen/alx-interview/tree/main/0x06-starwars_api) | A script that prints all characters of a Star Wars movie in same order as listed in api. |
