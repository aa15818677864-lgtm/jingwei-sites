# Google Sheets setup

1. Open your spreadsheet:
   `https://docs.google.com/spreadsheets/d/1hYeyWnGds1GkuEWOu3Y6GUivJ1PAZUsQzS_hZZPROXw/edit?gid=0#gid=0`
2. In Google Sheets, click `Extensions` -> `Apps Script`.
3. Replace the default script with the code from `GOOGLE_APPS_SCRIPT.gs`.
4. Click `Save`.
5. Run `setupSheet` once so the `Leads` tab and header row are created.
6. Click `Deploy` -> `New deployment`.
7. Choose `Web app`.
8. Set `Execute as` to `Me`.
9. Set `Who has access` to `Anyone`.
10. Deploy and copy the Web App URL ending in `/exec`.
11. Open `site-config.js` and replace `PASTE_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE` with that Web App URL.
12. After that, both `/ml/` and `/xj/` pages will submit to the same Google Sheet.
