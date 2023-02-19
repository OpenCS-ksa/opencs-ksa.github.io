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
    document.getElementById("result").innerHTML = `<py-script output="out">` + code + `</py-script>`;
}
</script>

<input id='code' onkeyup='Code()'/>
<div id='print'></div>

<div id='result'></div>

<div id="out"></div>