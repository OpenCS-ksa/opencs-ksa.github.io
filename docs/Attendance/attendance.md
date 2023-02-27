---
layout: default
title: Attendance
nav_order: 5
nav_exclude: false
---
## 출석부

- - -

<p>Sheets API Quickstart</p>

<!--Add buttons to initiate auth sequence and sign out-->
<button id="authorize_button" onclick="handleAuthClick()">Authorize</button>
<button id="signout_button" onclick="handleSignoutClick()">Sign Out</button>

<pre id="content" style="white-space: pre-wrap;"></pre>

<script type="text/javascript">
     const CLIENT_ID = '110007993587368451529';
     const API_KEY = 'e1a634edf54a256be9fbc66c0dad42b3a708d76a';
     const DISCOVERY_DOC = 'https://sheets.googleapis.com/$discovery/rest?version=v4';
     const SCOPES = 'https://www.googleapis.com/auth/spreadsheets';

     let tokenClient;
     let gapiInited = false;
     let gisInited = false;

     document.getElementById('authorize_button').style.visibility = 'hidden';
     document.getElementById('signout_button').style.visibility = 'hidden';
     function gapiLoaded() {
     gapi.load('client', initializeGapiClient);
     }

     async function initializeGapiClient() {
     await gapi.client.init({
     apiKey: API_KEY,
     discoveryDocs: [DISCOVERY_DOC],
     });
     gapiInited = true;
     maybeEnableButtons();
     }

     function gisLoaded() {
     tokenClient = google.accounts.oauth2.initTokenClient({
     client_id: CLIENT_ID,
     scope: SCOPES,
     callback: '', 
     });
     gisInited = true;
     maybeEnableButtons();
     }

     function maybeEnableButtons() {
     if (gapiInited && gisInited) {
     document.getElementById('authorize_button').style.visibility = 'visible';
     }
     }

     function handleAuthClick() {
     tokenClient.callback = async (resp) => {
     if (resp.error !== undefined) {
          throw (resp);
     }
     document.getElementById('signout_button').style.visibility = 'visible';
     document.getElementById('authorize_button').innerText = 'Refresh';
     await listMajors();
     };

     if (gapi.client.getToken() === null) {
     tokenClient.requestAccessToken({prompt: 'consent'});
     } else {
     tokenClient.requestAccessToken({prompt: ''});
     }
     }

     function handleSignoutClick() {
     const token = gapi.client.getToken();
     if (token !== null) {
     google.accounts.oauth2.revoke(token.access_token);
     gapi.client.setToken('');
     document.getElementById('content').innerText = '';
     document.getElementById('authorize_button').innerText = 'Authorize';
     document.getElementById('signout_button').style.visibility = 'hidden';
     }
     }

     async function listMajors() {
     let response;
     try {
     response = await gapi.client.sheets.spreadsheets.values.get({
          spreadsheetId: '1X3ZtRWpwc5G22bFo0dTFgs7UTjwW-mMY5cn_bEVIabw',
          range: 'Test!A1:E',
     });
     } catch (err) {
     document.getElementById('content').innerText = err.message;
     return;
     }
     const range = response.result;
     if (!range || !range.values || range.values.length == 0) {
     document.getElementById('content').innerText = 'No values found.';
     return;
     }
     const output = range.values.reduce(
          (str, row) => `${str}${row[0]}, ${row[4]}\n`,
          'Name, Major:\n');
     document.getElementById('content').innerText = output;
     }
</script>
<script async defer src="https://apis.google.com/js/api.js" onload="gapiLoaded()"></script>
<script async defer src="https://accounts.google.com/gsi/client" onload="gisLoaded()"></script>