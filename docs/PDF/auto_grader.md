---
layout: default
title: PDF Download
nav_order: 5
nav_exclude: false
---
<script src="js/jsPDF/dist/jspdf.umd.js"></script>

## PDF Download
      
- - -

[Download](javascript:ConvertHTML2PDF();){: .btn }

<script>
    window.jsPDF = window.jspdf.jsPDF;

    // Convert HTML content to PDF
    function ConvertHTML2PDF() {
        var doc = new jsPDF();
        
        // Source HTMLElement or a string containing HTML.
        var elementHTML = document.querySelector("#contentToPrint");

        doc.html(elementHTML, {
            callback: function(doc) {
                // Save the PDF
                doc.save('Open CS.pdf');
            },
            margin: [10, 10, 10, 10],
            autoPaging: 'text',
            x: 0,
            y: 0,
            width: 190, //target width in the PDF document
            windowWidth: 675 //window width in CSS pixels
        });
    }
</script>