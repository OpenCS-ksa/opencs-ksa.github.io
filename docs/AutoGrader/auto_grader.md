---
layout: default
title: Online Judge
nav_order: 3
nav_exclude: false
permalink: docs/AutoGrader
---
<head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/unstable/pyscript.js"></script>
</head>
    
<script>
    console.log("HelloWOrld")
</script>

Theme : 
<select id = 'theme' onclick="SetSelect()" style="background-color:#34333d"><option>1</option></select>
<br>
Problem : 
<select id = 'problem' style="background-color:#34333d"><option>1</option></select>

<br>
<br>    

<textarea id='code' name="code" rows="5" cols="50" style="background-color:#34333d"></textarea>
<br>
<button onclick="Check()">Run</button>
<br>
<br>
<br>
<div id='result'></div>

<div id="out"></div>