---
layout: default
title: PDF Download
nav_order: 5
nav_exclude: false
---
<script src="js/jsPDF/dist/jspdf.umd.js"></script>
<script src="js/html2canvas.min.js"></script>

## PDF Download
      
- - -

<script>
    window.jsPDF = window.jspdf.jsPDF;

    function ConvertHTML2PDF() {
        var doc = new jsPDF();
        
        var elementHTML = document.querySelector("#contentToPrint");

        doc.html(elementHTML, {
            callback: function(doc) {
                doc.save('Open CS.pdf');
            },
            margin: [10, 10, 10, 10],
            autoPaging: 'text',
            x: 0,
            y: 0,
            width: 190,
            windowWidth: 675 
        });
    }
</script>

[Download](javascript:ConvertHTML2PDF();){: .btn }