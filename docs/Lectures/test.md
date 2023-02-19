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
    document.getElementById("result").innerHTML = `<py-script output="out">` + code + `</py-script>`;
}
</script>

<textarea id='code' name="code"></textarea>

<button onclick="Code()">Run</button>

<div id='result'></div>

<div id="out"></div>