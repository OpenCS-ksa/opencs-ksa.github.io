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
    test_table = [
        [
            ['average',`print("Success")`],
            ['function', `print("Function")`]
        ],
        [
            ['test',`print("Test")`]
        ]
    ]

    function SetSelect() {
        html = ""
        for(int i = 1; i <= test_table.length; i++){
            html += "<option>" + String(i) + "</option>\n"
        }
        document.getElementById("theme").innerHTML = html;

        theme = document.getElementById('theme').value - 1;

        html = ""
        for(int i = 1; i <= test_table[theme].length; i++){
            html += "<option>" + String(i) + "</option>\n"
        }
        document.getElementById("problem").innerHTML = html;
    }

    function Check() {
        theme = document.getElementById('theme').value - 1
        problem = document.getElementById('problem').value - 1
        check_function = test_talbe[theme][problem][0]
        check_code = test_talbe[theme][problem][1]

        const code = document.getElementById('code').value;
        document.getElementById("out").innerHTML = ``;
        if(string.includes("print")) {
            alert("print 구문을 제외하고 넣으세요.")
        }
        else if (string.includes(check_function)) {
            alert(check_function + " 함수를 포함하고 있지 않습니다.")
        }
        else {
            document.getElementById("result").innerHTML = `<py-script output="out">` + code + "\n\n" + check_code + `</py-script>`;
        }
    }
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