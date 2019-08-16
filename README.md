README: Hierarchy/Seniority Calculating Algorithm

Let's say you have a spreadsheet full of HR data (csv format for this script - easy to fork for xlsx).

It's arranged by employee, and has a bunch of attributes of that employee (their name, title, etc)

It also includes a field that tells you who that employee reports to.

While you do have a secret love of repetitious manual work, you also know that your work should be a) reproducible and b) free of manual errors.

This repo contains an example recursive algorithm that should take in your data, so long as it is consistently formatted, and tag it up with levels of seniority. I didn't include any cleaning commands or functions to keep this example clean.

What is a level of seniority? Well, if no-one reports to employee A, then employee A has seniority level 0. For each successive person who reports to someone who reports to (...and so on) who reports to A, we add 1 to A's seniority level. So if A has a subordinate B, who has subordinate C, then A's seniority level is 2.

I created this just to control for hierarchy in some other analysis I was doing, but it might hae more general use. 

Note that it only works for a simple tree-like hierarchy. If the data is not set up with a single supervisor for each subordinate, with a single record per subordinate, then this function won't work.

Let me know how it goes for you, and if you find ways to improve on this approach :) You can reach me at: matt - dot - cummins - at - stanford - dot - edu

