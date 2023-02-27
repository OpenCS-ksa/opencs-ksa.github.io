---
layout: default
title: Attendance
nav_order: 5
nav_exclude: false
---
## 출석부

- - -
               
<script>
     let google = require('googleapis');
     let secretKey = require("client_secret.json");
     let jwtClient = new google.auth.JWT(
          secretKey.client_email,
          null,
          secretKey.private_key,
          ['https://www.googleapis.com/auth/spreadsheets']);
     //authenticate request
     jwtClient.authorize(function (err, tokens) {
     if (err) {
     console.log(err);
     return;
     } else {
     console.log("Successfully connected!");
     }
     });

     let spreadsheetId = '1X3ZtRWpwc5G22bFo0dTFgs7UTjwW-mMY5cn_bEVIabw';
     let sheetRange = 'Test!A4:E4'
     let sheets = google.sheets('v4');
     sheets.spreadsheets.values.get({
          auth: jwtClient,
          spreadsheetId: spreadsheetId,
          range: sheetRange
     }, 
     function (err, response) {
          if (err) {
               console.log('The API returned an error: ' + err);
          } 
          else {
               for (let row of response.values) {
                    console.log('Title [%s]\t\tRating [%s]', row[0], row[1]);
               }
          }
     });

     let values = [[“00004”,“Jack”,“Smith”,“1115748594”,“jack.smith@gmail.com”]];
     const sheetResource = { values, };
     sheets.spreadsheets.values.update({
          auth: jwtClient,
          spreadsheetId: spreadsheetId,
          range: sheetRange,
          resource: sheetResource
     }, 
     function (err, response) {
          if (err) {
               console.log('The API returned an error: ' + err);
          } 
          else {
               console.log('Movie list from Google Sheets:');
               for (let row of response.values) {
                    console.log('Title [%s]\t\tRating [%s]', row[0], row[1]);
               }
          }
     });
</script>