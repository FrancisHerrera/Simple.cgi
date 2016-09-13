#!/bin/bash
# Francis Herrera fah36765 101751271

echo 'Content-type: text/html'
echo ''

# return HTML
echo '<html>'
echo '<head>'

# one style sheet minimum

echo '<link rel="stylesheet" rev="stylesheet" href="http://www.csun.edu/~fah36765/css/simple.css">'
echo '<meta http-equiv="Content-Type" content="text/html; charst=UTF-8">'
echo '<title>Francis Herrera</title>'
echo '</head>'
echo '<body><p>'
echo '<span id="fah">Comp 490 Project 1 Senior Design </span><br>'
echo '</p>'
echo '<body><p>'
echo '<span id="fah">Primer Project 1 - Lets see if I did</span><br>'
echo '<span id="fah">the project right. Chances are I </span><br>'
echo '<span id="fah">didnt - Lame</span><br>'

echo '</p>'
# info from the file system
echo "<span id="fah"><p>$SCRIPT_FILENAME</p></span>"

/usr/bin/curl -s ${QUERY_STRING}
echo  '<span id="fah">Time is:</span>'
echo "<span id="fah"><p>$(date)</p></span>"
echo '</p></body>'
echo '</html>'

exit 0
