# Google Sheets setup

1. Open your spreadsheet:
   `https://docs.google.com/spreadsheets/d/1hYeyWnGds1GkuEWOu3Y6GUivJ1PAZUsQzS_hZZPROXw/edit`
2. In Google Sheets, click `Extensions` -> `Apps Script`.
3. Replace the current script with the code from `GOOGLE_APPS_SCRIPT.gs`.
4. Click `Save`.
5. Run `prepareSheet` once.
6. Grant the requested permissions.
7. `prepareSheet` will do three things:
   - change the header row to Chinese
   - remove old diagnostic rows where `site=diag` or `source=diagnostic`
   - keep using the `Leads` worksheet
8. Check that new submissions should be emailed to:
   `842598522@qq.com`
9. In Apps Script, click `Deploy` -> `Manage deployments`.
10. Edit the current Web app deployment and publish a new version.
11. Keep:
    - `Execute as`: `Me`
    - `Who has access`: `Anyone`
12. Then push the latest website code so the frontend also sends `client_ip` with each submission.

Email note:

- New submissions will be appended to the `Leads` sheet.
- New submissions will also be sent to `842598522@qq.com`.
- New submissions will include `client_ip`, fetched on the page before submit.
- If you do not see emails, check the QQ inbox spam folder first.
