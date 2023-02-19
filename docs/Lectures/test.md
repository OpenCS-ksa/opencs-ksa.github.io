---
layout: default
title: Test
parent: Lectures
nav_order: 4
nav_exclude: false
---

<head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/unstable/pyscript.js"></script>
</head>
    
<script>

function Code() {
    const code = document.getElementById('code').value;
    document.getElementById("out").innerHTML = ``;
    document.getElementById("result").innerHTML = `<py-script output="out">` + code + `</py-script>`;
}
</script>

<textarea id='code' name="code" rows="5" cols="50" style="background-color:#34333d"></textarea>

<button onclick="Code()">Run</button>

<div id='result'></div>

<div id="out"></div>