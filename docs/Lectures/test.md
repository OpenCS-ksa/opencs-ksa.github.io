---
layout: default
title: Test
parent: Lectures
nav_order: 4
nav_exclude: false
---

<script>
function Code() {
    const code = document.getElementById('code').value;
    document.getElementById("print").innerText = code;
    document.getElementById("result").innerText = code;
}
</script>

<input id='code' onkeyup='Code()'/>
<div id='print'></div>

<py-script id = "result" output="out">
</py-script>

<div id="out"></div>