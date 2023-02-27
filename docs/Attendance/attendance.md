---
layout: default
title: Attendance
nav_order: 5
nav_exclude: true
---
## 출석

- - -

<p>Sheets API Quickstart</p>

<!--Add buttons to initiate auth sequence and sign out-->
<button id="authorize_button" onclick="handleAuthClick()">Authorize</button>
<button id="signout_button" onclick="handleSignoutClick()">Sign Out</button>

<pre id="content" style="white-space: pre-wrap;"></pre>

<script type="text/javascript">
     /* exported gapiLoaded */
     /* exported gisLoaded */
     /* exported handleAuthClick */
     /* exported handleSignoutClick */

     const CLIENT_ID = '74045000255-dio9166ulopprbkvv0rs8taui8c77o42.apps.googleusercontent.com';
     const API_KEY = 'AIzaSyCK53c3ug2uQREiYGqpAXt_B8rP6A9Vbg0';

     const DISCOVERY_DOC = 'https://sheets.googleapis.com/$discovery/rest?version=v4';

     const SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly';

     let tokenClient;
     let gapiInited = false;
     let gisInited = false;

     document.getElementById('authorize_button').style.visibility = 'hidden';
     document.getElementById('signout_button').style.visibility = 'hidden';

     /**
     * Callback after api.js is loaded.
     */
     function gapiLoaded() {
     gapi.load('client', initializeGapiClient);
     }

     /**
     * Callback after the API client is loaded. Loads the
     * discovery doc to initialize the API.
     */
     async function initializeGapiClient() {
     await gapi.client.init({
     apiKey: API_KEY,
     discoveryDocs: [DISCOVERY_DOC],
     });
     gapiInited = true;
     maybeEnableButtons();
     }

     /**
     * Callback after Google Identity Services are loaded.
     */
     function gisLoaded() {
     tokenClient = google.accounts.oauth2.initTokenClient({
     client_id: CLIENT_ID,
     scope: SCOPES,
     callback: '', 
     });
     gisInited = true;
     maybeEnableButtons();
     }

     /**
     * Enables user interaction after all libraries are loaded.
     */
     function maybeEnableButtons() {
     if (gapiInited && gisInited) {
     document.getElementById('authorize_button').style.visibility = 'visible';
     }
     }

     /**
     *  Sign in the user upon button click.
     */
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

     /**
     *  Sign out the user upon button click.
     */
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

     /**
     * Print the names and majors of students in a sample spreadsheet:
     * https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
     */
     async function listMajors() {
     let response;
     try {
     response = await gapi.client.sheets.spreadsheets.values.get({
          spreadsheetId: '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms',
          range: 'Class Data!A2:E',
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