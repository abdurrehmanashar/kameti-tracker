# Supabase setup

The tracker stores one JSON document per signed-in user in `public.kameti_trackers`. Row-level security restricts each user to their own row. The browser uses Supabase Auth and the project's publishable key; never put a `service_role` key in this HTML app.

## Create and configure the Supabase project

1. Create a Supabase project.
2. In the Supabase SQL Editor, run [`supabase/schema.sql`](supabase/schema.sql).
3. In Authentication settings, enable email/password sign-in. Set the Site URL to `http://localhost:8000` and add `http://localhost:8000/**` to the redirect URL allow list. Add your deployed site's origin there too when you host the app.
4. From the project API settings, copy the Project URL and the publishable key (or legacy `anon` key). These are public client credentials; row-level security is what protects the data.

## Run the app

Create or edit a `.env` file in the project root with your Project URL and publishable key:

```dotenv
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_PUBLISHABLE_KEY=sb_publishable_your_key
```

Then install the server dependency and start the app:

```powershell
python -m pip install -r requirements.txt
python server.py
```

Open `http://localhost:8000/Kameti%20Tracker%20(MVP).html`. Sign in or create an account. If email confirmation is enabled, confirm the email and sign in.

The app reads its Supabase URL and publishable key from `.env`; there is no frontend configuration step. The publishable key is delivered to the browser, so never put a `service_role` key in `.env`. Each account has an independent tracker; this setup does not share one committee between multiple accounts.

## Existing local data

When you sign in for the first time in a browser, if that account has no cloud row, the app imports the existing `kameti_v1` local tracker and uploads it. The old local key is removed only after a successful upload; an account-specific local cache remains. If the old and new app are opened under different browser origins (for example, `file://` versus `http://localhost:8000`), browser storage is separate. Use the old app's **Backup** screen to copy its JSON, sign into the new app, then restore that JSON from **Backup**.

Edits are cached locally and uploaded shortly afterward. A sync failure is shown in a toast; the local cache remains available to retry on the next edit. The PIN remains a casual in-app lock, not encryption. Supabase stores the tracker data as JSON, so use Supabase's normal project security and backups appropriately.
