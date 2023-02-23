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

## Online Judge

Theme, Problem 번호를 선택하고, 함수 부분을 복사하여 코드를 채점할 수 있습니다.         
<br>

- - -
          
<script>
    const test_table = [
        /*Themes*/
        [
            /*Problems*/
            /*`Main Function Name`, `Test Code`*/
            [`test11`, `print("test1")`], 
            [`test12`, `print("test2")`]
        ],
        [
            [`test21`, `print("test3")`], 
            [`test22`, `print("test4")`], 
            [`test23`, `print("test5")`]
        ]
    ];

    function SetTheme() {
        var html = "";
        for(var i = 1; i <= test_table.length; i++){
            html += "<option>" + String(i) + "</option>\n";
        }
        document.getElementById("theme").innerHTML = html;
    }

    function SetProblem() {
        var theme = document.getElementById('theme').value - 1;

        html = "";
        for(var i = 1; i <= test_table[theme].length; i++){
            html += "<option>" + String(i) + "</option>\n";
        }
        document.getElementById("problem").innerHTML = html;
    }

    function Check() {
        var theme = document.getElementById('theme').value - 1;
        var problem = document.getElementById('problem').value - 1;
        var check_function = test_table[theme][problem][0];
        var check_code = test_table[theme][problem][1];

        var code = document.getElementById('code').value;
        document.getElementById("out").innerHTML = ``;
        if(code.includes("print")) {
            alert("print 구문을 제외하고 넣으세요.");
        }
        else if (!code.includes(check_function)) {
            alert(check_function + " 함수를 포함하고 있지 않습니다.");
        }
        else {
            document.getElementById("result").innerHTML = `<py-script output="out">` + code + "\n\n" + check_code + `</py-script>`;
        }
    }
</script>

Theme : 
<select id = 'theme' onclick="SetProblem()" style="background-color:#34333d"><option>1</option></select>
&nbsp;&nbsp;&nbsp;&nbsp;
Problem : 
<select id = 'problem' style="background-color:#34333d"><option>1</option></select>

<br>
<br>    

### Code :
<textarea id='code' name="code" rows="5" cols="50" style="background-color:#34333d"></textarea>
<br>
<button onclick="Check()">Run</button>

### Result : 
<div id='result'></div>
<h3 id="out"></h3>

<br>
<br>
<br>

<script>
    SetTheme();
    SetProblem();
</script>